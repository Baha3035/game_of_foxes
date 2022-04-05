# Game_of_foxes

Fun variation of Conway's game of life

**Game_of_foxes** is a simulation of foxes and rabbit's real life environment. Foxes eat rabbits and reproduce, rabbits eat grass and reproduce.

## Rules

1. Foxes can eat rabbits only if foxes are more than one. Because only one fox cant destroy entire population in one lifetime
2. Any live rabbit with two or three live neighbours survives.
3. Any dead rabbit with three live neighbours becomes a live rabbit.
4. All other living rabbits die in the next generation. Similarly, all other dead rabbits stay dead.
5. Any live fox with two or three live neighbours and more than one rabbit survives.

## How it works

- This project uses UI from tkinter to display live action
- As a map 2d matrix is used
- For counting neighbours of creatures loop with tuples is used
- Inside a matrix there are numbers: 0, 1, 2. Each corresponding to a character and its color, e.g. fox.
  - 0 - grass (green)
  - 1 - fox (orange)
  - 2 - rabbit (blue)

## Demonstration

**Starting map**

![Game_of_life3StartPositions](https://user-images.githubusercontent.com/77735480/161756552-a04f932b-4308-4d44-9f1e-bb9bf8b303e0.png)

**Rabbits won**

![Game_of_life2](https://user-images.githubusercontent.com/77735480/161756596-9e99f938-cb9d-4eda-aef1-3b51601f9159.png)
