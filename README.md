<div align="center">

# 🎓 Conference Management System

**A full-stack Django web application that handles the complete lifecycle
of an academic conference — from paper submission and peer review
to session scheduling and participant access.**

[![Live Demo](https://img.shields.io/badge/🌐%20Live%20Demo-Visit%20Now-2ea44f?style=for-the-badge)](https://conference-management-system-st2e.onrender.com)
[![GitHub](https://img.shields.io/badge/Source%20Code-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/selvaraj-aiml/conference-management-system)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)

</div>

---

## 🔑 Demo Credentials

| Role | Username | Password |
|---|---|---|
| Admin | admin | admin123 |
| Author | Register a new account | Select Author role |
| Reviewer | Register a new account | Select Reviewer role |
| Participant | Register a new account | Select Participant role |

---

## 💡 What It Does

Running an academic conference involves a lot of moving parts.
This system keeps it organized by giving each type of user
exactly what they need — nothing more.

| Role | What They Can Do |
|---|---|
| 🛡️ **Admin** | Assign reviewers · Make accept/reject decisions · Build schedule · Manage all users |
| ✍️ **Author** | Submit research papers (PDF) · Track review status · Get decisions |
| 🔍 **Reviewer** | Access assigned papers · Submit detailed reviews · Make recommendations |
| 👥 **Participant** | Browse finalized schedule · See papers in each session |

---

## ⚡ Features

- Role-based access with four distinct user types
- PDF paper submission workflow
- Admin-controlled reviewer assignment
- Structured review and recommendation system
- Accept / reject decision flow managed by admins
- Conference session creation and paper scheduling
- Clean per-role dashboards
- Deployed to production on Render

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python · Django 5.2 |
| Database | SQLite |
| Frontend | HTML · CSS · JavaScript |
| Auth | Custom Django User Model |
| Deployment | Render · Gunicorn · WhiteNoise |

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/selvaraj-aiml/conference-management-system.git
cd conference-management-system
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install django
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create admin account**
```bash
python manage.py createsuperuser
```

**6. Start the server**
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Project Structure
```text
conference-management-system/
├── conference_system/   → Project settings and URL config
├── core/                → Dashboards and main views
├── users/               → Custom user model and authentication
├── papers/              → Submission and review workflow
├── templates/           → HTML templates
└── manage.py
```

---

## 🗺️ Roadmap

- [x] Role-based authentication system
- [x] Paper submission and review workflow
- [x] Session scheduling
- [x] Production deployment on Render
- [ ] Email notifications on review decisions
- [ ] REST API using Django REST Framework
- [ ] Switch database to PostgreSQL
- [ ] Cloud deployment on AWS

---

## 👨‍💻 Author

<div align="center">

**Selvaraj**
*AI/ML Engineer · Backend Developer · Problem Solver*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-selvaraj--aiml-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/selvaraj-aiml)
[![GitHub](https://img.shields.io/badge/GitHub-selvaraj--aiml-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/selvaraj-aiml)

⭐ *If this project helped you, give it a star — it means a lot!*

</div>
