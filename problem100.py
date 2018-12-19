"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

def compute_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    distance = abs(dx - dy) + min(dx, dy)
    return(distance)

def main():
    n = int(raw_input("Enter no. of checkpoints?\n"))
    print("Enter the points:")
    check_points = []
    while(n):
        n = n - 1
        x, y = map(int, raw_input().split())
        check_points.append((x, y))

    distance = 0
    index = 0

    while(index < len(check_points) - 1):
        distance += compute_distance(check_points[index], check_points[index+1])
        index += 1

    print(distance)


if __name__ == '__main__':
    main()