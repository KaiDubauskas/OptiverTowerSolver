# Optiver Tower Puzzle Solver

A CLI tool to solve the Optiver Pymetrics Tower Puzzle

## Usage

1. Clone or download the project. All you really need is main.py, so if it makes it easier, you can just download that file.
2. Run main.py in your terminal

Eg.
   ```
   python3 main.py
   ```
## Example

The blocks in the towers are color-coded in the actual puzzle, so you will have to take some time to manually convey these as numbers.

For example, if this was your start position

<img width="318" alt="Screenshot 2024-02-14 at 3 25 00 PM" src="https://github.com/KaiDubauskas/OptiverTowerSolver/assets/105459947/6efe8a0e-cb79-4d2e-8cab-9d16630c7d05">

And this was the target position: 

<img width="223" alt="Screenshot 2024-02-14 at 3 25 36 PM" src="https://github.com/KaiDubauskas/OptiverTowerSolver/assets/105459947/c4762470-f51e-406e-926a-601ec20d32f0">

Here is what your initial and goal towers might look like:

Initial:
```
|       |       |
|       |       |
|       |       3
|       |       4
1       2       5
```

Goal:
```
|       |       4
|       |       3
|       |       5
|       |       2
|       |       1
```

## How It Works / Misc.

Uses the A* algorithm to efficiently calculate the shortest path from initial to goal state. I used the number of subgoals (blocks correctly placed) as the heuristic function.

I added the code to perform greedy and bfs to benchmark the effectiveness of each algorithm in different scenarios, but otherwise these methods aren't used (see benchmark.py for comparisons). 

Test.py is wholly useless as this project is nowhere near large enough to need unit tests, but I though this would be a good opporunity to learn how to use the pytest library, so it's there.

The algorithm tends to significantly slow down when the min number of moves is >15, taking 77 seconds to find a 19 move solution in a 5x4, 55% full tower. 
