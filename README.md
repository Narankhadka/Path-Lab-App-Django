# 🧪 Lab Tech – Path Lab Management System

## 📝 Project Overview

**Lab Tech** is an industry-aligned backend API for a pathology laboratory management system. Built using **Django** and **Django REST Framework (DRF)**, it provides a secure, scalable, and maintainable foundation for managing **patients**, **laboratory tests**, and **diagnostic reports**.

The system is designed with clean architecture principles and RESTful best practices, making it suitable for academic projects as well as real-world backend service development.

---

## ✨ Key Features

* Patient registration and record management
* Centralized catalog of pathology tests
* Generation and storage of lab reports
* RESTful API with versioning support (`/api/v1/`)
* Interactive API documentation using Swagger & ReDoc
* Modular, scalable project structure

---

## 🛠️ Technology Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework (DRF)
* **API Documentation:** drf-yasg (Swagger / OpenAPI)
* **Database:** SQLite (development) / PostgreSQL (production-ready)
* **Authentication:** Django authentication system (extendable)

---

## 🚀 Setup & Installation

### 1️⃣ Environment Initialization

Create and activate a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install required dependencies:

```bash
pip install django djangorestframework drf-yasg
```

---

### 2️⃣ Database Configuration

Prepare the database and admin access:

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser
```

---

### 3️⃣ Run the Application

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

---

## 📁 Project Structure

The project follows modular and industry-standard Django practices:

```
labtech/
├── labtech/          # Project settings, URLs, and configuration
├── app/              # Core application (models, serializers, viewsets)
├── templates/        # HTML templates (optional frontend support)
├── static/           # Static assets (CSS, JS, images)
└── media/            # Uploaded and generated lab reports
```

---

## 🔌 API Architecture

### API Versioning

All endpoints are prefixed with:

```
/api/v1/
```

This ensures backward compatibility and long-term maintainability.

### Core Entities

* **Patients** – Personal and medical identification details
* **Tests** – Available pathology and diagnostic tests
* **Lab Reports** – Reports linking Patients and Tests via foreign keys

---

### 📡 API Endpoints

| Method | Endpoint            | Description                    |
| ------ | ------------------- | ------------------------------ |
| GET    | `/api/v1/patients/` | List all registered patients   |
| POST   | `/api/v1/patients/` | Register a new patient         |
| GET    | `/api/v1/tests/`    | View available lab tests       |
| POST   | `/api/v1/reports/`  | Generate and store lab reports |

---

## 🧾 API Documentation & Testing

The API is fully documented and easy to test using the following tools:

* **Swagger UI:**

  ```
  http://127.0.0.1:8000/swagger/
  ```
* **ReDoc:**

  ```
  http://127.0.0.1:8000/redoc/
  ```
* **Postman:** All endpoints are Postman-compatible for external testing

---

## 🛡️ Best Practices Implemented

* **Security:** Authentication-ready architecture to prevent unauthorized access
* **Data Integrity:** DRF serializers enforce strict validation rules
* **Scalability:** ViewSets and Routers ensure clean and maintainable URLs
* **Clean Code:** Separation of concerns using Django app architecture

---

## 📌 Future Enhancements

* Role-based access control (Admin, Lab Technician, Doctor)
* PDF-based lab report generation
* Audit logs for report access
* Deployment with Docker and PostgreSQL

---

## 📄 License

This project is developed for educational and demonstration purposes. You are free to extend and customize it as required.

---

**Developed with Django & DRF for modern backend systems**
