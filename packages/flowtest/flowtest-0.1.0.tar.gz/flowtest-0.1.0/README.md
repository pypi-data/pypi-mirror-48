# Introduction to flow testing
Flow testing is a kind of hybrid testing and combines elements from unit testing with integration 
testing.

With flow testing, testing is done by implementing test steps. Each step can continue where a 
previous step stopped. Therefore, each step can define it's predecessor and the test steps are 
thus organized in a tree or more general a directed graph.

More formally, testing is defined as a _test graph_, where each node in the graph corresponds to a
test step (and a step is not necessarily a single test) and each edge denotes a _test continuation_.

Nodes without incoming edges are called _start nodes_, and start nodes cannot have incoming edges.
The flow graph is used to create a set of _test flows_ as follows: each possible path starting from
a start node corresponds to a single test flow. 


# Usage
Write and execute a test script like the following:

```
import operator
from functools import reduce

import sys
from flowtest import FlowGraph

graph = FlowGraph()


@graph.step_decorator()
def start():
    return [1, 2, 3]


@graph.step_decorator(start)
def verify_sum(data):
    assert sum(data) == 6


@graph.step_decorator(start)
def compute_product(data):
    return reduce(operator.mul, data, 1)


@graph.step_decorator(compute_product)
def verify_product(product):
    assert product == 6


if not graph.run_all_flows():
    sys.exit(1)
```