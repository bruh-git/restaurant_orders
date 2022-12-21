import csv
from track_orders import TrackOrders
from collections import defaultdict


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    track_orders = TrackOrders()
    try:
        with open(path_to_file, "r") as file:
            data = csv.reader(file)
            for orders in data:
                default = defaultdict(list)
                default["custumer"].append(orders[0])
                default["order"].append(orders[1])
                default["day"].append(orders[2])
                return default
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    maria_ordered_dish = track_orders.get_number_of_orders_per_dish("maria")
    arnald_burguer = track_orders.get_customer_count_dish(
        "arnaldo", "hamburguer")
    joao_never_ordered = track_orders.get_never_ordered_per_customer("joao")
    joao_never_visited_days = track_orders.get_days_never_visited_per_customer(
        "joao"
    )
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{maria_ordered_dish}\n"
            f"{arnald_burguer}\n"
            f"{joao_never_ordered}\n"
            f"{joao_never_visited_days}\n"
        )
