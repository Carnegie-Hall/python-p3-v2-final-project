from boba import Boba
from tea import Tea
from globals import clear, space, any_key_to_continue, invalid_choice

class Cli():
    def start(self):
        clear()
        print("Welcome To Grab & Go Boba!")
        space()
        self.main_menu()

    def restart_main_menu(self):
        any_key_to_continue()
        clear()
        self.main_menu()

    def restart_boba_details(self, boba):
        any_key_to_continue()
        clear()
        self.print_boba_details(boba)
        self.boba_details(boba)

    def restart_tea_details(self, tea):
        any_key_to_continue()
        clear()
        self.print_tea_details(tea)
        self.tea_details(tea)

    def main_menu(self):
        space()
        print("Type 1 to list Teas")
        print("Type 2 to list Bobas")
        print("Type 3 to create a Tea")
        print("Type 4 to create a boba")
        print("Type 5 to select a tea")
        print("Type 6 to select a boba")
        print("Type 'exit' to exit our app")
        space()
        self.main_menu_selection()

    def boba_details_menu(self, boba):
        space()
        print(f"Type 1 to edit {boba.name}")
        print(f"Type 2 to delete {boba.name}")
        print("Type 3 to purchase some teabags")
        print("Type 'main' to exit our app")
        space()
        self.boba_details_menu_selection(boba)

    def boba_details_menu_selection(self, boba):
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            print("upgrading boba")
            self.restart_boba_details(boba)
        elif user_input == "2":
            clear()
            print("that wasn't the right boba...")
            self.restart_boba_details(boba)
        elif user_input == "3":
            clear()
            print("fresh boba coming right up!")
            self.restart_boba_details(boba)
        elif user_input == "main":
            clear()
            print("Let's get you started from scratch!")
        else:
            clear()
            invalid_choice()
            self.restart_boba_details(boba)

    def tea_details_menu(self, tea):
        space()
        print(f"Type 1 to edit {tea.name}")
        print(f"Type 2 to delete {tea.name}")
        print("Type 3 to purchase some boba")
        print("Type 'main' to exit our app")
        space()
        self.tea_details_menu_selection(tea)

    def tea_details_menu_selection(self, tea):
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            print("changing tea")
            self.restart_tea_details(tea)
        elif user_input == "2":
            clear()
            print("that wasn't the right tea...")
            self.restart_tea_details(tea)
        elif user_input == "3":
            clear()
            print("fresh boba coming right up!")
            self.restart_tea_details(tea)
        elif user_input == "main":
            clear()
            print("Let's get you started from scratch!")
        else:
            clear()
            invalid_choice()
            self.restart_tea_details(tea)

    def main_menu_selection(self):
        user_input = input("Enter here: ")
        if user_input == "1":
            clear()
            self.list_teas()
            self.restart_main_menu()

        elif user_input == "2":
            clear()
            self.list_bobas()
            self.restart_main_menu()
            
        elif user_input == "3":
            clear()
            self.create_tea()
            self.restart_main_menu()

        elif user_input == "4":
            clear()
            self.create_boba()
            self.restart_main_menu()

        elif user_input == "5":
            clear()
            self.select_tea()
            self.restart_main_menu()

        elif user_input == "6":
            clear()
            self.select_boba()
            self.restart_main_menu()

        elif user_input == "exit":
            clear()
            print("Buh-bye!")

        else:
            clear()
            invalid_choice()
            self.restart_main_menu()

    def list_teas(self):
        print("Here are your Lovely Teas!")
        print('--------')
        i = 1
        for tea in Tea.all():
            self.print_tea(tea, i)
            i = i + 1

    def print_tea(self, tea, list_number):
        print(f"Name:{list_number}. {tea.name}")

    def print_tea_details(self, tea):
        space()
        print(f"{tea.name} Details")
        print("--------")
        space()
        print("")
        print(f"Name: {tea.name}")
        space()
        print("Bobas: ")
        self.print_tea_bobas(tea)
    
    def print_boba_details(self, boba):
        space()
        print(f"{boba.name} Details")
        print("--------")
        space()
        print("")
        print(f"Name: {boba.name}")
        space()
        print(f"Flavor: {boba.flavor}")

    def print_tea_details(self, tea):
        i = 1
        for boba in tea.bobas():
            self.print_boba(boba, 1)
            i = i + 1

    def list_bobas(self):
        print("Don't you just love boba?")
        print('--------')
        i = 1
        for boba in Boba.all():
            self.print_boba(boba, i)
            i = i + 1
    
    def print_boba(self, boba, list_number):
        print(f"Name:{list_number}. {boba.name}")

    def create_tea(self):
        print("Brewing Tea")
        print("-----------")
        space()
        tea_name = input("Enter Name: ")
        Tea.create(name=tea_name)
        clear()
        print("Order made!")

    def create_boba(self):
        print("Tapioca is Boba, Boba is Tapioca!")
        print("-----------")
        space()
        boba_name = input("Enter Name: ")
        flavor = input("What's your taste: ")
        Boba.create(name=boba_name, flavor=flavor)
        clear()
        print("That's a new flavor!")

    def select_tea(self):
        print("What tea would you like?")
        print("-----------")
        space()
        user_input = input("Enter number from the main menu: ")
        try:
            index = int(user_input) - 1
            teas = Tea.all()
            length_of_teas = len(teas)
            if index in range(0, length_of_teas):
                tea = tea[index]
                clear()
                self.print_tea_details(tea)
                self.tea_details_menu(tea)
            else:
                clear()
                invalid_choice()
        except ValueError as error:
            clear()
            invalid_choice()
            clear()

    def select_boba(self):
        print("What boba would you like?")
        print("-----------")
        space()
        user_input = input("Enter number from the main menu: ")
        try:
            index = int(user_input) - 1
            bobas = Boba.all()
            length_of_bobas = len(bobas)
            if index in range(0, length_of_bobas):
                boba = bobas[index]
                clear()
                self.print_boba_details(boba)
                self.boba_details_menu(boba)
            else:
                clear()
                invalid_choice()
        except ValueError as error:
            clear()
            invalid_choice()
            clear()
            