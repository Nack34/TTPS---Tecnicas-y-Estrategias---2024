'''Wrong Answer

En este ejemplo: 

8
1 2
1 3
1 4
0
2 6 7
1 8
1 8
0
0

Tendria que dar 1
Pero mi output es 5, eso es debido a que memo al final es: {4: 0, 3: 1, 2: 2, 1: 3, 8: 0, 6: 1, 7: 1, 5: 4}
O sea, estoy tomando la demendencia de 6 (8) y la dependencia de 7 (8) como diferentes, siendo que en realidad son la misma

'''


def dfs(task, memo, graph):
    if task in memo:
        return memo[task]
    
    count = 0
    for dep in graph[task]:
        count += 1 + dfs(dep, memo, graph)
    
    memo[task] = count
    return count

def find_task_with_most_dependencies(scenarios):
    results = []
    
    for dependencies in scenarios:
        n = len(dependencies)
        
        graph = [[] for _ in range(n + 1)]
        for i in range(n):
            task_deps = dependencies[i]
            task_id = i + 1
            for dep in task_deps:
                graph[task_id].append(dep)
        
        memo = {}
        max_dependencies = -1
        task_with_most_dependencies = None
        
        for task in range(1, n + 1):
            dep_count = dfs(task, memo, graph)
            if dep_count > max_dependencies or (dep_count == max_dependencies and task < task_with_most_dependencies):
                max_dependencies = dep_count
                task_with_most_dependencies = task
        
        #print(memo)
        results.append(task_with_most_dependencies)
    
    return results


scenarios = []
while True:
    n = int(input())
    if n == 0:
        break
    dependencies = []
    for _ in range(n):
        data = list(map(int, input().split()))
        dependencies.append(data[1:]) 
    scenarios.append(dependencies)

results = find_task_with_most_dependencies(scenarios)

for result in results:
    print(result)
