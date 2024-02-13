class TowerPuzzle:

    def __init__(self, initial_towers, goal_towers):
        self.initial_towers = initial_towers
        self.goal_towers = goal_towers
        self.num_towers = len(towers)
        self.max_height = len(towers[0])
        
    # def __str__(self):
    #     output = "\n"
    #     for h in range(self.max_height):
    #         for t in range(self.num_towers):
    #             output+=self.towers[t][h]+"\t" if self.towers[t][h] is not None else "|\t"
    #         output+="\n"
    #     return output

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

if __name__ == "__main__":
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
    tp = TowerPuzzle(initial_tower_grid, goal_tower_grid)

    
    
    # print(tp)

    # tp = TowerPuzzle(num_towers, max_height)
    # print(tp)


# output = ""
# for h in range(max_height):
#     for t in range(num_towers):
#         output+="|\t"
#     output+="\n"

# print(output)

