import csv

from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    if not path_to_file.endswith('csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    track_orders = TrackOrders()
    try:
        with open(path_to_file, encoding="utf-8") as file:
            orders1 = csv.reader(file, delimiter=",", quotechar='"')
            for customer, order, day in orders1:
                track_orders.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    ln1 = track_orders.get_most_ordered_dish_per_customer("maria")
    ln2 = track_orders.get_times_order_ordered_dish_per_customer(
        "arnaldo", "hamburguer"
    )
    ln3 = track_orders.get_never_ordered_per_customer("joao")
    ln4 = track_orders.get_days_never_visited_per_customer("joao")
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{ln1}\n" f"{ln2}\n" f"{ln3}\n" f"{ln4}\n")
