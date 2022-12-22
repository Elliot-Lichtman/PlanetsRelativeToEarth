import numpy as np
import pygame
import Planets

class System:

    def __init__(self):

        self.center = (375, 375)
        self.sun = Planets.Planet(0, 0, 50, "gold", True)
        self.centerPlanet = self.sun

        self.planets = [self.sun]

    def addPlanet(self, planet):
        self.planets.append(planet)

    def move(self, scalar):
        for planet in self.planets:
            planet.move(scalar)

        for planet in self.planets:
            planet.adjust(self.centerPlanet)


    def draw(self, screen):
        screen.fill("black")
        for planet in self.planets:
            planet.draw(screen)
