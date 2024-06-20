from tkinter import messagebox


class UpdateCart:
    def __init__(self):
        self.cart = {}

    def product_list(self):
        products = [
            ['Helmet', 2000], ['Shoes', 4000], ['Jersey', 1800], ['Ball', 600], ['Bat', 1200],
            ['Football', 1500], ['Football Jersey', 1800], ['Football shoes', 3500], ['Football nets', 2500],
            ['Football T-Shirt', 1500],
            ['Basketball', 2000], ['Crew socks', 500], ['Shooter sleeves', 800], ['Backpack', 2500],
            ['Skinny hairband', 300],
            ['Baseball Cleats', 3500], ['Baseball leg guards', 1500], ['Baseball chest protector', 2000],
            ['Baseball T-shirt', 1200], ['Baseball bat', 2500],
            ['Soccer Cleats', 3000], ['Soccer Shoes', 2800], ['Soccer pants', 1500], ['Soccer T-Shirt', 1000],
            ['Soccer ball', 700],
            ['Tennis ball', 600], ['Tennis T-shirt', 1200], ['Tennis shoes', 3500], ['Tennis rackets', 4500],
            ['Tennis P-cap', 500],
            ['Hockey Jersey', 1800], ['Hockey Hat', 400], ['Hockey Stick', 3000], ['Hockey ball', 600],
            ['Hockey shoes', 3500],
            ['T-shirts', 1200], ['Shorts', 800], ['Jackets', 2500], ['Hoodie', 2000], ['Cleats', 3000],
            ['Sleeves', 600], ['Head Bands', 300]
        ]
        return products

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

    def save_cart(self):
        products = self.product_list()

        with open('temporary_cart.txt', 'w+') as file:
            for product in self.cart:
                for item in products:
                    if item[0] == product:
                        price = item[1]

                file.write(f"{product} : {self.cart[product]} items : {self.cart[product]*price}\n")
