"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def findpair(lst,k):
    for i in range(0, len(lst)):
        lst2=lst.copy()
        lst2.pop(i)
        for j in range(0, len(lst2)):
            if k ==lst[i]+lst2[j]:
                return True
    return False

#using dictonaries
# def findpair(lst,k):
#     num_dict= dict(zip(lst,lst))
#     for x in num_dict:
#         remainder = k-num_dict[x]
#         if remainder in num_dict and remainder!=num_dict[x]: # check remainder in the dict keys; remainder should not be same number as value
#             return True
#     return False

num = [10,15,3,7]
k=18
print(findpair(num,k))



"""
Note: https://www.programiz.com/python-programming/methods/list/copy

A list can be copied using the = operator. 
The problem with copying lists in this way is that if you modify new_list, old_list is also modified.
However, if you need the original list unchanged when the new list is modified, you can use the copy() method.
"""