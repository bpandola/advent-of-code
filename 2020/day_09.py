

def is_valid(number, preamble):

    for i in range(len(preamble)):
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == number:
                return True
    return False

nums = [int(line) for line in open('day_09.in').read().split('\n')]

preamble = []
preamble_length = 25
secret_num = 0
for index in range(preamble_length, len(nums)):
    preamble = nums[index-preamble_length:index]
    if not is_valid(nums[index], preamble):
        print(nums[index])
        secret_num = nums[index]
        break

window = []
w_l, w_h = 0, 1
win_sum = 0
while win_sum != secret_num:

    window = nums[w_l:w_h]
    win_sum = sum(window)
    if win_sum == secret_num:
        print(min(window))
        print(max(window))
        print(min(window) + max(window))
        break
    if win_sum > secret_num:
        w_l += 1
        continue
    if win_sum < secret_num:
        w_h+=1
        continue
print(window)


