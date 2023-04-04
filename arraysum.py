#Giving a list of numbers, find 2 numbers that added will equal to a target number

def arraySum(nums, target):
    #i for index on all numbers in the length list
    for i in range(len(nums)):
        #j for index of numbers in the list starting at the second index(1)
        for j in range(i+1, len(nums)):
            #verify if the number at the index i + the number at index j = the target number
            if nums[i] + nums[j] == target:
                print(nums[i], "+", nums[j], "=", target)

array1 = [2,3,4,4,5]
sums = 8
array1.sort()
arraySum(array1, sums)
