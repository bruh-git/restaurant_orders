class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = dict(self.MINIMUM_INVENTORY)

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] <= 0:
                return False
            self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        """ ref:
        https://cienciaprogramada.com.br/2022/04/funcao-max-em-python/
        https://pythonacademy.com.br/blog/dict-comprehensions-no-python
        """
        return {
            key: max(self.MINIMUM_INVENTORY[key] - self.inventory[key], 0)
            for key in self.MINIMUM_INVENTORY
        }

    def get_available_dishes(self):
        ingredients_stock = set()
        dishes_stock = set()

        for ingredient in self.inventory:
            if self.inventory[ingredient] > 0:
                ingredients_stock.add(ingredient)

        for dish, ingredients in self.INGREDIENTS.items():
            if set(ingredients).issubset(ingredients_stock):
                dishes_stock.add(dish)

        return dishes_stock
