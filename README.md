# 🎓 Conference Management System (ConfSys)

> A full-featured, production-ready web application for managing academic conferences — built with Django.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.2-green?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

---

## 📌 About The Project

**ConfSys** is a complete conference management platform where Admins, Authors, Reviewers, and Participants each have their own role-based dashboard and workflow. Built from scratch with Django, it handles the full lifecycle of an academic conference — from paper submission to session scheduling.

This project was built to demonstrate real-world Django skills including custom user models, role-based access control, file uploads, and a modern UI.

---

## ✨ Features

### 👤 Role-Based Authentication
- 4 user roles: **Admin**, **Author**, **Reviewer**, **Participant**
- Each role has its own dedicated dashboard and permissions
- Secure login/logout system with custom user model

### 📄 Paper Submission & Review Workflow
- Authors can **submit papers** with PDF upload
- Admins can **assign reviewers** to submitted papers
- Reviewers can **submit detailed reviews** and recommendations
- Authors can **withdraw** their papers
- Admins can **accept, reject, or delete** papers

### 📅 Session Scheduling
- Admins can **create conference sessions**
- Papers can be **scheduled into sessions**
- Admins can **cancel sessions**
- Participants can **view full schedule**

### 🎨 Modern UI
- Clean, animated, fully responsive design
- Custom CSS design system
- Font Awesome icons throughout
- Mobile-friendly layout

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.2, Python 3.11 |
| Database | SQLite (easily switchable to PostgreSQL) |
| Frontend | HTML5, CSS3, JavaScript |
| Auth | Custom Django User Model |
| File Handling | Django FileField (PDF uploads) |
| Icons | Font Awesome |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- pip or conda

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/selvaraj-aiml/conference-management-system.git
cd conference-management-system

# 2. Create a virtual environment
conda create -n confsys python=3.11
conda activate confsys

# 3. Install dependencies
pip install django

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin superuser
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Then open your browser and go to: **http://127.0.0.1:8000/**

---

## 👥 User Roles — How To Test

| Role | How to Access |
|------|--------------|
| **Admin** | Create via `createsuperuser` command |
| **Author** | Register a new account → select Author role |
| **Reviewer** | Register a new account → select Reviewer role |
| **Participant** | Register a new account → select Participant role |

---

## 📁 Project Structure

```
conference-management-system/
│
├── conference_system/      # Main Django project settings
├── core/                   # Core app (home, dashboard logic)
├── users/                  # Custom user model & authentication
├── papers/                 # Paper submission & review workflow
├── templates/              # All HTML templates
├── manage.py               # Django entry point
└── .gitignore
```

---

## 📸 Screenshots

> _Coming soon — dashboard, paper submission, review panel, and session schedule views_

---

## 🔮 Future Enhancements

- [ ] Email notifications for review decisions
- [ ] PDF certificate generation for participants
- [ ] Payment gateway for conference registration
- [ ] Deploy to Render / Railway (free hosting)
- [ ] Switch database to PostgreSQL for production
- [ ] REST API with Django REST Framework

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it for your own projects.

---

## 👨‍💻 Author

**Selvaraj**  
🔗 GitHub: [@selvaraj-aiml](https://github.com/selvaraj-aiml)

---

> ⭐ If you found this project useful, please give it a star — it helps a lot!
