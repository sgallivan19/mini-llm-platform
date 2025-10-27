from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    external_id = Column(String(128), unique=True, nullable=False)
    text = Column(Text)
    metadata = Column(Text)
