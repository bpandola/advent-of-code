# Orientations
# 0 is normal 1 is flipped (horiz/vert)
# 0,0 0,1 1,0 1,1
from functools import reduce
import math


class Tile:

    def __init__(self, id_, grid):
        self.id = id_
        self.size = len(grid)
        self.shrink_factor = 0
        self.flipped_vertical = False
        self.flipped_horizontal = False
        self.flipped_axis = False
        self._orientations = {}
        for flip_horiz in [False, True]:
            for flip_vert in [False, True]:
                for flip_axis in [False, True]:
                    oriented = grid[:]
                    if flip_horiz:
                        oriented = self.flip_horizontal(oriented)
                    if flip_vert:
                        oriented = self.flip_vertical(oriented)
                    if flip_axis:
                        oriented = self.flip_axis(oriented)
                    self._orientations[(flip_horiz, flip_vert, flip_axis)] = oriented


    @property
    def grid(self):
        return self._orientations[(self.flipped_horizontal, self.flipped_vertical, self.flipped_axis)]

    @property
    def sides(self):
        return [self.top, self.bottom, self.left, self.right]

    @property
    def top(self):
        return ''.join(self.grid[0+self.shrink_factor])

    @property
    def bottom(self):
        return ''.join(self.grid[self.size - 1 - self.shrink_factor])

    @property
    def left(self):
        return ''.join([self.grid[y][0+self.shrink_factor] for y in range(0+self.shrink_factor,self.size-self.shrink_factor)])

    @property
    def right(self):
        return ''.join([self.grid[y][self.size - 1 - self.shrink_factor] for y in range(0 + self.shrink_factor, self.size - self.shrink_factor)])

    @property
    def orientations(self):
        for flip_horiz in [False, True]:
            for flip_vert in [False, True]:
                for flip_axis in [False, True]:
                    self.flipped_horizontal = flip_horiz
                    self.flipped_vertical = flip_vert
                    self.flipped_axis = flip_axis
                    yield self

    @staticmethod
    def flip_horizontal(grid):
        return [list(reversed(line)) for line in grid]

    @staticmethod
    def flip_vertical(grid):
        return [grid[i] for i in range(len(grid)-1, -1, -1)]

    @staticmethod
    def flip_axis(grid):
        grid_flipped = []
        for x in range(len(grid)-1,-1,-1):
            line = [grid[y][x] for y in range(len(grid))]
            grid_flipped.append(line)
        return grid_flipped

    @staticmethod
    def shrink(grid, shrink):
        grid_shrunk = []
        for y in range(shrink,  len(grid) - shrink):
            line = [grid[y][x] for x in range(shrink, len(grid)-shrink)]
            grid_shrunk.append(line)
        return grid_shrunk

    @classmethod
    def from_raw_data(cls, data):
        lines = data.split('\n')
        id_ = int(lines[0].split(' ')[1][:-1])
        grid = []
        for i in range(1,len(lines)):
            grid.append([c for c in lines[i]])
        return Tile(id_, grid)

    def __str__(self):
        return f'{self.id}'

    def print(self):
        for j in range(self.size):
            print(''.join(self.grid[j]))


#
# class Tile2:
#
#     def __init__(self, id_, grid):
#         self.id = id_
#         self.grid = grid
#         self.size = len(grid)
#         self.flipped_horizontal = False
#         self.flipped_vertical = False
#         self.shrink_factor = 0
#         # top = ''.join(grid[0+self.shrink_factor])
#         # bottom = ''.join(grid[self.size-1-self.shrink_factor])
#         # left = ''.join([grid[y][0+self.shrink_factor] for y in range(0+self.shrink_factor,self.size-self.shrink_factor)])
#         # right = ''.join([grid[y][self.size-1-self.shrink_factor] for y in range(0+self.shrink_factor, self.size-self.shrink_factor)])
#         # top_reversed = ''.join(reversed(top))
#         # bottom_reversed = ''.join(reversed(bottom))
#         # left_reversed = ''.join(reversed(left))
#         # right_reversed = ''.join(reversed(right))
#         # self.sides = [left, right, top, bottom, top_reversed, bottom_reversed, left_reversed, right_reversed]
#
#     @property
#     def sides(self):
#         return [self.top, self.bottom, self.left, self.right]
#
#     @property
#     def top(self):
#         if self.flipped_vertical:
#             top = ''.join(self.grid[self.size - 1 - self.shrink_factor])
#         else:
#             top = ''.join(self.grid[0+self.shrink_factor])
#         if self.flipped_horizontal:
#             return ''.join(reversed(top))
#         return top
#
#     @property
#     def bottom(self):
#         if self.flipped_vertical:
#             bottom = ''.join(self.grid[0+self.shrink_factor])
#         else:
#             bottom = ''.join(self.grid[self.size - 1 - self.shrink_factor])
#         if self.flipped_horizontal:
#             return ''.join(reversed(bottom))
#         return bottom
#
#     @property
#     def left(self):
#         if self.flipped_horizontal:
#             left = ''.join([self.grid[y][self.size - 1 - self.shrink_factor] for y in range(0 + self.shrink_factor, self.size - self.shrink_factor)])
#         else:
#             left = ''.join([self.grid[y][0+self.shrink_factor] for y in range(0+self.shrink_factor,self.size-self.shrink_factor)])
#         if self.flipped_vertical:
#             return ''.join(reversed(left))
#         return left
#
#     @property
#     def right(self):
#         if self.flipped_horizontal:
#             right = ''.join([self.grid[y][0+self.shrink_factor] for y in range(0+self.shrink_factor,self.size-self.shrink_factor)])
#         else:
#             right = ''.join([self.grid[y][self.size - 1 - self.shrink_factor] for y in range(0 + self.shrink_factor, self.size - self.shrink_factor)])
#         if self.flipped_vertical:
#             return ''.join(reversed(right))
#         return right
#
#     @property
#     def orientations(self):
#         for flip_horiz in [False, True]:
#             for flip_vert in [False, True]:
#                 self.flipped_horizontal = flip_horiz
#                 self.flipped_vertical = flip_vert
#                 yield self
#
#     @classmethod
#     def from_raw_data(cls, data):
#         lines = data.split('\n')
#         id_ = int(lines[0].split(' ')[1][:-1])
#         grid = []
#         for i in range(1, 11):
#             grid.append([c for c in lines[i]])
#         return Tile(id_, grid)
#
#     def __str__(self):
#         return f'{self.id}'

def parse_input(filename):
    blobs = open(filename).read().split('\n\n')
    tiles = []
    for data in blobs:
        tiles.append(Tile.from_raw_data(data))
    return tiles

class ImageAssembler:

    def __init__(self, tiles):
        self.size = int(math.sqrt(len(tiles)))
        self.image = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.tile_map = self._preprocess_tiles(tiles)
        self.assembled = None

    @property
    def corners(self):
        return [k for k, v in self.tile_map.items() if len(v) == 4]

    @property
    def borders(self):
        return [k for k, v in self.tile_map.items() if len(v) == 6]

    @property
    def interior(self):
        return [k for k, v in self.tile_map.items() if len(v) == 8]


    def _preprocess_tiles(self, tiles):
        tile_sides = {t: set([side for orientation in t.orientations for side in orientation.sides  ]) for t in tiles}
        tile_map = {}
        for tile in tiles:
            matching_sides = set()
            for side in tile_sides[tile]:
                for xtile in tiles:
                    if xtile.id == tile.id:
                        continue
                    if side in tile_sides[xtile]:
                        matching_sides.add(side)
            tile_map[tile] = matching_sides
        return tile_map

    def assemble(self):
        # left, right, top, bottom = 0,1,2,3 index array
        def orient_tile(tile_to_orient, sides_to_match, surroundings):
            matching = self.tile_map[tile_to_orient]
            correct = False
            for _ in tile_to_orient.orientations:
                correct = True
                if any(sides_to_match):
                    if sides_to_match[0] and tile_to_orient.left not in matching:
                        correct = False
                    if not sides_to_match[0] and tile_to_orient.left in matching:
                        correct = False
                    if sides_to_match[1] and tile_to_orient.right not in matching:
                        correct = False
                    if not sides_to_match[1] and tile_to_orient.right in matching:
                        correct = False
                    if sides_to_match[2] and tile_to_orient.top not in matching:
                        correct = False
                    if not sides_to_match[2] and tile_to_orient.top in matching:
                        correct = False
                    if sides_to_match[3] and tile_to_orient.bottom not in matching:
                        correct = False
                    if not sides_to_match[3] and tile_to_orient.bottom in matching:
                        correct = False
                if surroundings:
                    if surroundings[0] and tile_to_orient.left != surroundings[0].right:
                        correct = False
                    if surroundings[1] and tile_to_orient.right != surroundings[1].left:
                        correct = False
                    if surroundings[2] and tile_to_orient.top != surroundings[2].bottom:
                        correct = False
                    if surroundings[3] and tile_to_orient.bottom != surroundings[3].top:
                        correct = False
                    
                if correct:
                    break
            return correct

        #image = [[None for _ in range(self.size)] for _ in range(self.size)]
        image = {}
        def get_neighbors(x, y):
            # left, right, top, bottom
            deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            neighbors = []
            for m, n in deltas:
                neighb = None
                try:
                    neighb = image[(x+m, y+n)]
                except KeyError:
                    pass
                neighbors.append(neighb)
            return neighbors


        #while any(tile is None for row in image for tile in row):
        while len(image) < self.size**2:
            restart = False
            for i in range(self.size):
                for j in range(self.size):
                    if (i, j) in image:
                        continue
                    surrounding_tiles = get_neighbors(i, j)
                    sides_to_match = [False, False, False, False]
                    tiles = set()
                    if surrounding_tiles.count(None) == 4:
                        # Top - left corner special case
                        tiles |= set(self.corners)
                        sides_to_match = [False, True, False, True]
                    if surrounding_tiles.count(None) == 2:
                        tiles |=set(self.corners)
                    if surrounding_tiles.count(None) in [1,2,3]:
                        tiles|=set(self.borders)
                    if surrounding_tiles.count(None) in [0,2,3]:
                        tiles|=set(self.interior)
                    if (i,j) in [(0,0),(0,self.size-1),(self.size-1,0),(self.size-1, self.size-1)]:
                        tiles|=set(self.corners)

                    potential_tiles = []
                    for potential_tile in tiles:
                        if orient_tile(potential_tile, sides_to_match, surrounding_tiles):
                            potential_tiles.append(potential_tile)
                    if potential_tiles and len(potential_tiles) == 1 or set(potential_tiles) == set(self.corners):
                        potential_tile = potential_tiles[0]
                        image[(i,j)] = potential_tile
                        del self.tile_map[potential_tile]
                        restart = True
                        break
                    if restart:
                        break
                if restart:
                    break
        # Now we have our image with each tile shrunk by one
        # Now we stitch into one big tile
        for key, value in image.items():
            image[key] = Tile(value.id, value.shrink(value.grid, 1))
        full_grid = []
        tile_size = image[(0,0)].size
        for y in range(self.size):
            full_grid += [[] for _ in range(tile_size)]
            for x in range(self.size):
                tile = image[(x,y)]
                for j in range(tile_size):
                    full_grid[y*tile_size+j] += tile.grid[j]





        ret = Tile(-1, full_grid)
        return ret
                        


def find_sea_monsters(image):
    deltas = [
        (0,0),
        (18,-1),
        (5, 0),
        (6, 0),
        (11, 0),
        (12, 0),
        (17, 0),
        (18, 0),
        (19, 0),
        (1, 1),
        (4, 1),
        (7, 1),
        (10, 1),
        (13, 1),
        (16, 1),
    ]
    for orientation in image.orientations:
        grid = orientation.grid
        sea_monsters = 0
        for j in range(image.size):
            for i in range(image.size):
                if grid[j][i] != '#':
                    continue
                for m, n in deltas:
                    x = i + m
                    y = j + n
                    if x<0 or y <0 or x>=orientation.size or y>= orientation.size:
                        break
                    ch = grid[y][x]
                    if ch != '#':
                        break
                else:
                    sea_monsters += 1
        if sea_monsters > 0:
            num_hashes = sum([line.count('#') for line in grid])
            num_hashes -= sea_monsters*15
            print(f'Num Hashes: {num_hashes}')








if __name__ == '__main__':

    puzzle_input = parse_input('day_20.in')
    sample_input = parse_input('day_20.in.sample')

    # Part 1
    sample_ia = ImageAssembler(sample_input)
    assert reduce(lambda x, y: x * y, [tile.id for tile in sample_ia.corners]) == 20899048083289

    puzzle_ia = ImageAssembler(puzzle_input)
    print(reduce(lambda x, y: x * y, [tile.id for tile in puzzle_ia.corners]))

    # Part 2
    image = sample_ia.assemble()
    # for orientation in image.orientations:
    #     orientation.print()
    #     print('\n\n')
    find_sea_monsters(image)

    image = puzzle_ia.assemble()
    find_sea_monsters(image)
