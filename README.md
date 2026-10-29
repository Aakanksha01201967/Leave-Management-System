# 🏢 Flask Leave Management System

A lightweight, secure, and easy-to-use **Leave Management System** built with **Python (Flask)** and **SQLite (Flask-SQLAlchemy)**. It features separate user and admin roles, dynamic leave balance tracking via a ledger system, and a modern Bootstrap-powered UI.

---

## ✨ Features

- **User Authentication:** Secure registration and login system with role-based routing (User vs. Admin).
- **Automated Leave Ledger:** Every new user automatically receives initial leave credits (Casual, Privilege, Maternity, etc.).
- **Leave Application & Tracking:** Employees can apply for leaves, track pending/approved/rejected statuses, and view real-time remaining leave balances.
- **Admin Dashboard:** Admins can view all company-wide leave requests and approve/reject them.
- **Automatic Balance Deduction:** Approving a leave automatically debits the correct number of days from the user's leave balance ledger.
- **Responsive UI:** Built using Bootstrap 5 and clean custom CSS.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2 Templates

---

## 🚀 Getting Started Locally

Follow these steps to set up and run the project on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/your-repository-name.git](https://github.com/YOUR_USERNAME/your-repository-name.git)
cd your-repository-name