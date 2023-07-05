from math import factorial

def ith_permutation(i: int, digits: list):
    permutations_per_starting_digit = factorial(len(digits)-1)
    cycles = i // permutations_per_starting_digit
    starting_digit = digits[cycles]
    digits.remove(starting_digit)
    i -= cycles * permutations_per_starting_digit
    if digits == []:
        return [starting_digit]
    else:
        return [starting_digit] + ith_permutation(i, digits)

number = ith_permutation(999999, list(range(10)))
number = map(str, number)
number = int(''.join(number))
print(number)