from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reviewer', 'Reviewer'),
        ('participant', 'Participant'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='participant')

    def __str__(self):
        return f"{self.username} ({self.role})"


    def get_dashboard_url(self):
        if self.role == "admin":
            return "/admin-dashboard/"
        elif self.role == "author":
            return "/author-dashboard/"
        elif self.role == "reviewer":
            return "/reviewer-dashboard/"
        else:
            return "/participant-dashboard/"