import sys
import math
import re

def distancia(xA, yA, xB, yB):
    return math.sqrt((xB - xA) * (xB - xA) + (yB - yA) * (yB - yA))

def resolver():
    input = sys.stdin.read()
    datasets = re.split(r'\s*\n\s*\n\s*', input.strip())
    for data in datasets:
        if not data.strip():
            continue

        lines = data.splitlines()
        primera_linea = lines[0].split()
        
        n = int(primera_linea[0])
        gopher_x = float(primera_linea[1])
        gopher_y = float(primera_linea[2])
        dog_x = float(primera_linea[3])
        dog_y = float(primera_linea[4])

        puede_escapar = False

        for i in range(1, n + 1):
            hole_x, hole_y = map(float, lines[i].split())
            
            dist_gopher = distancia(gopher_x, gopher_y, hole_x, hole_y)
            dist_dog = distancia(dog_x, dog_y, hole_x, hole_y)
            
            if dist_gopher <= dist_dog / 2:
                print(f"The gopher can escape through the hole at ({hole_x:.3f},{hole_y:.3f}).")
                puede_escapar = True
                break
        
        if not puede_escapar:
            print("The gopher cannot escape.")

resolver()
