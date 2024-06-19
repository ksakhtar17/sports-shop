from tkinter import messagebox


class UpdateCart:
    def __init__(self):
        self.cart = {}

    # def product_list(self):
    # cricket = ['Helmet','Shoes', 'Jersey', 'Ball', 'Bat']
    #         football = ['Football', 'Football Jersey', 'Football shoes', 'Football nets', 'Football T-Shirt']
    #         basketball = ['Basketball', 'Crew socks', 'Shooter sleeves', 'Backpack', 'Skinny hairband']
    #         baseball = ['Baseball Cleats', 'Baseball leg guards', 'Baseball chest protector', 'Baseball T-shirt', 'Baseball bat']
    #         soccer = ['Soccer Cleats', 'Soccer Shoes', 'Soccer pants', 'Soccer T-Shirt', 'Soccer ball']
    #         tennis = ['Tennis ball', 'Tennis T-shirt', 'Tennis shoes', 'Tennis rackets', 'Tennis P-cap']
    #         hockey = ['Hockey Jersey', 'Hockey Hat', 'Hockey Stick', 'Hockey ball', 'Hockey shoes']
    #         other = ['T-shirts', 'Shorts', 'Jackets', 'Hoddie', 'Cleats', 'Sleeves', 'Head Bands']

    def increase(self, var, product): # function created to increase the quantity on clicking the + button
        if product not in self.cart:
            self.cart[product] = 1  # Add the product with quantity 1 if it's not in the cart
        else:
            if self.cart[product] < 50:
                self.cart[product] += 1  # Increase the quantity if the product is already in the cart
            else:
                messagebox.showerror("Error", f"sorry! currently we don't have {self.cart[product]} {product}")
        var.set(self.cart[product])

    def decrease(self, var, product): # function created to decrease the quantity on clicking the - button
        if product in self.cart and self.cart[product] > 0:
            self.cart[product] -= 1  # Decrease the quantity if the product is in the cart

            if self.cart[product] == 0:
                del self.cart[product]  # Remove the product from the cart if quantity is 0

        if product in self.cart:
            var.set(self.cart[product])  # Update the variable to reflect the new quantity if the product is still in the cart
        else:
            var.set(0)
