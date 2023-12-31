# EcommerceAPI

This is an API for managing ecommerce operations such as managing products and orders.

## Prerequisites

- Python 3.8 or higher
- MongoDB

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Jasleen8801/EcommerceAPI.git
    ```

2. Navigate to the project directory
    ```bash
    cd EcommerceAPI
    ```

3. Create and activate a virtual environment (optional but recommended):
   ```bash
    python3 -m venv env
    source env/bin/activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Make the MongoDB connection
   1. Make sure you have MongoDB installed and running on your local machine.
   2. Update the MongoDB connection settings in config.py file if necessary.

## Installation 

1. Start the server
   ```bash
   uvicorn main:app --host localhost --port 8000
   ```
2. The API will be accessible at http://localhost:8000/api
3. Use an API testing tool like Postman or cURL to interact with the API endpoints.

## API Endpoints

1. GET `/api/products`: Retrieve all products.
2. POST `/api/products`: Create a new product.
3. PUT `/api/products/{product_id}`: Update quantity of a specific product by ID.
4. GET `/api/orders`: Retrieve all orders.
5. POST `/api/orders`: Create a new order.
6. GET `/api/orders/{order_id}`: Retrieve a specific order by ID.

