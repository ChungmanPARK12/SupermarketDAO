import datetime
import atexit
# A custom modul that handles checkout operations
from CheckoutRegister import CheckoutRegister

if __name__ == "__main__":
    _continue = True
    scan_another = "Y"
    #Creates an instance of the CheckoutRegister class to handle the checkout process.
    cr = CheckoutRegister()
    products = []
    atexit.register(cr.exitDao)
    cr.amount_due = 0
    sel_product = None
    print("----------------------")
    print("Welcome to shopping at Coles!")
    print("----------------------")
    # Main loop keeps the checkout process running
    while _continue:
        # Inner loop scanning items
        while scan_another == "Y":
            barcode = input("Enter the barcode:")
            # scan_item method from CheckoutRegister(cr)
            sel_product = cr.scan_item(barcode)
            if sel_product is None:
                print("ERROR! Scanned item is not found")
            else:
                print(sel_product)
            scan_another = str.capitalize(input("would you like to scan another stuff?(Y/N)"))

        while True:
            print(cr.amount_due)
            if cr.amount_due < 0:
                break
            print(f"Payment due:${cr.amount_due}", end=" ")
            payment_amount = float(input("please enter an amount to pay"))
            balance_to_pay = cr.accept_Payment(payment_amount)
            if payment_amount <= 0:
                print("Error! amounts are not accepted")
                print(f"Payment due:${cr.amount_due}", end=" ")
                break
            if balance_to_pay <= 0:
                print("Thank you for your payment")
                break
        break
    print("Your Receipt")
    for product in products:
        print(product.print_Details())
    print(f"total cost of items {cr.getTotal()}")
    print(f"Total paid {cr.amount_paid}")
    print(f"Balance due {cr.amount_due*-1}")
    cr.save_transaction()

