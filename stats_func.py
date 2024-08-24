# takes in a list of numbers
# calculates:
# -mean
# -median
# -mode
# -variance
# -std dev
# no libraries

# square root approximation
def babylonian_sqrt(num, tolerance=1e-7):
    guess = num / 2
    while (guess * guess - num) > tolerance:
        guess = (guess + num / guess) / 2
    return guess

nums = []
total = 0 # sum of all numbers

# collect input list of numbers and sum them as user inputs
element = input('Input a list of numbers by typing a single number and hitting the [ENTER] key.'
                    '\nWhen finished type \'x\' or any non-numerical character.\nBegin input: ')
while True:
    try:
        nums.append(float(element))
        total += nums[-1]
        element = input()
    except ValueError:
        print("Thanks\n\nHere is your data summary:")
        break

nums.sort() # O(nlogn)
length = len(nums)

# print data summary
if length != 0:

    # calculate mean
    mean = total/length
    print(f'Mean = {mean:.2f}')

    # calculate median
    if length % 2 == 0:
        median = (nums[length//2] + nums[length//2 - 1]) / 2
    else:
        median = nums[length//2]
    print(f'Median = {median:.2f}')

    # calculate mode
    mode = nums[0]
    most = 1
    count = [nums[0], 1] # first element represents current number and second element represents current frequency
    for n in range(1, length):
        if nums[n] == nums[n - 1]:
            count[1] += 1
        else:
            if count[1] > most:
                most = count[1]
                mode = nums[n-1]
            count[0] = nums[n]
            count[1] = 1
    if count[1] > most:
        most = count[1]
        mode = nums[n - 1]
    print(f'Mode = {mode:.2f}')

    # calculate variance
    variance = 0
    for n in nums:
        variance += (mean - n) ** 2
    variance /= length - 1
    print(f'Variance = {variance:.2f}')

    # calculate std dev
    std_dev = babylonian_sqrt(variance)
    print(f'Standard Deviation = {std_dev:.2f}')

else:
    print('No data. No Summary.\nBye')




