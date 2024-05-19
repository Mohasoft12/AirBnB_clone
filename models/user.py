#!/usr/bin/python3
"""
User Model definition inheriting from BaseModel.
"""

from models.base_model import BaseModel

class UserModel(BaseModel):
    """User Model class."""

    def __init__(self, email='', password='', first_name='', last_name=''):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"User: {self.email}, {self.first_name} {self.last_name}"

    def update_info(self, email='', password='', first_name='', last_name=''):
        """Update user information."""
        if email:
            self.email = email
        if password:
            self.password = password
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name

# Example usage:
if __name__ == "__main__":
    user = UserModel(email='example@example.com', password='securepassword', first_name='John', last_name='Doe')
    print(user)
    user.update_info(password='newpassword')
    print(user)
