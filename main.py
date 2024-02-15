from typing import List, Tuple, Optional, TypeAlias
from collections import deque
import heapq, random

# Custom types
TowerPuzzle: TypeAlias = List[List[Optional[int]]]
MoveList: TypeAlias = List[Tuple[int, int]]

"""
- Solves the tower rearrangement puzzle (similar to Towers of London or Tower of Hanoi)
using breadth first search, greedy heuristic search, and the A* algorithm
"""
class TowerPuzzle:
    def __init__(self, initial_towers: TowerPuzzle, goal_towers: TowerPuzzle):
        if (len(initial_towers) != len(goal_towers)):
            raise ValueError("Initial and goal towers must have the same number of towers")
        self.initial_state = (tuple(tuple(tower) for tower in initial_towers))
        self.goal_state = (tuple(tuple(tower) for tower in goal_towers))
        self.num_towers = len(initial_towers)
        self.max_height = len(initial_towers[0])

    
    # Performs breadth first search from self.initial_state
    # Returns the sequence of moves to reach the goal state
    def bfs(self) -> MoveList:
        queue = deque([ (self.initial_state, []) ])
        reached = set([self.initial_state])
        
        while queue:
            state, path = queue.popleft()
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1

                        new_state = [list(tower) for tower in state] # Convert to list to allow mutability
                        
                        # Move the brick
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)] # Add the move to the path
                        new_state_tuple = tuple(tuple(tower) for tower in new_state) # Convert back to tuple to allow state to be added to heap

                        if new_state_tuple == self.goal_state:
                            return new_path
                        elif new_state_tuple not in reached:
                            queue.append((new_state_tuple, new_path))
                            reached.add(new_state_tuple)


    # Heuristic function for Greedy and A* search
    # Given a state, it returns the number of blocks that are in the correct place
    def h_val(self, state: Tuple[Tuple[Optional[int]]]) -> int:
        num_same = 0
        for i in range(self.num_towers):
            for j in range(self.max_height):
                if state[i][j] != self.goal_state[i][j]: 
                    num_same += 1
        return num_same
        

    # Greedy heurstic search. Chooses next node based soley on h values
    # Does not guarantee the shortest path
    # Returns the sequence of moves to reach the goal state
    # F value ties are broken randomely
    def greedy(self) -> MoveList:
        hp = [(self.h_val(self.initial_state), random.random(), self.initial_state, [])] # <f value, random number, current state, path>
        reached = set([self.initial_state])

        while hp:
            _, _, state, path = heapq.heappop(hp)
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1
                        
                        new_state = [list(tower) for tower in state] # Convert to list to allow mutability
                        
                        # Move the brick
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)] # Add the move to the path
                        new_state_tuple = tuple(tuple(tower) for tower in new_state) # Convert back to tuple to allow state to be added to heap

                        if new_state_tuple == self.goal_state:
                            return new_path
                        elif new_state_tuple not in reached:
                            heapq.heappush(hp, (self.h_val(new_state_tuple), random.random(), new_state_tuple, new_path))
                            reached.add(new_state_tuple)
    

    # Heurstic search. Chooses next node based h val and current depth: f(n) = g(n) + h(n)
    # Returns the sequence of moves to reach the goal state
    # F value ties are broken based on order inserted. (ie nodes seen first will be visited first)
    def a_star(self) -> MoveList:
        order_inserted = 0
        hp = [(self.h_val(self.initial_state), order_inserted, 0, self.initial_state, [])] # <f value, heap insert number, depth, current state, path>
        reached = set([self.initial_state])

        while hp:
            *_, depth, state, path = heapq.heappop(hp)
                  
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1
                        
                        new_state = [list(tower) for tower in state] # Convert to list to allow mutability
                        
                        # Move the brick
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)] # Add the move to the path
                        new_state_tuple = tuple(tuple(tower) for tower in new_state) # Convert back to tuple to allow state to be added to heap


                        if new_state_tuple == self.goal_state:
                            return new_path
                        elif new_state_tuple not in reached:
                            reached.add(new_state_tuple)
                            order_inserted += 1
                            heapq.heappush(hp, (self.h_val(new_state_tuple)+depth+1, order_inserted, depth+1, new_state_tuple, new_path))

# Given dimension of the puzzle, creates a TowerPuzzle state based on user input
def get_tower_input(num_towers: int, max_height: int) -> TowerPuzzle:
    tower_grid = []
    for tower in range(num_towers):
        single_tower = []
        print(f"Enter the blocks for tower {tower+1} from top to bottom, seperated by a space")
        tower_input = str(input())
        format_input = tower_input.strip().split(" ") if tower_input else []
        format_input = [None] * (max_height - len(format_input)) + format_input
        tower_grid.append(format_input)
        print_intermediate_tower(tower_grid, num_towers, max_height)
    return tower_grid

# Prints puzzle to console
def print_intermediate_tower(tower_grid: TowerPuzzle, num_towers: int, max_height: int) -> None:
    output = "\n"
    for h in range(num_towers):
        output += str(h+1) + "\t"
    output += "\n\n"
    for h in range(max_height):
        for t in range(len(tower_grid)):
            output += tower_grid[t][h]+"\t" if tower_grid[t][h] is not None else "|\t"
        output+="\n"
    print(output)

# Creates initial and goal tower states based on user input
def get_tower_from_input() -> None:
    print("How many towers are there?")
    num_towers = int(input())

    print("What is the max amount of blocks (height) for each tower?")
    max_height = int(input())

    print("CREATE INITIAL TOWER")
    initial_tower_grid = get_tower_input(num_towers, max_height)
    print("CREATE GOAL TOWER")
    goal_tower_grid = get_tower_input(num_towers, max_height)

    return TowerPuzzle(initial_tower_grid, goal_tower_grid)

# Given a puzzle state and a sequence of moves, applies the moves to the puzzle
def apply_moves(tower: TowerPuzzle, moves: MoveList) -> TowerPuzzle:
    for i, (curr_tower, next_tower) in enumerate(moves):
        if curr_tower == next_tower or tower[next_tower][0] != None or tower[curr_tower][-1] == None:
            raise Exception(f"Invalid set of moves. Error found on move {i} (0-indexed)")
        
        curr_top_elem_idx = next((i for i, x in enumerate(tower[curr_tower]) if x is not None), None)
        next_opening_idx = next((i for i, x in enumerate(tower[next_tower]) if x is not None), len(tower[next_tower])) - 1

        tower[next_tower][next_opening_idx] = tower[curr_tower][curr_top_elem_idx]
        tower[curr_tower][curr_top_elem_idx] = None
    
    return tower


if __name__ == "__main__":
    tp = get_tower_from_input()
    
    print("Calculating...\n")
    print("(Sit tight! This may take a minute)\n")
    
    res = tp.a_star()

    print(f"Min moves: {len(res)}\n\n")
    print("(note: towers are 0 indexed)\n")
    for i,move in enumerate(res):
        print(f"Move #{i+1}: {move[0]} --> {move[1]}\n")
    print("\n")
    


    
