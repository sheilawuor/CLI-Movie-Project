# models/__init__.py
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CRUDMixin:
    """Mixin to add CRUD operations to models"""
    
    @classmethod
    def create(cls, session, **kwargs):
        """Create a new instance"""
        instance = cls(**kwargs)
        session.add(instance)
        session.flush()
        return instance
    
    @classmethod
    def get_all(cls, session):
        """Get all instances"""
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, id):
        """Find instance by ID"""
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def delete(cls, session, instance):
        """Delete an instance"""
        session.delete(instance)
        session.flush()

from .user import User  
from .genre import Genre  
from .movie import Movie  
from .review import Review 
