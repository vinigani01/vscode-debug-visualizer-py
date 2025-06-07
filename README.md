# vscode-debug-visualizer-py
This is a Python module that provides a collection of visualization classes for use with the VS Code Debug Visualizer extension. It enables developers to create interactive visualizations of various data structures during debugging sessions without having to create JSON manually.


## Acknowledgements

This project is designed to work with the [VS Code Debug Visualizer extension](https://marketplace.visualstudio.com/items?itemName=hediet.debug-visualizer) created by [Henning Dieterichs](https://github.com/hediet). The visualizers in this package generate JSON in the format expected by this extension.
The VS Code Debug Visualizer extension is licensed under the [MIT License](https://github.com/hediet/vscode-debug-visualizer/blob/master/data-extraction/LICENSE.md).


## Installation
run the following command in your terminal to install:
```bash
pip install git+https://github.com/yourusername/vscode-debug-visualizer-py.git
```
## Usage

Ex: ListVisualizer to visualize lists

Steps:

1. Import the required Visualizer class from the DebugVisualizer module
   
   ![image](https://github.com/user-attachments/assets/33a91642-47df-4cd2-b01d-36bd04111b11)


2. Create an instance of Visualizer class
   
   ![image](https://github.com/user-attachments/assets/932d1a95-bc10-40a7-8ddf-932184bf6107)
   

3. Use ListVisualizer instance to call visualize() function and pass the List as argument
   
   ![image](https://github.com/user-attachments/assets/0de62db1-2050-44ef-8b84-b241fc9e712c)
   

5. During debugging, enter the same line as in in step3 into Debug Visualizer VScode extension's input field
   
   ![image](https://github.com/user-attachments/assets/d46685d0-b7c9-4b93-a3fc-742db58192fd)
   

The above steps remains the same for all the Visualizer classes available.
Find various use cases in the 'Demo' folder

## Available Visualizer classes

1. LinkedListVisualizer,
2. ListVisualizer,
3. GridVisualizer,
4. GraphVisualizer,
5. TreeVisualizer,
6. TableVisualizer,
7. PlotlyVisualizer,
8. Plotly3DVisualizer,
9. PlotlyTableVisualizer


