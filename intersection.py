
import time
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt

start_time = time.time()

class Intersection:
    def __init__(self, trajectory_vehicle, trajectory_ped):
        self.trajectory_vehicle = trajectory_vehicle
        self.trajectory_ped = trajectory_ped
    
    def create_circle(self, center):
        # Create a Shapely circle with the given center and radius
        circle = Point(center).buffer(1)
        return circle

    def find_intersection(self):
        # Create circles for each point in the vehicle trajectory
        circles = [self.create_circle(center) for center in self.trajectory_vehicle]

        # Create an empty list to store the intersection points
        intersections = []
        intersection_circles = []

        # Iterate over each circle and check if the line intersects
        for circle in circles:
            if LineString(self.trajectory_ped).intersects(circle):
                centroid = circle.centroid
                intersection_circles.append((centroid.x, centroid.y))
                intersection = LineString(self.trajectory_ped).intersection(circle)
                #print("intersection",intersection)
                intersection_line = LineString(self.trajectory_ped).intersection(circle)

                # Access the individual points from the intersection LineString
                for point in intersection_line.coords:
                    x, y = point
                    #print("Intersection point: ({}, {})".format(x, y))
                    intersections.append((x,y))

                # if intersection.geom_type.upper() == 'POINT':
                #     intersections.append((intersection.x, intersection.y))
                # elif intersection.geom_type.upper() == 'MULTIPOINT':
                #     for point in intersection:
                #         intersections.append((point.x, point.y))
        print("intersection_circles",intersection_circles)
        return intersections

    def print_intersection(self):
        intersections = self.find_intersection()
        if len(intersections) == 0:
            print("No intersections found.")
        else:
            print("Intersections found at the following points:")
            for intersection in intersections:
                print(intersection)


# Define the trajectories as lists of (x, y) points
trajectory_pedestrian = [(12, 1), (11, 1.5), (10, 1.8), (9, 2.5), (8, 3), (7, 3.5), (6, 4), (5, 4.25), (4, 4.6), (3, 4.7)]
trajectory_vehicle = [(0, 2), (0.05, 2.15875), (0.1, 2.314), (0.15, 2.46575), (0.2, 2.614), (0.25, 2.75875), (0.3, 2.9), (0.35, 3.03775), (0.4, 3.172), (0.45, 3.30275), (0.5, 3.43), (0.55, 3.55375), (0.6, 3.674), (0.65, 3.79075), (0.7, 3.904), (0.75, 4.01375), (0.8, 4.12), (0.85, 4.22275), (0.9, 4.322), (0.95, 4.41775), (1, 4.51), (1.05, 4.59875), (1.1, 4.684), (1.15, 4.76575), (1.2, 4.844), (1.25, 4.91875), (1.3, 4.99), (1.35, 5.05775), (1.4, 5.122), (1.45, 5.18275), (1.5, 5.24), (1.55, 5.29375), (1.6, 5.344), (1.65, 5.39075), (1.7, 5.434), (1.75, 5.47375), (1.8, 5.51), (1.85, 5.54275), (1.9, 5.572), (1.95, 5.59775), (2, 5.62), (2.05, 5.63875), (2.1, 5.654), (2.15, 5.66575), (2.2, 5.674), (2.25, 5.67875), (2.3, 5.68), (2.35, 5.67775), (2.4, 5.672), (2.45, 5.66275), (2.5, 5.65), (2.55, 5.63375), (2.6, 5.614), (2.65, 5.59075), (2.7, 5.564), (2.75, 5.53375), (2.8, 5.5), (2.85, 5.46275), (2.9, 5.422)]

# Create an instance of the Intersection class
intersection = Intersection(trajectory_vehicle, trajectory_pedestrian)

# Find and print the intersections
intersection.print_intersection()
a=intersection.find_intersection()
end_time = time.time()
# Plot the trajectories and circles
x1, y1 = zip(*trajectory_pedestrian)
x2, y2 = zip(*trajectory_vehicle)
x3,y3 = zip(*a)
plt.plot(x1, y1, 'o-', label='Trajectory pedestrian')
plt.plot(x3, y3, 'o-', label='inter')
for i, center in enumerate(trajectory_vehicle):
    circle = intersection.create_circle(center)
    label = 'vehicle' if i == 0 else None
    plt.gca().add_patch(plt.Circle(center, 4.4, fc='none', ec='blue', label=label))

plt.title('Trajectories with Circle Intersection')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()



print("time taken = ", end_time-start_time)
