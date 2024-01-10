class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
            print(f"{name} was already in the fridge and we added {quantity} more.")
        else:
            self.contents.append(Product(name, quantity))
            print(f"{name}x {quantity} was added to the fridge.")

    def remove_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name)
    
        if product.quantity >= quantity:
            product.quantity -= quantity
            print(f"{quantity} {name} removed from the fridge.")
        else:
            print(f"Not enough {name} in the fridge.")
            print(f"{name} not found in the fridge.")


    def print_contents(self):
        pass

    def check_recipe(self, recipe:Recipe):
        pass


def main():
    fridge = Fridge()

    while True:
        print("\nWelcome to the fridge menu:\n\n")
        print("0: Exit")
        print("1: Add product")
        print("2: Check product quantity")
        print("3: Check recipe")
        print("4: Remove product")
        print("5: Print fridge\n\n")

        choice = input("Select the menu item you would like to do: ")

        if choice.startswith('0'):
            break
        elif choice.startswith('1'):
            name = input("Which product would you like to add?: ")
            quantity = float(input("Quantity: "))
            fridge.add_product(name, quantity)

        elif choice.startswith('2'):
            name = input("List of products quantities: ")

        elif choice.startswith('3'):
            name = input("Which recipe would you like to add?: ")
            quantity = float(input("Quantity: "))
            fridge.check_recipe(name, quantity)

        elif choice.startswith('4'):
            name = input("Choose which product you would like to remove from the fridge: ")
            fridge.remove_product(name)

        elif choice.startswith('5'):
            name = input("Print the contents of your fridge: ")
            pass
        else:
            print("Incorrect command, please try again!")
            
if __name__ == "__main__":
    main()














    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)