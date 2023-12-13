import collections


class TrackOrders:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def add_new_order(self, costumer, order, day):
        self.list.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        filtra_cliente = [
            indice[1] for indice in self.list if indice[0] == costumer
        ]
        resultado = collections.Counter(filtra_cliente).most_common()[0][0]
        return resultado

    def get_never_ordered_per_costumer(self, costumer):
        conjunto_pratos_cliente = {
            indice[1] for indice in self.list if costumer not in indice
        }
        conjunto_pratos = {
            indice[1] for indice in self.list if costumer in indice
        }
        return conjunto_pratos_cliente - conjunto_pratos

    def get_days_never_visited_per_costumer(self, costumer):
        conjunto_dias = {
            indice[2] for indice in self.list if costumer not in indice
        }
        conjunto_dias_gerais = {
            indice[2] for indice in self.list if costumer in indice
        }
        return conjunto_dias - conjunto_dias_gerais

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
