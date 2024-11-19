from collections import defaultdict
from math import isclose

def max_points_on_line(points):
    if not points:
        return 0

    n = len(points)
    max_points = 1

    for i in range(n):
        pendientes = defaultdict(int)
        current_max = 0

        for j in range(i + 1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            if dx == 0:
                pendientes[float('inf')] += 1
            else:
                pendiente = dy / dx
                pendientes[pendiente] += 1

            current_max = max(current_max, pendientes[float('inf')] if dx == 0 else pendientes[pendiente])

        max_points = max(max_points, current_max + 1)

    return max_points


def main():
    results = []
    cases = int(input().strip())
    input()  

    for _ in range(cases):
        points = []

        while True:
            try:
                line = input().strip()
                if not line:
                    break
                x, y = map(int, line.split())
                points.append((x, y))
            except EOFError:
                break

        results.append(str(max_points_on_line(points)))

        if _ < cases - 1:
            results.append("")
    print("\n".join(results))


if __name__ == "__main__":
    main()
