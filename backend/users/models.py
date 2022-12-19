from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,  index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    knowledge_sections = relationship('KnowledgeSection', back_populates='user')
