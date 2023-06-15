sum_squares = sum([i*i for i in range(1, 101)])
square_sums = (100 * 101 // 2)**2
print(square_sums - sum_squares)