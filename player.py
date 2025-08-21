import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shooter_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        #code below allows you to make the game respond to your button presses
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        #reduce the time by the time passed since last update with dt
        self.shooter_cooldown -= dt

    def move(self, dt):
        # Use Vector to set a base direction and movespeed, then use rotate to change direction, and use player speed to magnify the speed. for position updates use dt which is delta of time since last frame to make sure movement stays consistent based of time
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #if statment to check if the shooting mech should be on cooldown, if it is, function exits with return, if not the rest of the code will execute
        if self.shooter_cooldown > 0: 
            return

        #using self.position with the x and y after allows you to pull the x and y data out of the pygame vector
        bullet = Shot(self.position.x, self.position.y)
        intial_direction = pygame.Vector2(0,1)
        rotated_direction = intial_direction.rotate(self.rotation)
        bullet.velocity = rotated_direction * PLAYER_SHOOT_SPEED 
        self.shooter_cooldown = 0.3

        

class Shot(CircleShape):
    #class for out bullets in the game
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)