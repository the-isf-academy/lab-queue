from queue import Queue as StudentQueue
from collections import deque

import random
import time
from tqdm import tqdm

from order import Order

data_size = 10000
iterations = 25

struct_names_dict = {
    StudentQueue: "StudentQueue",
    deque: "Python deque",
    list: "Python list "
}

def stub(structs):
    print(structs)

def generate_orders(data_size, randomize=False, repeat=False):
    orders = []
    for i in range(data_size):
        o = Order(i)
        o.buyer = "test buyer"
        o.shipping_address = "test order"
        o.contents = "test order"
        orders.append(o)
    if randomize:
        random.shuffle(orders)
    return orders

def basic(structs):
    random_orders = generate_orders(data_size, randomize=True)
    print()
    print("==========")
    print("Basic test")
    print("==========")
    print(f"Testing {data_size} appends followed by {data_size} pops:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        for i in tqdm(range(iterations), desc=struct_name):
            q = struct()
            for order in random_orders:
                q.append(order)
            for i in range(data_size):
                if struct == list:
                    q.pop(0)
                else:
                    q.popleft()
    print()
    print(f"Testing {data_size} append/pop combinations:")
    for struct in structs:
        struct_name = struct_names_dict[struct]
        for i in tqdm(range(iterations), desc=struct_name):
            q = struct()
            for order in random_orders:
                q.append(order)
                if struct == list:
                    q.pop(0)
                else:
                    q.popleft()

tests = {
        "Basic": { 
            "description": "(Append/Pop {} times)".format(data_size),
            "function": basic
        },
        "Append": {
            "description": "(Append {} times)".format(data_size),
            "function": stub
        },
        "Pop": {
            "description": "(Pop {} times)".format(data_size),
            "function": stub
        },
        "Remove": {
            "description": "(Remove {} times)".format(data_size),
            "function": stub
        },
        "Insert": {
            "description": "(Insert {} times)".format(data_size),
            "function": stub
        },
        "Length": {
            "description": "(Get len() of queues of varying sizes)",
            "function": stub
        },
        "Index": {
            "description": "(Get index of element {} times)".format(data_size),
            "function": stub
        },
        "Count": {
            "description": "(count from {} elements)".format(data_size),
            "function": stub
        },
        "[]": {
            "description": "(Get element at an index {} times)".format(data_size),
            "function": stub
        },
        "Grand Prix": {
            "description": "(All tests above)",
            "function": stub
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
    print("tracks:")
    for i, test in enumerate(tests):
        print("({}) {} Track ({})".format(i, test, tests[test]["description"]))
    test_choice = None
    while test_choice not in [str(num) for num in range(len(tests))]:
        test_choice = input("Select a track: ")
    test_choice = list(tests)[int(test_choice)]
    test = tests[test_choice]["function"]
    
    print()
    print("On your marks, get set, go!")
    test(structs)
    print()
    print("----------- Tests complete! -----------")
