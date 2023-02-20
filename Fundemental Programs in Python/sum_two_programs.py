#Python program for two sum problem
#Given a list of numbers, we have to find two numbers whose sum is equal to the given target

def twoSum(num_arr, pair_sum):
    for i in range(len(num_arr) - 1):
        for j in range(i + 1, len(num_arr)):
            if num_arr[i] + num_arr[j] == pair_sum:
                print("Pair with sum", pair_sum,"is: ", num_arr[i],",",num_arr[j])
num_arr = [3, 5, 2, 4, 8, 1]
pair_sum = 5
twoSum(num_arr, pair_sum)