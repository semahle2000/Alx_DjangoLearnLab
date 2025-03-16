import os
import subprocess

def check_django_version():
    try:
        version = subprocess.check_output(['python', '-m', 'django', '--version']).decode().strip()
        print(f"Django version: {version}")
    except subprocess.CalledProcessError:
        print("Django is not installed.")

def run_server_check():
    try:
        subprocess.check_call(['python', 'manage.py', 'runserver'])
    except subprocess.CalledProcessError:
        print("Failed to start the Django development server.")

if __name__ == "__main__":
    check_django_version()
    run_server_check()