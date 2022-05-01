'''
Qn: 
- Calculate the horizontal position and depth you would have after following the planned course. 
    What do you get if you multiply your final horizontal position by your final depth?
- Using this new interpretation of the commands, calculate the horizontal position and 
    depth you would have after following the planned course. 
    What do you get if you multiply your final horizontal position by your final depth?
Link: https://adventofcode.com/2021/day/2
ans: 188290, 1971232560
'''
def main():
    with open('input.txt') as f:
        data = f.readlines()

    lookup = {
            'down': 1,
            'up': -1,
            }
    hor = dep = 0

    for co in data:
        direction, value = co.split()
        value = int(value)
        if direction == 'forward':
            hor += value
            continue
        dep += lookup[direction] * value
    print('Part 1:', hor * dep)

    aim = hor = dep = 0
    for co in data:
        direction, value = co.split()
        value = int(value)

        if direction == 'forward':
            hor += value
            dep += aim * value
            continue
        aim += lookup[direction] * value
    print('Part 2', hor * dep)

if __name__ == '__main__':
    main()
