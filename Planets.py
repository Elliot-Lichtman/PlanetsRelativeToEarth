# DIMENSIONS
# 750x750 pixel screen
import numpy as np
import pygame

class Planet:

    def __init__(self, orbitRadius, velocity, size, color):

        # important for displaying the planet
        self.size = size
        self.color = color

        # used for calculations later
        self.orbitRadius = orbitRadius
        self.velocity = velocity

        # position -> start in horizontal line
        self.x = 325 + self.orbitRadius
        self.y = 325

        # velocity components (in i + j form)-> start pointing up
        self.v_i = 0
        self.v_j = velocity

        # to make movement easier, keep track of the angle with the horizontal
        self.angle = 0

    def setComponents(self):

        # We need to do a bit of a computation here
        # we have the angle -> we know ratio of i to j
        # we have the total magnitude as well

        self.v_i = -self.velocity * np.sin(self.angle)
        self.v_j = self.velocity * np.cos(self.angle)

    def move(self, scalar): # this scalar will be determined by the time/frame.
        # Think of our velocity as in m/s. scalar will be in s/frame and thus we'll move by m/frame

        self.x += self.v_i * scalar
        self.y += self.v_j * scalar

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, 10)

