# Orientations
# 0 is normal 1 is flipped (horiz/vert)
# 0,0 0,1 1,0 1,1
from functools import reduce
class Tile:

    def __init__(self, id_, grid):
        self.id = id_
        self.grid = grid
        top = ''.join(grid[0])
        bottom = ''.join(grid[9])
        left = ''.join([grid[y][0] for y in range(10)])
        right = ''.join([grid[y][9] for y in range(10)])
        top_reversed = ''.join(reversed(top))
        bottom_reversed = ''.join(reversed(bottom))
        left_reversed = ''.join(reversed(left))
        right_reversed = ''.join(reversed(right))
        self.sides = [left, right, top, bottom, top_reversed, bottom_reversed, left_reversed, right_reversed]

    @classmethod
    def from_raw_data(cls, data):
        lines = data.split('\n')
        id_ = int(lines[0].split(' ')[1][:-1])
        grid = []
        for i in range(1, 11):
            grid.append([c for c in lines[i]])
        return Tile(id_, grid)

    def __str__(self):
        return f'{self.id}'


def parse_input(filename):
    blobs = open(filename).read().split('\n\n')
    tiles = []
    for data in blobs:
        tiles.append(Tile.from_raw_data(data))
    return tiles

if __name__ == '__main__':

    puzzle_input = parse_input('day_20.in')
    sample_input = parse_input('day_20.in.sample')
    acc = 1
    tile_input = puzzle_input
    for tile in tile_input:
        matching_sides = []
        for side in tile.sides:
            for xtile in tile_input:
                if xtile.id == tile.id:
                    continue
                if side in xtile.sides:
                    matching_sides.append(side)
        if not matching_sides:
            print(tile.id)
        else:
            print(f'{tile.id}: \n{matching_sides}')
            if len(matching_sides) == 4:
                acc *= tile.id


    print(acc)

