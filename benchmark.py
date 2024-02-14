from main import TowerPuzzle, apply_moves
from time import time 

"""
Each search algorithm ran 3x for each puzzle and average of results was taken

Dim.    %Full   #Moves  |    Bfs          Greedy          A*
-----------------------------------------------------------------
5x3     47%     7       |    0.0115s      0.0133s         0.0016s
5x3     60%     7       |    0.0145s      0.0014s         0.0007s
7x5     37%     7       |   31.1617s      0.0008s         0.0015s
4x4     44%     11      |    3.3821s      0.0076s         0.0349s
5x4     55%     19      |        >5m      1.2776s        77.1872s



- Efficiency of heuristic algorithms (greedy and A*) is far less dependent on the number of moves 
and more on the space taken by disks

- Very surprised that A* had such a huge increase in speed when the size of the grid increased but 
num moves to solve remained at 7. I'm guessing this is more because of the state of the test. The minimum 
moves to solve this puzzle has less moves that result in a lower evaluation score than the other tests.

- Huge bottleneck of BFS is (expectedly) the size of the puzzle. Runtime exponentially increases compared
to Greedy or A*

- Greedy always does well, but almost never finds the shortest path. It can easily take >100 moves to find a solution

- These benchmark tests were created manually and dont test all situations. To create more representative tests, 
I should look at the starting evaluation score since 11 moves can mean very different things if it changes 
the position of 3 disks or 8 disks

"""
initial0 = [[None, None, '1', '2', '3'], [None, None, None, '4', '5'], [None, None, None, '6', '7']]
goal0 = [['7', '6', '2', '1', '3'], [None, None, None, None, '5'], [None, None, None, None, '4']]
tp0 = TowerPuzzle(initial0, goal0)

initial1 = [[None, None, None, '2', '3'], [None, '1', '4', '5', '6'], [None, None, '7', '8', '9']]
goal1 = [[None, '7', '8', '2', '3'], [None, None, None, '4', '6'], [None, None, '5', '1', '9']]
tp1 = TowerPuzzle(initial1, goal1)

initial2 = [[None, None, None, None, '1', '2', '3'], [None, None, None, None, '4', '5', '6'], [None, None, None, None, '7', '8', '9'], [None, None, None, None, '10', '11', '12'], [None, None, None, None, None, None, '13']]
goal2 = [[None, None, None, None, '1', '2', '3'], [None, None, None, None, '8', '5', '6'], [None, None, None, None, None, '7', '9'], [None, None, None, None, None, None, '4'], [None, None, None,'12', '11', '10', '13']]
tp2 = TowerPuzzle(initial2, goal2)

initial3 = [[None, '3', '2', '1'], [None, '6', '5', '4'], [None, None, None, '7'], [None, None, None, None]]
goal3 = [[None, '2', '3', '1'], [None, '4', '7', '6'], [None, None, None, '5'], [None, None, None, None]]
tp3 = TowerPuzzle(initial3, goal3)


initial4 = [[None, None, '1', '2', '3'], [None, None, '4', '5', '6'], [None, None, '7', '8', '9'], [None, None, None, '10', '11']]
goal4 = [[None, None, None, '3', '7'], [None, None, '9', '10', '1'], [None, None, '5', '6', '8'], [None, None, '11', '4', '2']]
tp4 = TowerPuzzle(initial4, goal4)

def timer_func(func):
    def wrap_func(*args, **kwargs): 
        sum = 0
        for i in range(3):
            t1 = time() 
            result = func(*args, **kwargs) 
            t2 = time() 
            sum += (t2-t1)
        return sum / 3.0
    return wrap_func
    
@timer_func
def benchmark_bfs(tower_puzzle):
    tower_puzzle.bfs()

@timer_func
def benchmark_greedy(tower_puzzle):
    tower_puzzle.greedy()

@timer_func
def benchmark_astar(tower_puzzle):
    tower_puzzle.a_star()

def print_single_row(tower_puzzle):
    return f"{benchmark_bfs(tower_puzzle):>8.4f}s\t{benchmark_greedy(tower_puzzle):>8.4f}s\t{benchmark_astar(tower_puzzle):>8.4f}s"


if __name__ == "__main__":
    print(f"\nDim.\t%Full\t#Moves\t|    Bfs\t  Greedy\t  A*")
    print("-" * 65)
    print(f"5x3\t47%\t7  \t|  {print_single_row(tp0)}")
    print(f"5x3\t60%\t7  \t|  {print_single_row(tp1)}")
    print(f"7x5\t37%\t7  \t|  {print_single_row(tp2)}")
    print(f"4x4\t44%\t11 \t|  {print_single_row(tp3)}")
    print(f"5x4\t55%\t19 \t|  {'>5m':>9}\t{benchmark_greedy(tp4):>8.4f}s\t{benchmark_astar(tp4):>8.4f}s")
    print("\n")
