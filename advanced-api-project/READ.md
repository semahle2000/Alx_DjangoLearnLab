# Advanced API Project

## Overview
This project is designed to demonstrate the use of Django REST Framework to create an advanced API with custom views and generic views.

## View Configurations

### BookListView
- **Endpoint**: `/api/books/`
- **Methods**: `GET`, `POST`
- **Description**: Handles listing all books and creating a new book.
- **Permissions**: 
  - `GET`: Read-only access for unauthenticated users.
  - `POST`: Full access for authenticated users.

### BookDetailView
- **Endpoint**: `/api/books/<int:pk>/`
- **Methods**: `GET`, `PUT`, `DELETE`
- **Description**: Handles retrieving, updating, and deleting a book by ID.
- **Permissions**: 
  - `GET`: Full access for authenticated users.
  - `PUT`: Full access for authenticated users.
  - `DELETE`: Full access for authenticated users.

## Permissions
- **IsAuthenticatedOrReadOnly**: Allows read-only access to unauthenticated users and full access to authenticated users.
- **IsAuthenticated**: Restricts access to authenticated users only.

## Testing
- Use tools like Postman or curl to test the API endpoints.
- Ensure that permissions are enforced correctly by attempting to access endpoints with and without proper credentials.

## Custom Settings
- Custom validation for the `publication_year` field in the `BookSerializer` to ensure it is not in the future.

## Advanced API Project

### Filtering, Searching, and Ordering

#### Filtering
- **Endpoint**: `/api/books/?title=SomeTitle`
- **Description**: Filter books by title.

#### Searching
- **Endpoint**: `/api/books/?search=AuthorName`
- **Description**: Search books by author name.

#### Ordering
- **Endpoint**: `/api/books/?ordering=publication_year`
- **Description**: Order books by publication year.

### Examples
- **Filter by title**: `http://127.0.0.1:8000/api/books/?title=SomeTitle`
- **Search by author name**: `http://127.0.0.1:8000/api/books/?search=AuthorName`
- **Order by publication year**: `http://127.0.0.1:8000/api/books/?ordering=publication_year`