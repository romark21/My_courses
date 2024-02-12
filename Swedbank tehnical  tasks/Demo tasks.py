# """
# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [?1, ?3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [?1,000,000..1,000,000].
# """

def solution(A):
    nums = []
    for i in A:
        if min(A) and max(A) < 0:
            n = 1
        elif i + 1 not in A:
            nums.append(i + 1)
            n = min(nums)

    return n


a = [7, 2, 3, 4, 6, 6]
print(solution(a))
