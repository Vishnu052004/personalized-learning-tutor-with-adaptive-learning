# 🎓 Personalized Learning Tutor with Adaptive Learning

An AI-assisted tutoring platform that adjusts course difficulty and learning paths for each student based on their quiz performance — built as a 4-member team's major project.

> 📌 **My role:** Backend architecture — Flask app logic, MySQL/SQLite schema design, adaptive test-staging engine, and progress-tracking system. *(edit this line to reflect exactly what you built vs. teammates)*

---

## ✨ What It Does

- **Adaptive assessments** — students take entry, checkpoint, and final tests per course; question sets and difficulty scale based on stage
- **Auto-generated learning paths** — course content adapts to the student's level (Beginner / Intermediate / Advanced) based on test scores
- **Progress tracking** — tracks watch time, lesson completion, and step-by-step progress per student per course
- **Certificates** — auto-issued on completing a course's final assessment, viewable per student
- **Course enrollment & dashboard** — students enroll, track multiple courses, and see aggregate stats (avg. score, total watch time, courses completed)

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python, Flask (REST endpoints), Flask-CORS |
| Database | SQLite / MySQL |
| Frontend | HTML, CSS, JavaScript (Jinja2 templates) |
| ML / Logic | Scikit-learn, NumPy, Pandas (adaptive engine) |
| Visualization | Matplotlib / Chart.js |

---

## 🚀 Running It Locally

```bash
# Clone the repo
git clone https://github.com/Vishnu052004/personalized-learning-tutor-with-adaptive-learning.git
cd personalized-learning-tutor-with-adaptive-learning

# Install dependencies
pip install -r requirements.txt

# Set environment variable (optional, has a dev default)
export FLASK_SECRET_KEY="your-secret-key"

# Run the app
python app.py
```

App runs at `http://localhost:5000` by default.

---

## 📸 Screenshots

*(Add 2-4 screenshots here — dashboard, adaptive test screen, learning path, certificate. This is the single biggest thing missing from most student GitHub repos — recruiters decide whether to read further based on whether they can **see** the product.)*

---

## 🧠 How the Adaptive Engine Works

1. Student takes an **entry test** on enrolling in a course
2. Score determines starting **level** (Beginner / Intermediate / Advanced)
3. As the student progresses, **checkpoint tests** re-evaluate performance and can adjust difficulty
4. A **final test** determines certificate eligibility and score
5. Learning path content (lessons, ordering) is served based on current level

---

## 📂 Project Structure

```
├── app.py                 # Main Flask app & routes
├── database.py             # DB connection & schema init
├── videos_data.py          # Course/lesson content mapping
├── templates/               # Jinja2 HTML templates
└── requirements.txt
```

---

## 🔒 Known Limitations / Roadmap

- [ ] Password hashing (currently plaintext — planned fix using Werkzeug security)
- [ ] Migrate from SQLite to production MySQL setup
- [ ] Add unit tests
- [ ] Deploy live demo (Render/Railway)

*(Being upfront about limitations reads as engineering maturity, not weakness — recruiters trust profiles that show self-awareness over ones that claim everything is perfect.)*

---

## 👥 Team

Built as a major project at JB Institute of Engineering & Technology, under guidance of Mrs. Zohra Naval, Assistant Professor.

---

## 📬 Contact

**Koleti Vishnuvardhan**
📧 vishnuvardhankoleti@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/koleti-vishnuvardhan-7248a629a)
