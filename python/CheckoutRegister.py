from Product_Class import Product
from Transactions import Transactions
from SupermarketDAO import SupermarketDAO

class CheckoutRegister:
    #asdfadsf
    # Initialize the SupermarketDAo interact with the database
    # Retrieves all products from the database
    def __init__(self):
        self.supermarketDAO = SupermarketDAO()
        self.products = self.supermarketDAO.listAllProducts()
        self.shopping_cart = []
        self.amount_paid = 0
        self.amount_due = 0

    def print_receipt(self):
        return self.amount_due

    def scan_item(self, barcode):
        # use barcode to find the product object from the products
        # if product found return product
        # add product shopping cart
        # else product id not found return none
        for a_product in self.products:
            if a_product[0] == barcode:
                self.shopping_cart.append(a_product)
                self.amount_due += float(a_product[3])
                return a_product
        return None

    def accept_Payment(self, payment_amount):
        # Processes payment, updating the amount paid and the remaining amount due
        if payment_amount <= 0:
            return
        self.amount_paid += payment_amount
        self.amount_due -= payment_amount
        return self.amount_due

    def getTotal(self):
        total = 0
        for p in self.shopping_cart:
            total += float(p[3])
        return total
        # return total the amount of all products in the shopping cart

    def save_transaction(self):
        cart = self.shopping_cart.copy()
        # Uses a dictionary to count quantities of each product
        tran_dict = dict()
        for product in cart:
            try:
                if tran_dict[product[0]] != 0:
                    temp_quantity = tran_dict[product[0]]
                    tran_dict[product[0]] = temp_quantity + 1
            except KeyError:
                tran_dict[product[0]] = 1
        for key in tran_dict.keys():
            new_transaction = Transactions(key, tran_dict[key])
            self.supermarketDAO.addTransactionToDB(new_transaction)

    def exitDao(self):
        self.supermarketDAO.disconnect()
