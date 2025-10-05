from datetime import datetime, timedelta
from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """User model for authentication"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    tasks = db.relationship('Task', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    """Task model with CRUD operations"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)  # Text field
    status = db.Column(db.String(20), nullable=False)  # Enum field
    is_urgent = db.Column(db.Boolean, default=False)  # Boolean field
    due_date = db.Column(db.DateTime, nullable=False)  # For calculation
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def days_remaining(self):
        """Calculated field - days until due date"""
        if self.due_date:
            delta = self.due_date - datetime.utcnow()
            return delta.days
        return 0

    @property
    def status_color(self):
        """Helper property for UI"""
        colors = {
            'pending': 'orange',
            'in_progress': 'blue',
            'completed': 'green'
        }
        return colors.get(self.status, 'gray')