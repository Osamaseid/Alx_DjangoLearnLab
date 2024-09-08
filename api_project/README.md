# Introduction to Building APIs with Django REST Framework
## Task 0. Setting Up a New Django Project with Django REST Framework
### Objective: 
Begin your journey with Django REST Framework by setting up a new Django project from scratch, specifically for building APIs. This task will introduce you to the initial steps necessary to integrate DRF and prepare for creating API endpoints.

### Task Description:
In this task, you will create a new Django project, configure Django REST Framework, and prepare the environment for future tasks focused on building APIs.

**Step 1: Create a New Django Project**
Start by setting up a new Django project dedicated to API development.
1. Install Django (if not already installed):
```bash
pip install django
```
2. Create the Project:
```bash
django-admin startproject api_project
```
**Step 2: Install Django REST Framework (DRF)**
Add Django REST Framework to your new project to facilitate API development.
1. Install DRF:
```bash
pip install djangorestframework 
```
2. Add DRF to Installed Apps:
. Open api_project/settings.py.
. Add 'rest_framework' to the INSTALLED_APPS list:
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```
**Step 3: Create a New Django App** 
Set up an app within your project that will be specifically used for handling API logic.
1. Create the App:
```bash
cd api_project
python manage.py startapp api
```
2. Add the App to Installed Apps:
. Open api_project/settings.py.
. Add 'api' to the INSTALLED_APPS list:
```bash
INSTALLED_APPS = [
    ...
    'api',
    ...
]
```
**Step 4: Define a Simple Model**
Create a model to be used for your first API. This model will be simple, designed to be easily understood and used in an API.
1. Create the Model:
. Open api/models.py.
. Define the Book model:
```bash
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
```
**Step 5: Run Migrations**
Set up your database tables based on the new models created.
1. Make Migrations:
```bash
python manage.py makemigrations
```
2. Apply Migrations:
```bash
python manage.py migrate
```
**Step 6: Start the Development Server**
Ensure that your setup is correct by running the Django development server.
1. Run the Server:
```bash
python manage.py runserver
```
2. Check the Server:
Open your browser and visit ```bash http://127.0.0.1:8000/ ``` to ensure the server is running correctly.
Your Django project with DRF is now set up and ready for API development!
## Task 1. Building Your First API Endpoint with Django REST Framework
### Objective: 
Develop a simple API endpoint using Django REST Framework that allows clients to retrieve information about books stored in your database. This will introduce you to the core components of DRF, including serializers and views.

### Task Description:
In this task within your newly created api_project, you will set up a basic API endpoint to list all books using Django REST Framework. This will involve creating serializers, views, and routing configurations.

**Step 1: Create the Serializer**
You need a serializer to convert your Book model instances into JSON format.
1. Create `serializers.py`:
. Inside the api app, create a new file named `serializers.py`.
. Define the BookSerializer class to convert Book model instances into JSON format:
```bash
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```
**Step 2: Create the API View**
Set up a view that uses the serializer to retrieve and return book data.
1. Define the View:
. Open `api/views.py`.
. Create a view named BookList that extends ListAPIView:
```bash
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```
**Step 3: Configure URL Patterns**
Ensure the API endpoint is accessible via HTTP by setting up the corresponding URL.
1. Set Up URLs:
.Inside the `api` app, create a file named `urls.py` if it doesn’t already exist.
. Add the URL pattern to route to the BookList view:
```bash
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
```
2. Include URLs in the Project:
. Open `api_project/urls.py`.
. Include the `api` app URLs:
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```
**Step 4: Test the API Endpoint**
After setting up the endpoint, test it to ensure it functions as expected.
1. Run the Server:
```bash
python manage.py runserver
```
2. Test the Endpoint:
. Open your browser or use a tool like Postman to visit http://127.0.0.1:8000/api/books/.
. You should see a JSON list of all books in the database.
**Testing Method:**
Use tools like curl, Postman, or your browser to access the endpoint and verify that it returns a JSON list of books.
## Task 2. Implementing CRUD Operations with ViewSets and Routers in Django REST Framework
### Objective: 
Expand your API functionality by using Django REST Framework’s ViewSets and Routers to implement CRUD (Create, Read, Update, Delete) operations on the Book model. This approach simplifies the management of standard database operations through RESTful APIs.

### Task Description:
In this task, you will replace the simple list view created previously with a full set of CRUD operations using DRF’s ViewSets. This will allow clients to not only retrieve but also create, update, and delete books via your API.

**Step 1: Create a ViewSet**
ViewSets in DRF allow you to consolidate common logic for handling standard operations into a single class that handles all HTTP methods (GET, POST, PUT, DELETE).
1. Define the ViewSet:
. Open `api/views.py`.
. Replace or extend the existing view with a BookViewSet that handles all CRUD operations.
. Use rest_framework.viewsets.ModelViewSet for the ViewSet:
Add this on `api/views.py`
```bash
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```
**Step 2: Set Up a Router**
Routers in DRF automatically determine the URL conf based on your ViewSet.
1. Configure the Router:
. Open `api/urls.py`.
. Import `DefaultRouter` from `rest_framework.routers`.
. Register the `BookViewSet` with the router.
. Update `urls.py` to use the router-generated URLs:
```bash
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
**Step 3: Test CRUD Operations**
Ensure that each of the CRUD operations works as expected. Test creating, retrieving, updating, and deleting books through your API.
**Testing Method:**
Use tools like Postman or curl to send POST, GET, PUT, and DELETE requests to your API endpoints and verify the responses.
1. **Prerequisites**
 . Ensure your Django development server is running by using:
 ```bash
 python manage.py runserver
```
. Your server should be accessible at ```bash http://127.0.0.1:8000/```.
1.1 Test Create (POST Request)
. Objective: Add a new book to the database.
. Endpoint: `http://127.0.0.1:8000/books/`
. Method: **POST**
. Body: JSON containing the book details (e.g., title and author).
**Using Postman:**
. Open Postman and set the request type to **POST**.
. Enter the URL: `http://127.0.0.1:8000/books/`.
. Go to the **Body** tab, select **raw**, and choose **JSON** format.
. Input the JSON data:
```bash
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```
. Click **Send**.
. If successful, you'll receive a 201 Created status with the book details in the response.
**Using `curl`:**
```bash
curl -X POST http://127.0.0.1:8000/books/ -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}'
```
1.2. Test Retrieve (GET Request)
. Objective: Fetch the list of books or a specific book.
. Endpoint:
  . For all books: `http://127.0.0.1:8000/books/`
  . For a specific book: `http://127.0.0.1:8000/books/<id>/` (replace `<id>` with the actual book ID)
. Method: **GET**
**Using Postman:**
. Set the request type to **GET**.
. Enter the URL for all books: `http://127.0.0.1:8000/books/`.
. Click **Send** to view the list of books.
. For a specific book, enter the URL with the ID: `http://127.0.0.1:8000/books/1/` and click **Send**.
**Using `curl`:**
```bash
curl http://127.0.0.1:8000/books/
curl http://127.0.0.1:8000/books/1/
```
1.3. Test Update (PUT Request)
.Objective: Update an existing book’s details.
. Endpoint: `http://127.0.0.1:8000/books/<id>/` (replace `<id>` with the actual book ID)
. Method: **PUT**
. Body: JSON containing the updated book details.
**Using Postman:**
. Set the request type to **PUT**.
. Enter the URL: `http://127.0.0.1:8000/books/1/`.
. Go to the **Body** tab, select **raw**, and choose **JSON** format.
. Input the JSON data with updated details:
```bash
{
    "title": "The Great Gatsby (Updated)",
    "author": "F. Scott Fitzgerald"
}
```
. Click **Send**.
. If successful, you’ll receive a 200 OK status with the updated book details.
**Using `curl`:**
```bash
curl -X PUT http://127.0.0.1:8000/books/1/ -H "Content-Type: application/json" -d '{"title": "The Great Gatsby (Updated)", "author": "F. Scott Fitzgerald"}'
```
1.4. Test Delete (DELETE Request)
. Objective: Remove a book from the database.
. Endpoint: `http://127.0.0.1:8000/books/<id>/` (replace `<id>` with the actual book ID)
. Method: **DELETE**
**Using Postman:**
. Set the request type to **DELETE**.
. Enter the URL: `http://127.0.0.1:8000/books/1/`.
. Click **Send**.
If successful, you'll receive a 204 No Content status indicating the book has been deleted.
**Using `curl`:**
```bash
curl -X DELETE http://127.0.0.1:8000/books/1/
```
## Task 3. Implementing Authentication and Permissions in Django REST Framework
### Objective:
Secure your API endpoints by implementing various authentication schemes and permission settings in Django REST Framework. This task will ensure that only authorized users can access and modify data through your API.

### Task Description:
For this task within your api_project, you will add authentication and permission layers to your existing API endpoints. This will involve configuring DRF to use token authentication and setting up permission classes to restrict access based on user roles or authentication status.

**Step 1: Configure Authentication**
Set up token authentication in DRF, allowing your API to handle and verify tokens for authenticated requests.
1. Install the Token Authentication Package
. Ensure that the `rest_framework.authtoken` package is installed and added to your `INSTALLED_APPS`.
. Update `settings.py`:
```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    ...
]
```
2. Run Migrations
Create the necessary database tables for token management by running:
```bash
python manage.py migrate
```
3. Update DRF Settings
Configure DRF to use token authentication. Update `DEFAULT_AUTHENTICATION_CLASSES` in `settings.py`:
```bash
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```
**Step 2: Generate and Use Tokens**
1. Create a Token Retrieval Endpoint
Use DRF’s built-in view for token retrieval. Add the following to your `api/urls.py`:
```bash
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # other paths...
]
```
2. Test Token Retrieval
Use Postman to send a POST request to `http://127.0.0.1:8000/api-token-auth/` with the following body parameters:
```bash
{
    "username": "your_username",
    "password": "your_password"
}
```
If successful, you will receive a token in the response.
**Step 3: Define Permission Classes**
1. Update ViewSets with Permissions
Modify your `BookViewSet` to include permission classes. For example, you can use   `IsAuthenticated` to ensure that only authenticated users can access the views.
In `api/views.py`:
```bash
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
```
**Step 4: Test Authentication and Permissions**
1. Testing with Postman
**Without Token:** Send a `GET` request to `http://127.0.0.1:8000/api/books/` without an authentication token. You should receive a `403 Forbidden` response.
**With Token:** Send a `GET` request to `http://127.0.0.1:8000/api/books/` with the token in the `Authorization` header:
```bash
Authorization: Token <your_token>
```
You should receive the expected response if the token is valid.
**Create, Update, and Delete:** Test **`POST`**, **`PUT`**, and **`DELETE`** requests similarly, ensuring that you have the correct permissions set up for each operation.

