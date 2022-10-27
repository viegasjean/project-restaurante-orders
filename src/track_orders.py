from collections import Counter


class TrackOrders:
    def __init__(self):
        self.data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({'customer': customer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = Counter(i['order']
                for i
                in self.data
                if i["customer"] == customer)
        return customer_orders.most_common(1)[0][0]

    def get_set_of_all_customer_orders(self):
        return set(i['order'] for i in self.data)

    def get_set_of_customer_orders(self, customer):
        return set(i['order'] for i in self.data if i['customer'] == customer)

    def get_never_ordered_per_customer(self, customer):
        all_orders = self.get_set_of_all_customer_orders()
        customer_orders = self.get_set_of_customer_orders(customer)
        return all_orders - customer_orders

    def get_set_of_all_customer_days(self):
        return set(i['day'] for i in self.data)

    def get_set_of_customer_days(self, customer):
        return set(i['day'] for i in self.data if i['customer'] == customer)

    def get_days_never_visited_per_customer(self, customer):
        all_days = self.get_set_of_all_customer_days()
        customer_days = self.get_set_of_customer_days(customer)
        return all_days - customer_days

    def get_busiest_day(self):
        days = Counter(i['day']
                for i
                in self.data)
        return days.most_common(1)[0][0]

    def get_least_busy_day(self):
        days = Counter(i['day']
                for i
                in self.data)
        return days.most_common()[-1][0]
