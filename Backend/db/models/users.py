from Backend.db.base import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    id = Column(Integer,primary_key=True,index=True,unique=True)
    email = Column(String, primary_key=True, index=True,unique=True)
    password = Column(String,nullable=False)
    is_active = Column(Boolean, default=True)
    blogs = relationship('Blog',back_populates='author')