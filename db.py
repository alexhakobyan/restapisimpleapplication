from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Enterprise(Base):
    __tablename__ = 'enterprise'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    activity_type = Column(String, nullable=False)  
    employees_count = Column(Integer, nullable=False)  
    searchable_data = Column(String, nullable=False)
    supplies = relationship('Supply', back_populates='enterprise')

class EnterpriseModel(BaseModel):
    name: str
    activity_type: str
    employees_count: int


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)  
    unit = Column(String, nullable=False)  
    shelf_life = Column(Date, nullable=False)  
    purchase_price = Column(Float, nullable=False)  

    supplies = relationship('Supply', back_populates='product')

class ProductModel(BaseModel):
    full_name: str
    unit: str
    shelf_life: str
    purchase_price: float


class Supply(Base):
    __tablename__ = 'supply'

    id = Column(Integer, primary_key=True)
    enterprise_id = Column(Integer, ForeignKey('enterprise.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    date = Column(Date, nullable=False)  
    volume = Column(Float, nullable=False)  
    selling_price = Column(Float, nullable=False)  

    enterprise = relationship('Enterprise', back_populates='supplies')
    product = relationship('Product', back_populates='supplies')

class SupplyModel(BaseModel):
    enterprise_id: int
    product_id: int
    date: str
    volume: float
    selling_price: float

engine = create_engine('sqlite:///production.db')
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    return SessionLocal()