import os

from flask import Flask, jsonify, redirect, render_template, request, url_for, session
from flask_cors import CORS
from database import get_db_connection, init_db
from videos_data import get_course_lessons

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-only-secret-key")
CORS(app)

init_db()


@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


def get_test_questions(course_id, stage="entry"):
    conn = get_db_connection()
    questions = conn.execute(
        """
        SELECT id, question, option1, option2, option3, option4
        FROM questions
        WHERE course_id=?
        ORDER BY id
        """,
        (course_id,)
    ).fetchall()
    conn.close()

    if len(questions) <= 3:
        return questions

    if stage == "final":
        return questions[:20]

    if stage == "checkpoint":
        return questions[5:10]

    return questions[:5]


def format_watch_hours(seconds):
    seconds = int(seconds or 0)
    hours = seconds / 3600
    if hours < 1:
        return f"{seconds // 60}m"
    return f"{hours:.1f}h"

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM students WHERE email=? AND password=?",
            (email, password)
        ).fetchone()
        conn.close()

        if user:
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()

        try:
            conn.execute(
                "INSERT INTO students (name,email,password) VALUES (?,?,?)",
                (name, email, password)
            )
            conn.commit()
            return redirect(url_for("login"))
        except:
            return render_template("register.html", error="Email already exists")
        finally:
            conn.close()

    return render_template("register.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    progress = conn.execute("""
        SELECT courses.id,
               courses.course_name,
               enrollments.progress as score,
               COALESCE(SUM(watch_progress.seconds_watched), 0) as seconds_watched,
               certificates.id as certificate_id
        FROM enrollments
        JOIN courses ON courses.id = enrollments.course_id
        LEFT JOIN watch_progress
            ON watch_progress.student_id = enrollments.student_id
           AND watch_progress.course_id = enrollments.course_id
        LEFT JOIN certificates
            ON certificates.student_id = enrollments.student_id
           AND certificates.course_id = enrollments.course_id
        WHERE enrollments.student_id = ?
        GROUP BY courses.id, courses.course_name, enrollments.progress, certificates.id
    """, (session["user_id"],)).fetchall()

    total_seconds = sum(p["seconds_watched"] for p in progress)

    enrolled_ids = [p["id"] for p in progress]

    if enrolled_ids:
        placeholders = ",".join(["?"] * len(enrolled_ids))
        all_courses = conn.execute(
            f"SELECT * FROM courses WHERE id NOT IN ({placeholders})",
            enrolled_ids
        ).fetchall()
    else:
        all_courses = conn.execute("SELECT * FROM courses").fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        name=session.get("user_name"),
        progress=progress,
        total_courses=len(progress),
        avg_score=round(sum(p["score"] for p in progress) / len(progress), 1) if progress else 0,
        total_watch_time=format_watch_hours(total_seconds),
        total_watch_seconds=total_seconds,
        all_courses=all_courses
    )


# ---------------- ENROLL ----------------
@app.route("/enroll/<int:course_id>")
def enroll(course_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    conn.execute("""
        INSERT OR IGNORE INTO enrollments (student_id, course_id, progress)
        VALUES (?, ?, 0)
    """, (session["user_id"], course_id))

    conn.execute("""
        INSERT OR IGNORE INTO learning_progress (student_id, course_id, current_step)
        VALUES (?, ?, 0)
    """, (session["user_id"], course_id))

    conn.commit()
    conn.close()

    return redirect(url_for("learning_path", course_id=course_id, level="Beginner"))


# ---------------- TEST ----------------
@app.route("/test/<int:course_id>")
def test(course_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    course = conn.execute(
        "SELECT * FROM courses WHERE id=?",
        (course_id,)
    ).fetchone()
    conn.close()

    if not course:
        return "Course not found"

    test_stage = request.args.get("stage", "entry")
    if test_stage not in {"entry", "checkpoint", "final"}:
        test_stage = "entry"

    questions = get_test_questions(course_id, test_stage)

    return render_template(
        "test.html",
        questions=questions,
        course_id=course_id,
        course_name=course["course_name"],
        test_stage=test_stage
    )


# ---------------- SUBMIT TEST ----------------
@app.route("/submit_test", methods=["POST"])
def submit_test():
    if "user_id" not in session:
        return redirect("/login")

    course_id = int(request.form["course_id"])
    course_name = request.form["course_name"]
    test_stage = request.form.get("test_stage", "entry")

    answers = request.form

    correct = 0
    total = 0

    conn = get_db_connection()
    cursor = conn.cursor()

    for key in answers:
        if key.startswith("question_"):
            qid = key.split("_")[1]
            selected = int(answers[key])

            cursor.execute(
                "SELECT correct_option FROM questions WHERE id=?",
                (qid,)
            )
            result = cursor.fetchone()

            if result:
                total += 1
                if selected == result["correct_option"]:
                    correct += 1

    conn.close()

    percentage = int((correct / total) * 100) if total else 0

    conn = get_db_connection()
    enrollment = conn.execute(
        """
        SELECT id
        FROM enrollments
        WHERE student_id=? AND course_id=?
        """,
        (session["user_id"], course_id)
    ).fetchone()

    if not enrollment:
        conn.execute("""
            INSERT INTO enrollments (student_id, course_id, progress)
            VALUES (?, ?, ?)
        """, (session["user_id"], course_id, percentage))

        conn.execute("""
            INSERT OR IGNORE INTO learning_progress (student_id, course_id, current_step)
            VALUES (?, ?, 0)
        """, (session["user_id"], course_id))
    else:
        conn.execute("""
            UPDATE enrollments
            SET progress=?
            WHERE student_id=? AND course_id=?
        """, (percentage, session["user_id"], course_id))

    progress = conn.execute(
        """
        SELECT current_step
        FROM learning_progress
        WHERE student_id=? AND course_id=?
        """,
        (session["user_id"], course_id)
    ).fetchone()

    lessons = get_course_lessons(course_name, "Beginner")
    if progress and test_stage == "checkpoint":
        current_step = progress["current_step"]
        if 0 <= current_step < len(lessons) and lessons[current_step]["test"]:
            next_step = min(current_step + 1, len(lessons))
            conn.execute("""
                UPDATE learning_progress
                SET current_step=?, updated_at=CURRENT_TIMESTAMP
                WHERE student_id=? AND course_id=?
            """, (next_step, session["user_id"], course_id))

    certificate_id = None
    if test_stage == "final":
        conn.execute("""
            INSERT INTO certificates (student_id, course_id, score)
            VALUES (?, ?, ?)
            ON CONFLICT(student_id, course_id)
            DO UPDATE SET score=?, issued_at=CURRENT_TIMESTAMP
        """, (session["user_id"], course_id, percentage, percentage))
        certificate = conn.execute(
            """
            SELECT id
            FROM certificates
            WHERE student_id=? AND course_id=?
            """,
            (session["user_id"], course_id)
        ).fetchone()
        certificate_id = certificate["id"] if certificate else None

    conn.commit()
    conn.close()

    # Level logic
    if percentage < 40:
        level = "Beginner"
    elif percentage < 70:
        level = "Intermediate"
    else:
        level = "Advanced"

    return render_template(
        "test_result.html",
        total=total,
        correct=correct,
        percentage=percentage,
        level=level,
        course_id=course_id,
        course_name=course_name,
        test_stage=test_stage,
        certificate_id=certificate_id,
        student_name=session.get("user_name", "Student")
    )


# ---------------- LEARNING PATH ----------------
@app.route("/learning_path/<int:course_id>/<level>")
def learning_path(course_id, level):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    course = conn.execute(
        "SELECT * FROM courses WHERE id=?",
        (course_id,)
    ).fetchone()

    progress = conn.execute(
        """
        SELECT current_step
        FROM learning_progress
        WHERE student_id=? AND course_id=?
        """,
        (session["user_id"], course_id)
    ).fetchone()

    watch_rows = conn.execute(
        """
        SELECT lesson_index, seconds_watched, last_position
        FROM watch_progress
        WHERE student_id=? AND course_id=?
        """,
        (session["user_id"], course_id)
    ).fetchall()

    conn.close()

    if not course:
        return "Course not found"

    lessons = get_course_lessons(course["course_name"], level)
    current_step = progress["current_step"] if progress else 0
    max_step = len(lessons)
    current_step = min(current_step, max_step)
    watch_progress = {row["lesson_index"]: dict(row) for row in watch_rows}
    total_watch_seconds = sum(row["seconds_watched"] for row in watch_rows)

    return render_template(
        "learning_path.html",
        lessons=lessons,
        course_name=course["course_name"],
        level=level,
        course_id=course_id,
        current_step=current_step,
        watch_progress=watch_progress,
        total_watch_time=format_watch_hours(total_watch_seconds)
    )


@app.route("/complete_step/<int:course_id>/<int:step_index>/<level>")
def complete_step(course_id, step_index, level):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    course = conn.execute(
        "SELECT * FROM courses WHERE id=?",
        (course_id,)
    ).fetchone()

    if not course:
        conn.close()
        return "Course not found"

    lessons = get_course_lessons(course["course_name"], level)
    max_step = len(lessons) - 1

    if step_index < 0 or step_index > max_step:
        conn.close()
        return "Invalid step"

    next_step = min(step_index + 1, len(lessons))

    conn.execute("""
        INSERT INTO learning_progress (student_id, course_id, current_step)
        VALUES (?, ?, ?)
        ON CONFLICT(student_id, course_id)
        DO UPDATE SET current_step=?, updated_at=CURRENT_TIMESTAMP
    """, (session["user_id"], course_id, next_step, next_step))

    conn.commit()
    conn.close()

    return redirect(url_for("learning_path", course_id=course_id, level=level))


@app.route("/track_watch", methods=["POST"])
def track_watch():
    if "user_id" not in session:
        return jsonify({"ok": False}), 401

    data = request.get_json(silent=True) or {}
    course_id = int(data.get("course_id", 0))
    lesson_index = int(data.get("lesson_index", 0))
    seconds_watched = max(0, min(int(data.get("seconds_watched", 0)), 60))
    last_position = max(0, int(data.get("last_position", 0)))

    if course_id <= 0 or lesson_index < 0:
        return jsonify({"ok": False}), 400

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO watch_progress (student_id, course_id, lesson_index, seconds_watched, last_position)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(student_id, course_id, lesson_index)
        DO UPDATE SET
            seconds_watched = seconds_watched + excluded.seconds_watched,
            last_position = excluded.last_position,
            updated_at = CURRENT_TIMESTAMP
    """, (session["user_id"], course_id, lesson_index, seconds_watched, last_position))
    conn.commit()
    conn.close()

    return jsonify({"ok": True})


@app.route("/remove_course/<int:course_id>")
def remove_course(course_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    conn.execute(
        "DELETE FROM watch_progress WHERE student_id=? AND course_id=?",
        (session["user_id"], course_id)
    )
    conn.execute(
        "DELETE FROM certificates WHERE student_id=? AND course_id=?",
        (session["user_id"], course_id)
    )
    conn.execute(
        "DELETE FROM learning_progress WHERE student_id=? AND course_id=?",
        (session["user_id"], course_id)
    )
    conn.execute(
        "DELETE FROM enrollments WHERE student_id=? AND course_id=?",
        (session["user_id"], course_id)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("mycourses"))


@app.route("/certificate/<int:certificate_id>")
def certificate(certificate_id):
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    certificate_row = conn.execute("""
        SELECT certificates.id,
               certificates.score,
               certificates.issued_at,
               students.name,
               courses.course_name
        FROM certificates
        JOIN students ON students.id = certificates.student_id
        JOIN courses ON courses.id = certificates.course_id
        WHERE certificates.id=? AND certificates.student_id=?
    """, (certificate_id, session["user_id"])).fetchone()
    conn.close()

    if not certificate_row:
        return "Certificate not found"

    return render_template("certificate.html", certificate=certificate_row)


# ---------------- MY COURSES ----------------
@app.route("/mycourses")
def mycourses():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()

    my_courses = conn.execute("""
        SELECT courses.id,
               courses.course_name,
               courses.description,
               enrollments.progress,
               COALESCE(SUM(watch_progress.seconds_watched), 0) as seconds_watched,
               certificates.id as certificate_id
        FROM enrollments
        JOIN courses ON courses.id = enrollments.course_id
        LEFT JOIN watch_progress
            ON watch_progress.student_id = enrollments.student_id
           AND watch_progress.course_id = enrollments.course_id
        LEFT JOIN certificates
            ON certificates.student_id = enrollments.student_id
           AND certificates.course_id = enrollments.course_id
        WHERE enrollments.student_id = ?
        GROUP BY courses.id, courses.course_name, courses.description, enrollments.progress, certificates.id
    """, (session["user_id"],)).fetchall()

    total_seconds = sum(c["seconds_watched"] for c in my_courses)

    conn.close()

    return render_template(
        "mycourses.html",
        my_courses=my_courses,
        total_courses=len(my_courses),
        avg_score=round(sum(c["progress"] for c in my_courses) / len(my_courses), 1) if my_courses else 0,
        total_watch_time=format_watch_hours(total_seconds)
    )


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=False)
