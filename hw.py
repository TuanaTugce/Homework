import math

points = [(0, 0), (1, 1), (2, 2), (3, 3)]  # Örneğin 4 nokta

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclidean_distance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)
print("Minimum mesafe:", min_distance)
