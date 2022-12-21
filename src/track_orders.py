from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append([customer, order, day])

    def get_number_of_orders_per_dish(self, customer):
        customer_orders = [
            order[1] for order in self._data if order[0] == customer
        ]
        return Counter(customer_orders).most_common()[0][0]

    def get_customer_count_dish(self, customer, dish):
        custumer_orders = [
            order[1]
            for order in self._data
            if order[0] == customer and order[1] == dish
        ]
        return len(custumer_orders)

    def get_never_ordered_per_customer(self, customer):
        dishes = set(order[1] for order in self._data)
        customer_orders = set(
            order[1] for order in self._data if order[0] == customer
        )
        return dishes - customer_orders

    def get_days_never_visited_per_customer(self, customer):
        days = set(order[2] for order in self._data)
        customer_days = set(
            order[2] for order in self._data if order[0] == customer
        )
        return days - customer_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
