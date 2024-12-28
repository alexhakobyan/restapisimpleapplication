from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import join, func
import uvicorn
from db import *
from datetime import datetime

# FastAPI app
app = FastAPI()

# Enterprise Endpoints
@app.post("/enterprises/")
def create_enterprise(enterprise: EnterpriseModel):
    db = get_db()
    db.add(enterprise)
    db.commit()
    db.refresh(enterprise)

@app.get("/enterprises/")
def read_enterprises():
    return get_db().query(Enterprise).all()

@app.get("/enterprises/{enterprise_id}")
def read_enterprise(enterprise_id: int):
    db = get_db()
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise

@app.delete("/enterprises/{enterprise_id}")
def delete_enterprise(enterprise_id: int):
    db = get_db()
    db_enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not db_enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    db.delete(db_enterprise)
    db.commit()
    return {"detail": "Enterprise deleted"}

@app.post("/products/")
def create_product(product: ProductModel):
    db = get_db()
    db.add(product)
    db.commit()
    db.refresh(product)

@app.get("/products/")
def read_products():
    db = get_db()
    return db.query(Product).all()

@app.get("/products/{product_id}")
def read_product(product_id: int):
    db = get_db()
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = get_db()
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"detail": "Product deleted"}

@app.post("/supplies/")
def create_supply(supply: SupplyModel):
    db = get_db()
    db.add(supply)
    db.commit()
    db.refresh(supply)

@app.get("/supplies/")
def read_supplies():
    db = get_db()
    return db.query(Supply).all()

@app.get("/supplies/{supply_id}")
def read_supply(supply_id: int):
    db = get_db()
    supply = db.query(Supply).filter(Supply.id == supply_id).first()
    if not supply:
        raise HTTPException(status_code=404, detail="Supply not found")
    return supply

@app.delete("/supplies/{supply_id}")
def delete_supply(supply_id: int):
    db = get_db()
    db_supply = db.query(Supply).filter(Supply.id == supply_id).first()
    if not db_supply:
        raise HTTPException(status_code=404, detail="Supply not found")
    db.delete(db_supply)
    db.commit()
    return {"detail": "Supply deleted"} 

@app.get("/products_expired")
def get_expired_products():
    db = get_db()
    today = datetime.now().date()
    expired_products = db.query(Product).filter(Product.shelf_life < today).all()
    return expired_products

@app.get("/high_brand_enterprise")
def get_high_brand_enterprise(price: int):
    db = get_db()

    joined = join(Supply,Enterprise, Supply.enterprise_id == Enterprise.id)
    enterprises = (
        db.query(Enterprise)
        .select_from(joined)
        .filter(Supply.selling_price > price)
        .distinct()
        .all()
    )
    return enterprises


@app.put("/update_price")
def update_selling_price(enterprise_name: str, product_name: str, percentage: float):
    db = get_db()
    joined = join(Supply, Product, Supply.product_id == Product.id).join(Enterprise, Supply.enterprise_id == Enterprise.id)
    supply = (
        db.query(Supply)
        .select_from(joined)
        .filter(Enterprise.name == enterprise_name, Product.full_name == product_name)
        .first()
    )

    if not supply:
        raise HTTPException(status_code=404, detail="Supply with given enterprise and product not found")

    supply.selling_price += supply.selling_price * (percentage / 100)
    db.commit()
    db.refresh(supply)

    return {"message": "Selling price updated successfully", "new_price": supply.selling_price}

@app.get("/hight_supplier_enterprise")
def get_enterprises_with_more_products(supply_count: int):
    db = get_db()
    result = (
        db.query(Enterprise, func.count(Product.id).label("product_count"))
        .join(Supply, Enterprise.id == Supply.enterprise_id)
        .join(Product, Supply.product_id == Product.id)
        .group_by(Enterprise.id)
        .having(func.count(Product.id) >= supply_count)
        .all()
    )

    enterprises = [{"enterprise": enterprise, "product_count": product_count} for enterprise, product_count in result]
    return enterprises

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

