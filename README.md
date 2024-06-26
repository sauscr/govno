# SITE FOR USPTU
1. Open terminal inside the `backend` dir.
2. Create (if not exists) and activate virtual environment.
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run server:

    ```bash
    python manage.py runserver
    ```
