import json

class LinkedListVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "graph": True },
            "nodes": [],
            "edges": []
        }
    
    def _get_id(self, obj):
        # Use object's memory address as unique identifier
        return str(id(obj))
    
    def add_node(self, obj, label=None, color=None):
        obj_id = self._get_id(obj)
        if not any(n["id"] == obj_id for n in self.data["nodes"]):
            node = {
                "id": obj_id,
                "label": label if label else str(getattr(obj, 'data', obj))
            }
            if color:
                node["color"] = color
            self.data["nodes"].append(node)
    
    def add_edge(self, from_obj, to_obj, color=None, dashes=False):
        from_id = self._get_id(from_obj)
        to_id = self._get_id(to_obj)
        edge = { 
            "from": from_id, 
            "to": to_id,
            "arrows": "to"  # Add arrow to show direction
        }
        if color:
            edge["color"] = color
        if dashes:
            edge["dashes"] = True
        self.data["edges"].append(edge)
    
    def visualize(self, head):
        # Clear previous data
        self.data["nodes"] = []
        self.data["edges"] = []
        
        # Track visited nodes to avoid cycles
        visited = set()
        
        curr = head
        while curr and self._get_id(curr) not in visited:
            visited.add(self._get_id(curr))
            self.add_node(curr)
            
            # Add forward edge (next pointer)
            if hasattr(curr, 'next') and curr.next:
                self.add_node(curr.next)
                self.add_edge(curr, curr.next)
            
            # Add backward edge (prev pointer) with different style
            if hasattr(curr, 'prev') and curr.prev:
                self.add_edge(curr, curr.prev, color="#999999", dashes=True)
            
            curr = curr.next
        
        # Print the JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class ListVisualizer:
    def __init__(self):
        self.data = {
            "kind": {"grid": True},
            "rows": []
        }
    
    def visualize(self, arr):
        # Clear previous data
        self.data["rows"] = []
        
        # Format the list as a grid with one row
        self.data["rows"] = [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ]
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class GridVisualizer:
    def __init__(self):
        self.data = {
            "kind": {"grid": True},
            "rows": []
        }
    
    def visualize(self, grid):
        # Clear previous data
        self.data["rows"] = []
        
        # Format the 2D grid
        for row in grid:
            self.data["rows"].append({
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in row
                ]
            })
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class GraphVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "graph": True },
            "nodes": [],
            "edges": []
        }
    
    def _get_id(self, node):
        if hasattr(node, 'id'):
            return str(node.id)
        return str(id(node))
    
    def visualize(self, graph_or_tree):
        # Clear previous data
        self.data["nodes"] = []
        self.data["edges"] = []
        
        # Check if it's a graph with nodes and edges collections
        if hasattr(graph_or_tree, 'nodes') and hasattr(graph_or_tree, 'edges'):
            self._visualize_graph(graph_or_tree)
        else:
            # Assume it's a tree (root node)
            self._visualize_tree(graph_or_tree)
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output
    
    def _visualize_graph(self, graph):
        # Add nodes
        for node in graph.nodes:
            self.data["nodes"].append({
                "id": self._get_id(node),
                "label": str(getattr(node, 'value', node))
            })
        
        # Add edges
        for edge in graph.edges:
            self.data["edges"].append({
                "from": self._get_id(edge.source),
                "to": self._get_id(edge.target),
                "label": str(getattr(edge, 'weight', ''))
            })
    
    def _visualize_tree(self, root):
        if not root:
            return
        
        # Use a queue for breadth-first traversal
        queue = [root]
        visited = set()
        
        while queue:
            node = queue.pop(0)
            node_id = self._get_id(node)
            
            if node_id in visited:
                continue
                
            visited.add(node_id)
            
            # Add node
            self.data["nodes"].append({
                "id": node_id,
                "label": str(getattr(node, 'value', node))
            })
            
            # Process children for general trees
            if hasattr(node, 'children'):
                for child in node.children:
                    if child:
                        child_id = self._get_id(child)
                        self.data["edges"].append({
                            "from": node_id,
                            "to": child_id
                        })
                        queue.append(child)
            
            # Process binary trees
            elif hasattr(node, 'left') or hasattr(node, 'right'):
                if hasattr(node, 'left') and node.left:
                    left_id = self._get_id(node.left)
                    self.data["edges"].append({
                        "from": node_id,
                        "to": left_id
                    })
                    queue.append(node.left)
                
                if hasattr(node, 'right') and node.right:
                    right_id = self._get_id(node.right)
                    self.data["edges"].append({
                        "from": node_id,
                        "to": right_id
                    })
                    queue.append(node.right)


class TreeVisualizer:
    def __init__(self):
        self.data = {
            "root": None,
            "kind": {"tree": True}
        }
    
    def visualize(self, root):
        # Create tree structure
        self.data["root"] = self._build_node(root)
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output
    
    def _build_node(self, node):
        if not node:
            return None
        
        # Create node structure
        tree_node = {
            "items": [{"text": str(node.value)}],
            "isMarked": False,
            "data": {},
            "children": []
        }
        
        # Process children for general trees
        if hasattr(node, 'children'):
            for child in node.children:
                if child:
                    child_node = self._build_node(child)
                    if child_node:
                        tree_node["children"].append(child_node)
        
        # Process binary trees
        elif hasattr(node, 'left') or hasattr(node, 'right'):
            if hasattr(node, 'left') and node.left:
                left_node = self._build_node(node.left)
                if left_node:
                    tree_node["children"].append(left_node)
            
            if hasattr(node, 'right') and node.right:
                right_node = self._build_node(node.right)
                if right_node:
                    tree_node["children"].append(right_node)
        return tree_node


class TableVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "table": True },
            "rows": []
        }
    
    def visualize(self, data):
        # Clear previous data
        self.data["rows"] = []
        
        # Add each row from the input data
        if isinstance(data, list):
            self.data["rows"] = data
        else:
            # If a single object is provided, add it as one row
            self.data["rows"] = [data]
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class PlotlyVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "plotly": True },
            "data": []
        }
    
    def visualize(self, *args):
        # Clear previous data
        self.data["data"] = []
        
        # Process each argument as a separate series
        for series in args:
            if isinstance(series, dict):
                # If already a dictionary with configuration, add it directly
                self.data["data"].append(series)
            else:
                # Otherwise, wrap it as a y-series
                self.data["data"].append({"y": series})
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class Plotly3DVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "plotly": True },
            "data": []
        }
    
    def visualize(self, x, y, z, type="mesh3d"):
        # Clear previous data
        self.data["data"] = []
        
        # Create 3D plot data
        plot_data = {
            "type": type,
            "x": x,
            "y": y,
            "z": z
        }
        
        self.data["data"].append(plot_data)
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output


class PlotlyTableVisualizer:
    def __init__(self):
        self.data = {
            "kind": { "plotly": True },
            "data": [],
            "layout": {}
        }
    
    def visualize(self, headers, values):
        # Clear previous data
        self.data["data"] = []
        
        # Create table data
        table_data = {
            "header": {
                "values": headers
            },
            "cells": {
                "values": values
            },
            "type": "table"
        }
        
        self.data["data"].append(table_data)
        
        # Print JSON for Debug Visualizer
        json_output = json.dumps(self.data)
        print(json_output)
        return json_output
