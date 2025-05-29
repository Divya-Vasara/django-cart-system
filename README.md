# ecommerce_project/README.md
# E-commerce Cart System

This project is a Django-based RESTful API for managing a shopping cart. It includes the ability to add, update, remove, list, clear items, and calculate the total cost for an authenticated user.

## 📁 Project Structure
```
ecommerce_project/
├── cart/               # Cart models, serializers
├── api/                # DRF views
├── ecommerce_project/  # Project settings
└── manage.py
```

## ✅ Features
- Token-based authentication using Django REST Framework
- CRUD operations on cart items
- Clear entire cart
- Calculate total cart price
- RESTful API endpoints secured per-user

## ⚙️ Setup Instructions
```bash
git clone <repo-url>
cd ecommerce_project
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🔐 Authentication Setup
This project uses **Token Authentication** from Django REST Framework.

### Step 1: Generate Token for a User
Run the following in Django shell:
```bash
python manage.py drf_create_token <username>
```
This returns a token like:
```json
{"token": "abc123..."}
```

### Step 2: Use the Token in API Requests
Include the token in the `Authorization` header of your HTTP request:
```
Authorization: Token abc123...
```

## 🚀 API Endpoints
| Method | Endpoint                | Description                    |
|--------|-------------------------|--------------------------------|
| GET    | `/api/cart/`            | List all cart items            |
| POST   | `/api/cart/`            | Add item to cart               |
| PUT    | `/api/cart/<id>/`       | Update item quantity           |
| DELETE | `/api/cart/<id>/`       | Remove item from cart          |
| DELETE | `/api/cart/clear/`      | Clear all items in the cart    |
| GET    | `/api/cart/total/`      | Get total price of cart items  |

## 📌 Sample cURL Request
```bash
curl -X GET http://127.0.0.1:8000/api/cart/ \
  -H 'Authorization: Token abc123...'
```

## 🧪 Bonus Features (Optional/Not Included Yet)
- JWT authentication using `djangorestframework-simplejwt`
- Pagination on the cart listing
- Using a Product model (instead of `product_name`)
- Unit and integration tests

---

**Note:** This is a minimal take-home project designed to showcase your ability to build REST APIs with Django. You may enhance or customize features further.
