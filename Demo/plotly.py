from DebugVisualizer import PlotlyVisualizer

# Create a PlotlyVisualizer instance
viz = PlotlyVisualizer()

# Simple line chart with multiple series
series1 = [1, 2, 4, 8, 16]
series2 = [14, 3, 0, 15, 10]
series3 = [1, 2, 3, 4, 5]
viz.visualize(series1, series2, series3)
