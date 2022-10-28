class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []
        self.inventory = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})
        for ingredient in self.INGREDIENTS[order]:
            if (
                self.MINIMUM_INVENTORY[ingredient]
                == self.inventory[ingredient]
            ):
                return False
            self.inventory[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_inventory(self):
        return set({k, i} for k, i in self.inventory.items() if i > 0)

    def get_available_dishes(self):
        avaiable = set()
        avaiable_ingredients = set()

        for k, v in self.MINIMUM_INVENTORY.items():
            if self.inventory[k] < v:
                avaiable_ingredients.add(k)

        for k, i in self.INGREDIENTS.items():
            if set(i).issubset(avaiable_ingredients):
                avaiable.add(k)

        return avaiable
