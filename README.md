# A* Search Algorithm in Graph

This repository contains an implementation of the A* (A-star) search algorithm to find the shortest path between two points in a graph, based on a representation of cities and their distances. The code is written in Python and uses custom data structures to represent vertices and adjacents.

## Project Overview

The project simulates a graph of cities, with each city represented as a vertex. The A* algorithm is used to calculate the most efficient path from a starting city to a destination city, considering both the actual travel cost and heuristic distances to the goal.

### Key Features:
- **Graph with Cities**: A graph representing cities as vertices, each with its distance to the destination (heuristic) and its connections to other cities (edges with costs).
- **A* Search Algorithm**: The core functionality that finds the shortest path between the starting city and the goal city.
- **Ordered Data Structure**: A custom data structure is used to maintain an ordered list of adjacent cities for efficient pathfinding.

## How to Use

### Requirements:
- Python 3.x
- `numpy` (for efficient array handling)

### Running the Code:
1. Clone the repository:
   ```bash
   git clone https://github.com/vallz0/A-star-Algorithm.git
   cd A-star-Algorithm
