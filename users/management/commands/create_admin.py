import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates superuser from environment variables'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('DJANGO_ADMIN_USERNAME', 'admin')
        email = os.environ.get('DJANGO_ADMIN_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_ADMIN_PASSWORD', 'admin123')

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.role != 'admin':
                user.role = 'admin'
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Fixed role for "{username}" to admin.'))
            else:
                self.stdout.write(self.style.SUCCESS(f'User "{username}" already exists with correct role.'))
            return

        User.objects.create_superuser(username=username, email=email, password=password, role='admin')
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created with admin role.'))
