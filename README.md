# CodeAlpha Backend Development Internship Projects

This repository contains all the backend projects completed for the **CodeAlpha Backend Development Internship**.  
The projects were built using **Python (Django & Flask)**, covering real-world backend tasks.

---

## 🏆 Completed Tasks

### **Task 1: Simple URL Shortener**
- Built with **Flask**.
- Features:
  - Accepts a long URL and generates a unique short code.
  - Stores mapping in **SQLite**.
  - Redirects short URL to original URL.
- Optional frontend included for URL input and display.

### **Task 2: Event Registration System**
- Built with **Django**.
- Features:
  - Create and manage events.
  - Users can register for events.
  - Admin panel to manage events and registrations.
- Models: `Event`, `UserRegistration`
- API endpoints for listing events, registering users, and viewing registrations.

### **Task 3: Restaurant Management System**
- Built with **Django**.
- Features:
  - Manage **Menu Items**, **Tables**, **Orders**, and **Order Items**.
  - Place orders, update inventory automatically, and check table availability.
  - Admin panel included for restaurant management.
- Models: `MenuItem`, `Table`, `Order`, `OrderItem`
- Templates for placing orders and viewing order details.

### **Task 4: Job Board Platform**
- Built with **Django**.
- Features:
  - Employers can post jobs.
  - Candidates can view jobs and apply with resumes.
  - Tracks applications, resumes, and status.
  - Optional admin panel for reporting.
- Models: `Employer`, `Candidate`, `JobListing`, `Resume`, `JobApplication`
- Full CRUD functionality and proper authentication implemented.

---

## ⚙️ Technologies Used
- **Backend:** Python, Django
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap (for templates)
- **Other:** Django REST Framework (for APIs), CSRF protection, Authentication & Authorization

---

## 🚀 Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd CodeAlpha_ProjectName
