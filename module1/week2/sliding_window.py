# sliding window

def sliding_window(nums, k):
    """
    Returns a list of maximum values in each sliding window of size k.

    Args:
        nums: A list of numbers.
        k: The size of the sliding window.

    Returns:
        A list of maximum values in each sliding window.
    """

    if k < 1:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i + k]
        result.append(max(window))

    return result

#testing

nums = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 2
result = sliding_window(nums, k)
print(result)