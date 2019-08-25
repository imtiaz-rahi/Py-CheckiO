def largest_histogram(histogram):
    length = len(histogram)
    if length == 1:
        return max(histogram)
    # if length >= maxx: return length * minn
    result = [length * min(histogram)]

    # peg = histogram[0]
    # squares = 1
    # for i, val in enumerate(histogram):
    #     if val < peg:
    #         peg = val
    #         result.append(squares)
    #     squares = peg * (i+1)
    # print(result)
    return max(result)


if __name__ == "__main__":
    # assert largest_histogram([5]) == 5, "one is always the biggest"
    # assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    # assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    # assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    # assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))
    # print("Done! Go check it!")
