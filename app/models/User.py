import bcrypt

# importing functions from modules
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


salt = bcrypt.gensalt()
# creating a User class that inherits from the Base class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

# The validate_email() method uses the assert keyword to check if an email address contains an at-sign character (@). 
# The assert keyword automatically throws an error if the condition is false, thus preventing the return statement from happening.

    @validates('email')
    def validate_email(self, key, email):
    # make sure email address contains @ character
        assert '@' in email
        return email
  
  # Again, we use assert to check the length of the password and throw an error if it has fewer than four characters.
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4
  
  # encrypt password
        return bcrypt.hashpw(password.encode('utf-8'), salt)