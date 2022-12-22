import csv
from track_orders import TrackOrders


def analyze_log(path_to_file):
    track_orders = TrackOrders()
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, 'r') as file:
            csv_reader = csv.reader(file)
            for customer, order, day in csv_reader:
                track_orders.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')


"""    maria_ordered = track_orders.get_most_ordered_dish_per_customer("maria")
    arnald_burguer = track_orders.get_customer_count_dish(
        "arnaldo", "hamburguer")
    joao_never_ordered = track_orders.get_never_ordered_per_customer("joao")
    joao_never_visited_days = track_orders.get_days_never_visited_per_customer(
        "joao"
    )
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{maria_ordered}\n"
            f"{arnald_burguer}\n"
            f"{joao_never_ordered}\n"
            f"{joao_never_visited_days}\n"
        ) """
