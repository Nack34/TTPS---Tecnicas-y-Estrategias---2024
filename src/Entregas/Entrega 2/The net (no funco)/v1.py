import sys
import heapq

def dijkstra(graph, initial_vertex, last_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[initial_vertex] = 0
    pq = [(0, initial_vertex)] 
    heapq.heappush(pq, (0, initial_vertex))  
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
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
                heapq.heappush(pq, (new_distance, neighbor))
    
    return None

def main():
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
            router_id = str(router_data[0])
            routers_vecinos = list(map(str, router_data[1].split(','))) if router_data[1] else []
            graph[router_id] = routers_vecinos

        # Procesar querys
        cant_routes_to_determine = int(input_data[index])
        index += 1
        for _ in range(cant_routes_to_determine):
            start_router, end_router = map(str, input_data[index].strip().split())
            index += 1
            
            path = dijkstra(graph, start_router, end_router)
            if path is None:
                results.append("connection impossible")
            else:
                results.append(" ".join(map(str, path)))
    
    print("\n".join(results))

main()
