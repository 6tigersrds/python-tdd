from Checkout import Checkout

checkout = Checkout()
checkout.addItemPrice("a",1)
print(checkout.calculateTotal())