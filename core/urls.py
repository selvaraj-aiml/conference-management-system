from django.urls import path
from . import views

from users.views import add_user, submit_paper

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('author-dashboard/', views.author_dashboard, name="author_dashboard"),
    path('reviewer-dashboard/', views.reviewer_dashboard, name="reviewer_dashboard"),
    path('participant-dashboard/', views.participant_dashboard, name="participant_dashboard"),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-users/update/<int:user_id>/', views.update_user, name='update_user'),
    path('manage-users/add/', add_user, name='add_user'),
    path('author/submit-paper/', submit_paper, name='submit_paper'),
    path('review-paper/<int:paper_id>/', views.review_paper, name='review_paper'),
    path('sessions/', views.admin_session_list, name='admin_session_list'),
    path('sessions/add/', views.admin_session_create, name='admin_session_create'),
    path('sessions/<int:session_id>/edit/', views.admin_session_edit, name='admin_session_edit'),
    path('admin/assign-paper/<int:paper_id>/', views.admin_assign_paper_to_session, name='admin_assign_paper_to_session'),
]