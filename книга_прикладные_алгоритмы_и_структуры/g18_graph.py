class Vertex:
    def __init__(self, value, adjacent_vertices=None):
        if adjacent_vertices is None:
            adjacent_vertices = []
        self.value = value
        self.adjacent_vertices = adjacent_vertices

    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    def dfs_traverse(self, visited_vertices=None):
        """
        Выполняет обход графа в глубину, начиная с текущей вершины.

        Аргументы:
            visited_vertices (dict): Словарь, который отслеживает посещенные вершины. По умолчанию None.

        Возвращает:
            None
        """
        if visited_vertices is None:
            visited_vertices = {}
        visited_vertices[self.value] = True

        # Выводим значение вершины, чтобы убедиться
        # в работоспособности алгоритма:
        print(self.value)
        # Перебираем соседей текущей вершины:

        for adjacent_vertex in self.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                adjacent_vertex.dfs_traverse(visited_vertices)

    def dfs(self, search_value, visited_vertices=None):
        """
        Алгоритм поиска в глубину (DFS) для обхода графа и поиска заданного значения.

        Параметры:
            search_value (любой): Значение, которое необходимо найти в графе.
            visited_vertices (dict): Словарь для отслеживания посещенных вершин. По умолчанию пустой словарь.

        Возвращает:
            bool: True, если значение найдено в графе, False в противном случае.
        """
        if visited_vertices is None:
            visited_vertices = {}
        visited_vertices[self.value] = True
        if search_value == self.value:
            return True
        for adjacent_vertex in self.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                if adjacent_vertex.dfs(search_value, visited_vertices):
                    return True
        return False


alias = Vertex("alias", [])
bob = Vertex("bob", [])
cynthia = Vertex("cynthia", [])

alias.add_adjacent_vertex(bob)
alias.add_adjacent_vertex(cynthia)
bob.add_adjacent_vertex(cynthia)
cynthia.add_adjacent_vertex(bob)

print(alias.adjacent_vertices)
print(bob.adjacent_vertices)

print(alias.dfs("cynthia"))


def my_decorator(argument):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"дополнительный аргумент {argument}")
            result = func(*args, **kwargs)
            print(f"вызвана функция {func.__name__}")
            return result

        return wrapper

    return decorator


@my_decorator("Привет")
def say_hello(name):
    print(f"hello, {name}")


d = {'name': 'Bob'}
say_hello(d.get('name'))


class Person:
    def __init__(self, name):
        __name__ = name

    def getAge(self):
        print(__name__)


p = Person("John")
p.getAge()


def my_function():
    if not hasattr(my_function, 'counter'):
        my_function.counter = 0
    my_function.counter += 1

    print(f"функция вызвана {my_function.counter} раз")


my_function()
my_function()
my_function()


class WeightedGraphVertex:
    def __init__(self, value, adjacent_vertices=None):
        if adjacent_vertices is None:
            adjacent_vertices = {}
        self.value = value
        self.adjacent_vertices = adjacent_vertices

    def add_adjacent_vertices(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight


class City:
    def __init__(self, name: str, routes: dict = None):
        if routes is None:
            routes = {}
        self.routes = routes
        self.name = name

    def add_route(self, city, price):
        self.routes[city] = price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)
boston.add_route(chicago, 120)
boston.add_route(denver, 180)
chicago.add_route(el_paso, 80)
denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

print(atlanta.routes)


def dijkstra_shortest_path(starting_city: City, final_destination: City):
    cheapest_price_table: dict = {}
    cheapest_previous_stopover_city_table: dict = {}

    unvisited_cities: list = []

    visited_cities: dict = {}

    cheapest_price_table[starting_city.name] = 0

    current_city: City = starting_city

    while current_city is not None:
        visited_cities[current_city.name] = True
        if current_city in unvisited_cities:
            unvisited_cities.remove(current_city)

        for adjacent_city, price in current_city.routes.items():
            if adjacent_city.name not in visited_cities:
                unvisited_cities.append(adjacent_city)

            price_through_current_city = cheapest_price_table[current_city.name] + price

            if (adjacent_city.name not in cheapest_price_table or price_through_current_city <
                    cheapest_price_table[
                        adjacent_city.name]):
                cheapest_price_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name

        # Переходим к следующему из еще не nосещенных городов. Выбираем тот,
        # куда дешевле всего добраться из НАЧАЛЬНОГО:

        if unvisited_cities:
            current_city = min(unvisited_cities, key=lambda city: cheapest_price_table[city.name])
        else:
            current_city = None  # TODO сделать на куче

    shortest_path = []

    current_city_name = final_destination.name

    while current_city_name != starting_city.name:
        shortest_path.append(current_city_name)
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]

    shortest_path.append(starting_city.name)
    shortest_path.reverse()

    return shortest_path


print("path:", dijkstra_shortest_path(atlanta, el_paso))
