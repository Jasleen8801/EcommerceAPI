from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .services import get_all_products, create_order_service, get_all_orders, get_order_by_id, update_product_service, create_product_service
from .models import Product as ProductModel
from .models import Order as OrderModel

app = APIRouter()

@app.get('/products')
def get_products():
    '''Implementation to fetch and return all products'''
    products = get_all_products()
    for product in products:
        product['_id'] = str(product['_id'])
    return products

@app.post('/orders')
def create_order(order: OrderModel):
    '''Implementation to create a new order'''
    res = create_order_service(order)
    return res

@app.get('/orders')
def get_orders():
    '''Implementation to fetch and return all orders'''
    orders = get_all_orders()
    return orders

@app.get('/orders/{order_id}')
def get_order(order_id: str):
    '''Implementation to fetch and return a specific order'''
    order = get_order_by_id(order_id)
    if order:
        order['_id'] = str(order['_id'])
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@app.put('/products/{product_id}')
def update_product(product_id: int, quantity: int):
    '''Implementation to update a product'''
    try:
        res = update_product_service(product_id, quantity)
        return res
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# Other necessary routes
@app.post('/products')
def create_product(product: ProductModel):
    '''Implementation to create a new product'''
    res = create_product_service(product)
    return res
