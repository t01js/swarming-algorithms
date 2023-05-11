
import pygame
import random
import math
import numpy as np

# Parameters
width, height = 1400, 800
num_boids = 20
min_distance = 50
max_speed = 3
alignment_weight = 0.5
cohesion_weight = 0.3
separation_weight = 0.2
avoid_edges_weight = 0.5
edge_margin = 30
arrow_size = 5

class Boid:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([random.uniform(-1, 1), random.uniform(-1, 1)], dtype=float)

    def update(self, boids):
        alignment = self.alignment(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        avoid_edges = self.avoid_edges()

        self.velocity += (alignment_weight * alignment +
                          cohesion_weight * cohesion +
                          separation_weight * separation +
                          avoid_edges_weight * avoid_edges)
        self.velocity = self.limit_speed(self.velocity)
        self.position += self.velocity

    def alignment(self, boids):
        avg_velocity = np.zeros(2)
        count = 0
        for boid in boids:
            if boid != self:
                avg_velocity += boid.velocity
                count += 1
        if count > 0:
            avg_velocity /= count
            avg_velocity = self.limit_speed(avg_velocity)
        return avg_velocity

    def cohesion(self, boids):
        center_of_mass = np.zeros(2)
        count = 0
        for boid in boids:
            if boid != self:
                center_of_mass += boid.position
                count += 1
        if count > 0:
            center_of_mass /= count
            return (center_of_mass - self.position) / 100
        return np.zeros(2)

    def separation(self, boids):
        repulsion = np.zeros(2)
        for boid in boids:
            if boid != self:
                distance = np.linalg.norm(self.position - boid.position)
                if distance < min_distance:
                    repulsion -= (boid.position - self.position)
        return repulsion

    def avoid_edges(self):
        force = np.zeros(2)
        if self.position[0] < edge_margin:
            force[0] = edge_margin - self.position[0]
        elif self.position[0] > width - edge_margin:
            force[0] = width - edge_margin - self.position[0]
        if self.position[1] < edge_margin:
            force[1] = edge_margin - self.position[1]
        elif self.position[1] > height - edge_margin:
            force[1] = height - edge_margin - self.position[1]
        return force

    def limit_speed(self, velocity):
        speed = np.linalg.norm(velocity)
        if speed > max_speed:
            velocity = (velocity / speed) * max_speed
        return velocity
    
    def draw(self, screen):
        angle = math.atan2(self.velocity[1], self.velocity[0])
        x1 = int(self.position[0] + arrow_size * math.cos(angle))
        y1 = int(self.position[1] + arrow_size * math.sin(angle))
        x2 = int(self.position[0] + arrow_size * math.cos(angle + 2.5 * math.pi / 3))
        y2 = int(self.position[1] + arrow_size * math.sin(angle + 2.5 * math.pi / 3))
        x3 = int(self.position[0] + arrow_size * math.cos(angle - 2.5 * math.pi / 3))
        y3 = int(self.position[1] + arrow_size * math.sin(angle - 2.5 * math.pi / 3))
        pygame.draw.polygon(screen, (0, 0, 0), [(x1, y1), (x2, y2), (x3, y3)])

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Boids Simulation")
    clock = pygame.time.Clock()

    boids = [Boid(random.randint(0, width), random.randint(0, height)) for _ in range(num_boids)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for boid in boids:
            boid.update(boids)
            boid.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
