def generate_triangular_numbers(limit):
    res = []
    for i in __import__('itertools').count(1, 1):
        res.append(int(i * (i + 1) / 2))
        if res[-1] >= limit: break
    return res


def checkio(number):
    t_nums = generate_triangular_numbers(number)

    for i in range(len(t_nums)):
        (t_sum, result, counter) = (0, [], i)
        while counter < len(t_nums):
            result.append(t_nums[counter])
            t_sum += t_nums[counter]
            if t_sum == number: return result
            # No need to continue loop when current sum is greater than number
            if t_sum > number: break
            counter += 1

    return []


if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
