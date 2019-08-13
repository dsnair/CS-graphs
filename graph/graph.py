from util import Stack, Queue

class Graph:
    # Represent a graph as a dictionary of vertices mapping vertices to edges
    def __init__(self):
        self.vertices = {}


    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex in self.vertices:
            print("Vertex {} already exists".format(vertex))
        else:
            # this vertex has no edges
            self.vertices[vertex] = set()
            

    # Add a directed edge to the graph
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)
        else:
            print("Either vertex {} or vertex {} does not exist".format(from_vertex, to_vertex))
        
     
    # Breadth-First Traversal:
    # 1. From starting_vertex, visit the adjacent unvisited vertex. 
    # Mark it as visited. Display it. Insert it in a queue.
    # 2. Once all adjacent vertices are visited, remove the first vertex from the queue.
    # 3. Repeat #1 and #2 until the queue is empty.
    def bft(self, starting_vertex):
        q = Queue()
        visited = [starting_vertex]
        q.enqueue(starting_vertex)

        while q.size():
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in visited:
                    visited.append(vertex)
                    q.enqueue(vertex)
            q.dequeue()                    

        return visited


    # Depth-First Traversal:
    # 1. From starting_vertex, visit the adjacent unvisited vertex. 
    # Mark it as visited. Display it. Push it in a stack.
    # 2. Once all adjacent vertices are visited, pop up a vertex from the stack. 
    # (It will pop up all the vertices from the stack, which do not have adjacent vertices.)
    # 3. Repeat #1 and #2 until the stack is empty.
    def dft(self, starting_vertex):
        s = Stack()
        visited = []
        s.push(starting_vertex)

        while s.size():  
            vertex = s.pop() 
            if vertex not in visited:
                visited.append(vertex)
                for next_vertex in self.vertices[vertex]:
                    s.push(next_vertex)

        return visited


    # Print each vertex in depth-first order beginning from starting_vertex.
    # This should be done using recursion
    def dft_recursive(self, starting_vertex):
        pass


    # Breadth-First Search: Return a list containing the shortest path 
    # from starting_vertex to destination_vertex in breath-first order
    # The difference between BFS and BFT is that BFS stops when destination_vertex is visited,
    # whereas, BFT keeps going until all vertices have been visited.
    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = []
        q.enqueue([starting_vertex])

        while q.size():
            path = q.dequeue()
            # print("Path", path)
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                
                visited.append(vertex)

                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex) 
                    q.enqueue(new_path)
        
        return None


    # Depth-First Search: Return a list containing the shortest path 
    # from starting_vertex to destination_vertex in depth-first order
    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        visited = []
        s.push([starting_vertex])

        while s.size():
            path = s.pop()
            # print("Path", path)
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                
                visited.append(vertex)

                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex) 
                    s.push(new_path)
        
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)


    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    print(graph.vertices)

    
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    print("BFT", graph.bft(1))


    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    print("DFT", graph.dft(1))

    
    # Valid DFT recursive paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    graph.dft_recursive(1)

    
    # Valid BFS path:
    #     [1, 2, 4, 6]
    print("BFS", graph.bfs(1, 6))

    
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    print("DFS", graph.dfs(1, 6))