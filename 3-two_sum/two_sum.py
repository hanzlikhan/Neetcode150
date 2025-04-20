# By using nested loop and By Brute Force approach 
# def two_sum(self, arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1 , len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i,j]
            

# By using hashmap and checking values like  target - arr[i] and check that answer from the hashmap

def two_sum(self, arr, target):
    seen = {}
    for i,num in enumerate(arr):
        comp = target - num
        if comp in seen:
            return [seen[comp],i]
        seen[num] = i