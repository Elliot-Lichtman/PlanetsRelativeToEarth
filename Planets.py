# DIMENSIONS
# 750x750 pixel screen
import numpy as np
import pygame

class Planet:

    def __init__(self, orbitRadius, velocity, size, color, sun = False):

        # important for displaying the planet
        self.size = size
        self.color = color

        # used for calculations later
        self.sun = sun
        self.orbitRadius = orbitRadius
        self.velocity = velocity

        # position -> start in horizontal line
        self.x = 375 + self.orbitRadius
        self.y = 375

        # velocity components (in i + j form)-> start pointing up
        self.v_i = 0
        self.v_j = velocity

        # to make movement easier, keep track of the angle with the horizontal
        self.angle = 0

        # necessary for adjusting
        self.drawX = self.x
        self.drawY = self.y

    def setComponents(self, scalar):

        if self.sun:
            self.v_i = 0
            self.v_j = 0
            return

        # there are some arbitrary constants here...
        self.angle += 0.1 * self.velocity * scalar

        correctX = 375 + self.orbitRadius * np.cos(self.angle)
        correctY = 375 + self.orbitRadius * np.sin(self.angle)

        self.v_i = correctX - self.x
        self.v_j = correctY - self.y



    def move(self, scalar): # this scalar will be determined by the time/frame.
        # Think of our velocity as in m/s. scalar will be in s/frame and thus we'll move by m/frame

        self.setComponents(scalar)

        self.x += self.v_i
        self.y += self.v_j

    def adjust(self, planet):

        # we basically want to move back by however far that planet moved
        self.drawX = self.x
        self.drawY = self.y

        self.drawX += (375 - planet.x)
        self.drawY += (375 - planet.y)


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.drawX, self.drawY), self.size, 10)

