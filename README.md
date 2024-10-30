# Django Recipe and Student Management Application

## Description

This Django application allows users to manage recipes and student information efficiently. Users can create, update, delete recipes, and view student details along with their marks. The application supports user authentication and features a random recipe view count generator.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <project-directory>
2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows use `venv\Scripts\activate`
3. ** Install dependencies: **
   ```bash
   pip install -r requirements.txt
4. ** Apply migrations: **
   ```bash
   python manage.py migrate
5. ** Run the server: **
   ```bash
   python manage.py runserver
6. ** Access the application: **
   Open your web browser and go to http://127.0.0.1:8000/.

## Features
### Recipe Management:

* View all recipes.
* Add new recipes (name, description, image).
* Update existing recipes.
* Delete individual or all recipes.
* Generate random view counts for recipes.

### User Authentication:

* User registration.
* User login/logout functionality.
### Student Management:

* View all students with pagination.
* Search students by name, department, email, or age.
* View individual student marks and calculate total marks.
## API Overview
### Recipes:

* GET /recipe/: List all recipes.
* POST /recipe/: Create a new recipe.
* GET /recipe/update/<id>/: Get details for updating a recipe.
* POST /recipe/update/<id>/: Update a specific recipe.
* POST /recipe/delete/<id>/: Delete a specific recipe.
* POST /recipe/delete_all/: Delete all recipes.
* GET /recipe/random_set/: Generate random view counts for recipes.
### Students:

* GET /students/: List all students with pagination.
* GET /students/search/: Search for students.
* GET /students/<id>/marks/: View marks for a specific student.
## Usage
* Home Page: Access the home page to navigate to various sections.
* Recipes: Manage recipes through the recipe section.
* Students: Access student information and view marks.
## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.


### Instructions
- Replace `<repository-url>` and `<project-directory>` with the actual URL of your repository and the directory name where your project is located.
- Feel free to modify or expand any section to fit your project's specifics better!
