day11 = """
Monkey 0:
  Starting items: 75, 63
  Operation: new = old * 3
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 2

Monkey 1:
  Starting items: 65, 79, 98, 77, 56, 54, 83, 94
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 66
  Operation: new = old + 5
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 51, 89, 90
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 75, 94, 66, 90, 77, 82, 61
  Operation: new = old + 1
  Test: divisible by 17
    If true: throw to monkey 6
    If false: throw to monkey 1

Monkey 5:
  Starting items: 53, 76, 59, 92, 95
  Operation: new = old + 2
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 6:
  Starting items: 81, 61, 75, 89, 70, 92
  Operation: new = old * old
  Test: divisible by 3
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 7:
  Starting items: 81, 86, 62, 87
  Operation: new = old + 8
  Test: divisible by 13
    If true: throw to monkey 3
    If false: throw to monkey 5
"""

day10 = """
addx 2
addx 3
noop
noop
addx 1
addx 5
addx -1
addx 5
addx 1
noop
noop
addx 4
noop
noop
addx 5
addx -5
addx 6
addx 3
addx 1
addx 5
addx 1
noop
addx -38
addx 41
addx -22
addx -14
addx 7
noop
noop
addx 3
addx -2
addx 2
noop
addx 17
addx -12
addx 5
addx 2
addx -16
addx 17
addx 2
addx 5
addx 2
addx -30
noop
addx -6
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx -12
addx 17
noop
noop
noop
noop
addx 5
addx 10
addx -9
addx 2
addx 5
addx 2
addx -5
addx 6
addx 4
noop
noop
addx -37
noop
noop
addx 17
addx -12
addx 30
addx -23
addx 2
noop
addx 3
addx -17
addx 22
noop
noop
noop
addx 5
noop
addx -10
addx 11
addx 4
noop
addx 5
addx -2
noop
addx -6
addx -29
addx 37
addx -30
addx 27
addx -2
addx -22
noop
addx 3
addx 2
noop
addx 7
addx -2
addx 2
addx 5
addx -5
addx 6
addx 2
addx 2
addx 5
addx -25
noop
addx -10
noop
addx 1
noop
addx 2
noop
noop
noop
noop
addx 7
addx 1
addx 4
addx 1
noop
addx 2
noop
addx 3
addx 5
addx -1
noop
addx 3
addx 5
addx 2
addx 1
noop
noop
noop
noop
"""

day9 = """
D 2
U 2
L 2
R 1
L 1
U 1
L 2
D 1
L 2
D 1
L 2
D 2
L 1
R 2
U 1
R 1
U 2
R 1
U 2
D 1
L 2
U 1
D 1
L 1
D 1
U 1
R 2
D 2
L 1
R 1
L 2
D 1
R 2
D 1
U 2
D 2
R 2
L 2
U 2
R 2
L 1
D 1
R 1
U 1
R 2
L 1
D 1
R 1
L 2
D 2
U 1
L 1
R 1
U 1
L 2
D 2
L 2
U 1
L 2
R 1
L 1
R 1
D 1
R 2
D 1
R 1
D 1
U 1
L 1
R 1
L 1
R 1
D 2
L 1
D 2
R 1
D 1
U 2
R 2
U 2
L 1
U 1
R 1
L 2
D 2
R 1
U 1
L 1
U 2
L 1
D 2
R 1
U 1
R 1
U 2
R 1
U 2
L 1
R 1
U 2
R 2
U 1
L 2
R 1
L 2
U 2
L 2
U 2
R 2
D 1
U 2
L 2
D 3
U 1
L 1
R 1
D 3
U 1
L 3
R 1
U 1
R 3
D 2
U 1
R 2
L 2
U 1
D 1
U 1
D 1
L 2
U 2
R 3
D 2
L 2
D 2
U 3
D 3
U 2
L 1
U 2
R 3
D 2
R 2
D 1
U 3
L 3
D 1
U 3
R 3
D 1
L 1
D 3
U 3
D 1
U 2
R 1
D 2
U 3
D 1
R 2
D 3
L 3
R 1
D 3
L 2
D 3
U 3
R 1
U 3
L 2
U 2
L 2
D 3
L 3
U 2
R 2
L 3
R 2
U 3
R 3
L 1
U 3
D 3
L 2
D 2
U 2
D 3
L 3
D 2
L 1
U 3
D 2
R 3
L 3
R 1
U 1
D 1
R 2
L 3
U 2
D 1
R 3
L 1
R 1
L 2
R 1
U 3
R 2
U 1
L 1
R 3
D 3
U 2
R 2
D 1
R 3
D 2
L 3
R 1
U 3
R 2
U 4
L 2
D 1
U 1
R 4
U 2
R 2
U 3
R 1
L 3
U 3
R 3
U 4
R 4
D 1
U 2
R 1
L 1
R 2
U 4
L 1
U 2
L 1
R 3
L 2
D 4
R 4
D 3
R 4
U 1
D 4
R 2
D 1
R 4
U 3
R 4
L 1
U 4
D 2
L 1
D 3
L 1
R 2
L 2
D 4
U 3
D 1
L 3
D 3
U 3
L 4
R 3
U 1
R 2
D 1
U 4
D 4
R 4
U 2
R 4
L 4
D 2
L 4
D 2
U 3
D 2
U 4
R 1
U 1
L 1
U 1
L 1
D 3
U 4
L 3
U 1
L 4
R 4
L 3
R 2
U 2
L 3
D 2
U 1
D 1
U 4
R 2
L 2
D 1
L 4
D 3
U 3
L 2
U 4
R 4
L 2
R 3
L 1
D 4
U 1
L 2
D 4
L 2
D 3
U 4
R 4
U 2
R 2
U 4
D 3
U 3
L 4
D 2
R 1
U 4
R 1
U 1
D 3
U 1
L 5
U 5
R 2
D 3
U 5
D 5
U 1
D 2
L 2
U 5
L 1
R 5
L 1
D 5
L 4
D 4
R 4
L 1
R 1
U 1
R 4
U 2
R 5
L 4
R 3
U 4
R 2
U 4
L 4
U 3
L 3
U 1
L 4
R 1
U 3
R 3
L 5
U 5
L 4
D 1
L 2
U 1
D 2
L 1
U 5
D 4
U 1
R 2
D 2
U 5
R 5
U 1
L 3
U 5
L 4
R 3
U 4
L 2
R 4
D 2
L 2
R 4
U 2
D 4
R 3
D 4
U 1
L 3
R 4
L 3
U 1
R 2
U 3
L 3
D 2
U 4
R 1
L 3
D 4
L 1
R 1
D 5
R 1
U 2
D 1
U 4
L 2
U 2
R 4
U 3
R 3
D 2
R 5
D 2
U 5
D 5
U 2
D 1
R 5
U 3
L 3
U 1
R 5
L 4
D 6
L 1
U 2
D 4
U 6
D 6
R 1
U 3
L 5
R 5
U 2
R 2
L 5
D 4
L 3
R 1
U 4
D 3
L 2
D 5
L 3
R 3
D 2
L 1
U 5
L 5
D 6
U 3
R 5
L 5
U 2
L 3
U 5
D 6
R 4
L 5
U 6
L 2
R 1
L 1
U 5
D 3
U 2
R 1
U 2
R 2
D 5
R 1
D 5
R 5
U 2
L 3
R 1
U 5
D 5
R 2
L 5
D 6
L 1
U 1
D 6
U 4
D 5
L 5
D 3
L 4
D 1
L 4
D 6
R 5
D 6
U 6
D 2
L 3
D 3
R 5
U 6
D 2
U 4
L 1
U 6
L 2
U 4
D 6
R 1
D 1
U 2
L 3
D 3
R 2
L 6
U 3
D 5
U 3
L 4
U 5
L 5
U 6
L 3
R 1
U 3
R 1
U 4
L 4
D 5
L 6
R 1
L 3
D 4
L 3
R 1
L 4
R 3
D 3
L 1
U 4
D 2
U 5
L 3
D 6
U 2
R 3
D 5
L 1
D 1
L 3
U 2
R 3
L 3
U 7
R 2
D 1
L 3
R 4
D 2
R 5
L 1
D 5
L 2
R 2
U 7
L 7
D 2
L 7
D 5
U 2
L 2
U 2
D 4
U 1
D 4
L 1
D 2
R 5
D 3
L 2
U 4
R 7
D 4
R 3
U 2
R 4
L 1
U 4
L 4
U 7
R 1
L 6
D 5
R 5
L 1
R 4
L 1
U 3
L 7
R 7
D 4
L 3
R 3
D 1
U 7
R 3
D 2
U 4
D 2
R 3
D 1
R 3
D 3
U 1
R 6
L 2
D 2
U 4
D 5
L 7
R 1
L 7
U 6
D 2
R 3
D 5
U 1
L 7
D 6
U 3
D 6
L 1
R 2
L 6
D 7
R 5
U 1
L 7
U 2
D 2
L 5
R 7
D 4
U 3
R 7
L 4
U 8
D 8
R 2
U 2
R 7
U 1
D 7
R 1
L 7
R 7
L 8
D 3
R 5
L 4
D 3
L 6
R 6
D 6
L 3
D 5
R 1
U 5
D 7
R 8
U 3
D 5
U 8
L 8
R 6
D 8
U 5
R 1
D 1
R 5
U 2
R 8
D 7
L 3
D 3
U 7
D 3
U 7
R 7
L 4
D 7
U 2
L 3
U 7
L 1
D 3
L 1
R 4
D 8
L 5
U 5
D 3
L 5
D 6
L 1
R 5
U 4
R 4
D 1
R 6
L 1
D 7
R 4
L 2
R 3
U 4
L 8
D 1
R 6
L 6
R 8
D 8
U 4
R 1
D 2
R 5
D 1
U 8
L 5
D 5
U 5
R 8
L 6
R 4
U 1
R 5
U 8
D 1
U 1
D 5
L 7
R 6
L 3
R 1
U 2
L 6
R 5
D 4
R 6
D 4
R 2
L 7
R 8
L 6
D 2
L 8
U 4
R 4
U 3
D 8
U 8
L 8
D 5
R 2
D 5
U 7
L 9
R 8
U 9
R 9
U 6
L 6
D 1
U 3
L 1
D 7
R 6
L 6
D 7
U 1
R 9
D 7
U 8
R 6
U 1
D 5
U 5
D 1
L 1
D 9
U 1
R 6
U 9
R 6
U 6
D 7
R 1
L 1
D 8
L 3
D 7
U 8
L 7
D 2
U 6
D 4
L 8
U 3
D 1
U 6
D 3
R 8
L 9
R 3
L 6
U 9
D 9
L 3
U 1
D 2
R 4
L 5
R 2
U 3
D 5
R 5
L 4
U 3
L 7
U 5
D 9
U 6
R 5
D 3
U 8
L 6
D 5
R 9
U 8
L 5
D 1
R 8
L 4
R 2
L 3
R 9
D 9
R 7
D 5
R 6
U 2
D 4
L 8
D 2
L 1
D 2
U 3
L 2
R 3
D 9
U 3
R 4
D 1
L 8
R 3
U 4
L 4
R 3
L 5
D 4
R 2
D 4
R 4
U 4
R 7
L 6
R 9
D 1
R 8
L 5
U 4
D 10
L 6
D 3
R 2
U 1
D 5
R 2
U 6
L 9
U 7
L 10
U 4
L 8
D 3
U 7
D 7
U 9
L 2
R 6
U 4
R 9
L 5
U 3
L 4
R 1
D 8
U 10
D 10
R 3
U 3
D 2
L 5
U 3
D 4
U 1
R 9
L 3
D 8
L 5
U 8
R 3
U 10
L 10
R 4
D 5
U 9
R 8
L 5
U 9
L 6
U 10
D 8
U 2
L 8
D 7
U 2
D 5
U 8
L 2
D 3
U 8
R 8
D 10
R 3
L 3
U 4
R 3
U 4
L 6
U 4
R 3
D 9
L 9
U 5
D 1
R 3
D 2
L 9
U 9
R 9
U 6
R 7
L 8
U 2
L 4
D 10
L 4
D 9
L 9
R 10
L 3
R 7
U 2
L 3
R 1
D 4
L 2
R 10
D 5
L 2
D 2
L 4
U 6
D 9
R 6
U 9
D 4
L 6
U 8
D 1
R 1
L 10
U 4
R 6
U 11
R 8
U 1
D 5
R 7
D 8
L 5
R 6
U 5
R 1
U 7
L 4
D 6
U 8
R 10
D 1
L 8
R 3
U 7
R 2
U 9
D 9
R 9
L 3
R 4
U 10
L 7
R 1
L 5
D 11
R 4
U 10
R 10
L 3
D 2
L 4
U 9
L 1
D 10
L 7
R 11
D 5
U 3
D 10
U 5
L 2
R 9
D 10
U 1
R 10
U 1
L 11
R 10
L 8
D 10
L 5
R 2
L 3
U 4
L 10
R 3
D 5
R 8
L 2
U 1
D 7
U 7
L 1
U 11
D 2
L 2
D 11
L 6
R 9
U 10
R 7
L 11
R 7
D 1
R 3
U 6
R 7
D 8
U 3
L 1
D 11
U 7
R 1
L 7
R 2
L 7
D 3
U 10
D 9
U 10
R 5
D 4
U 7
L 11
U 1
L 12
R 10
U 7
R 3
L 2
U 11
R 6
U 8
D 2
R 2
L 8
U 7
D 10
U 3
D 1
U 8
R 2
D 9
L 8
R 10
L 1
U 8
R 11
U 8
R 12
D 10
L 5
U 6
L 11
D 12
L 5
U 4
L 8
U 11
D 2
U 4
L 6
R 1
L 4
U 2
L 5
R 2
D 7
L 12
R 4
L 1
D 7
L 11
U 3
D 9
R 12
U 10
D 9
U 10
L 6
R 6
D 10
R 10
D 5
U 9
R 2
D 4
L 9
U 2
R 5
L 8
R 1
D 9
L 7
D 11
R 3
L 8
U 3
D 7
U 3
R 8
U 7
L 1
U 10
D 8
R 11
U 10
D 11
U 8
R 12
U 9
D 12
U 4
D 11
R 8
D 1
L 4
R 9
L 7
U 8
R 6
D 5
R 8
D 2
R 6
L 4
D 7
L 3
U 11
R 2
L 10
D 13
R 2
D 10
U 9
D 5
U 5
D 5
L 11
U 3
R 5
U 7
L 6
D 4
L 3
R 2
D 9
U 7
D 9
U 1
D 8
L 11
D 7
U 7
R 3
L 6
D 6
R 5
L 6
R 3
U 10
L 13
U 9
R 11
L 13
R 9
D 3
U 3
L 12
U 4
L 3
D 12
R 13
D 7
U 6
L 11
U 4
L 2
D 7
L 8
R 10
U 13
R 9
U 8
R 11
U 8
R 7
U 11
L 8
D 3
L 4
U 6
D 12
R 13
U 10
L 4
R 12
U 13
L 11
R 10
L 8
U 6
L 1
D 11
U 12
L 8
U 2
L 6
U 2
L 1
U 3
D 5
U 2
D 10
U 11
L 9
D 9
R 7
L 3
U 3
D 2
U 2
R 10
D 1
R 5
L 1
D 3
R 8
U 4
R 1
D 13
L 12
U 1
D 13
R 4
D 3
R 8
D 2
U 3
D 8
L 3
U 9
R 4
D 8
U 9
D 3
L 8
D 11
L 8
U 1
D 13
U 14
D 10
U 9
R 4
D 14
L 10
D 10
U 6
D 7
R 8
U 5
L 8
R 9
D 12
L 9
D 8
R 13
L 7
U 11
R 8
D 5
U 14
D 5
U 9
L 7
D 12
R 2
L 14
U 1
R 9
U 10
R 4
U 4
R 14
D 10
L 3
R 4
L 13
U 3
R 6
L 2
U 6
R 2
D 10
U 4
L 10
U 8
L 6
D 2
R 1
D 5
U 14
L 4
D 5
L 5
U 10
D 5
R 13
D 14
U 14
R 4
D 13
U 10
R 13
D 12
R 10
L 12
U 8
D 10
U 12
D 5
L 11
D 13
R 8
D 10
R 13
L 13
D 1
U 10
L 4
U 14
D 12
U 4
D 5
R 10
L 8
R 13
D 13
U 5
D 4
L 1
D 9
L 14
U 14
R 3
U 6
R 14
L 4
R 7
D 3
R 8
D 5
L 2
U 5
D 8
U 3
R 7
D 13
U 14
R 11
U 6
L 15
R 4
U 12
R 1
L 8
U 15
R 5
L 2
D 1
R 12
D 1
R 12
D 1
L 1
R 9
U 11
D 2
U 12
D 3
U 6
D 12
U 11
R 6
D 11
L 5
R 3
D 1
U 7
L 10
D 4
L 7
R 2
U 8
D 11
L 12
R 6
L 7
D 13
U 11
R 5
D 1
L 11
D 2
U 15
L 11
R 3
L 9
D 12
U 8
D 9
L 14
D 10
L 12
R 13
D 3
L 9
D 13
R 8
D 15
U 14
R 9
U 12
R 2
D 3
U 5
L 3
R 7
U 15
R 10
L 6
R 6
D 12
R 14
L 7
U 8
L 11
R 13
U 8
L 8
R 5
D 3
U 8
D 4
L 1
D 11
U 15
L 14
R 8
L 1
R 13
L 2
R 13
U 9
D 12
L 14
R 13
L 5
R 7
D 13
U 15
R 2
L 12
D 12
R 13
U 2
D 4
R 14
L 1
U 12
D 3
U 6
R 6
L 6
U 9
L 16
U 16
D 8
R 8
U 1
D 14
R 13
D 3
U 14
R 7
U 7
R 7
D 12
U 1
D 2
U 2
R 7
D 11
U 4
R 13
U 2
L 16
U 12
L 15
D 10
U 11
L 1
D 1
L 3
D 15
L 12
R 2
D 12
U 16
R 16
U 11
D 15
R 11
U 13
L 3
R 15
D 16
R 9
D 1
L 3
U 9
D 12
U 11
L 13
R 10
D 4
U 12
L 2
R 8
L 1
U 9
L 1
D 7
R 14
U 12
L 9
R 5
D 7
R 10
D 14
L 2
U 2
L 4
D 15
U 7
D 9
L 4
R 1
L 8
D 14
U 9
D 1
R 15
U 9
R 10
D 11
L 14
R 12
L 12
U 13
R 12
L 1
R 10
D 14
R 3
U 5
D 10
L 13
U 11
R 16
L 14
U 6
D 5
R 16
D 7
L 16
U 12
R 14
U 7
R 6
U 17
R 3
U 15
R 17
U 3
R 4
U 6
D 13
U 7
R 12
U 10
R 7
L 13
U 16
D 13
U 2
L 13
R 2
D 1
U 10
R 6
D 11
R 10
D 6
R 2
L 1
R 1
L 5
D 16
U 1
L 13
U 3
R 9
L 10
D 12
R 9
U 17
R 10
U 1
D 13
L 13
R 6
L 5
D 5
R 15
D 15
L 7
U 11
D 1
U 11
L 17
R 5
L 11
R 15
U 16
D 2
L 5
D 9
R 13
D 14
U 6
L 10
U 15
D 15
R 5
D 4
L 13
R 11
D 15
U 13
R 8
U 6
R 8
U 3
R 12
U 11
L 6
U 9
D 6
L 1
U 4
L 6
R 4
D 2
L 6
U 11
L 1
U 10
R 2
U 6
R 1
U 7
R 16
L 12
U 9
D 9
U 6
R 13
U 8
L 6
U 2
R 17
L 6
U 5
D 14
R 15
D 13
L 5
U 18
R 9
L 10
R 9
D 6
L 8
U 3
D 8
R 17
L 4
R 9
L 13
U 3
R 12
D 4
R 11
U 13
L 15
R 13
D 18
R 8
L 7
R 10
D 11
U 8
R 4
L 7
U 15
L 3
D 15
R 3
U 6
L 17
D 17
L 12
D 16
R 14
L 1
R 7
D 15
U 2
L 5
U 16
D 7
L 11
U 1
R 2
D 4
L 13
U 17
R 5
D 17
R 14
L 1
D 11
U 11
R 8
U 12
D 12
U 17
R 15
L 4
D 7
U 8
R 4
L 14
U 11
L 3
R 1
L 14
U 3
L 3
D 15
L 14
D 7
R 2
L 6
U 6
R 12
U 17
D 1
R 15
D 1
U 14
D 6
U 4
R 4
L 3
U 14
L 1
R 4
U 13
D 18
L 11
U 4
D 9
R 10
U 17
R 8
D 12
R 9
L 5
D 6
L 9
R 9
L 17
D 9
R 2
L 4
R 8
D 8
R 8
D 13
R 12
L 13
U 8
D 8
L 16
D 15
U 11
L 8
R 7
D 2
R 6
U 19
D 4
U 7
L 17
R 9
U 18
D 4
R 19
L 14
U 8
D 19
L 12
R 14
U 13
D 3
L 8
D 4
R 9
U 18
D 1
U 2
L 16
U 2
D 12
U 5
L 4
D 6
U 14
R 1
L 7
D 7
L 19
D 5
U 16
D 15
R 14
U 19
D 19
L 6
R 3
L 14
R 16
L 1
U 4
R 19
U 2
L 3
D 19
L 17
U 13
D 5
L 10
U 18
R 13
D 6
L 17
D 9
R 10
D 8
R 19
L 6
D 7
R 18
U 8
L 6
U 18
L 18
D 16
R 8
L 10
R 6
D 1
L 6
U 8
L 19
D 18
U 3
D 17
U 9
R 13
D 18
R 2
L 10
D 17
L 17
U 8
L 13
D 5
L 1
U 10
L 3
R 3
D 12
U 11
L 15
D 15
"""

day8 = """
200200221023111313131033314121142013103432145142351212334232423210101340410243413011333312111010010
021002023301222221234134021422342024344555521535143232341414552024224120114233210330203002020100112
120000123021210023111321143114331115334535223455511513445233523154411102203411040133312002213001021
110211312303200204232110124204135453554533435152342542252215415141133330323032234114310011301232202
112002122201001100330432244432552555524445123151222142521452233321152332132412434434431321322021220
000131233030332102140440124221314455255431113413445553414144524134315351524134030112312012102102122
011002120310213142402320144522121125454423123245535451115134412543215113433312403430132101003202030
001221312201314442411333454131552331253553254425236334643151355314514413411344034432330410221101023
133033302114012204213054544541124453214232545523665466356466451514332142121512400041213432211332332
122103100320433433403313515121232352332442555253656542336644235234542522322522414400320014312110331
220032121143103434234531224315451255225362634256634623342624242245654341134514413144333113211200033
320112113344013332224131114231235263526556625325625352254643224563365551253353323542200003301120011
130332114433413215333445212514445445656665256554333534422554442522234433415533124353022320300112030
122220320003402342433443415465352622564252264442264334335624365224645544545412124352220434440211220
012123032311134245212342233263346563632453535355553473445564362634252543555515242444423232000444220
210332422344222154315435122245243633424643346345734336333746422324336263624544151122442021330341202
122113144440445232235222443563362625543565533465377647363543377645634552632254214531354231413432430
312340402310532324322313244522226622547366756445444754767335355365264622465662241215332253310001232
203342203201331433144542522354633356376457563745333765735577477354743263423666625212251354244021004
023132211325442531332565334564256663665357767653737436565453774766335532544656254552332354313323032
104344140125552254523443534436547653753334746356364664565677777637444474643245425325454224440231203
030303323422144551254256535247737377634445575474654433333453643564664344462332353234553115322142242
043342223454513255464263333566337576377476354884845654658465735544446646436232534263314313142020101
340311214411551345423466343646644336367654787858788857666654635337366537645634644263323112331404131
040141315333331565455545334767475747755574585547567756844746644445646736447635456236413253453410130
211021153443415666656253646443465373878486485664464485545486846643475567536535465634262415153200040
434443334231526223353563373464374574547886487867474546748668788886554566336675234542522151345414431
342100553111533623655466757467553555676668887764575574556755884875687334634675256256443425223423211
421145141552463255552236436455476686566587654558577848647854485587448337355756554555544211113112433
401034232152434624233754647737667758845867866675595798957488447876578774367337742646625521543244120
201414142512656264345465456536564477766677986565767776589758477664747866666435364642236343442335143
422042442525465325256445643735574646548578959977866889666586787677748745536646677524242544332243420
101531424154626224664754337344565457557999965875599965977796778866568855445766577565632633451545144
111515354125252635577747557658555488765757696767797558565755699985844788764347763523465333315513212
222334234142233522754645544788567846579566995878775676667979868685866578655574543564453254615121150
121552233464445256557546467767485865866888757989977669966767877786686475874646454752632664243132511
412242332564644335747746348878865677677797755798669796798699855757865564547645373677564252625352445
104135225262634344357677645645458796767865979969889676688676788669777674757634454746666526341145313
021542323626266573437334685574765967759968767697666876767887775889896866845887736736426556541522241
321245255565266675757675486554868969567677786789686889669988776968557656488476534636744443443445532
424153123565322534465577464547665888797687899787966868666667897595997786576655333657432563645515114
151513345354454444763668544475487669995769769878776696968966788666679588686556634737544644543232332
315411214333624753546345646876778875556666766899787967667988799866697798768788653774352466325322155
411515135354235576553778556478657685968679689776697889878966888788686556488744645555636235464132151
521535123365535747465567756884789758877668899777979788877786896957896655744848765333672323354342345
511122245466262643344764588545559786677866787999989789989769786875585659588677463454335226643415231
234355522634365636744684556586586576767676868898988888987788888877768767654646777776645642226512141
113123464223654555566666486667798785887896678897787899778677766996769787745467865757755656543512345
513251343243554753654655574645569758987667887877878998789898989677659987488676836733553556554225344
514313564242345475335768454478576556889868687997999987778988866675979779845785867656464634654245123
114315542426623675675378664848688856798777688977789877988898769769667968885864643357435456442515251
342223563236537773664686558445968779787887987788777777899877867865678669767686535536743642245412355
125543254543547353647388564555887588899766978788778797797796898997787999888766547554567344424443422
235522554554262346774664445787579599869688998989778778978989968998575857577865454747575353226552114
222421136654623646474466478475666768686777899887878779887688896658596779765485853765563356364225314
521231534444644737467764858748655998796879877877788879799986898965697856444748453437553352232525543
451421316463534654736364878868555996777987969978898798976796968858967778666788533743354325346223354
353521254635223475773456867765596786879787787769889887896999898885688596454456655466765442452131244
112452332645434776643548885574558878789797669769989989886877966757566586444578445673434665652431423
125112515242255354574555588568695879785886989867778677698879979576678878668587547744623644323213555
222335123454333544773645644774469985799577787667779799699876685666756857858446357667422332624342332
342124352633564466565447655564575889567797869876686996679999868665879886844677564455723264641334552
211531121363532576364535865484865759689798698998996686966767965765789787447464533667726322444223531
003112555432534436636776465475555776887557956877687879969697585659596546865447775565562326263355343
433244413454525566563634447454784577659787856568996976596789778896764874668454673456462646455545115
315114535444536635475346535567864558579958679557799758766667597987857466754537555645552424625323424
041544243435426366744535764674465545875655656695956899997569789788477547755346553676234364525135211
110125213453624243247556736654454474595787967599557857997699578855767558775435554762633446551353134
230513132216566245267463366654684755868756978975659588575959655686655788733345435522656542222543322
042134352115436525535436657767864645756586865777685969969787676584458468744346376522324323225232212
113011555414226244554676353335845564485568555689599656977797776777868787473376444245355443123441231
141222553351554636564756467565656675455484874698998587887767666457458846465776554544333612224555323
410201213345143434422573347343756574748746464486554485756685477655667634334766422236535313341542224
400013155121116452255553534765374544884448574876457458645878446585657476536357256436654223345343132
142320132432156443246333547553474375466866456765867768748787675644755677446563663223424341524352200
130310433221343524424456477364543647448885475465487864674454548867635637545422424333245424354220221
104443025533452125362252625375463664447488646447874885476567646456653665465543643663511122334514003
302020415314212533664642446555554345445458887778858887685645576353536647674424342553325334543032421
241431045353353251642363462546445336355737566757557674865573447644353353564422462552323432524142311
123213233322144323666345645436644754537635574357377674465747755476333656624223243445125521412332331
012331042212144212425325652566536457633744775665435737646677453634637335562564643341411132411032042
312330023343231454516256365325363757435647543374644573757667446466553456424326532235455225410011222
330440423204155515131264636336326536353437335474474464535536754457526344465446535213522513202431334
111010303340451214252454445262262654354536464545434674354557674362552463364322545323344220103312142
011012340310414525221212256242445654336566374374366636534765356655652454533664444453134140113204011
230024312112245355233251252646423364546365646735756334573543653656365434363633141223321213032042131
031001023032240425233144214253446244556226622634747362226456645266342264223215113131540112130410110
322123043034044225552242443355356433432465646225242242422346453346634325254325435535313321413201023
022331002231110112224233354325624225342363424426633436565344545533465463152555421312331102120410200
013020314334233240543141441351342432435423252532545655664253435662546145412112135314414140233322202
023101011114024240134343343214355543453244325544366633232356362353335431215322232434231302030012200
121203223241323132430512521115213312263253263242264335335446352453314333354413113210133333212120303
102030123234100043232214342352345452215246465634534464364425653323345231332311444434220444330131120
000331303323044244144032522114521112125142214553424464423124453113211413324230342333130021200000221
121203123313224230334312325441234431451535345453515132125413445443323514321330302200100022013232311
000221331111234212331404233225332533323225131525322111443344452254442544201223424140243032213101301
010202021330012103042021024434411545123253214353525251521434235541535344240243403200122322133122101
121102231211003113342040440404003344542241345133131133414435235243325441120032344431223311313111221
011210032333020312123124101444102341443212553521355222414135533333310320012002223342012031112321112
"""

day7 = """
$ cd /
$ ls
dir ddpgzpc
dir mqjrd
dir mrqjg
dir rglgbsq
298050 tjmjp.cqm
dir wlqhpwqv
$ cd ddpgzpc
$ ls
290515 cvrd.hcf
dir mlm
122034 rrtnthnt.zgs
12680 tvnrl
49534 vljqzqg
dir zffbmlbd
18557 zfhnw.jfd
$ cd mlm
$ ls
102897 zfhnw.zpd
$ cd ..
$ cd zffbmlbd
$ ls
dir bqpwdh
dir gqrlmdhs
315267 mjm.dhc
294364 mrqdw.npr
dir szqz
76621 tvnrl
285948 vpdbrh
155914 vwl.vsq
dir zfhnw
$ cd bqpwdh
$ ls
dir bhmw
27669 dtzw
dir lfhgjw
dir pjqwq
$ cd bhmw
$ ls
190433 zbcbr
$ cd ..
$ cd lfhgjw
$ ls
dir ndrcgmd
$ cd ndrcgmd
$ ls
98160 mjm.dhc
$ cd ..
$ cd ..
$ cd pjqwq
$ ls
50937 dtzw
186171 mjm.dhc
305433 mlm
272969 mlm.rhf
$ cd ..
$ cd ..
$ cd gqrlmdhs
$ ls
dir blc
331077 dcchtmp
dir mlm
199021 rlzjl
253162 vghhgvjq
dir zfhnw
$ cd blc
$ ls
53872 drjdcqw.szd
115417 ggh.qsl
65105 pjqwq
$ cd ..
$ cd mlm
$ ls
dir bqpwdh
200734 gjhzr.ffz
277561 lwnl.jsl
dir sdjnlsf
dir trqhm
140014 tvnrl
$ cd bqpwdh
$ ls
dir jzfgz
$ cd jzfgz
$ ls
334790 dtzw
$ cd ..
$ cd ..
$ cd sdjnlsf
$ ls
326446 mjm.dhc
dir vpdbrh
$ cd vpdbrh
$ ls
20883 bwjjdszc
10518 dtzw
64779 ppmwtlj.btf
320555 rpf.tmw
295126 vwl.vsq
$ cd ..
$ cd ..
$ cd trqhm
$ ls
184138 rmnmsl
$ cd ..
$ cd ..
$ cd zfhnw
$ ls
dir pjqwq
$ cd pjqwq
$ ls
dir qjzscp
$ cd qjzscp
$ ls
299311 tvnrl
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd szqz
$ ls
dir bqpwdh
107678 jmqq
109752 vtmgq.bcz
301721 zjdlztw
dir zwvzzz
$ cd bqpwdh
$ ls
dir mlm
$ cd mlm
$ ls
178616 mlm.rnn
$ cd ..
$ cd ..
$ cd zwvzzz
$ ls
135690 rrbv.ntn
$ cd ..
$ cd ..
$ cd zfhnw
$ ls
dir dtgnbb
55267 dtzw
119612 mjm.dhc
$ cd dtgnbb
$ ls
74360 zjq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd mqjrd
$ ls
dir ccnpn
176761 rmnmsl
$ cd ccnpn
$ ls
116424 pjqwq.ctj
$ cd ..
$ cd ..
$ cd mrqjg
$ ls
dir bsphvqnh
266338 lwfdlqzq.wmj
287488 mjm.dhc
211569 mlm.mbn
231144 vpdbrh
260476 vtqjh.wfj
$ cd bsphvqnh
$ ls
101783 pscn.zdh
$ cd ..
$ cd ..
$ cd rglgbsq
$ ls
dir bqpwdh
dir fdmhnzw
dir fgz
213313 hbj.lgh
dir lftcr
dir pjqwq
1614 rmnmsl
dir rpz
dir vpcq
dir zfhnw
$ cd bqpwdh
$ ls
35649 mjm.dhc
53750 nqdlf.trh
102195 vpdbrh.lbn
$ cd ..
$ cd fdmhnzw
$ ls
222384 dtzw
$ cd ..
$ cd fgz
$ ls
dir rzrsgst
dir tqdghbj
$ cd rzrsgst
$ ls
120970 dtzw
dir zfhnw
$ cd zfhnw
$ ls
154286 fmbzztww.hvt
$ cd ..
$ cd ..
$ cd tqdghbj
$ ls
275314 rmblptm
$ cd ..
$ cd ..
$ cd lftcr
$ ls
148378 cwjj.trb
215545 zfhnw.fjl
$ cd ..
$ cd pjqwq
$ ls
dir bppdtc
dir dnlzz
$ cd bppdtc
$ ls
276258 zfhnw.rfn
$ cd ..
$ cd dnlzz
$ ls
286311 cjzm.nhs
239107 ggdr.rgz
dir zfhnw
$ cd zfhnw
$ ls
dir rzht
$ cd rzht
$ ls
100504 thj
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rpz
$ ls
182300 brsnhb
dir pblmwf
261712 rmnmsl
dir zfhnw
$ cd pblmwf
$ ls
121117 mlm.zdq
$ cd ..
$ cd zfhnw
$ ls
281353 gwbrctf
dir hgpnj
dir lvhwhz
dir mlm
dir pcfljzhm
dir vpdbrh
$ cd hgpnj
$ ls
103619 vwl.vsq
$ cd ..
$ cd lvhwhz
$ ls
236328 bqpwdh.qtn
dir gjwth
118100 jfcmcq
dir lwsdfhg
51327 mjm.dhc
41403 mlm
dir vpdbrh
313830 zmwhlcsw
$ cd gjwth
$ ls
dir bqpwdh
128093 css
290123 pjqwq.djg
89091 whdwbssf.tss
$ cd bqpwdh
$ ls
186274 rmnmsl
$ cd ..
$ cd ..
$ cd lwsdfhg
$ ls
218938 mjm.dhc
$ cd ..
$ cd vpdbrh
$ ls
139398 lrrjnvr
$ cd ..
$ cd ..
$ cd mlm
$ ls
278462 fdlb.jsr
176936 tvnrl
29208 vwl.vsq
$ cd ..
$ cd pcfljzhm
$ ls
295983 nnvq.lcg
$ cd ..
$ cd vpdbrh
$ ls
16998 lswwmjc.vmv
52872 pmbzp.mmg
$ cd ..
$ cd ..
$ cd ..
$ cd vpcq
$ ls
dir tnrpllzj
$ cd tnrpllzj
$ ls
226232 nqrjs.qds
$ cd ..
$ cd ..
$ cd zfhnw
$ ls
188324 dtzw
263511 lnwwh
217287 lst.wvw
178366 vzctflm
$ cd ..
$ cd ..
$ cd wlqhpwqv
$ ls
dir bqpwdh
dir ffw
dir lpzgcrd
dir lszdbd
51178 mlm
dir ntcpvg
dir pjqwq
dir pmpftw
dir ppf
dir vpdbrh
dir zfhnw
$ cd bqpwdh
$ ls
194389 dnqngfzh
$ cd ..
$ cd ffw
$ ls
dir mfqd
dir npgnwwf
dir tcvt
$ cd mfqd
$ ls
214846 vwl.vsq
$ cd ..
$ cd npgnwwf
$ ls
dir ddqsmtsj
dir gcq
dir ldtpnr
1802 vwl.vsq
$ cd ddqsmtsj
$ ls
309790 rmnmsl
$ cd ..
$ cd gcq
$ ls
80203 lvqhwzfn
$ cd ..
$ cd ldtpnr
$ ls
dir spzj
123522 tvnrl
$ cd spzj
$ ls
139171 bpgpdzt.zzp
$ cd ..
$ cd ..
$ cd ..
$ cd tcvt
$ ls
dir jcvcjz
dir qmtcr
dir vpdbrh
$ cd jcvcjz
$ ls
274564 hsv.wsr
309010 vpdbrh
$ cd ..
$ cd qmtcr
$ ls
dir mfjd
dir pmbdsb
$ cd mfjd
$ ls
202111 vpdbrh
$ cd ..
$ cd pmbdsb
$ ls
dir brghd
313440 chwzrz.bmf
$ cd brghd
$ ls
216516 dtzw
$ cd ..
$ cd ..
$ cd ..
$ cd vpdbrh
$ ls
134552 sbs.bsn
$ cd ..
$ cd ..
$ cd ..
$ cd lpzgcrd
$ ls
244257 bqpwdh.hsz
118275 flgfbstp.flp
dir gcwg
dir mlm
dir nfj
189443 rtwwbgfs.nvl
dir trbwtdb
dir vpdbrh
dir ztwbpvbq
$ cd gcwg
$ ls
dir bqpwdh
304960 dtzw
9496 pfpwtsp
dir pjqwq
dir vpdbrh
dir vqp
186883 vwl.vsq
$ cd bqpwdh
$ ls
79064 fbjdqsn.cgp
$ cd ..
$ cd pjqwq
$ ls
106371 cplcj
204740 mhdq.lhc
313462 pjqwq.lsn
249876 rmnmsl
209574 vwl.vsq
$ cd ..
$ cd vpdbrh
$ ls
166549 mjm.dhc
270734 rmnmsl
$ cd ..
$ cd vqp
$ ls
dir nbq
dir nts
dir rlbhdgm
dir srvqpq
dir zfhnw
$ cd nbq
$ ls
63369 mjm.dhc
314393 smd
70181 tbwpwtt.ccj
97954 vpdbrh.fmw
$ cd ..
$ cd nts
$ ls
11300 zfhnw.pnj
$ cd ..
$ cd rlbhdgm
$ ls
dir bzd
dir hfhzj
65400 mbrqjnp.wqz
dir pztwz
$ cd bzd
$ ls
dir bqpwdh
168832 cdlg.zhp
dir dtb
22418 fttt.twt
dir gmlgvnq
101839 hnpjbjsc.whd
dir pdmqn
122491 smvjvw
dir wmtdbrqm
52142 zfhnw.gmt
$ cd bqpwdh
$ ls
dir btb
37220 gzj.mhf
dir lwl
112215 qcfqd.fwz
210303 qlwgqnsp
dir trpm
$ cd btb
$ ls
dir rqftrtb
dir vsb
$ cd rqftrtb
$ ls
dir ndwphjw
dir pjqwq
dir zfhnw
$ cd ndwphjw
$ ls
256159 lpprpwjq.srz
$ cd ..
$ cd pjqwq
$ ls
dir fpb
$ cd fpb
$ ls
42692 pjqwq
$ cd ..
$ cd ..
$ cd zfhnw
$ ls
dir bqpwdh
$ cd bqpwdh
$ ls
17467 mshfwzv.ppr
$ cd ..
$ cd ..
$ cd ..
$ cd vsb
$ ls
278554 rmnmsl
$ cd ..
$ cd ..
$ cd lwl
$ ls
28409 mjm.dhc
$ cd ..
$ cd trpm
$ ls
dir mlm
$ cd mlm
$ ls
304742 dtzw
108223 mjm.dhc
dir mvh
52532 nzc.vhj
dir tdhrrhm
$ cd mvh
$ ls
99770 cgfw.pgm
$ cd ..
$ cd tdhrrhm
$ ls
326653 lrmsnt.fdh
157903 mlm
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd dtb
$ ls
179072 vpdbrh
3435 vpdbrh.hpv
$ cd ..
$ cd gmlgvnq
$ ls
dir rrjgswsd
$ cd rrjgswsd
$ ls
dir zfhnw
$ cd zfhnw
$ ls
278562 mvqbv
$ cd ..
$ cd ..
$ cd ..
$ cd pdmqn
$ ls
233744 pjqwq
$ cd ..
$ cd wmtdbrqm
$ ls
dir lngc
dir wgpwcj
225374 wphwht.nvn
$ cd lngc
$ ls
4415 zfhnw
$ cd ..
$ cd wgpwcj
$ ls
165889 bqpwdh.ngg
331254 dlpr
97910 mzjlswr.spn
dir rqhshd
49222 vwl.vsq
$ cd rqhshd
$ ls
145902 qwhr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd hfhzj
$ ls
92623 ldlpnvw
146918 mjm.dhc
$ cd ..
$ cd pztwz
$ ls
dir jllmcfjf
$ cd jllmcfjf
$ ls
245363 dtzw
81345 mbh.vdq
164199 ntwzgfr
14466 rmnmsl
$ cd ..
$ cd ..
$ cd ..
$ cd srvqpq
$ ls
271019 zfhnw.rlc
$ cd ..
$ cd zfhnw
$ ls
104520 bqpwdh.qqv
12312 lspg
$ cd ..
$ cd ..
$ cd ..
$ cd mlm
$ ls
259906 cbgmp
dir rjshqvb
$ cd rjshqvb
$ ls
309983 mlm.qmm
$ cd ..
$ cd ..
$ cd nfj
$ ls
44759 mlm
228634 njrrs.sjj
dir rfmw
$ cd rfmw
$ ls
273185 bcbjq.vlw
$ cd ..
$ cd ..
$ cd trbwtdb
$ ls
307053 mjm.dhc
301028 zzg
$ cd ..
$ cd vpdbrh
$ ls
dir bzdp
169466 grnvt.mst
dir pjqwq
123590 vwl.vsq
$ cd bzdp
$ ls
225941 trrzqz
241249 vpdbrh.lsj
$ cd ..
$ cd pjqwq
$ ls
dir ddfpql
dir fgbqzm
329174 mjm.dhc
6701 mlm.ffp
dir phf
$ cd ddfpql
$ ls
103799 lpbp.bpt
$ cd ..
$ cd fgbqzm
$ ls
dir spsz
$ cd spsz
$ ls
34049 mfgph
$ cd ..
$ cd ..
$ cd phf
$ ls
84883 qdj.hbt
$ cd ..
$ cd ..
$ cd ..
$ cd ztwbpvbq
$ ls
138429 bqpwdh.mlr
151403 cqmbgfdh.gvh
9087 ngm
335933 sswtt
318963 tvnrl
dir wdhjpzp
$ cd wdhjpzp
$ ls
119932 pjqwq
$ cd ..
$ cd ..
$ cd ..
$ cd lszdbd
$ ls
dir cpqpvbz
dir hnl
dir llprt
$ cd cpqpvbz
$ ls
dir ltlcz
dir wmpsvm
$ cd ltlcz
$ ls
262150 zfhnw.zsg
$ cd ..
$ cd wmpsvm
$ ls
dir bqpwdh
$ cd bqpwdh
$ ls
51488 pvhcb.qmw
44038 zfhnw
$ cd ..
$ cd ..
$ cd ..
$ cd hnl
$ ls
dir pjqwq
$ cd pjqwq
$ ls
170454 mhg.ddj
$ cd ..
$ cd ..
$ cd llprt
$ ls
268114 bmvwwbdt.cqm
207425 dtzw
180660 mgqz
297846 qbpcd
112867 zdb
$ cd ..
$ cd ..
$ cd ntcpvg
$ ls
74161 bqpwdh.gbr
257792 vwl.vsq
$ cd ..
$ cd pjqwq
$ ls
279738 hwdgzvj
dir jsdbnwrc
dir pcjfjsgs
11113 rqrtcq
208212 tvnrl
dir vllzsh
$ cd jsdbnwrc
$ ls
11720 fvj
$ cd ..
$ cd pcjfjsgs
$ ls
dir bqpwdh
195046 mjm.dhc
dir ssq
dir vpdbrh
$ cd bqpwdh
$ ls
42769 dlrvsj
159280 zfhnw
239759 zqqcb
$ cd ..
$ cd ssq
$ ls
67639 bqpwdh.csb
$ cd ..
$ cd vpdbrh
$ ls
dir bqdpwrst
dir qtj
$ cd bqdpwrst
$ ls
57800 fndpnj.fgt
132712 vpdbrh
$ cd ..
$ cd qtj
$ ls
dir szjtvcb
$ cd szjtvcb
$ ls
93993 mgmqtdb.fzd
dir stbczmlq
$ cd stbczmlq
$ ls
dir nhq
$ cd nhq
$ ls
27749 hqgngdt.tmq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd vllzsh
$ ls
dir nlwwrz
237293 wlgbt
dir zhmwl
$ cd nlwwrz
$ ls
99990 bjv.szl
$ cd ..
$ cd zhmwl
$ ls
dir hbpps
dir hfv
$ cd hbpps
$ ls
7520 mlm.ltq
$ cd ..
$ cd hfv
$ ls
dir qpfrd
$ cd qpfrd
$ ls
dir mlm
$ cd mlm
$ ls
288919 qmtpwqn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pmpftw
$ ls
118859 mlm
103896 pjqwq
128800 tvnrl
$ cd ..
$ cd ppf
$ ls
dir drszpqf
dir fbs
202594 gdpw.bds
dir ldnrpg
176398 mbbmmf.plr
dir tfjnj
$ cd drszpqf
$ ls
dir pjqwq
dir qtblb
191392 tvnrl
$ cd pjqwq
$ ls
dir lrrlbgwh
dir nfcc
dir pqm
$ cd lrrlbgwh
$ ls
182434 mjm.dhc
238706 vpdbrh.lgz
$ cd ..
$ cd nfcc
$ ls
253846 vpdbrh
268229 vwl.vsq
$ cd ..
$ cd pqm
$ ls
56573 vwl.vsq
$ cd ..
$ cd ..
$ cd qtblb
$ ls
28941 zcm.dtw
52282 zmhw.lhm
$ cd ..
$ cd ..
$ cd fbs
$ ls
dir gpttw
$ cd gpttw
$ ls
dir bqpwdh
$ cd bqpwdh
$ ls
98780 wvzhlfht.rdd
$ cd ..
$ cd ..
$ cd ..
$ cd ldnrpg
$ ls
205523 bqpwdh.qlb
54924 pcq.clf
$ cd ..
$ cd tfjnj
$ ls
237752 bqpwdh.bvf
dir lwl
295520 mjm.dhc
dir qsgpsmzw
278576 rmnmsl
dir vljqlw
225025 vwl.vsq
100780 zgjhtrv
$ cd lwl
$ ls
150713 dhrl
$ cd ..
$ cd qsgpsmzw
$ ls
265288 bqpwdh
92636 ntgrlr
182224 wdb
$ cd ..
$ cd vljqlw
$ ls
dir pcnd
dir pjqwq
317809 tvnrl
$ cd pcnd
$ ls
8283 gmq
195909 rmnmsl
183891 tvnrl
182837 vwl.vsq
$ cd ..
$ cd pjqwq
$ ls
dir vwp
$ cd vwp
$ ls
dir crpztfmf
dir fhrfrbqg
$ cd crpztfmf
$ ls
257441 dpztgnd
$ cd ..
$ cd fhrfrbqg
$ ls
64573 mjm.dhc
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd vpdbrh
$ ls
80449 mjm.dhc
266777 qfjwb
dir qzmz
100029 tvnrl
28910 zqnp
$ cd qzmz
$ ls
9583 wsfwpznj
$ cd ..
$ cd ..
$ cd zfhnw
$ ls
dir pmdsb
106595 vwl.vsq
dir zdv
$ cd pmdsb
$ ls
dir bqpwdh
dir pjqwq
$ cd bqpwdh
$ ls
dir tstqlh
143862 vpdbrh.thr
$ cd tstqlh
$ ls
119310 tcmglrz.hzp
$ cd ..
$ cd ..
$ cd pjqwq
$ ls
56885 rmnmsl
$ cd ..
$ cd ..
$ cd zdv
$ ls
209148 nhcdqmd.hgh
dir pjdhn
119411 pjqwq.vrq
154423 rmnmsl
178813 vhbjqhhq.tbf
$ cd pjdhn
$ ls
dir gnthzp
116732 qhrz.ssb
dir rvbw
117225 svmpwv
$ cd gnthzp
$ ls
dir bqpwdh
$ cd bqpwdh
$ ls
312253 rmnmsl
$ cd ..
$ cd ..
$ cd rvbw
$ ls
dir cjdhwbv
268173 lsmmthf
99445 vwl.vsq
$ cd cjdhwbv
$ ls
302711 tbhb
173182 tmj.frb
"""


day5 = """
move 3 from 6 to 2
move 5 from 6 to 7
move 6 from 2 to 5
move 1 from 9 to 7
move 1 from 1 to 9
move 1 from 5 to 3
move 1 from 2 to 5
move 3 from 4 to 5
move 10 from 7 to 3
move 1 from 4 to 9
move 6 from 8 to 7
move 4 from 7 to 8
move 1 from 7 to 3
move 1 from 1 to 2
move 1 from 2 to 8
move 1 from 9 to 1
move 3 from 9 to 4
move 4 from 8 to 3
move 4 from 7 to 1
move 4 from 4 to 6
move 2 from 8 to 7
move 9 from 3 to 8
move 2 from 7 to 4
move 3 from 4 to 9
move 4 from 1 to 9
move 4 from 3 to 9
move 2 from 1 to 4
move 1 from 4 to 6
move 3 from 3 to 2
move 1 from 2 to 8
move 1 from 2 to 7
move 3 from 6 to 2
move 2 from 6 to 7
move 4 from 2 to 3
move 3 from 7 to 9
move 2 from 5 to 6
move 15 from 9 to 4
move 4 from 9 to 2
move 12 from 5 to 4
move 9 from 8 to 5
move 25 from 4 to 7
move 1 from 4 to 7
move 1 from 4 to 8
move 2 from 2 to 5
move 1 from 4 to 2
move 23 from 7 to 6
move 2 from 5 to 2
move 22 from 6 to 8
move 4 from 5 to 9
move 1 from 7 to 9
move 2 from 6 to 4
move 2 from 4 to 7
move 25 from 8 to 3
move 1 from 2 to 1
move 3 from 2 to 3
move 1 from 6 to 8
move 1 from 1 to 8
move 1 from 2 to 8
move 1 from 8 to 1
move 4 from 5 to 7
move 1 from 8 to 4
move 5 from 9 to 8
move 5 from 8 to 9
move 1 from 8 to 5
move 3 from 5 to 4
move 3 from 9 to 1
move 30 from 3 to 4
move 3 from 1 to 4
move 2 from 9 to 5
move 4 from 7 to 9
move 16 from 4 to 8
move 6 from 3 to 9
move 3 from 7 to 3
move 19 from 4 to 7
move 8 from 9 to 4
move 1 from 1 to 9
move 13 from 7 to 9
move 3 from 7 to 8
move 3 from 5 to 9
move 4 from 8 to 3
move 2 from 7 to 3
move 14 from 9 to 4
move 10 from 3 to 1
move 12 from 4 to 8
move 6 from 1 to 9
move 1 from 1 to 2
move 1 from 7 to 1
move 6 from 9 to 3
move 17 from 8 to 6
move 10 from 8 to 5
move 1 from 7 to 8
move 1 from 9 to 5
move 2 from 3 to 1
move 4 from 5 to 9
move 1 from 8 to 7
move 6 from 9 to 7
move 4 from 4 to 2
move 3 from 4 to 6
move 4 from 5 to 9
move 4 from 9 to 3
move 1 from 2 to 4
move 4 from 4 to 7
move 3 from 5 to 3
move 1 from 4 to 5
move 5 from 1 to 2
move 1 from 1 to 9
move 7 from 2 to 7
move 1 from 5 to 7
move 8 from 3 to 5
move 20 from 6 to 7
move 9 from 7 to 9
move 2 from 2 to 9
move 2 from 3 to 1
move 2 from 1 to 3
move 2 from 3 to 4
move 2 from 4 to 6
move 1 from 3 to 9
move 1 from 4 to 9
move 1 from 6 to 9
move 2 from 5 to 8
move 2 from 8 to 5
move 1 from 6 to 7
move 2 from 5 to 8
move 6 from 9 to 5
move 2 from 8 to 6
move 11 from 9 to 2
move 1 from 6 to 5
move 11 from 2 to 5
move 1 from 6 to 4
move 7 from 5 to 9
move 7 from 9 to 1
move 1 from 4 to 9
move 28 from 7 to 5
move 1 from 7 to 5
move 5 from 5 to 9
move 5 from 9 to 3
move 6 from 1 to 8
move 1 from 1 to 7
move 5 from 3 to 2
move 1 from 7 to 8
move 7 from 8 to 1
move 1 from 9 to 4
move 2 from 2 to 5
move 22 from 5 to 3
move 1 from 7 to 8
move 1 from 4 to 7
move 1 from 8 to 9
move 1 from 9 to 4
move 14 from 5 to 7
move 5 from 5 to 9
move 19 from 3 to 4
move 1 from 2 to 9
move 2 from 2 to 5
move 1 from 5 to 1
move 6 from 1 to 7
move 2 from 7 to 6
move 1 from 1 to 9
move 2 from 5 to 8
move 8 from 4 to 5
move 3 from 4 to 7
move 3 from 3 to 5
move 2 from 8 to 9
move 16 from 7 to 5
move 9 from 4 to 6
move 22 from 5 to 3
move 1 from 5 to 8
move 1 from 8 to 7
move 10 from 3 to 4
move 1 from 5 to 4
move 10 from 4 to 5
move 8 from 5 to 2
move 5 from 2 to 7
move 5 from 7 to 1
move 4 from 7 to 6
move 3 from 9 to 7
move 2 from 2 to 3
move 3 from 5 to 1
move 6 from 9 to 7
move 5 from 7 to 8
move 6 from 1 to 5
move 6 from 3 to 4
move 4 from 4 to 2
move 1 from 4 to 6
move 5 from 8 to 7
move 3 from 2 to 3
move 1 from 1 to 4
move 1 from 1 to 9
move 2 from 2 to 1
move 2 from 4 to 3
move 4 from 3 to 7
move 3 from 7 to 3
move 13 from 6 to 1
move 1 from 9 to 2
move 6 from 3 to 5
move 8 from 1 to 4
move 1 from 2 to 7
move 9 from 4 to 9
move 7 from 5 to 1
move 2 from 5 to 6
move 1 from 1 to 4
move 1 from 4 to 3
move 2 from 1 to 2
move 5 from 3 to 6
move 2 from 6 to 1
move 13 from 7 to 6
move 2 from 3 to 4
move 2 from 2 to 9
move 2 from 7 to 8
move 6 from 9 to 2
move 1 from 9 to 3
move 1 from 5 to 2
move 7 from 1 to 2
move 1 from 6 to 7
move 1 from 4 to 8
move 1 from 3 to 1
move 1 from 7 to 8
move 7 from 1 to 9
move 4 from 8 to 6
move 1 from 5 to 3
move 9 from 9 to 5
move 1 from 1 to 2
move 14 from 2 to 7
move 2 from 9 to 3
move 13 from 5 to 3
move 24 from 6 to 9
move 6 from 3 to 5
move 14 from 7 to 9
move 1 from 4 to 1
move 20 from 9 to 7
move 9 from 3 to 8
move 15 from 9 to 6
move 1 from 5 to 8
move 1 from 2 to 3
move 14 from 6 to 3
move 2 from 3 to 4
move 2 from 3 to 6
move 13 from 7 to 1
move 8 from 3 to 5
move 1 from 3 to 9
move 8 from 5 to 4
move 4 from 5 to 2
move 10 from 1 to 3
move 6 from 4 to 5
move 4 from 5 to 1
move 3 from 1 to 6
move 7 from 8 to 2
move 4 from 4 to 3
move 13 from 3 to 6
move 3 from 8 to 1
move 3 from 7 to 8
move 3 from 8 to 4
move 1 from 4 to 2
move 2 from 3 to 4
move 1 from 5 to 7
move 4 from 7 to 1
move 2 from 3 to 5
move 3 from 2 to 1
move 1 from 4 to 7
move 7 from 2 to 4
move 2 from 4 to 3
move 1 from 7 to 5
move 4 from 9 to 5
move 1 from 4 to 2
move 3 from 2 to 9
move 8 from 1 to 7
move 1 from 3 to 5
move 7 from 5 to 7
move 10 from 6 to 4
move 1 from 5 to 1
move 4 from 1 to 3
move 9 from 7 to 6
move 3 from 1 to 8
move 12 from 4 to 6
move 5 from 4 to 6
move 2 from 9 to 3
move 3 from 8 to 7
move 1 from 1 to 3
move 3 from 7 to 8
move 5 from 7 to 5
move 1 from 7 to 5
move 2 from 3 to 1
move 2 from 8 to 7
move 3 from 5 to 1
move 1 from 9 to 7
move 1 from 8 to 3
move 4 from 7 to 8
move 4 from 5 to 9
move 4 from 1 to 7
move 3 from 8 to 6
move 1 from 8 to 1
move 1 from 7 to 1
move 1 from 5 to 8
move 1 from 8 to 7
move 7 from 3 to 1
move 3 from 9 to 1
move 1 from 9 to 3
move 28 from 6 to 3
move 3 from 7 to 8
move 2 from 8 to 2
move 1 from 2 to 7
move 2 from 6 to 1
move 18 from 3 to 9
move 5 from 3 to 4
move 2 from 7 to 4
move 2 from 1 to 8
move 1 from 2 to 6
move 7 from 6 to 4
move 4 from 4 to 3
move 3 from 8 to 1
move 4 from 9 to 8
move 1 from 4 to 8
move 9 from 1 to 6
move 5 from 1 to 3
move 4 from 6 to 7
move 7 from 6 to 3
move 5 from 8 to 1
move 12 from 3 to 6
move 7 from 6 to 4
move 4 from 3 to 5
move 5 from 6 to 7
move 12 from 4 to 3
move 6 from 1 to 4
move 4 from 4 to 2
move 14 from 9 to 8
move 17 from 3 to 2
move 5 from 4 to 9
move 1 from 9 to 6
move 5 from 2 to 1
move 1 from 9 to 8
move 5 from 1 to 6
move 2 from 2 to 6
move 12 from 2 to 4
move 6 from 7 to 2
move 3 from 7 to 6
move 3 from 9 to 8
move 5 from 4 to 7
move 4 from 2 to 6
move 3 from 6 to 8
move 5 from 8 to 2
move 7 from 6 to 8
move 1 from 7 to 3
move 6 from 4 to 3
move 1 from 8 to 1
move 1 from 5 to 7
move 2 from 6 to 8
move 13 from 8 to 2
move 3 from 5 to 4
move 1 from 1 to 2
move 3 from 6 to 2
move 1 from 1 to 4
move 4 from 4 to 8
move 8 from 3 to 1
move 2 from 4 to 8
move 15 from 2 to 4
move 16 from 8 to 3
move 1 from 8 to 6
move 1 from 7 to 2
move 8 from 1 to 2
move 1 from 6 to 8
move 6 from 3 to 1
move 3 from 3 to 8
move 6 from 3 to 1
move 6 from 2 to 9
move 2 from 1 to 4
move 1 from 8 to 5
move 8 from 2 to 9
move 8 from 1 to 4
move 3 from 8 to 6
move 21 from 4 to 7
move 1 from 9 to 7
move 2 from 6 to 8
move 1 from 5 to 1
move 1 from 3 to 9
move 8 from 9 to 4
move 1 from 1 to 7
move 1 from 1 to 4
move 1 from 6 to 8
move 1 from 9 to 3
move 2 from 9 to 5
move 2 from 5 to 3
move 1 from 9 to 4
move 3 from 8 to 2
move 1 from 1 to 4
move 4 from 4 to 9
move 3 from 3 to 2
move 5 from 9 to 1
move 17 from 7 to 1
move 1 from 9 to 1
move 2 from 2 to 4
move 1 from 4 to 2
move 8 from 2 to 9
move 5 from 4 to 5
move 6 from 4 to 8
move 20 from 1 to 6
move 2 from 9 to 8
move 1 from 2 to 9
move 2 from 8 to 7
move 8 from 7 to 8
move 4 from 5 to 9
move 14 from 8 to 7
move 1 from 5 to 7
move 7 from 9 to 1
move 3 from 6 to 4
move 3 from 9 to 7
move 12 from 6 to 7
move 22 from 7 to 9
move 2 from 2 to 5
move 10 from 1 to 7
move 1 from 4 to 1
move 2 from 6 to 1
move 1 from 1 to 3
move 2 from 4 to 8
move 2 from 8 to 6
move 1 from 3 to 8
move 1 from 4 to 1
move 2 from 5 to 3
move 1 from 8 to 4
move 2 from 3 to 7
move 19 from 9 to 7
move 1 from 1 to 4
move 2 from 9 to 1
move 2 from 1 to 6
move 1 from 6 to 5
move 42 from 7 to 8
move 1 from 7 to 6
move 2 from 4 to 8
move 7 from 6 to 8
move 2 from 1 to 5
move 2 from 9 to 5
move 14 from 8 to 3
move 22 from 8 to 2
move 3 from 5 to 6
move 10 from 8 to 6
move 5 from 8 to 9
move 12 from 6 to 7
move 2 from 5 to 1
move 5 from 3 to 2
move 7 from 3 to 5
move 2 from 5 to 1
move 2 from 3 to 7
move 4 from 1 to 2
move 1 from 5 to 7
move 1 from 5 to 4
move 1 from 6 to 2
move 1 from 9 to 2
move 9 from 7 to 3
move 1 from 4 to 1
move 3 from 7 to 5
move 4 from 3 to 2
move 5 from 2 to 3
move 2 from 5 to 2
move 34 from 2 to 9
move 1 from 1 to 5
move 15 from 9 to 3
move 2 from 3 to 2
move 1 from 5 to 4
move 7 from 3 to 8
move 3 from 9 to 2
move 6 from 9 to 4
move 5 from 9 to 3
move 4 from 4 to 6
move 1 from 6 to 8
move 1 from 3 to 5
move 6 from 3 to 2
move 1 from 4 to 9
move 2 from 4 to 2
move 4 from 5 to 8
move 1 from 5 to 6
move 1 from 7 to 6
move 1 from 9 to 6
move 1 from 7 to 2
move 12 from 8 to 7
move 2 from 7 to 3
move 4 from 6 to 9
move 7 from 9 to 4
move 9 from 3 to 9
move 11 from 7 to 4
move 3 from 9 to 6
move 1 from 4 to 1
move 15 from 4 to 3
move 2 from 4 to 1
move 3 from 1 to 4
move 17 from 3 to 7
move 4 from 3 to 7
move 7 from 9 to 2
move 3 from 4 to 1
move 4 from 6 to 9
move 1 from 9 to 6
move 1 from 3 to 1
move 5 from 7 to 9
move 8 from 9 to 4
move 1 from 1 to 6
move 6 from 4 to 9
move 4 from 2 to 3
move 1 from 4 to 3
move 1 from 4 to 9
move 1 from 1 to 7
move 1 from 7 to 9
move 3 from 6 to 2
move 9 from 2 to 3
move 1 from 9 to 4
move 1 from 1 to 5
move 12 from 7 to 6
move 4 from 9 to 8
"""

day5StackViz = """
[                   [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
"""

day4 = """
49-51,31-50
96-99,2-95
2-62,62-98
34-76,10-59
28-83,27-84
40-41,41-86
15-46,16-47
53-93,54-93
19-98,97-97
29-52,44-71
21-67,14-83
11-93,11-12
15-88,18-89
5-87,6-6
1-96,96-97
64-88,64-91
3-98,2-3
33-87,34-86
21-23,16-22
63-95,63-99
1-99,1-2
11-26,26-39
43-45,14-82
11-94,65-98
46-67,6-50
26-64,17-63
54-54,55-97
60-93,60-99
40-78,58-74
27-64,2-33
25-48,32-80
65-83,64-66
21-69,65-88
37-74,36-75
4-66,66-66
6-14,6-47
17-73,41-74
79-95,20-92
63-87,54-54
72-93,24-72
2-94,3-96
9-94,8-48
17-91,16-87
3-84,9-84
44-94,92-95
55-56,56-96
65-77,66-90
7-40,7-30
20-89,89-90
14-15,17-45
1-70,50-50
28-92,91-92
5-7,6-57
32-50,36-67
81-82,80-82
58-89,13-59
64-90,1-65
29-96,28-29
83-83,16-83
14-84,85-85
14-67,14-68
41-58,40-42
18-49,19-48
66-85,26-72
5-89,88-90
5-97,5-6
14-87,14-14
26-76,47-92
17-97,73-99
28-88,27-28
2-4,3-54
3-98,16-16
61-62,52-62
22-53,21-22
8-81,15-30
5-75,4-74
43-96,95-96
39-41,41-90
33-49,33-50
10-12,11-81
63-64,63-70
10-55,10-91
9-32,8-8
60-61,60-77
10-11,10-69
2-77,65-76
1-41,3-22
28-70,29-71
44-45,11-44
1-99,2-98
45-77,44-78
15-96,95-99
7-98,6-6
28-98,49-99
61-79,75-75
13-84,46-62
15-36,15-36
54-80,80-93
2-91,22-91
32-85,32-33
29-55,55-56
45-66,45-46
6-63,6-62
2-91,5-91
96-97,1-97
39-60,31-60
5-94,6-94
8-94,7-8
6-85,5-85
12-88,11-26
4-79,4-46
1-8,10-96
1-76,75-76
6-81,77-82
35-96,52-98
29-82,29-83
22-86,86-87
17-57,17-63
57-58,17-57
48-99,48-97
25-26,25-26
16-17,17-93
31-74,30-30
18-25,18-94
56-77,30-30
8-61,50-61
58-70,21-59
2-3,2-70
8-12,9-14
5-98,97-98
35-55,35-87
20-60,20-36
39-39,40-68
39-76,40-88
20-29,29-88
61-62,61-84
19-86,38-95
56-68,1-71
13-58,12-19
12-54,12-68
3-71,3-3
71-72,35-71
9-10,8-16
20-71,21-70
43-66,65-73
3-88,4-87
73-74,4-74
62-97,15-95
59-98,98-99
10-90,89-99
11-85,10-86
4-6,5-6
7-92,2-92
54-78,78-78
78-81,69-84
18-44,17-19
7-17,4-16
71-90,70-88
82-83,82-88
47-72,39-72
22-95,28-98
98-98,68-98
5-96,4-97
76-92,1-77
17-62,16-63
20-41,20-83
59-74,58-60
8-83,8-9
30-94,64-97
18-67,12-67
32-54,18-33
31-81,31-81
14-15,14-14
89-92,18-90
16-23,1-34
1-98,1-51
3-98,2-3
16-97,97-98
32-82,32-33
1-11,2-12
88-90,37-92
2-15,3-15
19-57,5-60
15-17,14-17
83-83,50-84
2-32,27-54
16-30,2-29
37-38,38-93
11-29,16-99
78-83,37-77
40-58,17-57
9-35,8-10
2-96,2-3
20-43,20-70
95-96,15-96
10-37,4-16
53-54,54-90
90-99,49-91
4-73,4-74
55-56,56-76
83-88,83-86
82-83,69-82
2-30,4-77
6-8,8-49
44-45,18-44
6-66,66-67
74-76,10-76
25-53,24-25
1-2,5-22
6-96,96-96
68-79,80-98
43-98,42-44
79-91,27-91
17-17,17-17
48-49,1-48
4-58,20-58
18-20,19-87
86-87,7-86
34-35,21-35
18-67,17-68
19-95,18-24
44-77,38-76
70-72,50-71
19-99,20-99
98-99,19-96
22-57,5-20
95-97,5-96
4-98,3-97
10-58,10-59
5-8,7-95
10-94,8-17
1-11,12-72
37-56,55-56
32-78,19-78
29-92,10-90
11-73,60-73
16-95,17-72
90-93,43-91
27-73,72-73
25-57,28-57
32-87,31-85
96-99,2-97
24-51,23-52
25-54,32-55
2-91,2-66
15-82,14-15
24-40,24-80
14-34,13-34
30-95,21-94
53-74,53-73
77-81,79-98
9-98,6-6
13-94,14-95
46-81,23-80
6-89,14-90
42-56,43-51
96-97,4-96
11-11,12-26
50-71,50-72
81-85,27-82
10-36,11-11
30-31,30-75
34-39,34-88
30-65,30-64
1-98,1-36
67-73,63-67
8-94,7-99
64-65,64-81
64-94,41-94
8-53,7-8
17-91,18-92
30-80,31-81
4-72,5-71
5-81,80-82
1-7,6-82
72-73,29-73
7-73,4-4
4-6,5-95
8-92,8-9
12-82,81-83
76-76,76-77
42-67,42-84
1-75,5-66
3-99,3-91
34-35,11-34
7-98,97-98
15-66,14-26
83-83,63-83
2-4,3-67
4-96,4-4
5-5,5-89
5-94,5-6
6-52,7-51
1-64,1-63
37-94,36-38
50-87,50-88
24-77,28-77
12-91,77-91
29-92,28-30
41-42,41-57
62-84,83-85
46-95,19-42
31-87,30-30
2-21,1-2
72-75,1-73
59-98,59-94
65-78,51-71
11-58,12-58
52-67,34-37
55-62,53-60
26-27,27-76
12-97,33-98
95-95,56-94
17-90,17-91
7-39,39-63
45-98,37-46
41-62,42-69
5-98,2-5
43-44,43-44
34-35,34-35
8-89,7-90
33-87,32-86
38-47,38-46
2-93,93-93
25-77,19-41
15-81,16-81
7-68,67-78
52-77,18-69
8-9,8-59
4-82,3-5
23-49,24-71
10-93,4-92
21-53,22-54
5-50,5-99
14-90,13-22
14-75,15-94
6-81,72-84
22-99,22-99
11-80,5-12
79-96,22-78
27-83,21-27
88-94,72-89
10-32,9-80
3-5,5-99
3-97,3-61
15-83,29-68
82-84,45-82
50-95,10-50
41-98,78-93
19-89,10-92
78-80,31-79
22-71,21-71
82-84,38-83
13-19,13-14
13-44,43-84
43-82,43-97
1-52,2-89
21-30,31-88
49-71,49-88
36-81,80-92
65-66,65-91
75-87,22-76
57-91,86-91
16-23,16-16
95-97,2-91
64-68,65-95
15-42,32-60
55-98,70-96
4-5,4-69
10-51,10-52
17-95,16-17
30-69,29-40
72-73,24-73
13-87,12-88
12-47,29-85
19-20,20-51
67-90,56-78
27-85,1-86
1-97,1-2
54-60,34-58
7-97,6-98
41-84,42-84
74-80,29-79
22-52,14-22
36-54,36-62
32-88,22-89
10-54,5-5
6-36,7-17
7-93,7-8
38-81,37-37
43-85,14-88
20-90,89-90
50-78,46-68
18-59,5-59
24-84,83-85
10-63,10-11
95-95,15-95
58-84,59-59
76-82,75-79
48-51,48-55
43-68,8-56
67-96,68-96
9-10,10-53
8-68,6-6
75-75,34-76
52-53,53-54
12-24,24-66
41-42,19-42
70-89,36-71
52-87,49-86
36-91,90-92
16-52,17-52
8-95,7-91
92-95,9-93
3-96,15-96
58-79,57-73
85-87,9-95
60-61,2-60
11-23,3-11
14-90,3-15
8-60,13-26
82-91,85-91
56-99,51-57
5-95,9-96
6-44,45-62
63-99,62-98
24-35,34-36
51-52,51-98
37-52,31-53
51-51,50-72
2-55,51-55
6-83,82-95
11-89,11-93
30-62,8-41
32-82,26-82
8-87,7-86
33-34,12-33
35-93,36-87
46-47,9-46
3-87,3-3
83-94,93-94
5-98,4-99
48-50,45-50
35-50,35-43
14-43,5-43
48-97,10-96
9-78,9-78
59-61,58-60
7-73,72-73
4-97,3-5
11-49,49-50
42-99,99-99
8-73,7-63
4-82,34-87
14-76,13-40
26-95,25-98
5-62,61-62
28-45,22-45
29-41,36-42
85-98,61-86
12-97,11-97
6-78,5-60
61-67,39-62
58-77,58-73
92-98,5-96
41-98,39-41
2-77,25-78
62-71,1-49
11-84,10-11
25-42,26-78
32-97,3-12
36-73,7-73
26-71,25-27
1-48,19-48
11-37,11-99
49-76,42-50
2-34,1-97
60-66,66-66
4-4,3-5
37-37,38-40
94-94,35-94
82-84,5-83
55-56,5-56
20-93,20-95
57-61,11-60
86-87,15-87
11-73,11-42
10-35,2-34
35-47,48-70
12-94,2-97
3-81,80-82
18-49,18-70
27-96,95-96
38-39,39-57
75-94,6-94
19-60,56-56
77-87,81-87
4-7,3-9
89-98,18-88
2-2,3-75
10-62,7-7
10-23,9-35
3-95,1-94
32-83,82-83
37-66,37-70
36-45,45-70
9-79,78-80
2-96,1-1
39-44,43-44
10-95,11-98
32-34,33-90
17-93,29-94
50-97,97-98
21-90,21-73
3-3,3-71
32-96,11-95
18-98,19-98
39-93,92-93
39-77,38-40
30-91,6-92
39-73,39-74
38-96,39-56
5-91,6-14
19-19,20-87
7-95,6-7
38-94,2-95
4-99,3-73
23-99,24-74
1-24,4-25
10-25,25-86
9-90,8-91
20-26,23-72
80-82,3-81
8-38,8-9
57-86,35-70
6-90,3-4
21-28,21-23
11-96,10-90
41-51,50-50
30-57,13-31
7-77,6-77
87-88,2-88
40-86,36-85
73-75,9-74
75-91,21-74
1-89,12-90
28-85,23-23
79-79,11-79
10-93,59-96
38-38,39-48
3-93,56-94
8-13,7-8
4-43,5-42
22-22,20-24
5-56,5-30
43-83,66-83
28-94,27-93
22-23,23-88
8-76,1-75
29-94,28-29
6-89,5-7
22-97,22-89
2-92,3-92
19-19,18-69
30-49,3-12
2-38,32-96
32-71,66-90
10-51,14-51
17-97,17-96
42-49,59-64
96-98,29-96
7-8,7-43
93-94,1-94
57-71,58-73
4-98,4-4
89-90,6-89
79-81,80-81
52-94,51-75
5-73,4-6
90-91,34-91
45-87,69-96
13-30,14-57
78-79,12-78
10-45,9-10
12-78,12-68
3-14,10-16
73-88,14-76
14-14,10-15
42-83,43-79
15-94,94-95
13-94,3-22
9-62,9-62
76-87,76-76
3-11,2-11
27-57,4-27
28-60,27-60
49-63,49-62
58-69,65-69
2-99,2-98
33-89,33-97
32-47,32-36
56-56,41-56
16-94,26-74
91-91,10-92
8-28,7-29
6-91,5-6
21-93,20-21
57-74,22-29
33-33,5-32
78-82,80-82
1-72,1-37
72-94,13-73
44-51,45-60
2-97,1-1
37-94,25-56
16-71,17-72
24-25,21-25
9-81,44-97
18-85,85-86
40-93,92-98
89-90,48-90
3-74,3-3
9-99,4-92
17-27,27-98
25-72,72-73
41-99,72-99
23-23,23-92
47-78,39-48
58-96,5-94
7-90,89-92
60-61,61-87
43-67,28-67
23-97,22-24
1-31,19-32
5-88,2-88
1-34,2-97
28-86,7-86
16-80,16-80
6-59,20-60
68-89,73-95
46-94,38-81
20-25,21-78
78-80,77-78
33-97,96-98
48-98,47-49
4-98,2-98
26-69,26-88
26-75,75-78
72-92,72-93
4-92,4-93
66-76,65-67
2-97,3-97
41-57,41-42
6-77,76-97
16-43,17-56
49-51,4-50
95-97,56-96
1-97,80-97
35-38,36-37
10-84,18-84
20-84,6-59
18-81,36-82
79-81,80-88
41-96,89-95
66-94,3-88
71-72,56-72
74-88,73-74
57-73,58-60
31-73,1-27
14-25,9-25
8-9,8-82
3-96,95-97
75-77,4-76
16-89,15-16
3-62,61-71
20-28,19-48
31-31,32-69
5-61,6-60
67-76,76-76
82-93,70-89
49-96,29-77
3-14,7-15
9-24,24-44
10-82,9-59
91-92,82-92
4-61,3-73
42-43,43-67
63-78,64-64
8-8,9-94
54-55,54-64
12-35,18-96
12-55,53-53
3-85,23-85
26-93,32-93
9-23,3-9
49-82,48-48
61-84,61-83
35-37,36-91
6-78,4-4
73-80,4-76
8-77,8-94
18-22,20-22
75-84,76-76
51-91,24-90
24-94,3-88
17-17,18-59
1-93,55-97
15-75,5-75
7-11,11-47
3-85,3-4
14-86,13-15
13-93,33-95
4-6,3-3
33-56,33-89
42-42,43-84
46-77,76-77
57-60,36-60
23-24,24-53
87-94,88-97
1-83,1-52
22-41,20-27
12-86,85-87
53-87,50-56
8-51,8-50
27-71,10-71
7-62,8-63
17-28,27-97
1-90,90-90
3-94,2-4
3-98,2-24
11-12,12-83
18-37,19-36
9-98,9-90
4-98,3-99
82-82,53-82
5-54,6-88
75-91,91-91
20-98,19-98
2-48,10-62
16-42,41-42
61-71,59-71
3-92,3-4
12-47,12-69
23-26,26-65
20-57,67-97
65-95,64-65
1-92,3-88
5-83,5-89
44-81,80-82
30-32,31-84
10-51,50-50
25-52,16-25
37-45,38-44
46-47,47-62
59-85,84-85
13-86,12-87
29-76,4-30
79-93,12-80
61-86,61-68
13-85,15-85
33-35,34-94
68-69,33-71
55-90,55-82
20-94,23-94
82-98,6-83
26-78,26-79
14-16,14-15
6-47,46-49
4-98,1-97
17-76,37-65
13-71,13-59
24-67,14-58
13-47,48-92
37-38,37-60
30-90,30-71
62-74,33-86
39-40,26-40
6-81,5-16
10-70,10-10
4-84,83-92
87-89,68-87
47-95,16-84
23-86,29-86
30-98,30-62
28-85,29-83
87-98,56-97
91-92,12-92
89-99,67-90
52-99,29-97
5-92,3-16
3-74,2-84
54-83,55-55
1-39,39-94
1-98,97-98
20-98,7-17
27-47,10-27
3-4,3-64
86-87,4-86
12-68,21-47
78-79,37-79
23-48,8-36
5-88,4-82
10-96,9-96
1-99,2-99
57-77,56-56
66-85,65-68
73-87,87-90
13-96,12-89
15-90,60-66
75-75,12-75
15-86,85-91
26-67,25-44
15-86,16-87
23-58,43-69
2-86,16-87
18-78,9-19
92-94,13-93
8-46,2-45
39-60,39-50
76-85,75-77
52-63,36-63
4-66,3-4
51-70,70-89
4-7,7-97
38-93,38-84
2-9,9-96
14-19,18-20
3-79,2-37
25-84,83-96
21-36,22-65
41-82,42-96
2-77,38-78
84-88,59-97
3-70,4-71
53-93,17-93
94-95,2-99
71-88,9-70
12-41,13-41
12-54,11-53
72-73,73-78
4-81,18-33
23-52,10-94
23-91,5-57
45-45,43-45
48-83,47-47
12-96,11-11
68-81,72-93
14-92,8-14
84-99,28-97
21-81,22-82
12-37,11-32
40-45,39-39
23-34,25-27
23-23,24-65
77-85,85-98
91-98,91-96
88-90,11-89
5-5,6-98
23-28,4-13
20-58,19-58
3-96,4-94
16-22,8-19
78-79,78-84
67-80,62-68
80-94,79-97
12-79,78-79
29-50,29-51
2-41,41-42
68-69,17-68
38-39,2-39
13-14,14-78
9-80,8-9
42-92,64-93
67-78,66-73
14-65,14-15
6-59,1-35
16-17,17-48
15-28,16-33
2-9,48-91
3-4,4-86
28-45,50-56
15-23,16-86
50-79,50-78
9-62,8-8
4-91,4-12
24-25,25-65
38-39,38-61
8-8,18-76
56-86,1-56
13-68,68-74
15-42,26-42
40-45,40-61
92-99,4-93
20-35,25-32
15-28,15-69
26-94,8-94
16-94,3-96
16-98,16-21
17-17,18-23
26-30,26-27
33-49,31-34
13-99,85-90
12-74,6-74
54-60,53-57
10-94,11-95
37-53,37-38
2-79,2-48
46-55,53-60
7-95,7-8
7-83,8-98
6-7,7-32
47-82,46-47
63-85,64-87
77-78,57-77
3-5,3-4
5-98,97-99
59-92,2-92
4-97,1-99
37-86,2-86
46-47,9-47
38-86,37-38
24-48,52-71
14-85,85-86
20-83,20-21
49-83,50-70
44-63,45-88
43-70,3-43
34-76,2-75
1-72,73-84
49-89,45-89
45-85,13-45
29-98,28-30
7-8,7-58
20-20,21-41
52-63,18-52
81-95,76-81
3-95,2-95
74-84,68-75
51-63,51-64
19-72,40-72
53-57,4-80
21-88,19-87
29-93,30-99
4-98,7-98
20-62,49-63
5-71,5-70
35-83,35-66
12-71,35-78
7-59,7-95
7-62,7-70
2-9,9-97
5-11,8-12
6-17,18-20
5-87,3-3
83-92,5-92
12-95,12-54
37-83,23-83
39-48,40-53
14-95,51-95
37-98,70-80
16-90,19-91
2-27,16-46
3-87,6-17
49-49,49-79
7-30,35-71
21-40,22-29
77-87,76-78
11-68,23-69
18-19,18-80
21-79,13-21
9-89,8-90
4-85,7-89
36-44,18-36
1-21,2-44
1-98,2-99
56-57,3-56
23-24,23-81
22-25,10-24
6-94,93-99
13-37,12-14
13-29,30-86
65-88,66-90
90-92,6-91
42-43,43-67
27-33,28-31
31-90,37-90
5-97,2-3
25-55,1-26
90-91,10-90
35-52,36-53
41-42,41-41
7-75,18-75
8-69,2-82
56-96,11-96
13-79,12-78
5-11,11-94
18-18,17-72
4-94,1-93
32-38,33-71
3-5,4-98
"""


day6 = """
mgtgddtfdtffzvznvnrncrrbqqhlhhffzqqzpqqthhrhhfphfphhcppcddnwdnwwtmwttfvvthvvrrbvbmvmssrlslfslflppblllwrlrzlldwdllqblqbqbsscmsmwwffjpppnlnhllbblvbvsbbzvzrzzsmsjsddfpftfvtffgjjfzjfjqfqjfjsscvcccgttgtzgzmgmtmbbwzzjqzzdfzfmzmzfzwzvwvggqcqrrcwrcrzrccqcwwbgbqqwdqqzjzsjjwbjjssmmcfcbcddlhhtltmtlljffvjffhghmggmvvfgfqgfgppnpllmvmfvvzjjzrztztvvstsvvppqdpprjjmtmjtmjjdrdcrdccgsccnsccqsqzszqsqgqwggbhbllvclljrrlrqlljtjcjjlrlhrhjhjnnnpllwtwstttlnlqnlnmnqnpqpbqqbgbzzrhzrhzhrzhrzhzshhqvqgqgbbcqccqmcqccvgccrwrgwrgrdrhhbshbhwbhwbhhvthvttfrrqsstqssqmmpnpwpfpcffcdchhrsshrhggtcttmrrhvvjfvjvvclvllmqmvvhddrdjjhdhvhlvhlltlstltffbbqbwqbbbnsbnbwbssjwsjsfjjsjwwzttqzzsdspprlrblrltrrfrsfffwqwpwddddnqqtbtwwhwpwdwmmcrmrsmmwppjzpjpcpdpjpdpdqppmjjlqqjfqqhgqhhbddtccthhwjhhlfftvtppwzpwzpznpzpqpgqpgpnpdndnbnddqrrjdjwwdmmtnntvnnrhrfhfrfwfvwffmnfnlfldfdjjwgwqqwwsslrrvhhrqqsfqfllrmrqmrrbppwjppmlmggvppdhppspjjzljjrzzrlzrrlldllvlpvpfprfprrhdrdlllpqqfhqqhchzzzwpwjpjjgzzwqqtqdqbdbdgggbrgrzzznwwbvbnbpnbpprnrvvfvsscncrczcbchhjqhjjzrznndwnnvttmtthssgvvbvfvtvptpthhzggnjjhrjdqzjbtfpqdtwtmgnngqdzhdrfzqvcqggmcdbsdrdrmgqhmvfvdgbvrnlbhfsbpjhwgzfndqgcjdbpsffcslfcltsbclspdjhscqrncfrjrbjfzspccshtrdggjbhthrrhgnjvsptfnjvjvhhdjfbtfgpfgszhhbcvzplclrnsrpffpjhbthnfsfflqphhjjdpcfwzhfdpnsftrnfhrdhndlrnfrnvprtvnmgclzlrdjrzdcllvlwdlrcfbsgcbwcnbvjztzfsgcgqlmgcbsgwbbrmrcthfpvmbfvtbhqstccfntmphqpjwpbcdpnffqpszlnqdcqtfhvlvpgdpljvcschdtpvcswfzcbpqdhfjzzdjvgldspcvlnfnwffhjzdnbmjjtnrqlgnggsvdltnrpcfwqvphtsmrfzhflwjjbnpwlzhhmdnpqptgcjnrrgcnhwllqsbsjjvzmqsghlzvhdfbrnfhrqjswrpgcctsqvdwzgpqdssfmtgwvsznlbhsgppwdhhtjmscjfrjdgflwcrlbsfwrnvtnmcwpndhtttgqfvmvmfnwdrrvgmgdqlqvvlphwzgmwcphjvcfsqbbwttntmgvfmlmctggmtlwtmfsmczbgdvbsjstzgflnjplgrlhbbgldlchwmhclzbcwpqzlzbjzbplnvpbzjhmwfmrfnwlnsvpzhrgjdpqvnjtbfjfsvdqcfwdjftsmfqdrqllwlbnbmgtswrhbtbqlchznbgnphgntrtwbtmsjtphhqpbngwmmsdnsdqcctrsrzbrtpwtvhvqbrjldfldllpvspthdhdljfvjzcjsltwflscfqsrvzhgvzhqnnjwdwdtnsvgchzrnbzfscvsmrmqsqjmrjjdhtspbzpqtqqbfbzrddwqzwpqjbpbbbghlwmzhqvqdwwwwvltvvcpgzlwzvmqzfcgnjpjnpgsccvzpnzjwwnnjrcpbvwljfrjqzwsrvdmqwwfpldqcdwlchvggclmwnbhlrlzvsrtrqmzchqfqfhqfjgqsfvclnchdnnvdbqpcddnldggwrpbgrwwtssfndhrhnwtqmgrwpggntlqmfgbzjhwwsclvfmwgzzfrsccdfddntnlldpnwzhnzlssnnfbvjjhnrvclmphgfpvnwjzznbvgqnpljcrjpndgrlbdzsbfrrrfztbqcbphlppwcvhmrrmtrlvfjcddtznlmflrpsclgjpqczwrptfsccmdpzfvwnfsvshcnzrjrmstrslhgtrsmgplvcwptfqrgzgwhvtvrqlrjpcbztgtfwpnzqpmctvpdlgrtzzlsmgnftqvtvcmndspjqbdnmrttwhdrncsntntmrwjrqstdrptnhbqgtlqsdqfmbjtvgstndlvndqqsbqvcghwwjdzpszrsfpdzvnmnbzngczndtwtmprbzjdzbthslttzwwfptbphqwczsrqcbcbqnhbtcpjpbcqpjgjmhmfnggcbvctslpmqrpqzbcfrcgzmzpbpwzsjlrmpfzhgnnbqfrbslrfsthgtmsdfhzgdmjwwsgcdptssmbvffhlmfvwnmbpnzbvpsvnwsvsgrcmhpclwsbvtfqstnpzvgmgfcrmjhbccwcptssjhbfmzsqljjcrnnszvffzfwgcpnqrtjnqdltwnbglwlwpschvqwfdztvcwsqtwmgwccgsqbsvlwdhlnqphwtcmdpvvrqfwmlbptbvghvjntqbcsqjspwnmvdqcfbqzqchhhwqgdcmdhfvtzprscpshpbmzhwsznlpvzrwvmhtqsclzffgnvvrfbzmvqmnrrzjbmhdbspjprrmflgrwhnhcqpczchpnrnfjgdlnlrnzwnvjpmzgpfzspwmfnwcrrdczdhtnscmwqwqbcrdrsndpwbdvpgpbpsfzbmvjlsrdcgnwgrvmjnzlpnwtcrmnfcqgmlnhqbwlrnzlbdrnzfhnqddsfmnhnrrrdjgqprmgvrnhzrlccjthhfzdbltgrbrjpmbhvgrlwngdlfsljhfvwhvpmltdfnzwzcgzdpppnzcnpjttdgpzzqppnfzlmhrngbmcmshtgzbjllwstdbnmmwlrlllgfgshvcsjbpnggzrvvmvdqhjhvhmmpvrdqbrfpdtcdbqrvwhdrtqgftnwwzrcgzwmwjmdgmfswqwlgmvmvhscjmzshtbzmfmbqtbsjppzbczwcqpqhhqdggcntdchjgwsvfnzfqdzvhpnwbjhbqnldzbzmctcdqgjsmbqdzmmtjzvqzdqzsfpmncdmqlnpsrwcznbtzqtbcwwdqjftcdmmwdjdnwvpchffsmqmmwvqfgcnfhbjsttwnwppssmvrrhrbqwsncpfnbfggdqjwbgtvgtwsmlqbwzlghnzhjwphswjtbtptmhlzhvvrwqqcgwnmcqtcjlndwgjrpschhhsmrvvwtrjplwrtswhrjlgjhzgzrjhsbrjhtgnmfdvbjlntcrphsnmdcjzgwtvgldrfpcfgpzlgsfthdmpbnhmlsbnbqzpqvzzmvswbbnbtzvbsznqdgqlbbwzhjrzndltfgswtszsmmrhrcrcrcpgtqfcrmjrtflsbcbbmrsrfgnsrmbrpcvfpmqtmbrbbqtzrjntnvbvwjwqmwmcvmzccmwcnhrfpgghlqczcfszfhqgrdnfpnrrzpzbnjqjtvbglvqlhpstpzzcwrdgfhghqtsgzgsmgnpgvbsvsjtnwbvtqpcfdvhnjjvwjwglplthmghrwpmsgbdbfpvqsmsdvjgchlnlnczlzczqmjsnpgrgqgndwzdtlmmgzjpqvbqmcmhnhpqvpjjsftctwsrfmhrlctrvhczjbfsvqnshmchdsrmlrlqdnfsvhlblwghsdnrtwnpdtqgczmghqcmfzvsgqvrngjvbjsvnpzvpsplhvndvqpjjrtmrqscjrhvdmqcgwjmrgsdmgswgnbpdtgvvbrzrcwtvvwhpmcqwdtsmwwfgdpdrjsbvtbdvbhwftqznpssnsnjnclblslfgz
"""


day3 = """
rGnRRccfcCRFDPqNWdwWJWRBdB
jZzVVSZSjmQvZTSZfjmLzNPJqWtJBwqpNtBpdWdNvd
fZfjlMLVshMFhcHnDG
vJRmRfJbfRfJsCpvgLggNVsv
zlzSrMPZMgBFFMNMVWsjsF
dzBSBlzdcggRGdndnn
hNwqVDVDdmQwQPrbDMSSMRSWSM
LvnzJJtlcHstlffCVpMSbRMpBMbCgVWM
lGvvscLHcfsHtvlsnZmmNGhNFVQqqTdqFd
sHGzGsfcZnHfhbLRFrdrhRFf
vwVqzSSjSSttjSqgNMqwzSSVCCgRPhPhFLdCRLLrdCRRrDLb
vvwwtvvVwSvMQzjvmNtJsHBnsZllmnnTBBcBlTnW
pzNVBVplhfLfVfVStZrZHbQHZQTb
sdPPJdCjbdQHMTWt
ngmJGFjJwJCmGcnJcFtgwcDBNLlqfBpvfBpqllhlfL
TGpphMZhJQpGLZTMCCtsBMCSDsStBFcB
jdfgHClHrdrbWvWgjqmctSDqltDsFFDFBc
dNWWvfgCLzzNNLZz
vvHzBrTSvHFbqZqZTBBtzdVfGCGhJSfGJGDSdGMhVG
lgmgslssslscsnRlVGWGWGVMRCll
pQPsjwnNgQmnNNwQgNLNnmgZqvFqtwqtrMMzvzwFtrqTrr
TNhNLTrswwsnFNrrGZVnJnZmVpSjjVDnPp
dBlzzCBqgfWMBpPSJDHVZSVP
cqzfpcdcNFFGrhcb
LLpzCzSzJnLQVnTNhQ
vtDqwBcRztQbthtV
qZZZqZvvsZwwjvjDjspFlPpSSCslpzPlls
rsZVlmStlFZllvmSSvLRqcGMswMMzjMsjqGCjzMG
VTPgQBQdBCwgjCnJGC
pBNTNHdbdWLrDVLbDmLZ
CFmsmwnCRmjCjnCzJZQhhBGQBsMzbP
WvltTWVDdNttdlDbbZzJvPJvBBhhzM
gHDfTNlDDdgVNdglgfqtpcSFwccCmmwnRSwzzHHF
hgmhWgCdzpjPCzFC
NVfgffZblZQVNtFZPntPDrJjPt
TwbQLLfMgdhswWGH
JStSPHPJNrBCtBZMPtHTVfVwLcbbLTcSgfbVfn
GdhhCplmdWbVddLV
qpFvhQppFRlqmFGppRhqvvFzZtQMHZMzBNBCCzNDHHMPzB
MvCMQmJCMDQjwMJCSJpQmDcnGBggfsgljGNslsNGjTHTNf
HRPtRRzVWWFhrFdZhTGlTTLLggBLVgGGLf
zZhdWZPWRdqttWWRPzRPmcpmpQqvvSCvwHwQmJqD
NwrVVWrvwtQDRdRqWbqh
jCCZjlJZZGclGPpCJlcCBhJshgqTsQgbDdshTbgLRh
ppppflPZlpvfffFzHqFV
VmTwGVwnwHnSnqGSVmBBwwmTZvzbCrsNWcsZsqFzCWsbWrNv
JMPPgRDPDgghJggtzsMbZvsNCrWcNsbM
DhgJllPPJcgJpptDDDPldpmTwjHBmSjBBwmBwHBdBmTQ
vblvFHvrQTjqqhCpFwLnFL
RDJRWsdRdgdWZMCMQSVppMJpVL
DzsgRNNsftWdQmcvbPcfcBfj
wTgbsTmgqSbzSlSvFb
rNdDdZnRtJFlmVSHZz
mfNjjmmdNWhWCsffwC
LltBNFLHHcJcfNdNTwbbNsfW
vQSMCzQSGdSdvjsTwmwfwWwV
nRCSzMCQDqlgdlRJHJ
vgqTGwnhpLFsVvrR
ZZzTHlTlJNbcLfRtppFzfs
PlWBWbjQjJgCDCMPTTGT
wtBdWdDpjDdwScBtnsFsPmmnPbPHHPghhh
fSSVGVzlTlqGfffLTQMGHsmFsbmPFbsPbhQZFhhs
TzLzfqJTVRGvRMvqvLGzMqRfSvcDpNjcjdcwSDBDtBDvSCDj
FrdCCzmqFrpDRTRHRLnQJJnr
SGfNRWlBZlgtRltGbvnTVbJnSHvLHVbH
NRWsfWBwwqwDMDpc
vSfsmsdssdjSdZdSgRnmLRGNzgGnqwwB
VrlThFPTPjHFDPRqGGnRnNLqqqHG
lPtTDVCCDrjppfdSQbcJMsbftv
RFFslstRRfSljtsRJPjRtRtngSHbmbbhGbHQQmgbmgGhGQ
DqBZdWZvTdMBBTLDzqBhFnvgVhnHHFbnQVnGnb
wcwMMMTzZwsjtCtjFN
CsscSlwwZDscMNhhpZhRZHRM
VjQvjbQvbhJVbvTbnQTnHHLrRFRqqFqFVdMHNHNH
QbTjjbtJnvttntjgjJjPDwwsBsSsSlslhlwwPCBS
RLjhhBBcNNBNhNjhpwScwSCTFwcFvMwvlc
dJqPJqbqtmgmgdPrdgwvDTCSSlMSFDlFTzFg
stCCqmbGrrbmPsqZhHhpjjNhfjBnnsnp
LfDzcMMVsDLLzNscGhFFcQhlhhBRll
ZCbSbwdmwPnPnPmHjdjWFWsWhdGjdH
bZnPbvnvqCvJDrLJNssf
bbldQHVltHQSSJJmTlwJGjCjCChchgMhHhprCpMv
WNPDFfqfzFsBFFnmgjGhgccjpcpgMGrs
mZFFzDnmzBBZltdlZSVtZS
hdJZZdJTvnJmRphvvpGnwvqzVFSwVlHVlFHFHNlzlgFgHF
QWWWBbrCCrtjQsMdcWMBfttHsgFHVHgFSNzDzFlVLggHzz
jQdBPCtrtcPcMQCTnqnhTvPGGvnJGR
ZhsmsbNVmFssmblMMpdvvQdwLQRppRvQ
GjnNNGNCGjfJcqrQDvQQpvQLPpnQQw
BJjWqWSCrNHrqjfhlHzlVbVtFmtHTV
mtJmPmQBbPFshnJzZpLZ
gMqMHRGrCHSvrRGrqPZLnplFzlVhFspL
RrDrgMGRDPNtfmDN
wqqvqVmlpqchqrDD
gzRltSjgFlWshrdngrpPcDcd
RRjtsbGfGLbsLWSLtjzGSHNNHmHBwNNHNmNfllwVfl
mqFBQgnMQQbJqnTswSMNWGsDswZZ
HgzlRzHccfHsfTwSWfNSNf
VLldvpHLVHrFJFJgpnQbJn
SzCJtLdDCCtqCcdDfZMVMfGVbsVZPPzz
wpwWQWjQgwQgjNBwgHQgsGfPfbPsZPGSPjZmrPrV
QFwpTwpHlnHFNFWQWlQgNwNLCddvDShtLJnSJCLqJJttDt
HMgCVHggtqMMvjgNjNCMMwfWfPwWPJQQNzWwJzlQlQ
bGFrqrFGZLLdFmSPcmPzQJlQcWzJmJ
hRphhShnLGFdGSFSLRGrdqdqsjTtsBTVTTBnVjVvHHBtHggt
hHhnFHQpcFcHjcjfZfZRnjjnNNBvNNNtwvNtbwPtNcPtBgbg
zzVLWCHLSdCttbvw
mMLsHDMVFlRhhmhm
MHMgBNQQPCMMQBbBQQgJHbWttdlfWpZJVWtGGztfWJZW
nvLzDTDFDFqSqncTFddLGfWfssVWWVdlGs
njScSmcnFDDhnmcmnSBzMggjjMQrQCjBQrwH
MFVFHqhHHfVVSGcVQCLttttWTtLQ
BgdJJrJzbGpLssCtTLLCpC
PGBGdjjllBGBjhmhHRlmSfhRDF
BLJmWwBJDDmLDFnVPzvTttvNhNFsHhvvQH
cjbSqfWbRrbSzNMjhtNzzTsT
dRdbgflfqmWggGmwWW
lBTTnDMnNwWdpwMllTMDdTBTSRJjRRcSJRhRGhwtccScgjtg
vvsnCVnHHnsvPzLfVJjtShgGJGVJSc
zQQvzCZbsnbHCWMdFpMqblBqND
CLggQjStSQjLgVRfhBRztwpBpt
DNVmJDFcGNGlmNDnGFnsGcDdwzzZwZPsBPZZhhfBTpwhPfZh
DMDccrnrdnDJcJGFGmCqbLvQqHVSSQVMCgHV
rZVNNDrCFCbjbRSgjhZv
czcMTcGMlcjjvvvGdhbb
pHMpHtLWHHHztMzsvqvnVqNvsnNDqW
hPhPBQVjzjQScjChRVVVsdfbvdmvvpGmvfdbff
nwZwZWNTrwLTTDtbfmHDpGccstDv
FLFJNllFrwTgTwNLnwTlFPhcjjhRhSMSjjBPhzJPQq
CgJCHgJfHzGrrMjJpl
SWqQLSQqdFSLrrCSZrvpzjMM
QLWqhFLQdwFqnPbHcCHPbhCh
jLplfcfjQfptPtLTTtPrRqCCCjZvhBhwhDjwhBBBqC
msznRWgSmmHbSJwDvvBqCCqWFF
mzdsVnbbSSznmbGgGSmTclPcrQffdLfMTLRLtl
PpQQFdNFBtdsFNNPPthTtldwGMnZVvmbbVGbMwrGvG
wHWRJDjHHRgJDZlmVZmnvDbDDM
JqJfgRWLSqWJfcsBfwPpPwFpNwfC
SjpVgjghVZvssgsHjQfHcfcnfNcnbqcRbr
WBtNWTWNJnCTCbRbQR
FlWGtwPJmJPBmwFtMGmpNhDSSSgZhSszzghsMD
fSfzvQSbbSSSTQQzDQTzHsqHmjHVFsjqVJsbrrLs
GWZncGGdBwlPGPJcGlBcPgNGqLqmjsHMVLrrVMwjsMMssLmr
ltGWNggZJnCRhDtzvtTt
zzSHMgsPWzLSJQMMWQWLJBLVqcmVrzmvcpFcqmqpmFprFV
TlDnwhDblbnbbtbjdpVCrmFVDgmprcRCcF
hTdjgdldgdfZWWGGHQJHWZQH
TZVsSRGsGMGWZTvpmrgcMCmrwwFFgF
BDPPnDDLDqDFLNLgctLNrm
PzDPfHPdDPdJPfdHJqdbnnSVvRvsjZSvbsrRGhvGRhTG
nnghnhLhgdVqSPLHcPHPNtpmrRptNt
DwvMWlsJlGzsGMlvsZcWWbRrNHNtZtHttHNTNttTrTTR
DDzDcwlWWGlcsszGwBCggFqgghCBfqCFdhSh
GzgQpJnwgJfbSWpSvqtvlBtmSLmLlvLS
zCHsRZjHdzVPRFNlLlvtlNMNNrtDrt
zzZVsCcCCHzRhcbpwGJGGpcf
lVQMrwlMwwMCBZmFtthmVmsgWhTL
bdzHSSFJcvzcpFDptsDDmhTgLmnmmmhT
SFpcGvdpddvGlBPZMCGrBZ
QmQTQTFTSQPNbsPjPnntZjjnnDlBBB
JHqJqhfCJpWfpHchRzzCnGBjtjDZltsZpljGntrr
chdMHqHcMhWMfRczMJmmQsVTSNbNNFbdQNST
HHdFqqDRdNsHfNRsjWPCBcCCZPwDCZVBVc
lhlgprMrlprbplzwZQPwwPjbZZCPwP
lpljllTGGGglhThpjSvdssSnfRRTdRnvsN
sDzjCqLLzddjsdRsSShgmtnCgFnmnffmmFcf
rJbqJMTqJGVTrgnFmfhcfmnJgm
GQbBWZGbVrqpqWpZZHlwDsDsRsdDlDRDBDsD
LbLbvbhQgblwwqbjGG
cFTTMsczJsTWJFfNNlVqvDqjNvlFqZ
mfMvJHvmdLgLRgpHRR
cvhRpWWhpfpcTpWvRcRcWVNwsjNLJFsJjwLtMLdsdsLJjL
ZZPqGqgZrllbbVMtnJtllwJtltnj
rrPCSQHbbrSqHqqZGGQbvzBVTpfzmvBvcvRCTpzT
VMzNNhWVlrbJHbjcJCjCSR
qgtDBgBtTGjqJvSPRJHCqHcd
GfnfLjjgGLmgBWpWrMMnzWZppl
zRtfBftCvvPSvPclZgcgJznWcgnq
dDpGpVdwdGphbDMpdQhnJjjqnZQWnZNcNWlqlJ
wdFdTDpGDSCmTtRqRq
bTGrRzjbmbmqsGDDjHPpWpfjHJZFVPJp
LwdwNNgMLfZTdCHPPd
lhtwtvttgnchcsrvmzTvmsTbbm
dfLjdlqLtqpbpPQpHS
ZGJnFZFDpBWWGBTzzrhmhHzHQPFPvQ
NgJGGGNGnJWgMDWGgDpWnZWgwdRCtwCCRVLdjwVcccdwct
MMtzRCTnVVnHbbMNrHMRRVQJFrPPDsrsJgjjQGJGpFFF
ZcqWqdfcmfhwDgGpDJmmQDQs
LhwBddvlddvdLCgCtCTzgzMN
ZffpWcfPcPrTwlVCvDhhcS
GMLBNHjMBGtmjtMQMJjLHTwwsSswdslhGwDhsDvCvV
tQgNRHMHQggHjQttbZqfFqrnqSZWfPZR
MDqbPdqGfwGbfMswqfJdPGgQpCZvQgmvJFCmQJQvRCQv
WFthczzzrpWgpHlRRC
BhLSFnFrcLzhtSFnSTznhGbMGwjGwjjPbGDqjdqTMd
zbQdJbBPTsWcCgdmfC
DNqZHjvwZMShDhwqvLmlgVnLmcnsfnVf
HHSFSjNZFqjZrhQpPtzrBgQzPrpB
BzzJHvJJvWsgzPPTWPSJsJgNtmMtNFlvNZFltFtttjmtVZ
cbccGnqhwhdpqRnnrdqdntZVFfMCltMtGFCmtFNFlj
wnlRRQbnpHQWHgSQTs
SQQBFnPzSnQVSzFSWlzlBSWFMsqmMmzLLChTmmMqzsTChmss
ZgdwrJdtJrgpcCwZNbbjsGhGDvMrrqmmMmDhTsqv
NtRZwCbZbbjRZNJcRbjWVWPnWHQWVPBQnHlfRB
jLtlpljLpsbRnDNtBpbjdqWcqChccbhqChqbWQbQ
gVwwggvJJwBqgWqfBCgT
VHZrPSHwzSwvDLnnLlsrDRBp
GBDGDrhwVrFhVCVBvhhvwBDVcmlfcPcMMmmmqNTScNNNflSF
RzRLRbddjZTbTQjJSWNzlNWNcPqNWqSf
dHjRgddHnZngjHLnQsgZHbGrrVpwpTtThnDBppVCTpDp
dpjwvdLwtvJszhmzhRVj
QfFQrffPBCBZMQrMRWzmzmVWVghVLs
GBPGBrFrHZTBSTqvvLNtqSpq
zFcGnQcZPZncbbbhPncpNCwzvwmjMvwwmwmpvd
tBRtdrRTJNvRjMMwRC
rlWSqVtTHqtVTrngQnfbQFdcghgW
RMjfvsbQPvvNpLmLprFJFrFJJT
SqCtGCcZZCwcCqqcGdWGdSZmMTmnVBdLnTTgTrMgrgVLTB
lGzGzHSCzHctsQRMsQPzDjNs
FQTWdTVMDWWVWFDTFcVcWJqTlCCCSlFmtCmNZStsmFmCwCgm
nPLbGZzrgwBlbBlS
PppGRnzPnpzvZVDJVvTfDVVVdD
CQlDsWWfflWDMMhRmTGqFwSjJFdqwSQJzF
PgpVbZPcHgBcgZrBZcHNTTbdqTGjSqFjRFjwSjGG
VvgRBBNLRrPhsfhLWLWDtW
hHhZDcDcPZWpLZWpCQ
pbqdwmbqqmBpdMsgdqjCGvfCWGTWLGmWfGQtVt
wjjbsFBRbwFgMpDznPDrrFcShr
zGmsJQsDBBmDDJJpRZzSqZZPRffWRSqh
LQlVHjCCNCLRSgWlZnhPZW
bLtHCHtjVHQDTJcGDQbs
QPRlnHfPllgRfnqhcwgwGMGzBWzBBBBB
LCtVCZtDbdttjZFtvjvdDMGGBmBWWZWBBWGSsWJSJm
dFVNTVbTjMnHlThHnpHR
hGhZLlqmqZWTcWrmWqrWmTrqjQVQwNHPgPwPPSgPjNwVSLjD
bsMJBRMvRsvsJMRRbspFgQwSNNSNwVNjgwDMDgHH
pFnFtvCQFsbBQzsBrmnTWchWZqWqWqGZ
wpwlJdCWJWdzlWGRRcrDrwRqrqDFrF
ZmPsSVnnTvmHDgFcDTHFTF
smVvnSQhbsNsvsmsnQQclzGCWpphppLJCdJWBpll
FfSmMJmBDfBjDSjFtBVmftBQPwPhPCbhQvbhwCCbvhhjhq
ZnZHZgclJWNbwbcbcwPrQv
ZNNGLHzHNZTTJnlFFfVmDBsFSVLdSD
DDBvjMvBJMtWjNRNrvdtbshTdpssdPSgpFpP
LwGQcwLGJTSssQbg
wcfcCcmHfJmcLLVZVqBBBqWDRqBRDWzHNN
LhnpcdcdrChplvllHptlgR
TsSTSBqPBTGNzqGfzfffGfVtPlHHvMDtHtRMlvjHHgtv
sBfWNGQmQbCgQhQn
pnnHngqsRjstjRgtrBDlBwDgwDZBldlD
SFvJMGhhvcbMSWPJbFzVDdzDZwDFlFlzfFBV
JJNWGSWSMNMCPhcvMhGStwtjtRRtRRqRsCtQjqRj
nQZfJswFffjJplqhlqZlVVhp
vtdCvGdBCzVHgnzLDlpL
BbCTGvtGnBBCPjrsccjrwbrFjj
wjjvDQwWvSQDLbwfNrrJcMHrczcpWN
tTnqlRsTRthFhnnpfNrmcTNMzfCzHr
slsBGVlqghMRhsRlltsFDgQSDbQwPSPLQSZjPSLQ
PcQmmQRQZRFQPjjDWhgCgWdM
nBGtbGNBBGvJbbtpWhCNCjmMjHlWHDdM
vbBnBBrrvVBtJJbvtzzptRQLLZLRFfqLSTSfzqwfqm
PBFZDFPsDZBnTTBdDHSNSpNzmVTVmVGlNH
WvqFLWQCMQLMRtQJFWQLvQCJVzmNjNzVCllVmGSlNHlVzljH
WRtrhtWQWFbrrBwBZrbn
MwWnMPnMPNswjPDvRbsblCGFZGZF
JdJVVVtLdgZhvGVBDZhZ
rqmdqtgcLQLTfWffwGGmmp
QQhhWzQWsMhZjbbmffgfjrGDdfdGvv
HnCJVHcnnHttCRVRCcnBCqJBGfPmTvTvdDfvqfrddNDDggGG
wBwwcRBBCJpFcFcpnVVFQWQLSLbQZLmhzshMlMwQ
CgDNbsDcHjTcgDCgjRHMJrlHFrBHFmrttrGGtFwG
VfQJnvJdhvSJZphSzWpvSzZSltGGBllGBqPPFPrwrmfqtFFB
VJLvdQhphhQnjLsjDDjDcRbL
LjljTPdLdccLhcMZhTTMdzrrtzGgtvrgnttNDGrWtDgn
hbCmCHqHmSbRgNrtvCgGgttN
SJFJRFpHqwSFSpsHwbHwRhSJPTjMMMPdPlPLcVQscLVQQVlL
QmTTQVqrVrMvbCwLczbRlQ
sSNtNGZFjBSsjSSShcRvwCFLlzWcWRzCWv
LLNjZhSGZBnjhJjjrrTgPqgPgTfqfJpf
DCCjDDtHVptCtvMZlJbSnScWWfHlhW
qsTFmTgmqRRLswQGmfWwSnZSSfJSSWZcWb
dsmqgqdsNgTFLFRLGmRpBtBDtDNVpPCCfVrtpD
LLNRhHhRbsNGjqCBPBrLCw
lgcFfvWGTllzfJVVFVWDzFqqMrZCMBrZZqvSrCPZSSrr
fFGGlTTTlzWQGzzDFttQmHnpnhtmmpRssm
LZNnBgtlNZztzmGHmpHHPPPm
QwjjQRCQScbFFFchhFrFjwmsNPHSSWJGsGppMSWMmWqs
dQCwwbwhrjQQjCwRwbhRBlDDfBtVlnNnlgLdnvvd
wRbGbqqGCwnGTRqBqlMVphpgMgMFdnFVnt
cgzvssscgHJVdhDdhDMvDM
PjcZcsJrJHWgrPBQmCqRBPSSRCSb
rHBmLlPLlTzztvRtGsVL
NWJJWWjJDJWWhphqwCFCwzvRVcgRtctRgNNVVscsGc
hqCCsnCpCDnbCnWhwpbHbBHmMBMMmdPrZfdP
GRPprPQdsprGpGgGTlqfVqnZLgnLnwNZLw
CCWJMMvhhCvthtCjvDWFjMcCVZJLNnfqnllwzlzNnzzwVNnN
cDtZFjDjcMCDDtZFSMCvvDpmsmSRRpmmbSpdPRdTmTsp
mmPpsbZZbbzvzgbrZRPgPMWqtHtqDnGCnMWCDwGHwtwW
cBFBNNccsTLjJjfcjfGDGQtWwFCnCGtqCCQH
TNsTLJlffdldzvrmbmrPzp
"""



day2 = """
C Y
C Z
B Z
A Z
A Z
A Y
A Z
C Y
C Z
A Y
A Y
B X
A Y
C Z
C Z
B X
C Z
A Z
B Y
C Z
A Y
C X
B Y
A Z
B Y
C Z
B Z
B Y
C Z
A Z
A Z
B Z
C Z
A X
B X
C Y
C Z
C Z
C Z
A Y
C Z
C Z
C Z
C X
A Z
A Z
C Y
A Z
C Z
C Z
C Z
A Z
B Y
C Z
A Z
B Z
A Z
A Y
B X
B X
C Z
C X
C Z
C Z
A Z
B Z
B X
B X
B Y
C X
C Y
A Y
C Z
A Y
C Z
A X
B X
B X
C X
B X
B X
A Y
B Y
C Y
A Z
C Y
B Y
B X
B X
B Z
B X
B Z
A Z
B Y
C Z
B Z
B Z
B Y
A Y
C Z
A Z
C Y
C Z
B Z
C Z
C Z
B Y
A Z
C Z
C Z
A Z
A Z
B X
C Y
A Y
C Z
B Y
C Z
A Y
C X
C X
B Y
C Z
C X
C Z
B Y
A Y
B Z
C Z
B Y
C Y
C Z
C Z
B Z
C Z
A Z
A Y
C Z
C Z
B Y
A Z
C Z
C Z
C Y
B Y
C Z
C Z
C Z
C Z
A X
B Y
C Z
B Y
C Z
B Y
C X
C Y
A X
C Z
B X
B X
A Z
A Z
A Z
B Y
C Z
B Z
A Z
B Y
C Y
C Z
C Z
C Z
C Y
C Z
B Y
C Z
C Z
B Z
A Y
B Z
C Z
C Y
A Z
C X
B Z
C Y
B Y
C Z
C Z
A Z
C Y
C Y
C Y
B Y
C Z
C X
B Y
C Z
C Y
B Z
A Y
C Z
A Y
B Z
A Y
A Y
B Z
A Z
C Z
C Z
B X
C Z
C Z
B X
B Y
C Z
C X
A X
C Z
C Z
C Z
B X
B X
A Z
C Z
C X
A Z
C Z
C Z
A Z
B Z
C Z
B Y
C Z
A Y
B Z
C Z
C Z
C Z
C X
A X
A Y
B Y
C Z
B Y
C X
A Y
C Z
C Z
B Y
B Z
C Z
B Y
B Y
B Y
A Y
C Z
B Z
A X
B Y
C Z
C Z
C X
A Y
C Z
A X
B Y
A X
A Z
B X
B X
C Z
C Z
A X
C Z
A Y
B Y
B Z
C X
C Y
B X
C Z
C Y
B Y
C Z
C X
B Z
C Z
C Z
C X
C Y
C Z
A Y
C Z
C Z
C Z
C Z
C Z
C Y
B Y
C Z
A X
A Z
C Y
B Z
B X
A Z
C Z
C Y
C Z
C X
A Y
C Z
A Z
B Y
B Z
C Z
B Z
A Y
C Z
B Y
C Z
C Y
C Z
C X
A Y
A Y
C Y
C Z
C Z
B Y
A Z
C Z
C Y
A Y
A Z
A Z
C X
C Z
B X
C Y
C Z
C Z
B Y
C Z
B X
C Z
B Z
B Y
C X
C X
A X
B Y
A Z
C X
B X
A Z
C Z
C Z
A X
A Y
B X
C Z
A X
C Z
B Y
C Z
A Y
B Y
C Z
B Z
B Y
A Z
C Z
A X
B Z
C Y
B Z
B Y
A Z
A Y
A Z
A X
C X
A X
C Y
C Z
A Y
C Y
B X
A X
A Y
C Y
B Y
C Z
C Z
B Z
C Z
C Z
C Z
C Z
C Z
C Z
C Z
B Y
C Z
A Y
B Y
C Y
C X
C Z
B Z
B Y
C Y
C Z
A Z
C Y
B Z
C Z
A Z
C X
B Y
B Y
B Y
C Z
B Y
A Y
C Z
C Z
A Z
A Z
C Z
B Z
B Y
C Z
B Y
B Z
C Z
A X
A X
C X
C Y
A Y
C Z
A Y
A Z
C Z
C Z
C Z
B Y
A Z
B Z
C X
B X
C X
B Y
C Z
A Z
C Z
A X
B Z
B Z
B Y
A Y
C Z
B X
C Z
B Z
C X
A X
C Z
C Z
B Z
B Y
C Z
C Z
A Z
C Y
C Z
B Y
A Y
B Y
A Y
C Z
C Y
B Z
A Y
C Z
B X
B X
B X
C Y
C Z
A Y
C Z
C Z
C Z
A Y
C Z
B X
A Z
C Z
C Z
A Y
C Z
C Z
B X
C Z
B Y
A Z
C X
C Y
C Y
C Z
C Y
A Y
B Z
C Z
C Z
C Z
B Y
C Z
C Z
A Y
A X
A Y
C Y
C Z
C Z
A X
B Z
C Z
C Z
B Z
B Y
C Z
A X
C X
A Z
B Z
C Z
A X
C X
C Z
B Y
A X
A X
C Z
C Z
B X
C Z
B Z
B Y
A X
C Y
C Z
C X
A Y
B Y
C Z
C Z
C Z
C Z
B Z
A Y
C Z
C Z
B Z
C Y
B Z
B X
B Y
A Z
C Z
A Z
B Y
C Y
C Z
C Z
C Z
B Z
C Z
C X
C Z
B X
C Y
B Y
C Z
C Z
C Z
C Z
B Y
B Y
C Z
B Y
C X
B Z
A X
C X
C Z
B X
C Z
C X
C Z
A X
A Z
B X
C Z
C Z
B Y
C Z
A Y
C Z
C Z
C Y
C Z
A Z
A X
C X
B Y
A Y
B Y
A X
C Z
B Y
B Y
C Z
C Z
B Y
B X
A Y
C Z
B Y
C Y
C Z
C Z
C X
B Y
A Z
C Z
A Z
A X
C X
A Z
C Z
C Z
A X
B Z
C Z
B Y
A Z
A Y
A X
A Y
A X
C Z
A X
B Y
A Y
B Z
C Y
C Z
B Z
C X
A Y
A Y
C Z
C Y
C Z
B Y
B Y
B Y
B X
C Z
C X
B Y
C Z
C Z
B Y
C Z
C Z
B Y
C Z
C Y
C Z
C Y
C Z
C Y
A Y
A Y
C Y
C Y
C Y
C Y
C Z
C X
B Z
B Z
C X
C Z
B Y
B Y
A Z
C Y
C Z
C Z
C X
C Z
C Z
A Z
B Y
C Z
A Y
C Z
C Z
C Z
A Z
C X
C Y
B Y
A Z
B Z
C Z
B Y
C Z
B Z
C X
A X
C Y
A Y
B Z
B Y
A X
C Z
B Z
C Z
C Z
C X
B Z
C X
A Z
B Z
C Z
C Z
C Z
B Y
A X
C Z
C Y
C Y
C Z
A Z
C Z
C Z
A X
C Y
B Y
A Y
A Z
A Z
B Z
C Z
A Z
B Y
B Y
A Y
A Z
A Z
C Z
C Z
C Z
A X
C Z
B Z
B X
C Y
A Z
B Y
C Z
B Y
A X
C Z
A Z
C Z
B Z
C Y
C Z
B Y
A Z
B Z
A Y
B X
C Z
B Y
C Z
C Z
C X
C Y
C Z
B X
C X
A Y
A Y
C Z
C Y
B Y
C Y
C Y
C Z
A Y
A Z
B Y
C Z
C Z
A X
C Z
C Y
C Z
B X
C Y
A Z
A Y
A Z
C X
C Z
C Z
C Z
B Z
C Y
B Z
C Z
B Y
C Z
B Y
A Y
B X
C Z
A Y
C Z
A Y
A Z
A Z
B Z
A Y
C Z
A X
B Y
C Z
B Z
C Z
A Y
A Y
B Z
B X
B X
C Y
C Z
C Z
C Y
A X
B Z
C X
B Y
C X
B X
C X
C X
C Z
A Y
C Y
C Z
B Z
A Z
A Z
C Z
A Z
C Z
A Z
A X
B Y
A X
A Y
C X
B Y
C Z
A X
B X
C Z
C Z
C X
B X
A Z
B X
C Z
B Y
C Z
C X
C Z
C X
C Z
B Z
B Y
C Z
B X
C X
C Z
C Y
A Z
B Z
A X
B X
B X
C Z
B Z
C X
A Y
C Z
C Z
B Y
C X
C Z
A X
B Y
C Z
C Z
C Z
C Z
C Z
A X
A Z
C X
A Z
C Z
A Z
C Z
B Y
B Z
A X
C X
C Z
B Z
A Z
C Z
C Y
C Z
C Z
C X
A Y
B Y
C Z
A Y
C Z
B Z
C X
B Z
B Z
B X
B Z
C Y
C Z
C Y
B Y
C Y
C Z
C X
C X
A Z
B Y
C Z
A Y
B X
C Y
A Y
A Z
B Y
B Y
A Y
B Y
B Z
A X
C Z
B Y
A X
C Z
C Z
C X
B Y
A Z
A X
B Y
A Z
C Z
B Z
B Z
B Y
B Y
A Z
A Z
A Y
C Z
C Z
A Z
C Z
C Z
C Z
A X
C Z
A Y
C Y
A Z
C Z
B Y
C X
B Y
C Z
C Z
C Z
A Z
B Z
B X
C Z
C Z
A Y
B Z
B X
C Z
C Y
A Y
C Y
C Y
C Z
C Y
C X
C Y
B Z
B Y
C Z
A Z
A Y
C Z
C Z
B Y
B Y
A Z
A Z
A X
C Z
C Z
A Y
B Y
C X
C Z
C Z
A Z
C Z
B X
B Y
A Y
C Z
A X
A Y
C Z
B X
C X
B Z
C Y
C X
B Y
B Y
C Z
C Z
C X
C Z
A Y
A Z
C Y
C Z
A Z
C Z
C Y
A X
C X
C Z
B X
C Z
B X
C Z
C Z
C Z
B X
B Y
B Y
B Y
C X
B Y
C Z
C Y
C Z
C Z
B X
C Y
B Z
C Z
C Y
C X
C Z
A X
A Z
C Z
C Y
C X
C Z
B Y
C X
C Y
C Z
C X
A Z
B Y
B X
C X
C Y
B Z
C Z
C Y
B Z
C X
A Z
A Y
C Z
C Z
C X
B Y
C Y
C Z
A Z
B Z
B Y
B Y
B Z
C Z
A X
B Y
A Z
A Y
C Z
C Z
B Y
C Y
C Z
B Z
A Z
B Z
C Z
C Z
B Y
B X
C Z
C Y
C Z
A Y
C Z
A X
C X
B Y
B X
C X
C Z
C X
B Z
C Z
A Z
B Z
C Z
A X
C Z
C Z
A Y
B Y
B Z
B X
B Z
C X
B Y
C Z
C Z
C Z
A Z
C Z
C X
C X
B Y
C X
C X
C Z
C Z
A Z
C Y
C Z
C Z
B Z
C Z
A Y
B Y
C Z
C Z
B Y
B Y
C X
C Z
B X
A Y
B Z
A Y
A Y
A Y
C Y
C Y
C Z
B X
B Z
C Z
C X
C X
B Z
A Z
A X
B Y
C Z
B Z
A Z
B X
C Z
A Y
C Z
A Z
A Z
C Z
C X
C Z
C Y
A X
B Y
C Z
C Z
C Z
C Z
C Z
A Y
C X
C Z
A Y
B X
C Z
A Y
C Z
C Z
C Y
B Z
B X
C Z
A X
B Y
C Z
C Z
A X
A Y
C Z
C Y
B Y
C Z
C Z
A Y
A Y
A Y
A Y
C Z
A X
A Z
B Y
B Z
A Z
C Y
C Z
C Z
C Z
A Z
C Z
A Z
C Z
C Z
A Z
C Z
C Z
A Z
B X
C Z
A Y
B Y
C Z
A X
C Z
A Y
C Z
C Z
C Y
C Z
A X
B Y
C Z
A Z
C Z
A Z
A Z
B Y
C X
B Y
C X
C X
C Z
A Y
B Z
A Y
C Z
C Z
B Z
A Y
C Z
B Y
C Z
A X
C Z
C Z
C Z
B Z
A X
B Y
C Z
A X
C Z
C X
B Y
C Z
A Y
C Y
B Y
A Y
C Z
A X
B Y
A Y
A Z
C Z
C Z
C X
A Z
C Z
C Z
B Y
B X
A Z
C Z
B X
C Z
C Y
C Z
C Z
C Z
C Y
A Y
C Z
C Y
C Z
C Z
B Y
B Y
B X
C Y
B Z
C Z
B Y
C Z
C Z
C Z
A Z
A Y
C Y
C Z
C Z
A Z
C Z
C Z
C Z
B Y
B X
B Y
A Y
C Z
B Z
C Z
B Y
B Z
A Y
C Z
C Z
C Y
A Y
C Z
C Z
B Y
A Z
A Y
C Z
C Z
B Y
C Z
B Y
B Z
C X
C Y
C Z
A Y
C Z
A Z
A X
B X
C Z
C Y
C Z
C X
B X
B Y
B Y
C Z
C Z
C Z
A X
B Z
C Z
A Z
A Z
C Z
B Y
B X
B Y
C Z
B Z
C Z
B X
B Z
C Z
B X
A X
C Z
C X
B Z
C Y
C X
C Z
C X
A X
A X
C Z
C Z
C Z
B X
B X
C Z
C Z
C X
C X
C Z
A Y
B Y
B Y
B Y
C Z
C Y
C Z
C Z
C Z
B Y
C Y
C Z
B X
C Z
A X
C Y
A Y
C X
A Y
A Z
C Z
B Y
B Y
A Z
C Y
B Z
B Z
A X
B Y
C Z
B X
A Z
A Z
C Z
B Z
A Z
C X
B Z
C Z
C Z
C Z
C Z
B X
B Y
C Z
C Z
C X
C Y
A Z
B X
B Y
B Z
C Z
B Z
C Z
C Z
C Z
C Z
A Y
C X
C Z
A Y
C Z
C Z
B Z
C Z
A Z
C Z
A Y
C X
C Z
A X
C X
C Z
C Z
B Y
C Z
A Z
C X
C Z
B Y
A Y
B Y
C Z
B X
A X
C Z
B Y
C Z
B Y
A Z
A Z
C Z
A Z
B Y
C Z
C Y
B X
C Z
A Z
B Z
C Z
C Y
C Z
B Z
A X
A X
A Z
C Z
C Z
C Y
C X
C X
A X
C X
B X
C X
A Y
C Y
C Z
C Z
C Z
C Z
C X
A Y
C Y
A Y
B X
C Y
C Z
A X
A Z
C Z
C Z
B Y
C Z
B Z
C Z
C Z
A Y
A Y
C Z
C Z
A Z
C Z
C Z
B X
C Y
C Z
C Z
C Z
C Z
A X
B Y
B X
B Z
C Z
A Z
A Z
B Z
A Z
B X
C Z
B Z
C Z
A Z
C Z
C Z
A Y
B Y
C Y
B X
A Z
C X
C Z
C X
B Y
B Z
C Z
C Z
C Z
C Y
C Z
A X
A X
A Y
C X
C X
A Y
B Y
C X
C Z
C Z
B X
B Z
B X
C X
B X
A Y
C Z
A Z
C Z
C Z
C Z
C Z
C X
A Z
B Y
C Z
C X
A Y
A Y
C Z
C Z
B Z
B X
C Z
A Z
B Y
C Z
C Z
B Y
A Y
C Z
B Z
B Z
A Z
C X
C Z
B Z
C Z
C Z
B Y
C X
B Y
A Z
C Z
A X
C Z
B Y
C Z
A Z
B Z
C Z
A Z
A Y
C Y
B X
C Z
A Y
C Y
A X
A Z
A Y
C X
C Z
C Z
B Z
A Z
C Z
C Z
C Y
C X
C Y
B Y
C Z
B Y
C Y
C Y
C Y
A X
C Z
C Z
B X
B Y
C Z
A Y
C Z
A Y
B Z
C Z
C Z
C Z
A Y
A X
B Z
B Y
A Y
A Y
B Y
B Z
C X
A Y
B Y
C X
C Z
C Z
B Y
C Z
C X
C Z
C X
C Z
A Y
A Y
B Y
C Z
A Z
C Y
C Z
A X
C Y
C Y
C Y
A Z
C X
C Z
C Z
A Z
C Z
B Y
C Y
C Z
C Z
C Z
B Z
C X
C Z
C Z
C X
C Z
C Z
C X
C Z
C X
B Z
B X
A X
C Z
A Y
C Z
B X
C Y
A X
C X
B Z
C Z
A Y
A X
C X
B Z
B Z
C X
A Y
C Y
A Y
C Z
C Y
A X
C Z
A Y
A Z
C Z
B Y
C X
A Y
A Y
C Y
B Y
A Z
B Y
C X
A Y
B Z
B Z
C Z
C Y
C Z
B Y
C X
C Z
C Z
A Y
C Z
C X
A Y
C Z
C Z
B X
C Z
A X
C Z
A Y
C Y
A Y
B X
C Y
C Y
A Y
C Z
A Z
C Z
C Y
C Z
A Z
A Z
C Z
C Z
C Z
C Z
C Z
A Y
A Z
B Y
C Z
A Y
C Y
C Z
A Y
C X
C Z
A Z
C Z
C Y
C X
C Z
C Y
A X
B Y
C Z
A Y
A Z
C X
C X
C Z
A Z
C Z
C Z
C Z
C Z
A X
C Z
C Z
C X
C Z
A Y
C Z
C Z
B X
B Y
C Y
B Z
C Y
C Z
B Y
A Y
A Y
B Y
A Z
B Z
B Y
A X
C Z
B X
A Y
C X
C Z
C X
C Z
C Z
C X
A Z
B Y
A X
C Z
C Z
B Z
C X
C X
B Z
A Y
A Y
A Y
A Z
C Y
C Z
A X
B Y
C Z
B Y
B Y
C Y
C Z
C Y
B Y
C Z
B Z
C X
C X
A X
C Z
C Z
B Z
A Y
A Z
B X
B Z
B Y
C Z
A Z
C X
A Z
B Y
C Z
B Y
A Y
C Z
A Y
B Z
C Z
A Z
B Z
B Y
B Y
A X
B Y
B Y
C Z
B Y
C Z
B Z
A Z
A Y
C Z
B Y
C Z
C Z
C X
C X
C Y
B Y
C Y
A Z
C Z
A Z
C Z
B Z
C Y
C Z
A X
B X
A Z
A Y
A Y
C Z
C Z
C Z
C Y
C Z
C Z
A Z
A X
B X
A Z
C Y
C Z
B Y
A Y
A Y
B X
B X
C Z
C Z
C Z
C X
C Z
C Y
C Z
A Y
C Z
C Z
C Y
A Z
B Y
A Y
B Y
B Y
A Y
A Y
B Z
C Z
C X
B Y
C Z
C Z
C X
A Z
B Y
A Z
C Z
C Z
B Y
C X
C Z
C Y
A Y
C Z
A Y
B Y
A Y
C X
C Y
C Y
B Y
B Z
A Z
C Z
C Y
B Z
B Y
A Y
A Z
A Y
A Y
B X
C Z
A X
B Y
B Y
C Z
B Y
B Y
B Z
C Z
A Y
C X
A X
A Y
C X
A Y
A Z
C Z
B Y
B Y
B Y
C Y
A Y
B Z
C Z
C Z
B Z
C Z
B X
C Y
B Y
A Z
C X
A Z
C Z
B X
C Z
C Z
B Z
C Z
A Z
A Z
B Y
C Z
A Z
C Y
B Y
B Z
C Z
C X
C Z
A Z
C Z
C Y
C X
A Y
B Y
B X
C X
C Z
A Z
C X
B Z
C Z
A Y
C Y
C Z
A Z
C Z
A Z
C Y
C X
C Y
B Z
B Y
A Z
A Y
B X
A Z
C X
C Y
C X
C Z
C X
A X
C Z
B Y
C Z
A Y
B Z
C X
B Y
C Z
A Z
C Z
C Z
C Y
A Y
A Z
A Y
C X
B Z
A Z
C Z
C Z
C Z
A X
C Z
A Z
A Y
C X
B X
C Z
C Z
A X
A Y
C Z
C X
C Z
A Z
C Y
C Z
B Z
C Y
C X
A Y
A X
A Z
C Z
C Z
C Z
C Z
A Y
C Z
A Z
A Y
C Z
B Z
B Y
C X
C Z
C X
C Z
B X
A Y
C Z
B Z
A Z
A Z
B Z
B Z
C Z
C Z
B Y
C Z
A Y
C X
A X
A X
C X
C X
B Y
B X
A Y
C Z
B X
B Y
A Z
B Z
A Z
A Z
C X
C Z
A X
A Y
C X
C Y
C Y
C X
A Z
C Z
C X
C X
A Y
A X
C Z
C Z
B Y
B Z
C X
C X
C Z
B Z
B Z
B Z
B Z
B Y
B X
C Z
C Z
C Z
C X
C Z
C Z
B Y
C Z
C X
B Y
C Z
C Y
B Z
C Y
C Z
C Z
C Z
C Z
C Z
C Z
C Z
A X
A Y
C Y
C Z
A Y
B X
C Z
B Y
C Y
C Z
C Z
C Z
C Y
C Z
A Z
B Y
A Z
C Z
B Z
C X
C X
A Z
C Z
C X
C Z
B Z
C Z
C Y
B X
C Z
A Z
C X
B Y
B Y
C Z
C Z
C Z
B Y
C Z
B Y
A Y
B Z
B Z
B Y
C Z
B Z
A X
C Z
C Z
C Z
B Y
B Y
C Z
C Y
C Z
B Y
C Z
B X
B Z
C X
B Y
C Y
B Y
C Z
A Y
B Z
C X
B Y
A Z
C Z
C X
A Z
B Z
A Y
C Z
C X
B Y
C Z
C Z
B Y
B Z
C X
C X
C Z
C Z
C X
B Z
A Y
C Z
C X
A Z
C Z
C Z
C Z
C Y
B Z
A X
B Z
B Z
C Z
C Z
B Z
C Z
B Z
A X
B Z
B Y
B Z
B Z
B Y
C X
A Y
B Y
B X
B X
A X
C Z
C Y
C Y
C Y
C Y
B Y
A X
C Y
A X
C Z
B Z
C Z
C Y
B Y
A Z
C Y
A Z
B Y
B X
C Z
A X
A Z
C Z
C Z
A X
C Z
C X
A Z
C Y
B Z
C Y
B Z
A Y
A Z
C Z
A Y
C Z
C Z
A X
C Z
C Z
C Z
B Y
C X
C Y
C Z
B X
A Z
C Z
C X
B Y
A Y
B Y
C Z
C Z
C Z
A Y
A X
C Z
C Z
C Z
C Z
B Y
A Z
C Z
A X
A Y
B Z
"""
day1 = """
5118
5554
4186
4729
1242
4360
1427
5312
6012
1017
5581
5203
3811
4945
3960

3812
7757
4448
2205
15715

4164
6482
4479
3061
4082
2474
1175
1918
4755

4056
5122
11426
5529
3659
9592
10257

3435
3106
4933
2695
3107
6567
5579
1463
5734
4547
4532
2152
5132

6074
11600
4337
3444
7637
6725
1189

5637
1226
7068
6290
4411
3858
6677
1858
2840
1175
5056
6569

32887
19643

4951
2276
4300
4473
1895
5251
1770
4623
4602
4925
1769

68012

5760
2687
3192
2730
4867
4723
2591
1677
4458
4388
6038
3127
6416
3048

2485
1630
1595
2864
2125
3852
2216
3883
4293
4165
2762
4016
2508
1396
4541

5918
6874
6644
4024
3229
1318
1851
1566
1035

7625
1369

3894
18802
1362
12368

10251
6249
2784
9394
5932
5610
7201
9922

10994
10092
4121
2966
1178
2235
9379

2592
1895
1740
4357
5314
1068
2228
3775
3949
7162
3078
1450

9484
1796
8055
7901
9323
1982
2517
8358
2614

18536
23454
12107

6703
6966
1086
7022
3487
3871
2568
6441
1216
2105
5100
2945

3268
4866
3569
4374
3666
2477
3263
1312
5121
6592
5337
1417

17864
11775
1345
11675

6636
1678
3982
4552
2719
2736
1342
6375
2671
1541
1093
5538

21177
36871

4608
5474
5004
3229
2744
1577
2182
4518
4930
1986
5776
5023
2070
5342
1952

13940
15506
13799

3672
3303
4866
5507
5282
5768
2847
2214
1688
2255
4302
4962
4585
4285
3602

4766
4358
4532
10741
13311
2271

3073
5990
8256
3692
4658
4561
6347
3260
6938
8643

5261
1524
1671
3277
2326
5603
5837
1638
5104
3696
1910
2319
2305
1373
4801

2593
3527
1517
4626
2003
4414
4677
2282
3000
1457
3530
5344
1890
1703
1268

9002
7173
3848
6891
1741
5303
1670
1342
1865

10319
10539
2972
4667

4318
1366
1430
5003
2691
7117
3015
6516
6895
1618
3189
6739

2494
7140
2905
8784
8727
4711
2284
6894
7030
1688

1853
7351
7815
3222
8276
1461
5028
8048
5534

12546
6236
20372

2778
5745
2783
5774
4508
3691
6097
4637
5643
5902
1166
1208
3983
5030

3767
2558
3988
1056
6570
5437
1920
2822
9126

3173
3242
5762
4311
5206
3892
4978
5065
1319
2577
1347
3232
1915
5986
3536

2308
2812
1119
3845
4589
4779
1503
3613
1576
3827
1468
1533
5896
4981

9740
16395
19471
12882

4779
7293
12593
15897

36970

2386
1094
2957
4452
4005
2723
1124
3533
2671
1701
2508
3075
4741
1471
3416

37202

5272
2736
4756
2235
4679
4093
1773
4088
2419
3192
4429
3959
5230
4342

8514
11430
5023
9565
3726
11026
6334

6563
2638
12569
3458
5449
1216

1320
4708
1627
4189
3962
1463
2628
5667
5494
6105
4925
3540
1613
2288

5974
7710
5200
4859
2346
5619
1337
4814
1359
3020
1798

2744
1957
10669
4877
3507
7657
7748

1021
4297
1689
6925
16175

7147
11617
5654
11861
6065
3090
1744

3782
6658
2389
4339
2312
7245
2039
3411
6251
1778
2345
5814

13113
10123
18700
6991

16138
11645
18610

9586
6653
1001
4547
2891
2726
7618
5679
1567

2380
1858
1059
1160
5115
2588
1969
2629
5525
5831
2139
5469
2783

10606
4518
9057
5905
4187
4693
4396
2191

4374
4407
1083
7787
7716
7505
10096
10650

5809
4387
3426
3730
3699
4944
4176
2681
5197
1325
5920
4957
5876
5345

20155

1243
11423
13133
4539
4880
4276

1073
1316
1841
5102
1196
4847
1293
2424
2345
2298
4214
4215
5760
5775

4542
1152
5164
5642
2069
1419
5614
7343
1507

2840
3922
3563
1856
5216
4886
3794
4637
1826
3520
5582
4602
2442
3631
4946

7956
3248
7897
7846
2054
5576
3753
3378
1899
3490
6142

9837
10901
15019
1735
5306

3246
2485
5573

2722
2084
18774

7940
10855
8498
5547
13550
4239

1857
7355
4374
6798
2341
13128

14215
9770
2447
1035

8426
1873
4518
2812
7611
2465
4770

8166
19955
6472

10884
11212
1463
2716
1796
12003
1240

2802
2639
3268
2492
6676
8851
4054
9603
5354

1483
3080
6696
8713
6856
4796
7728
4600
3616
8565

26580
15329

6074
15758
5707
13583
2595

4957
9125
6534
8684
1728
3690
7983
4131
8907

12147
15776
14765
17316

27492
12173

5967
1170
7896
7865
7945
2261
2026
1751
3988
3759
5258

20764

7020
7441
8780
6111
3483
8606
4547
8153
3543
6791

5397
4408
1572
2315
3376
2021
1140
2876
5045
6034
4404
5705
3814
3981
3814

6836
3601
7452
8519
2302
2382
8481
1455
7154
6565

2077
5139
5462
1508
2094
4850
1688
4382
1991
2297
1930
4720
4995
2891
1967

2201
3673
9817
7417
1283

4988
3052
2258
6022
3678
2938
7073
6437
2402
5973

2492
4592
1501
4818
3141
3470
2821
4367
4952
2779
2237
4283
5625
2935

2422
5273
4053
4471
1343
1128
4538
4328
2974
3674
4155
5472
3520
2427
4145

19383
13539
9822
2453

2244
3506
2573
3837
1725
5081
4668
4438
2414
1446
1862
2453
2049
4867
5438

16970
5265

7417
8051
7490
1175
11316
4219

1065

6974
1232
6746
3660
3883
5403
3793
4956
4253
2237
5815

6537
4906
11084
7541
10019
5164
11601

4215
4216
1160
2096
1453
6271
5534
4353
6423
4060
6811
4701
3383

2138
12998
19743

8678
6328
6426
7184
8008
7896
5365
9506
1955

1498
19856
7833

17023
7023
21278

2110
5542
7191
6509
8813
5236
7771
9593
1262

11625
19032
17458

5266
4751
7950
2185
7837
5710
2053
7332
7422
6356

5781
1330
2974
2628
7407
7339
3767
5411
3400

5330
3441
6203
5272
5867
6034
3167
2187
6006
6614
1089
2485

3792
4129
1207
1121
3599
6143
4394
5550
1488
2675
6064
1527
4429

1606
1129
5426
5260
3827
5595
2286
1974
7525
1290
4569

2181
5045
7730
5502
5467
7720
1780
4553
1188
4213

2565
10635
12032
3283

9902
2896
9653
6296
2656
11583
5835

4932
4548
3832
2377
3371
2612
1907
3494
4567
3130
3375
2750

7757
1033
8201
13544
13481

3382
12952
9450
4982
13966

4691
3678
1026
7359
1885
1245
5281
8602
6744

13041
9202

3621
3558
2279
2854
6415
5368

1102
5319
5768
1990
2526
1900
6294
4744
3655
5011
3092
2697
3864

12013

27776
14644

5434
1501
1439
4972
1365
6076
1428
6291
6020
5509
3835
2571
6308
1483

3972
9357
8383
11037
9557
10966

8344
1761
10183
4200
3936
5778
9722
1298

3962
2611
7361
1156
2522
2462
4249
5127
1443
5989
2942

5384
7053
2194
11964
5937
7708

3052
3192
3224
5708
2120
5756
6107
1198
5519
3803
1169
2903
5942
4376
3675

11517
9051
2084
4508
4197
7219
9902

4566
5562
4263
1970
1965
1333
1601
2665
3443
5463
4981
3792
2588
3282

1243
3604
4947
1044
6962
2276
2828
6334
2508

1339
3050
10158
2095
7779
5165
9420
6101

4512

3273
2248
2082
12415
13944

5638
5204
3327
1361
3775
3421
7597
1917
1802
3896
4058

1901
1813
7388
3861
6838
6154
5500
3086
6403
3654
7471
6904

1932
1303
1930
1720
5505
1595
2260
5629

38957

4629
3672
3629
5011
5182
3952
2295
4943
2644
2851
5894
4654
5257
3972

48469

3481
1398
3837
2611
3330
3229
7619
4106
6816
3486
2763

6591
2522
6262
5458
3025
2804
6403
1390
2964
3081
3449

6408
3223
4302
1079
5836
5580
1538
2616
3850
5272
3688
2381
5775
5497

1891
1448
4283
5965
2726
1425
5399
2795
1583
2489
5171
3133
2547
5117
3092

11463
11581
6972
5410
3675
8578
4283

1398
1747
1341
5365
5086
2268
4544
5286
5910
1393
4580
4726
1123
3949
1223

7526
3223
5495
7184
10259
7681
4795

7168
6278
7939
3829
3670
7969
4917
7406
9035

5687
4872
2967
10772
9196
6207
6244
2801

3500
1786
1517
1585
4536
2645
5249
4808
5681
4591
5595
2751
3336
1615
2200

6894
4752
1794
6507
2184
5589
3016
4532
2321
6843
2909
2104
4065

24126

3293
8274
1297
4841
4653
1817
1972
6169
1001
7070

6969
5331
4779
5316
5249
3315
4355
3596
3868
5647
1110

5235
5846
5619
6259
4372
2600
7526
3962
3840

4260
4484
6361
4276
6344
4776
1173
1884
4572
1411
5230
3976
1800
2426

19185
15235
19905
8664

3346
7532
8840
2182
10048
4181
5030
8078

2080
2279
6250
3388
6097
4607
6262
4259
3261
4653
3338
7025

1138
2851
5912
8592
7341
3596
7669
1030
7624

6551
6753
7807
4296
3515
6873
5010
8497
1742
5767

8921
7840
9067
3809
4347
2876
3886
9982

11455
10295
15198

1574
4240
4052
1739
5701
8449
5055
3893
2700

3864
4306
4190
1165
1708
5705
5654
6753
3840
4139
2121
5735

1662
3541
2480
6124
3355
5737
5537
6806
7953
1109

14180
15876
25965

7732
33422

5918
5146
6768
9366
1687
1440
3115
1065
6514

2316
4905
2945
5351
6196
6207
5751
3811
4765
1419
5253
1616
2274
6363

5125
2491
5057
2749
1586
4997
5249
3944
3964
3845
2457
5972
5313
6453

30602
6865

4413
1651
6256
6524
3466
1160
4599
6477
2681
1855
4785

6435
5377
6008
1744
5182
4469
3999
2913
3367
3233
2369
1712
5408
4622

4201
5475
1117
2679
2649
1446
4043
1136
3750
4523
3800
3245
3179
6183

7682
7213
5144
1557
5579
5005
6307
5906
7244
6230

1205
2764
3576
5212
1723
4138
1801
1772
4809
1429
2010
3093
4435
2268
4904

4386
6822
1865
3688
6771
5433
1430
4870
6745
5758
4456
6549
6203

2413
3287
3376
5780
1190
1177
1577
4375
5558
5117
6773
2483
4436

5870
4195
5932
1117
5072
4581
6922
2695
3134
2021
3327
5538
2324

2609
4270
5809
1096
6794
3530
3222
4881
3806
2887
7158

2989
5279
6821
2474
3144
8621
3854
5012
1144
1354

9033
7624
5535
2433
1433
5568
8161

5691
5394
3445
4619
1703
6197
2113
4277
2506
3380
6039
6423
6429

23751
4571
7508

9674
3084
3612
3841
3555
8146
6263
7746
3586

7907
6263
2320
4430
15429

2825
2248
7184
3650
1008
5219
5600
2610
7357
5113
1039
2019

2167
4159
6290
3757
10133
1345
7250
10590

6712
5361
3243
6239
1667
2699
5389
1400
1334
2382
1604
3256
2439

6520
1478
3049
6452
6899
1850
2466
3485
3020
6683
8000

7715
6597
5588
2062
6732
3811
10470

4793
1206
6481
11715
8827
3174

3492
1535
2603
5877
4937
6805
1620
9488
1593

2182
8258
3319
5499
6257
1466
6435
8334
1140
6764

15599
28121

5804
6653
1670
7337
4711
8303
10073
6327

2754
2040
2295
8503
2231
11685
6556

16325
4057
11110

6482
2035
5189
6641
4232
1100
1088
2779
2220
3078
2847
6009
1981

8655
8687
7225
4133
4449
7193
4009
7455

2014
2691
1207
1140
6736
4780
2781
2855
5056
3590
2372
6188

6779
4130
5169
5726
1503
1520
8302
3054
3037
6190

6862
7039
1305
4226
5769
5068
8362
7612
6856

17695
18988
3757
15137

5268
3234
2073
1529
1190
5659
7316
3075
4191
6111
2582
7122

9316
2087
2980
12121
1703
6661
4286

20694
6712
15401

4342
3838
3208
2372
1410
1648
2342
6113
5573
6091
2624
1749
5643
4258

2303
2178
3449
3150
3825
3673
1326
6377

10398
3801
11714
7455
3382
6182

27882

6667
3268
11915
7045
10478
10538
2287

5694
5516
6094
4909
5685
4931
5949
6361
6476
6439
1667
5691
3883
3307

9977
7477
6533
9766
4576
2051
1376

5966
7654
5784
2727
7568
4600
2150
1333
6583
4119
2648

11274
8674
4155
2163
1897
6579
11099

2751
4530
5488
1491
2456
2752
1767
6113
7730
7127

8657
6947
4803
5103
4373
9501
1486
5689

4382
5176
2533
6017
6100
4935
1841
4530
6120
4735
3438
3305
5324
2814

41401

20975
30628

2099
5390
4829
5845
2674
1029
3312
3412
3402
5544
4773
5274
2458
4309
2741

4345
7095
7361
2171
6003
5069
1941
2473
2116
6508
6491
7227

8137
8052
5372
1086
2369
5763
8937
9055
1208

4359
3906
5012
2086
4937
4239
3390
3280
4948
3906
6387

6430
11071
1179
6918
12028
1855

11059
14754
15751
15821
9411

8722
1104
7422
9229
7919
6200
2274
2980
5686

3277
4325
9477
9651
4798
8742
4308
6656
6746

5777
6805
4337
4847
4966
3525
2729
6611
3070
3734
1957
1360
1678
"""