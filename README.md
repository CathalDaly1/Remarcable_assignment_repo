## Music Store - Product Search Project

## Overview
Music Store - Product Search is a web application that allows users to browse and filter a catalog of music-related 
products (e.g., instruments, vinyl records). Built with Django, it includes:

1. Search Functionality: Filter products by description, category, and tags.
2. Pagination: Displays results in manageable chunks (5 products per page).
3. Optimized Queries: Uses select_related and prefetch_related to minimize database queries.

## Features:
1. Product Search: Search by description (e.g., "guitar" returns "Electric Guitar," "Acoustic Guitar").
2. Filters: Combine category (e.g., "Instruments") and tag (e.g., "new-release") filters with search terms.
3. Pagination: Limits results to 5 per page with "Previous" and "Next" navigation.
4. Query Efficiency: Reduces queries from 40+ to ~4 using select_related and prefetch_related.

## Performance Optimizations
- **Indexed `description` Field**: Added `db_index=True` to the `description` field in the `Product` model to optimize `icontains` searches. This reduces potential full-table scans from O(n) to faster index-based lookups (closer to O(log n)) as the dataset grows, significantly improving search performance for large product catalogs.
- **Query Optimization with `select_related`**: Used `select_related('category')` to fetch the related `Category` objects in a single SQL query, avoiding N+1 query problems when accessing the category for each product.
- **Query Optimization with `prefetch_related`**: Applied `prefetch_related('tags')` to efficiently fetch all related `Tag` objects in one query, optimizing the many-to-many relationship access and reducing database hits.
- **Efficient Filter Options**: Limited `categories` and `tags` querysets to only those with associated products using `filter(product__isnull=False).distinct()`, preventing empty options in the UI and reducing unnecessary data retrieval.
- **Pagination**: Limits results to 5 per page with "Previous" and "Next" navigation.

Use of AI Generated Code:
\products\management\commands\insert_data_script.py
I used an artificial intelligence code generator to insert data into the 
Seeds the database with predefined music-related data (categories, tags, products) 
or clears all existing data, based on a command-line option.

I used this in order to quickly automate the process of inserting these records in to the database. 


Project Structure:
remarcable_django_app
├── manage.py
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Product, Category, Tag models
│   ├── insert_data_script.py     # Database population script
│   ├── templates/
│   │   └── products/
│   │       └── search.html  # Main template with CSS
│   ├── tests.py            # Tests
│   └── views.py         # product_search view
├── remarcable_assignment/
│   ├── __init__.py
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   └── wsgi.py
├── db.sqlite3           # SQLite database
└── READ.ME     # Read me document

Instructions to Run "Music Store Search"
1. Clone the repository
 git clone https://github.com/CathalDaly1/Remarcable_assignment_repo.git
cd Remarcable_assignment_repo

2. Set Up and activate the Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Database Migrations
python manage.py migrate

5. Seed the Database
cd products/managemement/commands/
python manage.py insert_data_script.py

6. Create a superuser(for admin access) 
    `python manage.py createsuperuser`

7. Start the Development Server
python manage.py runserver

8. Access the Application
http://127.0.0.1:8000/
