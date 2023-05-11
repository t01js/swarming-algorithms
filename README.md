# swarming-algorithms
Implementation of Craig Reynold's Boids algorithm in Python


Boids is a simple algorithm for simulating the flocking behavior of birds, fish, and other animals that travel in groups. The algorithm was developed by Craig Reynolds in 1986 and is based on three main principles: alignment, cohesion, and separation.

Alignment refers to the tendency of animals to align their velocities with the average velocity of their neighbors. This helps to maintain group cohesion and avoid collisions. In the Boids algorithm, each animal calculates a desired velocity that points in the same direction as the average velocity of its neighbors. The animal then adjusts its actual velocity to gradually match the desired velocity.

Cohesion refers to the tendency of animals to move towards the center of mass of their neighbors. This helps to maintain group cohesion and avoid stragglers. In the Boids algorithm, each animal calculates a desired position that corresponds to the center of mass of its neighbors. The animal then adjusts its actual velocity to move towards the desired position.

Separation refers to the tendency of animals to avoid collisions with their neighbors. This helps to maintain group cohesion and avoid accidents. In the Boids algorithm, each animal calculates a desired velocity that points away from its neighbors that are too close. The animal then adjusts its actual velocity to move away from the neighbors.

These three principles are combined in the Boids algorithm to create a simple model of flocking behavior. The algorithm can be implemented in various ways, but a common approach is to represent each animal as a point in space with a position and velocity vector. The algorithm is typically applied in discrete time steps, with each animal updating its velocity and position based on its neighbors' positions and velocities at each time step.

The Boids algorithm can be extended to include additional behaviors, such as obstacle avoidance and predator evasion. It can also be applied to other types of agents, such as robots and virtual characters.

Mathematically, the Boids algorithm uses vector calculus to compute the desired velocities and positions of the animals. The alignment behavior is computed by taking the average of the velocities of the neighboring animals and subtracting the animal's own velocity. The cohesion behavior is computed by taking the average of the positions of the neighboring animals and subtracting the animal's own position. The separation behavior is computed by summing up the vectors that point away from the neighboring animals that are too close and subtracting the animal's own position.
