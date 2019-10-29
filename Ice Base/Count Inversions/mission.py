def count_inversion(nums):
    nums = list(nums)
    count = 0
    while nums != sorted(nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return count


if __name__ == '__main__':
    print(count_inversion([1, 2, 5, 3, 4, 7, 6]));
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
