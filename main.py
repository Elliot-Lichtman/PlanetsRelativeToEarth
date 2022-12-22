import numpy as np
import pygame
import Planets
import System
import time

# initialize pygame
pygame.init()


# a few helpful variables - hopefully names are somewhat self-explanatory
paused = False
running = True
screen = pygame.display.set_mode((750, 750))

# make our system
solarSystem = System.System()

# add a few planets
grayPlanet = Planets.Planet(100, 12, 10, "gray")
bluePlanet = Planets.Planet(170, 8, 15, "blue")
maroonPlanet = Planets.Planet(250, 6, 25, "maroon")

solarSystem.addPlanet(grayPlanet)
solarSystem.addPlanet(bluePlanet)
solarSystem.addPlanet(maroonPlanet)

# SET THE CENTER PLANET!!!!!
solarSystem.centerPlanet = solarSystem.sun

# Start our timer -> calculate scalars
prevTime = time.time()

# make the main game loop
while running:

    # check for input -> for now, just closing the program and pausing
    for event in pygame.event.get():

        # if they hit the x button, close the program
        if event.type == pygame.QUIT:
            running = False

        # same with the escape key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        # spacebar -> pause the simulation if it's unpaused, otherwise unpause it
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = not paused

    # now we need to move everything
    currentTime = time.time()
    scalar = currentTime - prevTime # which is just the seconds/frame

    # move all the stuffs
    solarSystem.move(scalar)

    # draw it all
    solarSystem.draw(screen)

    # update the display
    pygame.display.update()

    # update our time
    prevTime = currentTime

