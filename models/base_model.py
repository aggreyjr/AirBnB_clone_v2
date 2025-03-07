#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    update_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if kwargs.get("created_at", None) and type(self.created_at) is str:
                        self.created_at = datetime.strptime(kwargs["created_at"], time)
        else:
            self.created_at = datetime.utcnow()
            if kwargs.get("id", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
                if kwargs.get("id", None) is None:
                    self.id = str(uuid.uuid4())
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.utcnow()
                    self.update_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
            if "updated_at" in new_dict:
                new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
                new_dict["__class__"] = self.__class__.__name__
                if "_sa_instance_state" in new_dict:
                    del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """deletes current instance from storage by calling mtd"""
        models.storage.delete(self)
