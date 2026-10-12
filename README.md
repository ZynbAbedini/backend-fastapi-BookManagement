# 📚 Book Management API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-In--Memory-blue?style=for-the-badge)

</div>

---

## 🇬🇧 Overview

A lightweight, standard RESTful API for managing books built with **FastAPI** and **Pydantic**. 
Data is managed in-memory without requiring an external database.

### 📌 API Endpoints

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/books` | Retrieve the list of all books | `200 OK` |
| `POST` | `/books` | Add a new book | `201 Created` |
| `GET` | `/books/{id}` | Get details of a specific book | `200 OK` |
| `PATCH` | `/books/{id}` | Partially update book details | `200 OK` |
| `DELETE` | `/books/{id}` | Delete a book by ID | `200 OK` |

### 📖 Interactive Docs
- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`

---

## 🇮🇷 معرفی پروژه (فارسی)

یک وب‌سرویس سریع، ساده و استاندارد برای مدیریت کتاب‌ها (سیستم کتابداری) با استفاده از **FastAPI** و **Pydantic**. 
داده‌ها به صورت In-Memory (در متغیرهای درون برنامه) نگهداری می‌شوند و نیازی به دیتابیس خارجی ندارد.

### 📌 اندپوینت‌های وب‌سرویس

| متد | آدرس | توضیحات | کد وضعیت |
| :--- | :--- | :--- | :--- |
| `GET` | `/books` | دریافت لیست تمامی کتاب‌ها | `200 OK` |
| `POST` | `/books` | افزودن کتاب جدید | `201 Created` |
| `GET` | `/books/{id}` | دریافت اطلاعات یک کتاب با شناسه | `200 OK` |
| `PATCH` | `/books/{id}` | ویرایش مشخصات کتاب (ویرایش جزئی) | `200 OK` |
| `DELETE` | `/books/{id}` | حذف کتاب بر اساس شناسه | `200 OK` |

### 📖 مستندات تعاملی
- **محیط تست سواگر**: `/docs`
- **محیط ریداک**: `/redoc`
