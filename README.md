# AI Campus Assignment - Task Manager

A simple task management application with authentication and CRUD operations.

## Features
- User authentication (login/register)
- Create, Read, Update, Delete tasks
- Pagination (5 items per page)
- Filter by status
- Calculated field (days remaining)

## Prerequisites
- Python 3.8+
- pip

## Setup Instructions

1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-campus-project
```

2. Create virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open browser and navigate to
```
http://localhost:5000
```

## Default Test Account
- Username: admin
- Password: admin123

## Tech Stack
- Backend: Flask (Python)
- Database: SQLite
- Frontend: HTML, CSS, Jinja2
- Authentication: Flask-Login