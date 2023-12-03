from modules import day_1

def test_day_1_part_1():
    input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert day_1.solve_part_1(input) == 142

def test_day_1_part_2():
    input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert day_1.solve_part_2(input) == 281

def test_word_num_conv():
    assert day_1.convert_eng_to_str_int('onetwothreefour') == '1234'

def test_first_last_num():
    assert day_1.get_calib_val('12345') == 15