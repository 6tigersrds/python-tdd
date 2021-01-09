from Checkout import Checkout

checkout = Checkout()
checkout.addItemPrice("a",1)
checkout.addItem("a")
print(checkout.calculateTotal())