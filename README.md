# Django Category Project

This project is a Django application that manages categories and subcategories. It uses Django framework and MySQL as the database.

## Project Structure

The project consists of the following main files:

1. `models.py`: Defines the Category model
2. `views.py`: Contains views for handling category-related operations
3. `urls.py`: Defines URL patterns for the application
4. `categories.html`: Template for rendering the category selector

## Setup

1. Ensure you have Python and Django installed on your system.
2. Set up a MySQL database for the project.
3. Update the database settings in your project's `settings.py` file to connect to your MySQL database.
4. Run migrations to create the necessary database tables:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the Django development server:
   ```
   python manage.py runserver
   ```

## Functionality

### Models

The `Category` model is defined in `models.py`:

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

This model allows for creating hierarchical categories with a self-referential foreign key.

### Views

Two main views are implemented in `views.py`:

1. `category_selector`: Renders the main page with top-level categories.
2. `get_subcategories`: An AJAX view that returns subcategories for a given parent category.

### URLs

The URL patterns are defined in `urls.py`:

- `/`: The main category selector page
- `/get_subcategories/`: Endpoint for fetching subcategories

## Usage

1. Access the main page to view the top-level categories.
2. Use the category selector to navigate through the category hierarchy.
3. The subcategories are loaded dynamically using AJAX calls to the `get_subcategories` view.

## Database Structure and Test Data

The project uses a hierarchical structure for categories, allowing for multiple levels of subcategories. To test the functionality, we've added sample data to the database. Here's an overview of the test data structure:

- Top-level categories: Category A, Category B
- Subcategories under Category B:
  - SUB Category B1
  - SUB Category B2
    - SUB SUB Category B2-1
    - SUB SUB Category B2-2
      - SUB SUB SUB Category B2-2-1
        - Sub4 B1
        - 4Sub B2

This structure demonstrates the ability to create up to 5 levels of subcategories, showcasing the flexibility of the hierarchical model and we can do any numbers of subcategories.


## Technologies Used

- Django: Web framework for building the application
- MySQL: Database for storing category data
- AJAX: For dynamically loading subcategories without page refresh