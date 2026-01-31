from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=(
            ('author', 'Author'),
            ('reviewer', 'Reviewer'),
            ('participant', 'Participant'),
        ),
        default='participant'
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Paper(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('assigned', 'Assigned to Reviewer'),
        ('under_review', 'Under Review'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('scheduled', 'Scheduled'),
    )

    title = models.CharField(max_length=255)
    abstract = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='submitted_papers'
    )
    file = models.FileField(upload_to='papers/')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_papers'
    )

    review_comment = models.TextField(blank=True, null=True)
    review_score = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ReviewAssignment(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='review_assignments')
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_reviews'
    )
    feedback = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paper.title} → {self.reviewer.username}"


class ConferenceSession(models.Model):
    SESSION_TYPES = (
        ('KEYNOTE', 'Keynote'),
        ('PRESENTATION', 'Paper Presentation'),
        ('WORKSHOP', 'Workshop'),
        ('PANEL', 'Panel Discussion'),
    )

    title = models.CharField(max_length=200)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    hall = models.CharField(max_length=100, blank=True)
    speaker = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date}"


class PaperPresentation(models.Model):
    paper = models.OneToOneField(
        Paper,
        on_delete=models.CASCADE,
        related_name='presentation_slot'   # ← this is the key for author slot query
    )
    session = models.ForeignKey(
        ConferenceSession,
        on_delete=models.CASCADE,
        related_name='presentations'
    )
    presentation_order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.paper.title} in {self.session.title}"