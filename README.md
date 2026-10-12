# 📚 Library Management API (FastAPI)

یک وب سرویس ساده، استاندارد و سریع برای مدیریت کتاب‌ها (سیستم کتابداری) با استفاده از **FastAPI** و **Pydantic**. 
داده‌ها به صورت In-Memory (در متغیرهای درون حافظه) ذخیره می‌شوند و نیازی به پایگاه داده خارجی ندارد.

---

## 🚀 ویژگی‌ها (Features)

- معماری ساده و استاندارد مطابق مستندات رسمی FastAPI
- اعتبارسنجی داده‌ها (Data Validation) با استفاده از **Pydantic v2**
- مدیریت کدهای وضعیت HTTP استاندارد (`200 OK`, `201 Created`, `404 Not Found`, `409 Conflict`)
- پشتیبانی از ویرایش جزئی با متد `PATCH`
- داکیومنت تعاملی خودکار Swagger UI و ReDoc

---

## 📌 اندپوینت‌های API (Endpoints)

| متد (Method) | مسیر (Path) | توضیح (Description) | کد وضعیت موفق |
| :--- | :--- | :--- | :--- |
| **GET** | `/books` | دریافت لیست تمام کتاب‌ها | `200 OK` |
| **POST** | `/books` | افزودن یک کتاب جدید | `201 Created` |
| **GET** | `/books/{id}` | دریافت اطلاعات یک کتاب با شناسه خاص | `200 OK` |
| **PATCH** | `/books/{id}` | به‌روزرسانی مشخصات یک کتاب (ویرایش جزئی) | `200 OK` |
| **DELETE** | `/books/{id}` | حذف یک کتاب بر اساس شناسه | `200 OK` |

---

## 📋 ساختار داده‌ها (Data Schema)

### مدل کتاب (`Book`):
```json
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925
}
```

### نمونه بدنه ویرایش (`PATCH /books/{id}`):
در متد PATCH تمام فیلدها اختیاری (Optional) هستند:
```json
{
  "title": "New Title"
}
```

---

## 🛠 راه‌اندازی و اجرا (Installation & Run)

### ۱. پیش‌نیازها
- پایتون نسخه 3.10 به بالا

### ۲. نصب وابستگی‌ها
اگر از `pip` معمولی استفاده می‌کنید:
```bash
pip install -r requirements.txt
```

یا اگر از `uv` استفاده می‌کنید:
```bash
uv pip install -r requirements.txt
```

### ۳. اجرای سرور
با استفاده از `uvicorn`:
```bash
uvicorn main:app --reload
```
یا با دستور جدید FastAPI CLI:
```bash
fastapi dev main.py
```

پس از اجرا، سرور روی آدرس `http://127.0.0.1:8000` در دسترس خواهد بود.

---

## 📖 مستندات تعاملی (Interactive API Docs)

FastAPI به صورت خودکار مستندات تعاملی را ایجاد می‌کند:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
