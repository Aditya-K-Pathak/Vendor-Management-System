---

# Vendor Management System with Performance Metrics

## Overview
The Vendor Management System (VMS) with Performance Metrics is a web application built using Django and Django REST Framework. It provides a platform for managing vendor profiles, tracking purchase orders, and evaluating vendor performance metrics. The system is designed to adhere to RESTful principles, implement comprehensive data validations, and utilize Django ORM for database interactions.
The code is hosted on https://aditya28704.pythonanywhere.com/
You can also read the documentation on https://aditya28704.pythonanywhere.com/docs

## Core Features
1. **Vendor Profile Management:**
   - Create, retrieve, update, and delete vendor profiles.
   - Each vendor profile includes name, contact details, address, and a unique vendor code.

2. **Purchase Order Tracking:**
   - Track purchase orders with details such as PO number, vendor reference, order date, items, quantity, and status.
   - View, create, retrieve, update, and delete purchase orders.
   - Filter purchase orders by vendor.

3. **Vendor Performance Evaluation:**
   - Calculate performance metrics for vendors, including:
     - On-Time Delivery Rate
     - Quality Rating
     - Response Time
     - Fulfilment Rate
   - View performance metrics for each vendor.

## Technologies Used
- Django: Web framework for building the backend of the application.
- Django REST Framework: Toolkit for building Web APIs.
- SQLite: Relational database management system used for storing data.
- Python: Programming language for backend development.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Aditya-K-Pathak/Vendor-Management-System/
   cd vendor-management-system
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```
5. Access the application at `http://localhost:8000`.

## Security
The application implements token-based authentication to secure API endpoints. Users need to authenticate with a valid token to access protected resources. Additionally, the application follows best practices for securing data and preventing common security vulnerabilities.

## API Endpoints
- **Vendor Profile Registeration:**
  - `POST /api/user/`: Create a new authorization token
    
- **Vendor Profile Management:**
  - `POST /api/vendors/`: Create a new vendor.
  - `GET /api/vendors/`: List all vendors.
  - `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
  - `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
  - `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

- **Purchase Order Tracking:**
  - `POST /api/purchase_orders/`: Create a purchase order.
  - `GET /api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
  - `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
  - `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
  - `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

- **Vendor Performance Evaluation:**
  - `GET /api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

## Implementation/ Code
- **User Registration**
```
import requests

def register_user(username, email, password):
    url = 'http://localhost:8000/api/user/'
    data = {'username': username, 'email': email, 'password': password}
    response = requests.post(url, data=data)
    if response.status_code == 201:
        print("User registered successfully.")
        return response.json().get('token')
```

- **Vendor Operation**
```
import requests

# Base URL of the API
base_url = 'http://localhost:8000/api/'

# Token for authentication (replace 'YOUR_TOKEN_HERE' with the actual token)
token = 'YOUR_TOKEN_HERE'

# Function to register a new vendor
def register_vendor(vendor_name, contact_number, address):
    url = base_url + 'vendors/'
    headers = {'Authorization': f'Token {token}'}
    data = {
        'vendor_name': vendor_name,
        'contact_number': contact_number,
        'address': address
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# Function to retrieve all vendors
def get_all_vendors():
    url = base_url + 'vendors/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Function to retrieve details of a specific vendor
def get_vendor(vendor_id):
    url = base_url + f'vendors/{vendor_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Function to update details of a specific vendor
def update_vendor(vendor_id, data):
    url = base_url + f'vendors/{vendor_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.put(url, headers=headers, data=data)
    return response.json()

# Function to delete a specific vendor
def delete_vendor(vendor_id):
    url = base_url + f'vendors/{vendor_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.delete(url, headers=headers)
    return response.status_code

```

## For Purchase Orders 
```
import requests

# Base URL of the API
base_url = 'http://localhost:8000/api/'

# Token for authentication (replace 'YOUR_TOKEN_HERE' with the actual token)
token = 'YOUR_TOKEN_HERE'

# Function to create a new purchase order
def create_purchase_order(vendor_code, order_status, items, quantity):
    url = base_url + 'purchase_orders/'
    headers = {'Authorization': f'Token {token}'}
    data = {
        'vendor_code': vendor_code,
        'items': '{"item1": 1, "item2": 1}',
        'quantity': quantity
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

# Function to retrieve all purchase orders
def get_all_purchase_orders():
    url = base_url + 'purchase_orders/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Function to retrieve details of a specific purchase order
def get_purchase_order(po_id):
    url = base_url + f'purchase_orders/{po_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Function to update details of a specific purchase order
def update_purchase_order(po_id, data):
    url = base_url + f'purchase_orders/{po_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.put(url, headers=headers, data=data)
    return response.json()

# Function to delete a specific purchase order
def delete_purchase_order(po_id):
    url = base_url + f'purchase_orders/{po_id}/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.delete(url, headers=headers)
    return response.status_code

```

## Vendor's Performance
```
import requests

# Base URL of the API
base_url = 'http://localhost:8000/api/'

# Token for authentication (replace 'YOUR_TOKEN_HERE' with the actual token)
token = 'YOUR_TOKEN_HERE'

# Function to retrieve performance metrics of a specific vendor
def get_vendor_performance(vendor_id):
    url = base_url + f'vendors/{vendor_id}/performance/'
    headers = {'Authorization': f'Token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

```

## Authors
- [Aditya Pathak]([https://github.com/author](https://github.com/Aditya-K-Pathak))

---
