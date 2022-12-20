import csv
from collections import defaultdict


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, "r") as file:
            data = csv.reader(file)
            for orders in data:
                default = defaultdict(list)
                default["cliente"].append(orders[0])
                default["pedido"].append(orders[1])
                default["dia"].append(orders[2])

                print(orders)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
