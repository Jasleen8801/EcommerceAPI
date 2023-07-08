from .models import Order, Product
from .database import product_collection, order_collection
from datetime import datetime
from bson import json_util, ObjectId
from flask import json 


def get_all_products():
    """Implementation to fetch and return all products"""
    products = list(product_collection.find())
    products = json.loads(json_util.dumps(products))
    return products


def create_order_service(order: Order):
    """Implementation to create a new order"""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total_amount = 0

    for item in order.items:
        product = product_collection.find_one({"id": item.product_id})
        if product:
            total_amount += product["price"] * item.bought_quantity
        else:
            raise Exception(f"Product not found for id: {item.product_id}")

    order_doc = {
        "timestamp": timestamp,
        "items": [item.dict() for item in order.items],
        "total_amount": total_amount,
        "user_address": order.user_address.dict(),
    }

    res = order_collection.insert_one(order_doc)

    if res.inserted_id:
        order_id = str(res.inserted_id)
        return {"message": "Order created successfully", "order_id": order_id}
    else:
        raise Exception("Failed to create order")


def get_all_orders(limit: int = 10, offset: int = 0):
    """Implementation to fetch and return all orders"""
    orders = list(order_collection.find().skip(offset).limit(limit))
    orders = json.loads(json_util.dumps(orders))
    return orders


def get_order_by_id(order_id: str):
    """Implementation to fetch and return a specific order"""
    order = order_collection.find_one({"_id": ObjectId(order_id)})
    return order


def update_product_service(product_id: int, quantity: int):
    """Implementation to update a product"""
    product = product_collection.find_one({"id": product_id})
    if product:
        result = product_collection.update_one(
            {"id": product_id}, {"$set": {"quantity": quantity}}
        )
        if result.modified_count > 0:
            return {"message": "Product updated successfully"}
        else:
            raise Exception("Failed to update product")
    else:
        raise Exception(f"Product not found for id: {product_id}")


# Other necessary functions
def create_product_service(product: Product):
    """Implementation to create a new product"""
    product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }

    res = product_collection.insert_one(product_data)

    if res.inserted_id:
        product_id = str(res.inserted_id)
        return {"message": "Product created successfully", "product_id": product_id}
    else:
        raise Exception("Failed to create product")

