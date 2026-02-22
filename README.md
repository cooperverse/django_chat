# 💬 Django Real-Time Multi-Room Chat

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Django](https://img.shields.io/badge/django-5.0+-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> **🚀 Project Resources:**
> - 📄 **Interactive API Docs:** [Swagger UI](http://127.0.0.1:8000/api/docs/)
> - 🔌 **WebSocket Entry:** `ws://127.0.0.1:8000/ws/chat/{room_name}/`

---

## 📖 Overview
A production-ready Real-Time Chat Backend built with **Django Channels**, **Redis**, and **DRF**. This system supports dynamic isolated chat rooms, JWT-authenticated WebSocket connections, and persistent message history.

## ✨ Key Features
* **Real-Time Messaging**: Low-latency bidirectional communication via WebSockets.
* **Multi-Room Support**: Dynamic room creation via URL routing (e.g., `/ws/chat/global/`).
* **JWT Authentication**: Secure handshakes and REST API endpoints using `simplejwt`.
* **Persistent History**: Chat history stored in DB and accessible via optimized Generics-based REST endpoints.
* **Auto-Documentation**: OpenAPI 3.0 specs generated dynamically via `drf-spectacular`.

## 🛠️ Tech Stack
* **Core**: Python 3.12, Django 5.x
* **Real-time**: Django Channels, Daphne
* **API**: Django Rest Framework (DRF)
* **Documentation**: drf-spectacular


## 📦 Installation & Local Setup

1. **Clone & Navigate**
   ```bash
   git clone [https://github.com/yourusername/django_chat.git](https://github.com/yourusername/django_chat.git)
   cd django_chat

2. **Setup Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: .\venv\Scripts\activate
   pip install -r requirements.txt

3. **Database & Migrations**
   ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

4. **Run Development Server**
    ```bash
    # Ensure your Redis server is running
    python manage.py runserver

## ⚡ Quick Start: The WebSocket URL
To connect to any room, use the following URL structure. Room names are dynamic and created upon connection.

**URL Template:**
`ws://127.0.0.1:8000/ws/chat/<ROOM_NAME>/?token=<YOUR_JWT_ACCESS_TOKEN>`

**Example:**
`ws://127.0.0.1:8000/ws/chat/global/?token=eyJhbGci...`

🛡️ License
Distributed under the MIT License. See LICENSE for more information.



