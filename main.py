from collections import deque
import heapq
import random

class TowerPuzzle:
    def __init__(self, initial_towers, goal_towers):
        if (len(initial_towers) != len(goal_towers)):
            raise ValueError("Initial and goal towers must have the same number of towers")
        self.initial_state = (tuple(tuple(tower) for tower in initial_towers))
        self.goal_state = (tuple(tuple(tower) for tower in goal_towers))
        self.num_towers = len(initial_towers)
        self.max_height = len(initial_towers[0])
        # count_not_none = lambda tower: (len(list(filter(lambda x: x != None, tower))))
        # self.total_numbers = sum(count_not_none(tower) for tower in initial_towers)

    # queue<state, path>
    def bfs(self):
        queue = deque([ (self.initial_state, []) ])
        reached = set([self.initial_state])
        
        while queue:
            state, path = queue.popleft()
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1

                        new_state = [list(tower) for tower in state]
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)]
                        new_state_tuple = tuple(tuple(tower) for tower in new_state)

                        if new_state_tuple == self.goal_state:
                            return (len(new_path), new_path)
                        elif new_state_tuple not in reached:
                            queue.append((new_state_tuple, new_path))
                            reached.add(new_state_tuple)

    def eval(self, state):
        num_same = 0
        for i in range(self.num_towers):
            for j in range(self.max_height):
                if state[i][j] != self.goal_state[i][j]: 
                    num_same += 1
        return num_same
        

    # uses a random number to break ties in heap
    # does not guarantee the shortest path
    def greedy(self):
        hp = [(self.eval(self.initial_state), random.random(), self.initial_state, [])]
        reached = set([self.initial_state])

        while hp:
            _, _, state, path = heapq.heappop(hp)
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1
                        
                        new_state = [list(tower) for tower in state]
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)]
                        new_state_tuple = tuple(tuple(tower) for tower in new_state)

                        if new_state_tuple == self.goal_state:
                            return (len(new_path), new_path)
                        elif new_state_tuple not in reached:
                            heapq.heappush(hp, (self.eval(new_state_tuple), random.random(), new_state_tuple, new_path))
                            reached.add(new_state_tuple)
    

    # hp <evaluation, tiebreaker, current depth, state, path>
    # uses order inserted to break ties in the heap
    def a_star(self):
        order_inserted = 0
        hp = [(self.eval(self.initial_state), order_inserted, 0, self.initial_state, [])]
        reached = set([self.initial_state])

        while hp:
            *_, depth, state, path = heapq.heappop(hp)
                  
            for i,curr_tower in enumerate(state):
                for j,next_tower in enumerate(state):
                    if i != j and next_tower[0] == None and curr_tower[-1] != None:
                        curr_top_elem_idx = next((i for i, x in enumerate(curr_tower) if x is not None), None)
                        next_opening_idx = next((i for i, x in enumerate(next_tower) if x is not None), len(next_tower)) - 1
                        
                        new_state = [list(tower) for tower in state]
                        new_state[j][next_opening_idx] = new_state[i][curr_top_elem_idx]
                        new_state[i][curr_top_elem_idx] = None

                        new_path = path + [(i, j)]
                        new_state_tuple = tuple(tuple(tower) for tower in new_state)


                        if new_state_tuple == self.goal_state:
                            return (len(new_path), new_path)
                        elif new_state_tuple not in reached:
                            reached.add(new_state_tuple)
                            order_inserted += 1
                            heapq.heappush(hp, (self.eval(new_state_tuple)+depth+1, order_inserted, depth+1, new_state_tuple, new_path))

def get_tower_input(num_towers, max_height):
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

def print_intermediate_tower(tower_grid, num_towers, max_height):
    output = "\n"
    for h in range(num_towers):
        output += str(h+1) + "\t"
    output += "\n\n"
    for h in range(max_height):
        for t in range(len(tower_grid)):
            output += tower_grid[t][h]+"\t" if tower_grid[t][h] is not None else "|\t"
        output+="\n"
    print(output)

def apply_moves(tower, moves):
    for i, (curr_tower, next_tower) in enumerate(moves):
        if curr_tower == next_tower or tower[next_tower][0] != None or tower[curr_tower][-1] == None:
            raise Exception(f"Invalid set of moves. Error found on move {i} (0-indexed)")
        
        curr_top_elem_idx = next((i for i, x in enumerate(tower[curr_tower]) if x is not None), None)
        next_opening_idx = next((i for i, x in enumerate(tower[next_tower]) if x is not None), len(tower[next_tower])) - 1

        tower[next_tower][next_opening_idx] = tower[curr_tower][curr_top_elem_idx]
        tower[curr_tower][curr_top_elem_idx] = None
    
    return tower


def get_tower_from_input():
    print("How many towers are there?")
    num_towers = int(input())

    print("What is the max amount of blocks (height) for each tower?")
    max_height = int(input())

    print("CREATE INITIAL TOWER")
    initial_tower_grid = get_tower_input(num_towers, max_height)
    print("CREATE GOAL TOWER")
    goal_tower_grid = get_tower_input(num_towers, max_height)


    print("\n\nINITIAL\n")
    print(initial_tower_grid)
    print("\n\nGOAL\n")
    print(goal_tower_grid)
    return TowerPuzzle(initial_tower_grid, goal_tower_grid)

if __name__ == "__main__":
    # tp = get_tower_from_input()

    # tp = TowerPuzzle(
    #     [[None, None, None, '2', '3'], [None, '1', '4', '5', '6'], [None, None, '7', '8', '9']],
    #     [[None, '7', '8', '2', '3'], [None, None, None, '4', '6'], [None, None, '5', '1', '9']]
    # )
    tp = TowerPuzzle(
        [[None, None, '1', '2', '3'], [None, None, None, '4', '5'], [None, None, None, '6', '7']],
        [['7', '6', '2', '1', '3'], [None, None, None, None, '5'], [None, None, None, None, '4']]
    )
    
    # print(tp.eval(
    #     [[None, '3', '4', '1'], ['11', '7', '6', '5'], [None, '2', '10', '9'], [None, '14', '13', '12']]
    # ))
    print(tp.bfs())
    # print(apply_moves(
    #     [[None, None, '1', '2', '3'], [None, None, '4', '5', '6'], [None, None, '7', '8', '9'], [None, None, None, '10', '11']],
    #     [(0, 3), (1, 2), (0, 2), (1, 0), (1, 0), (3, 1), (3, 1), (3, 1), (2, 3), (2, 3), (1, 3), (2, 3), (2, 0), (2, 1), (0, 2), (0, 2), (0, 2), (0, 1), (3, 0), (1, 0)]
    # ))


    # initial = [['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
    #     goal = [['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]

