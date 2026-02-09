import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Learning_Djengo.settings")
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = 'admin@123'
email = 'admin@mars.com'

try:
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Updated password for existing details user '{username}'.")
    else:
        User.objects.create_superuser(username, email, password)
        print(f"Created new superuser '{username}'.")
except Exception as e:
    print(f"Error: {e}")
