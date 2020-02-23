#!/usr/bin/python3

nums = []


for num in range(1,1000):
    if num%3==0 or num%5 == 0:
        nums.append(num)
        #print(num)

print(sum(nums))
