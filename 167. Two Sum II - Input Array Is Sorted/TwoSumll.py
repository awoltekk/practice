class Solution(object):
    def twoSum(self, numbers, target):
        hash = set()   
        for i in range(len(numbers)):
            if numbers[i] not in hash and numbers[i+1:].count(target - numbers[i]) > 0:
                return [i+1,  i+2+numbers[i+1:].index(target-numbers[i])]
            else:
                hash.add(numbers[i])
        
