from modules import day_1, day_2

def get_puzzle_input(input_name)-> str:
    with open(f"inputs/{input_name}") as file:
        return file.read().strip()
    
def solve():

    day1_input = get_puzzle_input('day_1')
    day1_part1 = day_1.solve_part_1(day1_input)
    print(f"the day 1 part 1 answer is {day1_part1}")

    day1_part2 = day_1.solve_part_2(day1_input)
    print(f"the day 1 part 2 answer is {day1_part2}")

    day2_input = get_puzzle_input('day_2')
    day2_part1 = day_2.solve_part_1(day2_input)
    print(f"the day 2 part 1 answer is {day2_part1}")

    day2_part2 = day_2.solve_part_2(day2_input)
    print(f"the day 2 part 2 answer is {day2_part2}")




if __name__ == "__main__":
    solve()
