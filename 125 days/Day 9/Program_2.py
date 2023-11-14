#2.Write a Python program to create a class diagram for a simple online shopping system.

class Customer:

def init(self, customer_id, name, email):

self.customer_id = customer_id

self.name = name

self.email = email

class Product:

def init(self, product_id, name, price):

self.product_id = product_id

self.name = name

self.price = price

class ShoppingCart:

def init(self):

self.items = {

def add_item(self, product, quantity): if product.product_id not in self.items: self.items[product.product_id] = {'product': product, 'quantity': quantity}

else: self.items[product.product_id] ['quantity'] += quantity

def remove_item(self, product): if product.product_id in self.items: del self.items[product.product_id]

class Order:

def init(self, order_id, customer, cart, total_amount):

self.order_id = order_id

self.customer = customer

self. Cart
self. total_amount=total_amount
