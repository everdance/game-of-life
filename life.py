# Conway's game of life cell autometa
# https://en.wikipedia.org/wiki/Conway's_Game_of_Life

from random import randint

class Cells:
    """
    Cell rules:
    Any live cell with fewer than two live neighbours dies
    Any live cell with two or three live neighbours lives on
    Any live cell with more than three live neighbours dies
    Any dead cell with exactly three live neighbours becomes a live cell
    """
    def __init__(self, cells=None):
        if cells is None:
            cells = set()
            while len(cells) < 6:
                cells.add((randint(5, 10), randint(5, 10)))
        self.cells = cells
        self.init_cells = cells.copy()
        self.cycles = 0

    def is_dead(self): return len(self.cells) == 0

    def _live_nb_count(self, c):
        """ calculate a cell's live neighbor count """
        return len([
                n for n in [
                    (c[0]-1,c[1]),(c[0],c[1]-1),
                    (c[0]+1,c[1]),(c[0],c[1]+1),
                    (c[0]-1,c[1]-1),(c[0]-1,c[1]-1),
                    (c[0]+1,c[1]+1),(c[0]+1,c[1]+1)
                ]
                if n in self.cells
            ])

    def range2d(self, ex=0):
        """ get cells coordinate ranges with expand offset """
        xs = [c[0] for c in self.cells]
        ys = [c[1] for c in self.cells]

        return range(min(xs)-ex, max(xs)+ex+1),\
               range(min(ys)-ex, max(ys)+ex+1)
    
    def next(self):
        """ compute next generation of live cells """
        next_gen = set()

        for c in self.cells:
            nb_count = self._live_nb_count(c)
            if nb_count > 3 or nb_count < 2:
                continue
            next_gen.add(c)

        # check dead cells, expand checking to 1 cell outward
        x_r, y_r = self.range2d(1)
        dead_cells = [
            (x, y) for x in x_r for y in y_r
            if (x, y) not in self.cells
        ]
        for c in dead_cells:
            if self._live_nb_count(c) == 3:
                next_gen.add(c)
                
        self.cells = next_gen
        self.cycles += 1

    def _normalize(self, origin=0):
        """ normalize cell coordinates """
        x_r, y_r = self.range2d()
        x_of = origin - x_r.start
        y_of = origin - y_r.start
        self.cells = [(x + x_of, y + y_of) for (x, y) in self.cells]
        
    def __str__(self):
        self._normalize(2)
        x_r, y_r = self.range2d(2)
        
        str_r = '\n\n'
        for y in y_r:
            for x in x_r:
                if (x, y) in self.cells:
                    str_r += '\u2612'
                else:
                    str_r += '\u2610'
            str_r += '\n'

        return str_r
        
