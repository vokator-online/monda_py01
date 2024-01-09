class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # Options: kg, g, L, ml 
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.quantity}"


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity


    def add_product(self, name:str, quantity):
        product_id, product = self.check_product(name)
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self):
        pass

    def print_contents(self):
        pass
    def cheack_recipe(self):
        pass
    

class Recipe:
    ingredients = []
    instructions =[]

    def add_ingredient(self, product:Product):
        self
        pass

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float)


def main():
    Fridge = Fridge() # Paleidimas.