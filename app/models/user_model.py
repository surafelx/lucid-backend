from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    posts = relationship("Post", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
