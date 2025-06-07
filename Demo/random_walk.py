import random
from DebugVisualizer import PlotlyVisualizer

viz = PlotlyVisualizer()

data = []
cur_value = 0

def add_random_value():
    global cur_value
    delta = 1 if random.random() > 0.5 else -1
    data.append(cur_value)
    cur_value += delta

def add_many_random_values():
    for i in range(100):
        add_random_value()

for j in range(100):
    add_many_random_values()
    viz.visualize(data)

