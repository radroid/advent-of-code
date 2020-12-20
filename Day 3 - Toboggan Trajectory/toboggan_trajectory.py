import pathlib


class TrajectoryCalculator:
    """
    The class calculates the number of trees encountered when a Toboggan
    follows a certain slope, in a specific forest.
    """
    def __init__(self, forest_filename: str, dx: int, dy: int = 1):
        """Instantiate class

        Args:
            forest_filename (str): path to the file containing 
            slope_value (int): [description]
        """
        forest = ''
        if pathlib.Path(forest_filename).exists():
            with open(forest_filename) as f:
                forest = list(f.read().split('\n'))
        self.forest = forest
        self.dx = dx
        self.dy = dy

    def calculate_trees_hit(self):
        x_pos = 0 + self.dx
        y_pos = 0 + self.dy
        trees_encountered = 0
        while y_pos < len(self.forest):
            if self.forest[y_pos][x_pos] == '#':
                    trees_encountered += 1
            x_pos += self.dx
            y_pos += self.dy
            if x_pos >= len(self.forest[0]):
                x_pos -= len(self.forest[0])
        
        print(f'Number of trees encountered: {trees_encountered}')
        return trees_encountered


if __name__ == '__main__':
    x_slopes = [1, 3, 5, 7, 1]
    y_slopes = [1, 1, 1, 1, 2]
    product = 1
    for dx, dy in zip(x_slopes, y_slopes):
        tc = TrajectoryCalculator('forest.txt', dx, dy)
        product *= tc.calculate_trees_hit()
    
    print(f'Product of all slopes: {product}')