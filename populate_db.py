from db import *
from datetime import datetime

def populate_database():
    db = get_db()

    enterprises = [
        Enterprise(name="Alpha Corp", activity_type="Manufacturing", employees_count=150),
        Enterprise(name="Beta LLC", activity_type="Retail", employees_count=80),
        Enterprise(name="Gamma Industries", activity_type="IT", employees_count=200),
        Enterprise(name="Delta Co.", activity_type="Manufacturing", employees_count=300),
        Enterprise(name="Epsilon Ltd", activity_type="Retail", employees_count=50),
        Enterprise(name="Zeta Group", activity_type="IT", employees_count=120),
        Enterprise(name="Eta Solutions", activity_type="Manufacturing", employees_count=90),
        Enterprise(name="Theta Inc", activity_type="Retail", employees_count=70),
        Enterprise(name="Iota Systems", activity_type="IT", employees_count=110),
        Enterprise(name="Kappa Enterprises", activity_type="Manufacturing", employees_count=250),
    ]
    db.add_all(enterprises)
    db.commit()

    products = [
        Product(full_name="Sugar", unit="kg", shelf_life=datetime(2025, 12, 31).date(), purchase_price=100.00),
        Product(full_name="KeyBoard", unit="pieces", shelf_life=datetime(2024, 11, 30).date(), purchase_price=50.00),
        Product(full_name="Cola", unit="liters", shelf_life=datetime(2026, 1, 15).date(), purchase_price=75.00),
        Product(full_name="Apple", unit="kg", shelf_life=datetime(2025, 7, 20).date(), purchase_price=120.00),
        Product(full_name="Bread", unit="pieces", shelf_life=datetime(2023, 10, 10).date(), purchase_price=200.00),
        Product(full_name="Vodka", unit="liters", shelf_life=datetime(2024, 8, 5).date(), purchase_price=30.00),
        Product(full_name="Gas", unit="kg", shelf_life=datetime(2026, 3, 25).date(), purchase_price=90.00),
        Product(full_name="Pinaple", unit="pieces", shelf_life=datetime(2024, 6, 18).date(), purchase_price=40.00),
        Product(full_name="Water", unit="liters", shelf_life=datetime(2025, 9, 12).date(), purchase_price=150.00),
        Product(full_name="Almond", unit="kg", shelf_life=datetime(2025, 12, 1).date(), purchase_price=110.00),
    ]
    db.add_all(products)
    db.commit()
    

    supplies = [
        Supply(enterprise_id=1, product_id=1, date=datetime(2023, 12, 1).date(), volume=20.0, selling_price=120.00),
        Supply(enterprise_id=2, product_id=2, date=datetime(2023, 11, 25).date(), volume=15.0, selling_price=60.00),
        Supply(enterprise_id=3, product_id=3, date=datetime(2023, 10, 15).date(), volume=10.0, selling_price=80.00),
        Supply(enterprise_id=4, product_id=4, date=datetime(2023, 9, 5).date(), volume=25.0, selling_price=140.00),
        Supply(enterprise_id=5, product_id=5, date=datetime(2023, 8, 20).date(), volume=30.0, selling_price=220.00),
        Supply(enterprise_id=6, product_id=6, date=datetime(2023, 7, 30).date(), volume=40.0, selling_price=35.00),
        Supply(enterprise_id=7, product_id=7, date=datetime(2023, 6, 10).date(), volume=50.0, selling_price=100.00),
        Supply(enterprise_id=8, product_id=8, date=datetime(2023, 5, 15).date(), volume=45.0, selling_price=45.00),
        Supply(enterprise_id=9, product_id=9, date=datetime(2023, 4, 12).date(), volume=35.0, selling_price=160.00),
        Supply(enterprise_id=10, product_id=10, date=datetime(2023, 3, 25).date(), volume=60.0, selling_price=120.00),
    ]

    db.add_all(supplies)
    db.commit()

if __name__ == "__main__":
    populate_database()