SIZE = 20

M = {(SIZE, SIZE): 1}
def path(x, y):
    if not (x, y) in M:
        print('path', (x, y))
        right = path(x + 1, y) if x < SIZE else 0
        down  = path(x, y + 1) if y < SIZE else 0
        M[(x, y)] = right + down
    return M[(x, y)]

print(path(0, 0))