import life
import time

cs = life.Cells()

while not cs.is_dead():
    print(cs)
    cs.next()
    time.sleep(1)

print(cs.init_cells, cs.cycles)    

