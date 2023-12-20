from modules import day_1, day_2, day_3, day_4


def get_puzzle_input(input_name) -> str:
    with open(f"inputs/{input_name}") as file:
        return file.read().strip()


def solve():
    day1_input = get_puzzle_input("day_1")
    day1_part1 = day_1.solve_part_1(day1_input)
    print(f"the day 1 part 1 answer is {day1_part1}")

    day1_part2 = day_1.solve_part_2(day1_input)
    print(f"the day 1 part 2 answer is {day1_part2}")

    day2_input = get_puzzle_input("day_2")
    day2_part1 = day_2.solve_part_1(day2_input)
    print(f"the day 2 part 1 answer is {day2_part1}")

    day2_part2 = day_2.solve_part_2(day2_input)
    print(f"the day 2 part 2 answer is {day2_part2}")

    day3_input = get_puzzle_input("day_3")
    day3_part1 = day_3.solve_part_1(day3_input)
    print(f"the day 3 part 1 answer is {day3_part1}")
    day3_part2 = day_3.solve_part_2(day3_input)
    print(f"the day 3 part 2 answer is {day3_part2}")

    #day_4_input = get_puzzle_input("day_4")

    #day4_part1 = day_4.solve_part_1(day_4_input)
    #print(f"the day 4 part 1 answer is {day4_part1}")

    #day4_part2 = day_4.solve_part_2(day_4_input)
    #print(f"the day 4 part 2 solution is {day4_part2}")


if __name__ == "__main__":
    solve()
