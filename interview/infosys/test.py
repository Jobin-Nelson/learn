def main(input: list[list[int]]) -> list[list[int]]:
    return list(map(list, zip(*input)))


if __name__ == "__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(main(input))
