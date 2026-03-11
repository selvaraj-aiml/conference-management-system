# Conference Management System (ConfSys)

A complete, production-ready Django web application for managing academic conferences.

## ✨ Features
- Role-based authentication (Admin, Author, Reviewer, Participant)
- Paper submission with PDF upload
- Reviewer assignment & review workflow
- Conference session creation & paper scheduling
- Author can withdraw papers
- Admin can cancel sessions and delete papers
- Participant schedule view + registration
- Modern, animated, responsive UI (custom CSS + Font Awesome)

## 🛠 Tech Stack
- **Backend**: Django 5.2
- **Database**: SQLite (easy to switch to PostgreSQL)
- **Frontend**: HTML, CSS (modern design system), JavaScript
- **Authentication**: Custom User Model

## 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/conference-management-system.git
cd conference-management-system

# 2. Create virtual environment
conda create -n confsys python=3.11
conda activate confsys

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Create admin account
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
