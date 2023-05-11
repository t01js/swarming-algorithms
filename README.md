# Boids Simulation

This is a Python implementation of the Boids algorithm, a simple model of flocking behavior in birds. In this simulation, a group of boids (bird-like objects) move around the screen and exhibit three behaviors: alignment, cohesion, and separation.

## Requirements

This simulation requires [Pygame](https://www.pygame.org/).

To install Pygame with pip, run:

```sh
pip install pygame
```

## Parameters

The following parameters can be adjusted in the code:

- `width`, `height`: The size of the screen in pixels.
- `num_boids`: The number of boids in the simulation.
- `min_distance`: The minimum distance between boids for separation behavior.
- `max_speed`: The maximum speed of the boids.
- `alignment_weight`, `cohesion_weight`, `separation_weight`: The weights for each behavior.
- `avoid_edges_weight`: The weight for avoiding the edges of the screen.
- `edge_margin`: The margin around the edges of the screen for the avoid edges behavior.
- `arrow_size`: The size of the arrow indicating the direction of the boids.

## **Boid class**

The `Boid` class represents a single boid in the simulation. It has the following methods:

### `__init__(self, x, y)`

Creates a new boid at position `(x, y)` with a random velocity.

### `update(self, boids)`

Updates the boid's velocity based on the alignment, cohesion, separation, and avoid edges behaviors. It then limits the boid's speed and updates its position.

### `alignment(self, boids)`

Returns the average velocity of nearby boids for the alignment behavior.

### `cohesion(self, boids)`

Returns the vector pointing towards the center of mass of nearby boids for the cohesion behavior.

### `separation(self, boids)`

Returns the vector pointing away from nearby boids for the separation behavior.

### `avoid_edges(self)`

Returns the vector pointing away from the edges of the screen for the avoid edges behavior.

### `limit_speed(self, velocity)`

Limits the speed of the boid to the maximum speed.

### `draw(self, screen)`

Draws the boid as a triangle pointing in the direction of its velocity.

## **Main function**

The `main()` function initializes the Pygame window, creates the boids, and runs the simulation loop. It also includes an option to have the boids move towards a target point when it is clicked.

To run the simulation, simply run:

```sh
python boids.py
```

Have fun!
