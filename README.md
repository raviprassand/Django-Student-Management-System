## Setup Process

1. **Cloning the Repository**:
   - Clone the project repository using the following command:
     ```bash
     git clone https://github.com/username/repository.git
     ```

2. **Creating a Virtual Environment**:
   - Navigate to the project directory and create a virtual environment to isolate the dependencies:
     ```bash
     python -m venv venv
     ```

3. **Activating the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Installing Dependencies**:
   - Install all required dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Applying Database Migrations**:
   - Apply the initial migrations to set up the database schema:
     ```bash
     python manage.py migrate
     ```

6. **Creating a Superuser**:
   - Create an admin user to access the Django admin panel:
     ```bash
     python manage.py createsuperuser
     ```

7. **Running the Development Server**:
   - Start the server and access the project at `http://127.0.0.1:8000`:
     ```bash
     python manage.py runserver
     ```

Homepage: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/

## Challenges Encountered

1. **Admin Redirect Issue**:
   - **Problem**: When initially running the project, accessing `http://127.0.0.1:8000` redirected to the home page instead of the admin page.
   - **Solution**: Added proper routing in the `urls.py` file to ensure the `/admin/` URL works as expected.

2. **Database Migration Errors**:
   - **Problem**: Errors while migrating due to unrecognized or conflicting migrations.
   - **Solution**: Resolved by checking for missing models and recreating migrations.
