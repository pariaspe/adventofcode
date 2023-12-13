from dataclasses import dataclass


@dataclass
class Tree:
    size: int
    visible: bool = False
    scenic_score: int = 1

    def __repr__(self) -> str:
        return f"({self.size}, {self.visible}, {self.scenic_score})"


def read_tree_grid(filename):
    with open(filename) as fin:
        trees = fin.readlines()

    tree_grid_ = []

    for tree_row in trees:
        if not tree_row.strip():
            break

        tree_grid_.append([Tree(int(tree)) for tree in list(tree_row.strip())])
    return tree_grid_


def check_visibility_right(x_, y_, grid):
    for i in range(y_+1, len(grid)):
        if grid[x_][i].size >= grid[x_][y_].size:
            grid[x_][y_].scenic_score *= i-y_
            return False
    grid[x_][y_].scenic_score *= (len(grid)-1)-y_
    return True


def check_visibility_left(x_, y_, grid):
    for i in range(y_-1, -1, -1):
        if grid[x_][i].size >= grid[x_][y_].size:
            grid[x_][y_].scenic_score *= y_-i
            return False
    grid[x_][y_].scenic_score *= y_
    return True


def check_visibility_down(x_, y_, grid):
    for i in range(x_+1, len(grid)):
        if grid[i][y_].size >= grid[x_][y_].size:
            grid[x_][y_].scenic_score *= i-x_
            return False
    grid[x_][y_].scenic_score *= (len(grid)-1)-x_
    return True


def check_visibility_up(x_, y_, grid):
    for i in range(x_-1, -1, -1):
        if grid[i][y_].size >= grid[x_][y_].size:
            grid[x_][y_].scenic_score *= x_-i
            return False
    grid[x_][y_].scenic_score *= x_
    return True


def check_visibility(x_, y_, grid):
    a_ = check_visibility_up(x_, y_, grid)
    b_ = check_visibility_down(x_, y_, grid)
    c_ = check_visibility_right(x_, y_, grid)
    d_ = check_visibility_left(x_, y_, grid)
    return a_ or b_ or c_ or d_


# TODO use yield to only go through list once
def count_visible(grid):
    cont = 0
    for row in grid:
        for tree in row:
            if tree.visible:
                cont += 1
    return cont


def find_max_score(grid):
    max_score = []
    for row in grid:
        max_score.append(max([tree.scenic_score for tree in row]))

    print(max_score)
    return max(max_score)


if __name__ == "__main__":
    # tree_grid = read_tree_grid("8-test.txt")
    tree_grid = read_tree_grid("8-input.txt")

    # print(check_visibility_right(0, 3, tree_grid))
    # exit()

    for x, row in enumerate(tree_grid):
        for y, tree in enumerate(row):
            if check_visibility(x, y, tree_grid):
                tree.visible = True
        #     print(tree, end=" ")
        # print()

    print(f"part one: {count_visible(tree_grid)=}")
    print(f"part 2: {find_max_score(tree_grid)=}")
