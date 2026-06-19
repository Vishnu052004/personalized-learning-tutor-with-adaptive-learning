import sqlite3
from questions_data import get_questions_for_course

DATABASE_NAME = "learning_tutor.db"


# =========================
# DATABASE CONNECTION
# =========================
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = MEMORY")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# =========================
# AUTO QUESTION GENERATOR
# =========================
def insert_default_questions(cursor):
    cursor.execute("SELECT id, course_name FROM courses")
    courses = cursor.fetchall()

    for course in courses:
        course_id = course[0]
        course_name = course[1]

        # Check how many questions already exist
        cursor.execute(
            "SELECT COUNT(*) FROM questions WHERE course_id = ?",
            (course_id,)
        )
        count = cursor.fetchone()[0]

        if count >= 20:
            continue

        # 🔥 Get real questions from separate file
        questions = get_questions_for_course(course_name, course_id)
        questions.extend(get_supplemental_questions(course_name, course_id))

        if questions:
            cursor.executemany("""
                INSERT OR IGNORE INTO questions
                (course_id, question, option1, option2, option3, option4, correct_option)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, questions)


def get_supplemental_questions(course_name, course_id):
    fallback = [
        ("What is the main goal of this course?", "Build practical understanding", "Play audio", "Change wallpaper", "Buy hardware", 1),
        ("What should you do after learning a concept?", "Practice it", "Ignore it", "Delete it", "Hide it", 1),
        ("Why are examples useful?", "They make ideas concrete", "They slow the browser", "They erase data", "They block login", 1),
        ("What does a checkpoint test measure?", "Understanding so far", "Screen size", "Internet cost", "Keyboard speed", 1),
        ("What helps long-term learning?", "Review and practice", "Skipping lessons", "Guessing only", "Closing the app", 1),
        ("What is a learning path?", "Ordered course steps", "Random files", "One password", "A printer setting", 1),
        ("When should you use notes?", "To remember key ideas", "To delete videos", "To change code color", "To block pages", 1),
        ("What does course progress show?", "How much you completed", "Battery level", "Server brand", "Mouse speed", 1),
        ("Why take a final test?", "To verify course mastery", "To change email", "To install fonts", "To resize images", 1),
        ("What is the best next step after completion?", "Apply the skill in a project", "Forget the course", "Delete the browser", "Stop practicing", 1),
    ]
    extras = {
        "Python Programming": [
            ("Which Python structure stores key-value pairs?", "Dictionary", "List", "Tuple", "String", 1),
            ("What does a loop help you do?", "Repeat actions", "Style pages", "Store passwords", "Compile Java", 1),
            ("Which keyword starts a conditional block?", "if", "when", "check", "case", 1),
            ("Which method adds an item to a list?", "append()", "pushRow()", "insertTable()", "addPage()", 1),
            ("What is indentation used for in Python?", "Defining code blocks", "Changing fonts", "Opening files only", "Installing packages", 1),
            ("Which package manager is commonly used with Python?", "pip", "npm", "composer", "maven", 1),
            ("What is an exception?", "Runtime error condition", "HTML element", "Database row", "Network device", 1),
            ("Which keyword imports a module?", "import", "include", "require", "module", 1),
            ("What does len() return?", "Number of items", "File type", "CPU speed", "Network address", 1),
            ("Which file extension is used for Python files?", ".py", ".java", ".css", ".sql", 1),
        ],
        "Machine Learning": [
            ("What is a feature in ML?", "Input variable", "Web page", "Password", "Server", 1),
            ("What is a label?", "Target output", "Image border", "Database index", "Cloud region", 1),
            ("Which split tests generalization?", "Test set", "Keyboard", "Router", "Header", 1),
            ("Which task predicts categories?", "Classification", "Styling", "Routing", "Indexing", 1),
            ("Which task groups similar data?", "Clustering", "Compiling", "Rendering", "Encrypting", 1),
            ("What does model training adjust?", "Model parameters", "Screen brightness", "HTML tags", "File names", 1),
            ("What can prevent overfitting?", "Validation and regularization", "More passwords", "Larger fonts", "Offline mode", 1),
            ("Which library helps with arrays?", "NumPy", "Flask", "CSS", "SQLite", 1),
            ("What is accuracy used for?", "Classification evaluation", "Video editing", "Table deletion", "Web hosting", 1),
            ("What is prediction?", "Model output for input", "Database backup", "Color choice", "Network cable", 1),
        ],
        "Web Development": [
            ("Which HTML tag creates a link?", "<a>", "<img>", "<table>", "<style>", 1),
            ("Which CSS property changes text color?", "color", "href", "src", "method", 1),
            ("Which JavaScript keyword declares a constant?", "const", "fixed", "same", "hold", 1),
            ("What does a form collect?", "User input", "Only images", "CPU data", "Router logs", 1),
            ("Which method sends a form securely for login?", "POST", "PAINT", "DRAW", "STYLE", 1),
            ("What is responsive design?", "Adapts to screen sizes", "Deletes pages", "Encrypts files", "Runs only offline", 1),
            ("Which status code means not found?", "404", "200", "301", "5000", 1),
            ("What does CSS flexbox help with?", "Layout alignment", "Database joins", "Server routing", "Password hashing", 1),
            ("Which file usually contains page styles?", ".css", ".py", ".db", ".exe", 1),
            ("What does Flask route define?", "URL behavior", "Screen color", "CPU usage", "Video duration", 1),
        ],
        "Data Science": [
            ("What is a dataset?", "Collection of data", "Web button", "Firewall", "Compiler", 1),
            ("What does missing data mean?", "Values are absent", "Files are encrypted", "Charts are colored", "Rows are sorted", 1),
            ("Which chart compares categories?", "Bar chart", "Router chart", "Password chart", "Memory chart", 1),
            ("What does mean measure?", "Average value", "Maximum file size", "Network speed", "Page width", 1),
            ("Which library supports numerical arrays?", "NumPy", "Django", "HTML", "Docker", 1),
            ("What is data cleaning?", "Preparing data for analysis", "Painting UI", "Compiling C", "Routing packets", 1),
            ("What does correlation describe?", "Relationship between variables", "Cloud login", "Screen size", "File extension", 1),
            ("Which format stores rows and columns?", "CSV", "MP4", "PNG", "EXE", 1),
            ("What is visualization used for?", "Seeing patterns", "Deleting rows only", "Starting servers", "Writing passwords", 1),
            ("What does train-test split support?", "Model evaluation", "CSS styling", "Video playback", "User login", 1),
        ],
    }
    return [(course_id, *question) for question in extras.get(course_name, fallback)]

# =========================
# INITIALIZE DATABASE
# =========================
def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA journal_mode = MEMORY")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # -------------------------
    # STUDENTS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # -------------------------
    # COURSES TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT UNIQUE NOT NULL,
            description TEXT,
            category TEXT,
            image_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # -------------------------
    # QUESTIONS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL CHECK(correct_option BETWEEN 1 AND 4),

            UNIQUE(course_id, question),

            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    """)

    # -------------------------
    # ENROLLMENTS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            progress INTEGER DEFAULT 0 CHECK(progress BETWEEN 0 AND 100),
            enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(student_id, course_id),

            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    """)

    # -------------------------
    # LEARNING PROGRESS TABLE
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            current_step INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(student_id, course_id),

            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watch_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            lesson_index INTEGER NOT NULL,
            seconds_watched INTEGER DEFAULT 0,
            last_position INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(student_id, course_id, lesson_index),

            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            UNIQUE(student_id, course_id),

            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY(course_id) REFERENCES courses(id) ON DELETE CASCADE
        )
    """)

    # -------------------------
    # INDEXES (Performance)
    # -------------------------
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_enrollment_student ON enrollments(student_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_enrollment_course ON enrollments(course_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_questions_course ON questions(course_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_learning_progress_student_course ON learning_progress(student_id, course_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_watch_progress_student_course ON watch_progress(student_id, course_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_certificates_student_course ON certificates(student_id, course_id)")

    # -------------------------
    # DEFAULT COURSES
    # -------------------------
    courses = [
        ("Python Programming", "Learn Python from basics", "Programming", ""),
        ("Machine Learning", "Intro ML concepts", "AI", ""),
        ("Web Development", "HTML CSS JS Flask", "Development", ""),
        ("Data Science", "Data analysis and visualization", "Data", ""),
        ("Artificial Intelligence", "AI fundamentals", "AI", ""),
        ("Deep Learning", "Neural networks and DL", "AI", ""),
        ("SQL & Databases", "Database design and SQL", "Database", ""),
        ("Cyber Security", "Security and ethical hacking", "Security", ""),
        ("Cloud Computing", "AWS Azure cloud basics", "Cloud", ""),
        ("Java Programming", "Core Java concepts", "Programming", ""),
        ("C Programming", "Programming fundamentals", "Programming", ""),
        ("Data Structures", "DSA concepts", "Computer Science", ""),
        ("Operating Systems", "OS fundamentals", "Computer Science", ""),
        ("Computer Networks", "Networking basics", "Computer Science", ""),
        ("DevOps", "CI/CD and deployment", "Cloud", "")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO courses
        (course_name, description, category, image_url)
        VALUES (?, ?, ?, ?)
    """, courses)

    # Insert auto questions
    insert_default_questions(cursor)

    conn.commit()
    conn.close()
