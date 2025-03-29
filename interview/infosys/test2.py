def main(input: list[list[int]]) -> list[list[int]]:
    res = [input[0]]

    for cur_start, cur_end in input[1:]:
        prev_end = res[-1][1]
        if prev_end >= cur_start:
            res[-1][1] = cur_end
        else:
            res.append([cur_start, cur_end])

    return res


if __name__ == "__main__":
    input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    output = [[1, 6], [8, 10], [15, 18]]
    print(main(input))
