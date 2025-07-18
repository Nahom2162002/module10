from datetime import datetime, timedelta 
import uuid 
from typing import Optional, Dict, Any 

from sqlalchemy import Column, String, DateTime, Boolean 
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.exc import IntegrityError 
from passlib.context import CryptContext 
from jose import JWTError, jwt 
from pydantic import ValidationError 

from app.schemas.base import UserCreate 
from app.schemas.user import UserResponse, Token 

Base = declarative_base()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'

    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

    @staticmethod 
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password)