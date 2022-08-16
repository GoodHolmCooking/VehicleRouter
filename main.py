import math
import data


# Truck object acts as a truck, carries packages, and travels
class Truck:
    def __init__(self):
        self.mileage = 0
        self.distance_dict = {}
        self.final_hub = 1
        self.cargo = []
        self.route = []
        self.hour = 8
        self.minute = 0

    # determines time of day based on distance traveled
    def update_time(self, traveled):
        new_time = round((traveled / 18) * 60)
        old_time = self.hour * 60 + self.minute
        current_time = old_time + new_time
        hours = math.floor(current_time / 60)
        minutes = current_time % 60
        self.hour = hours
        self.minute = minutes

    # takes a package and adds it to the truck's contents
    def load(self, package):
        self.cargo.append(package)
        package.update_status("en route")
        # self.update_time(self.mileage)
        minutes = self.minute
        if self.minute < 10:
            minutes = "0" + str(self.minute)
        else:
            minutes = str(self.minute)
        timestamp = str(self.hour) + ":" + minutes
        package.load_time = timestamp

    # modifies mileage and marks package as delivered
    def deliver(self, package):
        traveled = self.distance_dict[package.pkg_id]

        self.mileage += traveled
        self.update_time(traveled)
        minutes = self.minute
        if self.minute < 10:
            minutes = "0" + str(self.minute)
        else:
            minutes = str(self.minute)
        timestamp = str(self.hour) + ":" + minutes
        package.update_status("delivered", timestamp)

    # returns trucks current hub
    def location(self):
        return self.final_hub

    # adds a route to a trucks current traversal
    def add_route(self, pkg_id, route, distance):
        if not self.route:
            self.route = route
        elif len(route) > 1:
            if route[0] == self.route[-1]:
                route = route[1:]
            self.route.extend(route)
        else:
            if route[0] != self.route[-1]:
                self.route.extend(route)

        self.final_hub = route[-1]
        if pkg_id:
            self.distance_dict[pkg_id] = distance

    # truck travels, delivering packages along its route
    def travel(self):
        timestamp = str(self.hour) + ":" + str(self.minute)

        for hub in self.route:
            display_list = []
            for package in self.cargo:
                display_list.append(package.pkg_id)

            removal_list = []
            for package in self.cargo:
                destination_id = data.pkg_info[package.pkg_id]["destination"]

                if destination_id == hub:

                    self.deliver(package)
                    removal_list.append(package)
            temp_list = []
            for package in self.cargo:
                if package not in removal_list:
                    temp_list.append(package)
            self.cargo = temp_list

    # move from current hub back to base hub
    def head_home(self):
        generate_paths_from(self.final_hub)
        route_info = shortest_route(self.final_hub, 1, self)
        route = route_info["path"]
        traveled = route_info["distance"]
        self.add_route(None, route, traveled)
        self.mileage += traveled
        self.update_time(traveled)
        minutes = self.minute

        if minutes < 10:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)
        timestamp = str(self.hour) + ":" + minutes

        # reset route
        self.route = []

    # hold truck until a given time
    def delay(self, hr, min):
        self.hour = hr
        self.minute = min


# Create Vertex objects with that are connected to other Node objects via edge weights. (OPTION 2.2)
class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.prev_vertex = None


# Graph object acts as a data structure connecting verticies
class Graph:
    def __init__(self):
        self.vertex_dict = {}
        self.adjacency_list = {}
        self.edge_weights = {}

        # populate from data file. Delivery map is a dictionary containing distances
        for hub in data.delivery_map:
            hub_vertex = Vertex(hub)
            self.add_vertex(hub_vertex)

        for hub in data.delivery_map:
            for adjacent in data.delivery_map[hub]:
                self.add_directed_edge(
                    self.get_vertex(hub),
                    self.get_vertex(adjacent),
                    data.delivery_map[hub][adjacent]
                )

    # add vertex to the graph data structure
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        self.vertex_dict[new_vertex.label] = new_vertex

    # add a directed edge to the graph data structure
    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    # add an undirected edge to graph structure
    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # return vertex object based on a provided id
    def get_vertex(self, id):
        return self.vertex_dict[id]

    # remove distance information from verticies. Used for determining shortest path.
    def reset(self):
        for vertex in self.adjacency_list:
            vertex.distance = float('inf')
            vertex.prev_vertex = None


# Create a Package class that includes the 8 fields needed for the Excel spreadsheet.
class Package:
    def __init__(self, pkg_id, address, deadline, city, zipcode, weight):
        self.pkg_id = pkg_id
        self.address = address
        self.delivered = None
        self.load_time = None
        self.deadline = deadline
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.status = "at the hub"

    def get_address(self):
        return self.address

    def get_id(self):
        return self.pkg_id

    def update_status(self, update, *args):
        self.status = update
        if update == "delivered":
            self.delivered = args[0]


# Node class is used in hash table to contain data
class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
        self.tail = None

    def get_tail(self):
        return self.tail

    def set_tail(self, data):
        self.tail = data

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


# LinkedList structure made of connected Nodes
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # add information onto the end of a LinkedList
    def append(self, data):
        current_node = self.head

        if not current_node.get_data():
            current_node.set_data(data)
        else:
            while current_node.get_tail():
                current_node = current_node.get_tail()

            current_node.set_tail(Node(data))

    # return information from a node based on a provided ID
    def fetch(self, id):
        current_node = self.head

        while current_node.get_data().get_id() != id:
            current_node = current_node.get_tail()

            if not current_node.get_tail():
                break

        return current_node.get_data()

    # display information in a LinkedList
    def display(self):
        if not self.head.get_tail():
            print(self.head.get_data())

        else:
            current_node = self.head

            while current_node.get_tail():
                current_node = current_node.get_tail()


# HashTable object stores packages. Each bucket contains a LinkedList for scalability.
class HashTable:
    def __init__(self):
        self.capacity = range(40)
        self.structure = []
        for bucket in self.capacity:
            self.structure.append(LinkedList(None))

    # takes an id and creates a hash for insertion and retrieval into the hashtable
    def get_hash(self, id):
        table_hash = id / 40
        table_hash = math.ceil(table_hash)
        table_hash = 40 * table_hash
        table_hash = table_hash - id - 1
        return table_hash

    # take a package and insert into the HashTable based off the id
    def insert(self, pkg):
        id = pkg.get_id()
        table_hash = self.get_hash(id)

        self.structure[table_hash].append(pkg)

    # take an id and return package from the HashTable
    def lookup(self, id):
        table_hash = self.get_hash(id)

        pkg = self.structure[table_hash].fetch(id)
        return pkg

    # display the information in the HashTable for troubleshooting purposes
    def display(self):
        count = 1
        for node in self.structure:
            print("Bucket #", count, "contents:")
            node.display()
            print("\n")
            count += 1


# traverse the graph. Find the shortest route between the start and end
def shortest_route(start_id, end_id, truck):
    start_vertex = graph.get_vertex(start_id)
    end_vertex = graph.get_vertex(end_id)
    route = []

    distance = end_vertex.distance

    current_vertex = end_vertex

    # keep checking until start is found
    while current_vertex is not start_vertex:
        # label is the name of the vertex. This is also the id. The id can be used to fetch data. Appended as label for this reason.
        route.append(current_vertex.label)
        if current_vertex.prev_vertex:
            current_vertex = current_vertex.prev_vertex
        else:
            break

    route.append(start_vertex.label)

    # the reverse method makes sure that the truck will begin at its starting point and travel to the end.
    route.reverse()

    route_info = {"path": route, "distance": distance, "truck": truck}

    return route_info


# this function traverses the graph and assigns distance values to each vertex
def generate_paths_from(start_hub):
    # graph stores distances between vertices as a dictionary
    # this function would add information onto previously set distances
    # the reset function clears all the data and resets the information to zero
    graph.reset()
    unvisited_queue = []

    # adjacency list is a dictionary. Every vertex is assigned a list of all adjacent vertices
    # this should run through the entire graph and create a queue the algorithm will need to visit
    for current_vertex in graph.adjacency_list:
        unvisited_queue.append(current_vertex)

    start_vertex = graph.get_vertex(start_hub)
    start_vertex.distance = 0

    # while still unvisited vertices, record the distance from the start to the unvisited vertex
    # this information is then stored into the graph itself as a variable
    while len(unvisited_queue) > 0:
        smallest_index = 0

        for i in range(0, len(unvisited_queue)):

            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i

        current_vertex = unvisited_queue.pop(smallest_index)

        for adj_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.prev_vertex = current_vertex


# take a package
# generate all possible routes
# choose compare all possible routes and choose the shortest one
def route_packages(to_load, truck):
    # the while loop states to run until every package has been routed
    while to_load:
        possible_routes = {}

        # use the truck's location to find distances to every vertex
        generate_paths_from(truck.location())
        for package in to_load:
            destination_id = data.pkg_info[package]["destination"]
            route_info = shortest_route(truck.location(), destination_id, truck)
            possible_routes[package] = route_info

        # now the shortest route is generated for each package
        # of these routes compare them and choose the shortest
        lowest_cost = 1000000
        closest_pkg = None
        for package in possible_routes:
            if possible_routes[package]["distance"] < lowest_cost:
                lowest_cost = possible_routes[package]["distance"]
                closest_pkg = package

        # the shortest of possible routes has been found. Add that package as the next to deliver and loop
        truck.load(table.lookup(closest_pkg))
        truck.add_route(closest_pkg, possible_routes[closest_pkg]["path"], possible_routes[closest_pkg]["distance"])
        to_load.remove(closest_pkg)


# take in times, compare them. Assign a status based on user entered time and retrieved time
def compare_delivery(entered, fetched, load):
    entered_hr = int(entered.split(":")[0])
    entered_min = int(entered.split(":")[1])
    # the total variable means to unpack the hour into minutes
    # this allows times to be compared in a single operation
    entered_total = entered_hr * 60 + entered_min

    fetched_hr = int(fetched.split(":")[0])
    fetched_min = int(fetched.split(":")[1])
    fetched_total = fetched_hr * 60 + fetched_min

    load_hr = int(load.split(":")[0])
    load_min = int(load.split(":")[1])
    load_total = load_hr * 60 + load_min

    if entered_total <= fetched_total:
        # if the user entered time is less than the retrieved time, the package has not been delivered
        if entered_total < load_total:
            # if the user entered time is less than the load time, the package is still sitting at the hub
            return "At the Hub"
        else:
            # the user entered time is after the load time but before delivery. The package is en route.
            return "En Route"
    else:
        return "Delivered"


# create instances of necessary tools
graph = Graph()
table = HashTable()
truck_1 = Truck()
truck_2 = Truck()
truck_3 = Truck()

# Create 40 package objects with the appropriate data for each one
for pkg_id in data.pkg_info:
    destination_id = data.pkg_info[pkg_id]["destination"]
    destination = data.hub_info[destination_id]["street"]
    deadline = data.pkg_info[pkg_id]["deadline"]
    city = data.hub_info[destination_id]["city"]
    postal = data.hub_info[destination_id]["postal"]
    weight = data.pkg_info[pkg_id]["mass"]
    package = Package(pkg_id, destination, deadline, city, postal, weight)

    # Add each package object to the hash table using the insert() function.
    table.insert(package)

# Load packages into truck 1 based on package id
truck_1_load = [15, 13, 14, 16, 19, 20, 1, 29, 30, 31, 34, 40, 37, 5]

# Load packages into truck 2 based on package id
truck_2_load = [38, 7, 17, 21]

# Take the packages and determine appropriate routes for trucks 1 & 2
route_packages(truck_1_load, truck_1)
route_packages(truck_2_load, truck_2)

# Send truck 1 along its route
truck_1.travel()

# Tell truck 1 to head back to home base after finishing its deliveries
truck_1.head_home()

# Send truck 2 along its route
truck_2.travel()

# Tell truck 2 to head back to home base after finishing its deliveries
truck_2.head_home()

# Repeat above methods to route and deliver the remaining packages
truck_2_load = [28, 32, 36, 18, 2, 4, 6, 25, 3]
route_packages(truck_2_load, truck_2)
truck_2.travel()

# The driver from truck 1 now steps into the already loaded truck 3
truck_3.delay(10, 20)
truck_3_load = [9, 8, 7, 10, 11, 12, 22, 23, 24, 26, 27, 33, 35, 39]
route_packages(truck_3_load, truck_3)
truck_3.travel()


# Begin user interface
input_valid = False
entered_time = input("Enter a time in military time:\n")

# Validate input
while not input_valid:
    colon_present = False
    correct_format = False
    correct_range = False

    if ':' in entered_time:
        colon_present = True

        hours = entered_time.split(':')[0]
        minutes = entered_time.split(':')[1]

        if hours.isdigit() and minutes.isdigit() and len(minutes) == 2:
            correct_format = True
            hours = int(hours)
            minutes = int(minutes)

            if (hours >= 0 and hours <= 24) and (minutes >= 0 and minutes <= 60):
                correct_range = True

            else:
                print("Time must be in correct range. Do not enter minutes greater than 60 or hours greater than 24.")

        else:
            print("Do not include AM, PM, or other characters. Enter time in military time. Not 1:00 PM but 13:00. Include two digits after colon.")

    else:
        print("Time must be in format: %%:%%.")

    if colon_present and correct_format and correct_range:
        input_valid = True
    else:
        entered_time = input("Enter a time in military time:\n")

# Create graph displayed in CLI
cell_width = 30
empty_cell = "{:<%s}" % cell_width
display_row = empty_cell * 4
break_row = "#" * cell_width * 5
header_row = display_row.format("ID", "Status", "Time delivered", "Address")
print(header_row)

# Display information based on time entered
for pkg_id in data.pkg_info:
    package = table.lookup(pkg_id)
    delivery_time = package.delivered
    delivery_status = compare_delivery(entered_time, delivery_time, package.load_time)

    if delivery_status == "Delivered":
        package_row = display_row.format(pkg_id, delivery_status, delivery_time, package.address)
    else:
        package_row = display_row.format(pkg_id, delivery_status, "", package.address)

    print(break_row)
    print(package_row)
    print(break_row)
    print("\n")

total_mileage = truck_1.mileage + truck_2.mileage + truck_3.mileage
print("Total mileage by all trucks when using this algorithm:", total_mileage)

# Holds program open so information may be observed
input("Enter a character to exit the code")
