## Health_App
### Health App Using Django

1. Created a GitHub repo named Health_App

2. Created a virtual environment:
    ##### python -m venv Myenv

3. Activated the virtual environment:
    ##### Myenv\Scripts\Activate

4. Installed Django inside the virtual environment:
    ##### pip install django

5. Checked Django version to verify installation:
    ##### django-admin --version

6. Created a Django project named Health:
    ##### django-admin startproject Health .

7. Created a Django app named Patients:
    ##### python manage.py startapp Patients

8. Applied initial database migrations:
    ##### python manage.py migrate

9. Added Patients to INSTALLED_APPS in settings.py.

10. Created view functions in Patients/views.py.

11. Created URL patterns in Patients/urls.py.

12. Included Patients URLs in the main project’s urls.py.

13. Created an Images folder and added image files.
