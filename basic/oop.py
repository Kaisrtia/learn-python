from abc import ABC, abstractmethod

class PaymentMethod(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

class CreditCardPayment(PaymentMethod):
  def __init__(self, cardNumber, cardHolder):
    super().__init__()
    self.__cardNumber = cardNumber
    self.cardHolder = cardHolder
  
  def pay(self, amount):
    hiddenCard = f"**** **** **** {self.__cardNumber[-4:]}"
    return f"Successfuly: Paid {amount}$ from credit card {hiddenCard}"

class MomoPayment(PaymentMethod):
  def __init__(self, phoneNumber):
    super().__init__()
    self.phoneNumber = phoneNumber
  
  def pay(self, amount):
    return f"Successfuly: Paid {amount}$ via Momo E-wallet (Phone: {self.phoneNumber})"

class Product:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price
  
  def getName(self):
    return self.__name
  
  def getPrice(self):
    return self.__price
  
  def getDescription(self):
    pass
  
class Iphone(Product):
  def __init__(self, name, price):
    super().__init__(name, price)
  
  def getDescription(self):
    return "A device make you don't be left behide"
  
class Car(Product):
  def __init__(self, name, price):
    super().__init__(name, price)
  
  def getDescription(self):
    return "A thing replace your legs"
  
class ShoppingCart:
  def __init__(self):
    self.__cart = []

  def addItem(self, product: Product, quantity = 1):
    self.__cart.append({"product": product, "quantity": quantity})
    print(f"Added {quantity} {product.getName()} into your cart!")
  
  def calculateTotal(self):
    total = 0
    for item in self.__cart:
      p: Product = item["product"]
      total += p.getPrice() * item["quantity"]
    return total 
  
  def checkout(self, paymentMethod: PaymentMethod):
    total = self.calculateTotal()
    if total == 0:
      print("Empty cart!!!")
      return 
    
    print("\n" + "="*35 + " DETAILS " + "="*35)
    for item in self.__cart:
      p: Product = item["product"]
      print(f"x{item["quantity"]} {p.getName()} | Description: {p.getDescription()}")
    print(f"--> Total amount: {total:,} $")
    print("-" * 79)

    result = paymentMethod.pay(total)
    print(result)
    print("-" * 79)

# Test
if __name__ == "__main__":
  cart = ShoppingCart()
  cart.addItem(Iphone("Iphone 15 Pro Max", 1500), 2)
  cart.addItem(Car("Roll Royce", 100000), 1)
  cart.addItem(Iphone("Iphone 17 Pro Max", 3000), 5)

  print("\n" + "="*35 + " PAYMENT " + "="*34)
  paymentMethod = CreditCardPayment("1234567890123456", "John Doe")
  cart.checkout(paymentMethod)

  print("\n" + "="*35 + " PAYMENT " + "="*35)
  paymentMethod = MomoPayment("0987654321")
  cart.checkout(paymentMethod)