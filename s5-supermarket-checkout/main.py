from Checkout import Checkout

checkout = Checkout()

checkout.addItemPrice("a", 1)
checkout.addItemPrice("b", 2)

checkout.addDiscount("a", 3, 2)

checkout.addItem("a")
checkout.addItem("a")
checkout.addItem("a")

print("==================== [TOTAL] ====================")
print("Your checkout total is: ", checkout.calculateTotal())