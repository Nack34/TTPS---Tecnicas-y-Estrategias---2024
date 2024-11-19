def dfs(tasks_visited, route, current_task, real_dependencies, graph):
    current_task_visited = current_task in tasks_visited
    if not current_task_visited:
        route.append(current_task)

    for dep in graph[current_task]:
        for task_id in route:
            real_dependencies[task_id].add(dep)
        if not current_task_visited:
            dfs(tasks_visited, route, dep, real_dependencies, graph)

    if not current_task_visited:
        tasks_visited.add(current_task)
        route.pop()

def find_task_with_most_dependencies(scenario):
    n = len(scenario)

    tasks_visited = set()
    route = []
    real_dependencies = [set() for _ in range(n + 1)]

    #Crear grafo
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        task_deps = scenario[i]
        task_id = i + 1
        for dep in task_deps:
            graph[task_id].append(dep)
            
    #Crear lista de dependencias reales 
    for task in range(1, n + 1):
        if task not in tasks_visited:
            dfs(tasks_visited, route, task, real_dependencies, graph)

    #Obtener task_with_most_dependencies
    max_dependencies = -1
    task_with_most_dependencies = None
    for task_id, dependencies in enumerate(real_dependencies[1:], 1):
        dep_count = len(dependencies)
        if dep_count > max_dependencies or (dep_count == max_dependencies and task_id < task_with_most_dependencies):
            max_dependencies = dep_count
            task_with_most_dependencies = task_id
    
    return task_with_most_dependencies


results = []
while True:
    n = int(input())
    if n == 0:
        break
    scenario = []
    for _ in range(n):
        data = list(map(int, input().split()))
        scenario.append(data[1:]) 
    results.append(find_task_with_most_dependencies(scenario))

for result in results:
    print(result)
