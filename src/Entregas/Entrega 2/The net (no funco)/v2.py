class HeapQueue:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def heappop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def heapify(self, iterable):
        self.heap = list(iterable)
        for i in reversed(range(len(self.heap) // 2)):
            self._sift_down(i)

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            # Check if the right child exists and is smaller than the left child
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1][0] < self.heap[child_index][0]:
                child_index += 1
            # If the current node is less than or equal to the smallest child, we are done
            if self.heap[index][0] <= self.heap[child_index][0]:
                break
            # Swap the current node with the smallest child
            self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
            index = child_index
            child_index = 2 * index + 1

def dijkstra(graph, initial_vertex, last_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[initial_vertex] = 0
    pq = HeapQueue()
    pq.heappush((0, initial_vertex))
    
    while pq.heap:  # Change to pq.heap to check if the heap is empty
        current_distance, current_vertex = pq.heappop()
        
        # Si llegamos al destino, reconstruimos el camino
        if current_vertex == last_vertex:
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous[current_vertex]
            return path[::-1]

        # Si la distancia es mayor que la antes registrada, no nos sirve
        if current_distance > distances[current_vertex]:
            continue

        # Analizar los vecinos
        for neighbor in graph[current_vertex]:
            new_distance = current_distance + 1  
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_vertex
                pq.heappush((new_distance, neighbor))
    
    return None 

def main():
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    index = 0
    results = []
    
    while index < len(input_data):
        results.append("-----")

        # Crear grafo 
        cant_routers = int(input_data[index])
        index += 1
        graph = {}
        for _ in range(cant_routers):
            line = input_data[index].strip()
            index += 1
            router_data = line.split('-')
            router_id = int(router_data[0])
            visible_routers = list(map(int, router_data[1].split(','))) if router_data[1] else []
            graph[router_id] = visible_routers 

        # Procesar querys
        cant_routes_to_determine = int(input_data[index])
        index += 1
        for _ in range(cant_routes_to_determine):
            start_router, end_router = map(int, input_data[index].strip().split())
            index += 1
            
            path = dijkstra(graph, start_router, end_router)
            if path is None:
                results.append("connection impossible")
            else:
                results.append(" ".join(map(str, path)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
