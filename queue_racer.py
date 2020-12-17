from queue import Queue as StudentQueue
from collections import deque

import unittest
from io import StringIO
from test_queue import TestGetItemBuiltin, TestCountMethod, TestIndexMethod, \
                        TestLenBuiltin, TestInsertMethod, TestRemoveMethod, \
                        TestPopleftMethod, TestAppendMethod, TestBasic

import random
import time
from tqdm import tqdm
from copy import copy

from order import Order

data_size = 10000 
iterations = 10

struct_names_dict = {
    StudentQueue: "StudentQueue",
    deque: "Python deque",
    list: "Python list "
}

class time_iterations():
    def __init__(self, struct_name, iterations):
        self.struct_name = struct_name
        self.iterations = iterations

    def __enter__(self):
        self.elapsed_time = 0
        return self

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.stop_time = time.perf_counter()
        self.elapsed_time += self.stop_time - self.start_time

    def __exit__(self, exc_type, exc, exc_tb):
        print(f" ---> {self.struct_name} .............. {self.elapsed_time / self.iterations} sec/it")
        return False

def test_functionality(TestCase):
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(TestCase))
    if len(result.errors) > 0:
        print()
        print(" -------------------------------------------------------------------")
        print("|                          ⚠️   Warning  ⚠️                           |")
        print("|      It seems your StudentQueue queue has not passed all the      |")
        print("|  functionality tests for this queue function. This may cause the  |")
        print("|  performace of your queue to be worse (or better) than expected.  |")
        print("|                                                                   |")
        print("|  Make sure that your queue passes the functionality tests in the  |")
        print("|    test_queue.py file before doing speed tests with this file.    |")
        print(" -------------------------------------------------------------------")
        print()

def generate_orders(data_size, randomize=False, unique=True):
    orders = []
    if unique:
        for i in range(data_size):
            o = Order(i)
            o.buyer = "test buyer"
            o.shipping_address = "test order"
            o.contents = "test order"
            orders.append(o)
    else:
        for i in range(0, data_size, 5):
            o = Order(i)
            o.buyer = "test buyer"
            o.shipping_address = "test order"
            o.contents = "test order"
            for i in range(5):
                orders.append(o)
        for i in range(data_size%5):
            o = Order(data_size-1)
            o.buyer = "test buyer"
            o.shipping_address = "test order"
            o.contents = "test order"
            orders.append(o)

    if randomize:
        random.shuffle(orders)
    return orders

def basic_tests(structs):
    random_orders = generate_orders(data_size, randomize=True)
    print()
    print("===========")
    print("Basic Tests")
    print("===========")
    TestCase = tests["Basic"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing {data_size} append() followed by {data_size} pop():")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for order in random_orders:
                    q.append(order)
                for i in range(data_size):
                    if struct == list:
                        q.pop(0)
                    else:
                        q.popleft()
                timer.stop()
    print()
    print(f"Testing {data_size} append()/pop() combinations:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for order in random_orders:
                    q.append(order)
                    if struct == list:
                        q.pop(0)
                    else:
                        q.popleft()
                timer.stop()

def append_tests(structs):
    random_orders = generate_orders(data_size, randomize=True)
    print()
    print("============")
    print("Append Tests")
    print("============")
    TestCase = tests["Append"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing {data_size} append():")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for order in random_orders:
                    q.append(order)
                timer.stop()

def pop_tests(structs):
    random_orders = generate_orders(data_size, randomize=True)
    print()
    print("=========")
    print("Pop Tests")
    print("=========")
    TestCase = tests["Pop"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing {data_size} popleft():")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        base_q = struct()
        for order in random_orders:
            base_q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                if struct == StudentQueue: #need to recopy queue every time to preserve pseudo-pointers

                    q = struct()
                    for order in random_orders:
                        q.append(order)
                else:
                    q = copy(base_q)
                timer.start()
                for i in range(data_size):
                    if struct == list:
                        q.pop(0)
                    else:
                        q.popleft()
                timer.stop()

def remove_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("============")
    print("Remove Tests")
    print("============")
    TestCase = tests["Remove"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing {data_size} remove() from front of queue:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        base_q = struct()
        for order in orders:
            base_q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                if struct == StudentQueue: #need to recopy queue every time to preserve pseudo-pointers

                    q = struct()
                    for order in orders:
                        q.append(order)
                else:
                    q = copy(base_q)
                timer.start()
                for order in orders:
                    q.remove(order)
                timer.stop()

    print()
    print(f"Testing {data_size} remove() from end of queue:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        base_q = struct()
        for order in orders:
            base_q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                if struct == StudentQueue: #need to recopy queue every time to preserve pseudo-pointers
                    q = struct()
                    for order in orders:
                        q.append(order)
                else:
                    q = copy(base_q)
                timer.start()
                for order in reversed(orders):
                    try:
                        q.remove(order)
                    except ValueError:
                        print(order)
                        raise ValueError
                timer.stop()

    print()
    print(f"Testing {data_size} remove() from random location in queue:")
    orders_random = copy(orders)
    random.shuffle(orders_random)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        base_q = struct()
        for order in orders:
            base_q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                if struct == StudentQueue: # need to recopy queue every time to preserve pseudo-pointers
                    q = struct()
                    for order in orders:
                        q.append(order)
                else:
                    q = copy(base_q)
                timer.start()
                for order in orders_random:
                    q.remove(order)
                timer.stop()

def insert_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("============")
    print("Insert Tests")
    print("============")
    TestCase = tests["Insert"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing {data_size} insert() into front of queue:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for order in orders:
                    q.insert(0, order)
                timer.stop()

    print(f"Testing {data_size} insert() into back of queue:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for i, order in enumerate(orders):
                    q.insert(i, order)
                timer.stop()

    print(f"Testing {data_size} insert() into random index of queue:")
    insert_sequence = [random.randint(0, i) for i in range(data_size)]
    for struct in structs:
        struct_name = struct_names_dict[struct]
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                q = struct()
                timer.start()
                for index, order in zip(insert_sequence, orders):
                    q.insert(index, order)
                timer.stop()

def len_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("=========")
    print("Len Tests")
    print("=========")
    TestCase = tests["Length"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing getting len() of queue of size {data_size}:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                len(q)
                timer.stop()

def index_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("===========")
    print("Index Tests")
    print("===========")
    TestCase = tests["Index"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing getting index() of element in sorted queue with {data_size} unique elements:")
    search_sequence = random.sample(orders, iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.index(order)
                timer.stop()

    print(f"Testing getting index() of element in unsorted queue with {data_size} unique elements:")
    random_orders = generate_orders(data_size, randomize=True)
    search_sequence = random.sample(random_orders, iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.index(order)
                timer.stop()

    print(f"Testing getting index() of element in unsorted queue with {data_size} nonunique elements:")
    random_orders = generate_orders(data_size, randomize=True, unique=False)
    search_sequence = random.sample(set(random_orders), iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.index(order)
                timer.stop()

def count_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("===========")
    print("Count Tests")
    print("===========")
    TestCase = tests["Count"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing getting count() of elements in sorted queue with {data_size} unique elements:")
    search_sequence = random.sample(orders, iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.count(order)
                timer.stop()

    print(f"Testing getting count() of elements in unsorted queue with {data_size} unique elements:")
    random_orders = generate_orders(data_size, randomize=True)
    search_sequence = random.sample(random_orders, iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.count(order)
                timer.stop()

    print(f"Testing getting count() of elements in unsorted queue with {data_size} nonunique elements:")
    random_orders = generate_orders(data_size, randomize=True, unique=False)
    search_sequence = random.sample(set(random_orders), iterations)
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                order = search_sequence[i]
                q.count(order)
                timer.stop()

def get_elem_at_index_tests(structs):
    orders = generate_orders(data_size)
    print()
    print("========")
    print("[] Tests")
    print("========")
    TestCase = tests["[]"]["functionality_test_class"]
    test_functionality(TestCase)
    print(f"Testing getting element at an index ([]) from a sorted queue with {data_size} unique elements:")
    random_indices = [random.randint(0,data_size) for i in range(iterations)]
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                index = random_indices[i]
                q[index]
                timer.stop()

    print(f"Testing getting element at an index ([]) from an unsorted queue with {data_size} unique elements:")
    random_orders = generate_orders(data_size, randomize=True)
    random_indices = [random.randint(0,data_size) for i in range(iterations)]
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                index = random_indices[i]
                q[index]
                timer.stop()

    print(f"Testing getting random element at an index ([]) from an unsorted queue with {data_size} nonunique elements:")
    random_orders = generate_orders(data_size, randomize=True, unique=False)
    random_indices = [random.randint(0,data_size) for i in range(iterations)]
    for struct in structs:
        struct_name = struct_names_dict[struct]
        q = struct()
        for order in random_orders:
            q.append(order)
        with time_iterations(struct_name, iterations) as timer:
            for i in tqdm(range(iterations), desc=struct_name, leave=False):
                timer.start()
                index = random_indices[i]
                q[index]
                timer.stop()

def all_tests(structs):
    for test in tests:
        if not test == "Grand Prix":
            test_func = tests[test]["function"]
            test_func(structs)

tests = {
        "Basic": { 
            "description": "Append/Pop {} times".format(data_size),
            "function": basic_tests,
            "functionality_test_class": TestBasic
        },
        "Append": {
            "description": "Append {} times".format(data_size),
            "function": append_tests,
            "functionality_test_class": TestAppendMethod
        },
        "Pop": {
            "description": "Popleft {} times".format(data_size),
            "function": pop_tests,
            "functionality_test_class": TestPopleftMethod
        },
        "Remove": {
            "description": "Remove {} times".format(data_size),
            "function": remove_tests,
            "functionality_test_class": TestRemoveMethod
        },
        "Insert": {
            "description": "Insert {} times".format(data_size),
            "function": insert_tests,
            "functionality_test_class": TestInsertMethod
        },
        "Length": {
            "description": "Get len() of queues of varying sizes",
            "function": len_tests,
            "functionality_test_class": TestLenBuiltin
        },
        "Index": {
            "description": "Get index of element {} times".format(data_size),
            "function": index_tests,
            "functionality_test_class": TestIndexMethod
        },
        "Count": {
            "description": "count from {} elements".format(data_size),
            "function": count_tests,
            "functionality_test_class": TestCountMethod
        },
        "[]": {
            "description": "Get element at an index {} times".format(data_size),
            "function": get_elem_at_index_tests,
            "functionality_test_class": TestGetItemBuiltin
        },
        "Grand Prix": {
            "description": "All tests",
            "function": all_tests
        }
}



if __name__ == '__main__':
    print()
    print("======================================")
    print("🏁 Welcome to the cs10 queue racer! 🏁")
    print("======================================")
    print()
    print("The following data structures are warming up for today's race:")
    print("(0) StudentQueue")
    print("(1) Python deque")
    print("(2) Python list")
    print()
    choice = input("Input the numbers of the structures to compete: ")
    structs = []
    if "0" in choice:
        structs.append(StudentQueue)
    if "1" in choice:
        structs.append(deque)
    if "2" in choice:
        structs.append(list)

    print()
    print("Tracks:")
    for i, test in enumerate(tests):
        print("({}) {} Track ({})".format(i, test, tests[test]["description"]))
    test_choice = None
    while test_choice not in [str(num) for num in range(len(tests))]:
        test_choice = input("Select a track: ")
    test_choice = list(tests)[int(test_choice)]
    test_func = tests[test_choice]["function"]
    
    print()
    print("On your marks, get set, go! {}".format("  ".join(["🏎" for i in range(len(structs))])))
    test_func(structs)
    print()
    print("----------- Tests complete! -----------")
