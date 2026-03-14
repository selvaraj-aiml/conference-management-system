# Conference Management System

A Django web application that handles the full lifecycle of an academic conference — from paper submission and peer review to session scheduling and participant access.

---

## What it does

Running an academic conference involves a lot of moving parts. This system keeps it organized by giving each type of user exactly what they need, nothing more.

**Admins** control everything — they assign reviewers to papers, make accept/reject decisions, build the conference schedule, and manage users across all roles.

**Authors** submit their research papers (PDF), track review status, and get notified on decisions.

**Reviewers** access the papers assigned to them, submit detailed reviews, and make accept/reject recommendations.

**Participants** browse the finalized conference schedule and see which papers are in which sessions.

---

## Features

- Role-based access with four distinct user types (Admin, Author, Reviewer, Participant)
- PDF paper submission workflow
- Admin-controlled reviewer assignment
- Structured review and recommendation system
- Accept/reject decision flow managed by admins
- Conference session creation and paper-to-session assignment
- Clean per-role dashboards

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Auth | Custom Django User Model |

---

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/selvaraj-aiml/conference-management-system.git
cd conference-management-system
```

**2. Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install django
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create an admin account**
```bash
python manage.py createsuperuser
```

**6. Start the server**
```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Project Structure

```
conference-management-system/
├── conference_system/   # Project settings and URL config
├── core/                # Dashboards and main views
├── users/               # Custom user model and authentication
├── papers/              # Submission and review workflow
├── templates/           # HTML templates
└── manage.py
```

---

## Roadmap

- [ ] Email notifications on review decisions
- [ ] Conference registration and attendance tracking
- [ ] REST API using Django REST Framework
- [ ] Cloud deployment (Railway / Render)

---

## Author

**Selvaraj**  
[GitHub](https://github.com/selvaraj-aiml) · [LinkedIn](https://linkedin.com/in/selvaraj-aiml)
