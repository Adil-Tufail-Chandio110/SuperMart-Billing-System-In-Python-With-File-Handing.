import os
from colorama import init, Fore, Style

# Initialize colorama for colored console output
init()


class Bill:
    def __init__(self):
        self.itemcode = 0
        self.itemName = ""
        self.rate = 0.0
        self.quantity = 0.0
        self.discount = 0.0
        self.buyerName = ""
        self.cashierName = ""
        self.date = ""
        self.time = ""

    def logo(self):
        print("\n")
        print(Fore.YELLOW + Style.BRIGHT)
        print("  ##      ## ##                                         ")
        print("   ##    ##   ##          INSANT GROCERY DELIVERY       ")
        print(" ## ##   ####                   03332537040             ")
        print(" ##  ##   #####                Open 10am-10pm           ")
        print(" ## ###      ###                7 days a week           ")
        print(" ##  ##  ##   ##          SAHBAZ ROAD-ALI TOWN-BADIN    ")
        print("###  ##   ## ##            THANK YOU FOR YOUR TRUST     ")
        print(" Since 1990                                             ")
        print(Style.RESET_ALL)

    def print_title(self):
        print("\n")
        print(Fore.YELLOW + Style.BRIGHT)
        print(
            "   ##     ### ##     ####   ####               ## ##   ##  ###  ### ##   ### ###  ### ##   ##   ##    ##     ### ##   #### ##  ")
        print(
            "    ##     ##  ##     ##     ##               ##   ##  ##   ##   ##  ##   ##  ##   ##  ##   ## ##      ##     ##  ##  # ## ##  ")
        print(
            "   ## ##   ##  ##     ##     ##               ####     ##   ##   ##  ##   ##       ##  ##  # ### #   ## ##    ##  ##    ##     ")
        print(
            "   ##  ##  ##  ##     ##     ##                #####   ##   ##   ##  ##   ## ##    ## ##   ## # ##   ##  ##   ## ##     ##     ")
        print(
            "   ## ###  ##  ##     ##     ##                   ###  ##   ##   ## ##    ##       ## ##   ##   ##   ## ###   ## ##     ##     ")
        print(
            "   ##  ##  ##  ##     ##     ##  ##           ##   ##  ##   ##   ##       ##  ##   ##  ##  ##   ##   ##  ##   ##  ##    ##     ")
        print(
            "  ###  ## ### ##     ####   ### ###            ## ##    ## ##   ####     ### ###  #### ##  ##   ##  ###  ##  #### ##   ####    ")
        print("PROJECTED BY ADIL TUFAIL!")
        print()
        print(Style.RESET_ALL)

    def menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_title()
            print("\t\t\t\t ===========================")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|     SUPERMART MAIN MENU   |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t ___________________________")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|  1) ADMINISTRATOR.        |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|  2) BUYER.                |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|  3) EXIT.                 |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t ===========================")
            choice = input("\t\t\t\t Please Select: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Please select from given Options:")
                continue

            if choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.print_title()
                print("\t\t\t Please Login ")
                admin = input("\t\t\t Enter UserName: ")
                password = input("\t\t\t Enter Password: ")
                if admin == "AdilTufail" and password == "Adil2903":
                    self.administrator()
                else:
                    print("Invalid UserName & Password!")
                    print("Please Enter Correct UserName & Password!")
                    input()
            elif choice == 2:
                self.buyer()
            elif choice == 3:
                exit(0)
            else:
                print("Please select from given Options:")
                input()

    def administrator(self):
        product = Product()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_title()
            print("\t\t\t\t ===========================")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|     ADMINISTRATOR  MENU   |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t ___________________________")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 1) Add the Product.       |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 2) Modify the Product.    |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 3) Delete the Product.    |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 4) Back to main menu.     |")
            print("\t\t\t\t ===========================")
            choice = input("\t\t\t\t Please Select: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice")
                input()
                continue

            if choice == 1:
                product.add_product()
            elif choice == 2:
                product.edit_product()
            elif choice == 3:
                product.remove_product()
            elif choice == 4:
                self.menu()
            else:
                print("Invalid choice")
                input()

    def buyer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        self.buyerName = input("Enter Buyer Name: ")
        self.cashierName = input("Enter Your Cashier Name: ")
        self.date = input("Enter Today Date (format: DD-MM-YYYY): ")
        self.time = input("Enter Current Time (format: HH:MM): ")
        print()
        while True:
            print("\t\t\t\t ===========================")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t|     BUYER  MENU           |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t ___________________________")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 1) Buy Product.           |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t| 2) Go Back to Menu.       |")
            print("\t\t\t\t|                           |")
            print("\t\t\t\t ===========================")
            choice = input("\t\t\t\t Please Select: ")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice!")
                input()
                continue

            if choice == 1:
                self.receipt()
            elif choice == 2:
                self.menu()
            else:
                print("Invalid choice!")
                input()

    def list_of_item(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        print("\n\n\t\t\t List of Products ")
        try:
            with open("Database7.txt", "r") as data:
                print("\nCode\tItem Name\t\tPrice\tDiscount\tQuantity")
                for line in data:
                    itemcode, itemName, rate, discount, quantity = line.strip().split("\t")
                    print(f"{itemcode}\t\t{itemName}\t\t{rate}\t{discount}\t\t\t{quantity}")
        except FileNotFoundError:
            print("File does not exist.")

    def receipt(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        print("\n\n\t\t\t\t RECEIPT")
        try:
            with open("Database7.txt", "r") as data:
                pass
        except FileNotFoundError:
            print("\n\n Empty Database")
            input()
            return

        self.list_of_item()
        print("\n ____________________________")
        print("\n|                            |")
        print("\n|   PLEASE PLACE THE ORDER.  |")
        print("\n|____________________________|")

        arrc = []
        arrq = []
        while True:
            try:
                code = int(input("\n\n Enter code: "))
                quantity = int(input("\n\n Enter the Quantity: "))
                if code in arrc:
                    print("\n\n Duplicate product code. Please Try Again.")
                else:
                    arrc.append(code)
                    arrq.append(quantity)
                choice = input("\n\n Do you want to buy another product? (y/n): ")
                if choice.lower() != 'y':
                    break
            except ValueError:
                print("\n\n Invalid input. Please enter numeric values.")

        self.logo()
        print(f"\nBUYER NAME: {self.buyerName}\t\tCASHIER NAME: {self.cashierName}")
        print(f"DATE: {self.date}\t\t\t\tTIME: {self.time}")
        print("\n\n\t\t\t_________________RECEIPT__________________")
        print("\nProduct No\tProduct Name\t\t\tQuantity\tPrice\tAmount\tDiscounted Amount")

        total = 0
        found = False
        for i in range(len(arrc)):
            try:
                with open("Database7.txt", "r") as data:
                    for line in data:
                        itemcode, itemName, rate, discount, quantity = line.strip().split("\t")
                        itemcode = int(itemcode)
                        rate = float(rate)
                        discount = float(discount)
                        quantity = float(quantity)
                        if arrc[i] == itemcode:
                            amount = rate * arrq[i]
                            discount_amount = amount - (amount * discount / 100)
                            total += discount_amount
                            print(f"{itemcode}\t\t\t{itemName}\t\t\t\t{arrq[i]}\t\t\t{rate}\t{amount}\t{discount_amount}")
                            found = True
            except FileNotFoundError:
                print("File does not exist.")
                return

        if not found:
            print("\n\n No items found.")
        print("\n\n________________________________")
        print(f"\n Total Amount: {total}")
        print("\n\nPress any key to return to the Buyer Menu...")
        input()
        self.buyer()


class Product(Bill):
    def add_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        print("\n\n\t\t\t Add New Product:")
        try:
            self.itemcode = int(input("\n\n\tEnter Code of the Product: "))
            self.itemName = input("\n\n\tEnter the Name of Product: ")
            self.rate = float(input("\n\n\tEnter the Price of Product: "))
            self.discount = float(input("\n\n\tEnter the Discount on Product: "))
            self.quantity = float(input("\n\n\tEnter the Quantity of Product: "))
        except ValueError:
            print("\n\n Invalid input. Please enter correct values.")
            input()
            self.administrator()
            return

        item_exists = False
        try:
            with open("Database7.txt", "r") as data:
                for line in data:
                    c, _, _, _, _ = line.strip().split("\t")
                    if int(c) == self.itemcode:
                        item_exists = True
                        print("\n\tProduct Already Exists!")
                        break
        except FileNotFoundError:
            pass

        if not item_exists:
            with open("Database7.txt", "a") as data:
                data.write(f"{self.itemcode}\t{self.itemName}\t{self.rate}\t{self.discount}\t{self.quantity}\n")
                print("\n\n\tRecord Inserted Successfully!")

        print("\n\nPress any key to return to the Administrator Menu...")
        input()
        self.administrator()

    def edit_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        print("\n\t\t\t MODIFYING THE RECORD OF PRODUCTS ")
        try:
            pkey = int(input("\n\t\t\tProduct Code: "))
        except ValueError:
            print("\n\n Invalid input. Please enter a numeric value.")
            input()
            self.administrator()
            return

        found = False
        temp_data = []
        try:
            with open("Database7.txt", "r") as data:
                for line in data:
                    itemcode, itemName, rate, discount, quantity = line.strip().split("\t")
                    itemcode = int(itemcode)
                    if pkey == itemcode:
                        print("\n\t\t Enter the New Code of Product: ")
                        itemcode = int(input())
                        print("\n\t\t Enter the New Name of Product: ")
                        itemName = input()
                        print("\n\t\t Enter the New Price of Product: ")
                        rate = float(input())
                        print("\n\t\t Enter the New Discount of Product: ")
                        discount = float(input())
                        print("\n\t\t Enter the New Quantity of Product: ")
                        quantity = float(input())
                        temp_data.append(f"{itemcode}\t{itemName}\t{rate}\t{discount}\t{quantity}\n")
                        print("\n\n\tRecord Edited.")
                        found = True
                    else:
                        temp_data.append(line)
        except FileNotFoundError:
            print("\n\n File Does Not Exist.")
            input()
            self.administrator()
            return

        with open("TempDatabase.txt", "w") as data1:
            data1.writelines(temp_data)

        os.remove("Database7.txt")
        os.rename("TempDatabase.txt", "Database7.txt")

        if not found:
            print("\n\n Record not found.")

        print("\n\nPress any key to return to the Administrator Menu...")
        input()
        self.administrator()

    def remove_product(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_title()
        print("\n\n\t Delete Product.")
        try:
            pkey = int(input("\n\n\t Product code: "))
        except ValueError:
            print("\n\n Invalid input. Please enter a numeric value.")
            input()
            self.administrator()
            return

        found = False
        temp_data = []
        try:
            with open("Database7.txt", "r") as data:
                for line in data:
                    itemcode, _, _, _, _ = line.strip().split("\t")
                    itemcode = int(itemcode)
                    if pkey == itemcode:
                        print("\n\n\t Product Deleted Successfully.")
                        found = True
                    else:
                        temp_data.append(line)
        except FileNotFoundError:
            print("File does not exist.")
            input()
            self.administrator()
            return

        with open("TempDatabase.txt", "w") as data1:
            data1.writelines(temp_data)

        os.remove("Database7.txt")
        os.rename("TempDatabase.txt", "Database7.txt")

        if not found:
            print("\n\n Record not found.")

        print("\n\nPress any key to return to the Administrator Menu...")
        input()
        self.administrator()


if __name__ == "__main__":
    b = Bill()
    b.menu()