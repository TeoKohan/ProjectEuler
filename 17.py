U = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
N = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
T = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def written_form(i):
    if i < 10:
        return U[i]
    elif i < 20:
        return N[i]
    elif i < 100:
        return T[i//10] + ('-' + U[i%10] if i%10 != 0 else '')
    else:
        return U[i//100] + ' ' + 'hundred' + (' and ' + written_form(i%100) if i%100 != 0 else '')

def letters(s):
    return sum([1 for c in s if c.isalpha()])

result = 0
for i in range(1, 1000):
    result += letters(written_form(i))
result += letters('one thousand')
print(result)