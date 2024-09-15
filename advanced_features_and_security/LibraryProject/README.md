# LibraryProject

This is a Django project called `LibraryProject` that includes an app named `bookshelf`.

## Project Structure

- `bookshelf/`: Contains the core application files for managing books.
- `bookshelf/models.py`: Defines the `Book` model for storing book information.
- `bookshelf/views.py`: Contains views like `book_list` to display books.
- `bookshelf/urls.py`: URL routing for the `bookshelf` app.

## Features

- **Book Management**: Add, edit, and view books in the library.
- **Custom User Model**: A custom user model is implemented for managing user data.
- **Permissions and Groups**: Implemented permissions and groups to control access to different parts of the application.

## Setup

1. Clone the repository.
2. Install the dependencies.
3. Run the migrations.
4. Start the development server.

## Usage

- Access the book list at `/books/`.
- Admin users can manage books via the Django admin interface.

