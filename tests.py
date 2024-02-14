from main import TowerPuzzle, apply_moves

# Automated tests
# "pytest tests.py" to run

class Tests():
    def test_applymoves1(self):
        tower = [['1', '2', '3'], [None, None, None], [None, None, None]]
        moves = [(0, 1), (0, 2), (0, 2), (1, 0)]
        goal = [[None, None, '1'], [None, None, None], [None, '3', '2']]
        assert apply_moves(tower, moves) == goal
        
    def test_bfs1(self):
        initial = [['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        num_moves = 6

        res = TowerPuzzle(initial, goal).bfs()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)
    
    def test_bfs2(self):
        initial = [[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [[None, None, None, None], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        num_moves = 6

        res = TowerPuzzle(initial, goal).bfs()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)

    def test_bfs3(self):
        initial = [[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [[None, None, None, '14'], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, None, '13', '12']]
        num_moves = 7

        res = TowerPuzzle(initial, goal).bfs()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)
        
    def test_bfs4(self):
        initial = [[None, '3', '2', '1'], [None, '6', '5', '4'], [None, None, None, '7'], [None, None, None, None]]
        goal = [[None, '2', '3', '1'], [None, '4', '7', '6'], [None, None, None, '5'], [None, None, None, None]]
        num_moves = 11

        res = TowerPuzzle(initial, goal).bfs()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)
    
    def test_greedy1(self):
        initial = [[None, None, None, None], ['4', '3', '2', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, '14', '13', '12']]
        goal = [[None, None, None, '14'], ['2', '3', '4', '1'], [None, '7', '6', '5'], [None, '11', '10', '9'], [None, None, '13', '12']]
        num_moves = 7

        res = TowerPuzzle(initial, goal).greedy()
        assert (apply_moves(initial, res[1]) == goal)
    
    def test_greedy2(self):
        initial = [[None, '3', '2', '1'], [None, '6', '5', '4'], [None, None, None, '7'], [None, None, None, None]]
        goal = [[None, '2', '3', '1'], [None, '4', '7', '6'], [None, None, None, '5'], [None, None, None, None]]
        num_moves = 11

        res = TowerPuzzle(initial, goal).greedy()
        assert (apply_moves(initial, res[1]) == goal)

    def test_astar1(self):
        initial = [[None, None, '1', '2', '3'], [None, None, '4', '5', '6'], [None, None, '7', '8', '9'], [None, None, None, '10', '11']]
        goal = [[None, None, None, '3', '7'], [None, None, '9', '10', '1'], [None, None, '5', '6', '8'], [None, None, '11', '4', '2']]
        num_moves = 19

        res = TowerPuzzle(initial, goal).a_star()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)

    def test_astar2(self):
        initial = [[None, '3', '2', '1'], [None, '6', '5', '4'], [None, None, None, '7'], [None, None, None, None]]
        goal = [[None, '2', '3', '1'], [None, '4', '7', '6'], [None, None, None, '5'], [None, None, None, None]]
        num_moves = 11

        res = TowerPuzzle(initial, goal).a_star()
        assert (res[0] == num_moves) and (apply_moves(initial, res[1]) == goal)
