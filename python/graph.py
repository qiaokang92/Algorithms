#!/usr/bin/python3.6

#https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python

class Graph:
   def __init__(self, graph):
      self.graph = graph

   def dfs(self):
      print("dfs the graph:")
      pass

   def bfs(self):
      print("bfs the graph:")
      pass

   def dfs_paths(self, start, goal):
      pass

   def bfs_paths(self, start, goal):
      pass

if __name__ == "__main__":
   graph_dict = {'A': set(['B', 'C']),         \
                 'B': set(['A', 'D', 'E']),    \
                 'C': set(['A', 'F']),         \
                 'D': set(['B']),              \
                 'E': set(['B', 'F']),         \
                 'F': set(['C', 'E'])}

   graph = Graph(graph_dict)
   graph.dfs()
   graph.bfs()