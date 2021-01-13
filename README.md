# Queue Project
In this project, students will implement a queue in Python.

## Functionality Tests
You can test the functionality of your queue implementation using the following
command:

```
python test_queue.py <TEST_TYPE>
```
Use the `TEST_TYPE` argument to test specific functionalities.
You can choose to run tests for the following interfaces (defined below):

- `min`
- `basic`
- `extension`
- `all`

## Speed Tests
Once your queue passes the all funcationlity tests for the `min` interface, you can start
running speed tests by running the following command:

```
python queue_racer.py
```

These speed tests will be used to assess the time-based efficiency of your queue implementation.

*Note: you can also run the speed tests directly from the command line. Run `python queue_racer.py -h`
for more information.*

## Interface Definitions
The following functions define different levels of the queue interface.

### Min Functions
These are the minimum requirements of a queue. We will cover these in class.

#### `append()`
Given a `data` parameter, adds the data as a new item to the end of the queue.

#### `popleft()`
Returns the first element in the queue and sets the second element to be the first.
Raises an error if no elements exist in the queue.


### Basic Functions
These are the basic functionalities for the queue that are expected for the assignment.
The speed of these functions will determine the time-based efficiency of your queue.

#### `append()`
As defined above.

#### `popleft()`
As defined above.

#### `insert()`
Given a `data` and an `index` parameter, inserts the data into the queue at the given index.
If the index is greater than the length of the queue, the data should be added to the end of the queue.

#### `__len__()`
Returns the number of elements in the queue as an `int`.

### Extension Functions
These functions are not required for the assignment. However, if you would like to push
your queue further and get extra credit, you can implement these additional interfaces of
a queue

#### `__getitem__()`
Given an `index` as an `int`, returns the item at the index but does not change the queue.

#### `remove()`
Given a `value` parameter, removes the first instance of the value in the queue.
Raises an exception if the value doesn't exist in the queue.

#### `index()`
Given a `value` parameter, finds the first instance of the value in the queue
and returns the index as an `int`.

#### `count()`
Given a `value` parameter, counts the number of times a value appears in the queue and
returns the count as an `int`.
