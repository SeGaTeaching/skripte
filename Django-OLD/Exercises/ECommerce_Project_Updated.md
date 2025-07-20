
# 7. Projekt: Ein kleines E-Commerce-System

## a) Modelle
```python
class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_date = models.DateTimeField(auto_now_add=True)
```

---

## b) Befüllung der Datenbank (Schritt-für-Schritt-Anleitung)

### 1. Kategorien erstellen
```python
electronics = Category.objects.create(name="Electronics")
clothing = Category.objects.create(name="Clothing")
```

### 2. Produkte erstellen
```python
laptop = Product.objects.create(
    name="Laptop",
    description="High-performance gaming laptop",
    price=1500.00,
    category=electronics
)

tshirt = Product.objects.create(
    name="T-Shirt",
    description="Comfortable cotton t-shirt",
    price=20.00,
    category=clothing
)

smartphone = Product.objects.create(
    name="Smartphone",
    description="Latest model smartphone",
    price=800.00,
    category=electronics
)

jeans = Product.objects.create(
    name="Jeans",
    description="Stylish denim jeans",
    price=50.00,
    category=clothing
)

headphones = Product.objects.create(
    name="Headphones",
    description="Noise-cancelling headphones",
    price=200.00,
    category=electronics
)
```

### 3. Kunden erstellen
```python
customer1 = Customer.objects.create(name="John Doe", email="john.doe@example.com")
customer2 = Customer.objects.create(name="Jane Smith", email="jane.smith@example.com")
customer3 = Customer.objects.create(name="Bob Brown", email="bob.brown@example.com")
```

### 4. Bestellungen erstellen
```python
# Bestellung 1
order1 = Order.objects.create(customer=customer1)
order1.product.add(laptop, tshirt)

# Bestellung 2
order2 = Order.objects.create(customer=customer2)
order2.product.add(smartphone, jeans)

# Bestellung 3
order3 = Order.objects.create(customer=customer3)
order3.product.add(headphones, tshirt)
```

---

## c) HTML-Formular (Ohne Django Forms)

### View:
```python
from django.shortcuts import render
from .models import Order, Customer, Product, Category

def create_order(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        product_ids = request.POST.getlist("product_ids")

        # Kunde abrufen
        customer = Customer.objects.get(id=customer_id)

        # Bestellung erstellen
        order = Order.objects.create(customer=customer)

        # Produkte hinzufügen
        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.product.add(product)

        return render(request, "order_success.html", {"order": order})
    else:
        customers = Customer.objects.all()
        products = Product.objects.all()
        return render(request, "create_order.html", {"customers": customers, "products": products})
```

### Template (create_order.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>Create Order</title>
</head>
<body>
    <h1>Create Order</h1>
    <form method="post">
        {% csrf_token %}
        <label for="customer">Select Customer:</label>
        <select name="customer_id" id="customer">
            {% for customer in customers %}
                <option value="{{ customer.id }}">{{ customer.name }}</option>
            {% endfor %}
        </select>
        <br><br>

        <label for="products">Select Products:</label>
        <br>
        {% for product in products %}
            <input type="checkbox" name="product_ids" value="{{ product.id }}">
            {{ product.name }} ({{ product.price }} USD)<br>
        {% endfor %}
        <br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Template (order_success.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>Order Success</title>
</head>
<body>
    <h1>Order Created Successfully!</h1>
    <p>Order ID: {{ order.id }}</p>
    <p>Customer: {{ order.customer.name }}</p>
    <h2>Products:</h2>
    <ul>
        {% for product in order.product.all %}
            <li>{{ product.name }} - {{ product.price }} USD</li>
        {% endfor %}
    </ul>
</body>
</html>
```
