# square root approximation
def babylonian_sqrt(num, tolerance=1e-7):
    guess = num / 2
    while (guess * guess - num) > tolerance:
        guess = (guess + num / guess) / 2
    return guess

label1 = 'original numbers'
nums = [1,4,9,16,25,169,225]
print(f'{label1:20}\t',end=' ')
for num in nums:
    print(f'{num:4.2f}', end='\t')
print()

label2 = 'babylonian sqrt'
print(f'{label2:20}\t',end=' ')
for num in nums:
    print(f'{babylonian_sqrt(num):4.2f}', end='\t')
print()

label3 = 'built-in sqrt'
print(f'{label3:20}\t',end=' ')
for num in nums:
    print(f'{num ** 0.5:4.2f}', end='\t')