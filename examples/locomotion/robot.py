
import math

'''
Global heading range (in degrees)
- 0   -> Right
- 90  -> Up
- 180 -> Left
- 270 -> Down
'''


class Robot2DDot():
    def __init__(self, initial_position=[0, 0], initial_heading=0):
        # Position is [x, y]
        # Heading is angles in degrees
        self.position = initial_position
        self.heading = math.radians(initial_heading)

    def move(self, adjust_direction=0):
        self.heading += math.radians(adjust_direction)
        self.position = [
            round(self.position[0] + math.cos(self.heading), 3),
            round(self.position[1] + math.sin(self.heading), 3)
        ]

    def getPosition(self):
        return self.position

    def getHeading(self):
        return self.heading
