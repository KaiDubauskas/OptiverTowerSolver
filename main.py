from collections import deque

class Tests():
    def test_applymoves(self):
        tower = [['1', '2', '3'], [None, None, None], [None, None, None]]
        moves = [(0, 1), (0, 2), (0, 2), (1, 0)]
        goal = [[None, None, '1'], [None, None, None], [None, '3', '2']]
        assert apply_moves(tower, moves) == goal
        
    def test_bfs1(self):
        initial = [['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        num_moves = 6
        assert TowerPuzzle(initial, goal).bfs()[0] == num_moves

    def test_bfs2(self):
        initial = [[None, '1', '2'], [None, None, '3'], [None, None, None]]
        goal = [[None, None, None], [None, None, None], ['2', '3', '1']]
        num_moves = 3
        assert TowerPuzzle(initial, goal).bfs()[0] == num_moves
    
    def test_bfs3(self):
        initial = [[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [[None, None, None, None], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        num_moves = 6
        assert TowerPuzzle(initial, goal).bfs()[0] == num_moves

    def test_bfs4(self):
        initial = [[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [[None, None, None, '14'], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, None, '13', '12']]
        num_moves = 7
        assert TowerPuzzle(initial, goal).bfs()[0] == num_moves


class TowerPuzzle:
    def __init__(self, initial_towers, goal_towers):
        if (len(initial_towers) != len(goal_towers)):
            raise ValueError("Initial and goal towers must have the same number of towers")
        self.initial_towers = initial_towers
        self.goal_towers = goal_towers
        self.num_towers = len(initial_towers)
        self.max_height = len(initial_towers[0])

    # queue<state, path>
    def bfs(self):
        initial_state_tuple = (tuple(tuple(tower) for tower in self.initial_towers))
        goal = (tuple(tuple(tower) for tower in self.goal_towers))
        queue = deque([ (initial_state_tuple, []) ])
        reached = set([initial_state_tuple])

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

                        if new_state_tuple == goal:
                            return (len(new_path), new_path)
                        else:
                            queue.append((new_state_tuple, new_path))
                            reached.add(new_state_tuple)
                    
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




if __name__ == "__main__":

    # run_tests()

    # print("How many towers are there?")
    # num_towers = int(input())

    # print("What is the max amount of blocks (height) for each tower?")
    # max_height = int(input())

    # print("CREATE INITIAL TOWER")
    # initial_tower_grid = get_tower_input(num_towers, max_height)
    # print("CREATE GOAL TOWER")
    # goal_tower_grid = get_tower_input(num_towers, max_height)


    # print("\n\nINITIAL\n")
    # print(initial_tower_grid)
    # print("\n\nGOAL\n")
    # print(goal_tower_grid)
    # tp = TowerPuzzle([[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']],
    #  [[None, None, None, '14'], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, None, '13', '12']])
    # print(tp.bfs())

    print("k")
    

    # print(tp)
