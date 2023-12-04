valid_string_words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

def convert_eng_to_str_int(line:str, string_words_dict=valid_string_words) -> str:
    res = line.lower()
    for key, val, in string_words_dict.items():
        res = res.replace(key, str(key + val + key))
    return res

def get_calib_val(line:str) -> int:
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(char)
    try:
        res = nums[0] + nums[-1]
        return int(res)
    except Exception as e:
        raise e


def solve_part_1(input:str):
    values = input.split('\n')
    
    total = 0
    for value in values:
        val = get_calib_val(value)
        total += val
    
    return total

def solve_part_2(input:str):
    values = input.split('\n')

    total = 0
    parsed_str = []

    for val in values:
        parsed_str.append(convert_eng_to_str_int(val))
    
    for val in parsed_str:
        res = get_calib_val(val)
        total += res
    
    return total
