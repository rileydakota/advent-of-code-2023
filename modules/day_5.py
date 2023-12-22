import re
from dataclasses import dataclass

@dataclass
class Almanac:
    input: str
    seeds = []
    seed_to_soil = []
    soil_to_fert = []
    fert_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_humd = []
    humd_to_loc = []
    expand: bool

    def __post_init__(self):
        self._parse_alamanac()
    

# seeds: [0-9 ]*
# seed-to-soil map:\n[0-9 \n]*
# soil-to-fertilizer map:\n[0-9 \n]*
# fertilizer-to-water map:\n[0-9 \n]*
# water-to-light map:\n[0-9 \n]*
# light-to-temperature map:\n[0-9 \n]*
# temperature-to-humidity map:\n[0-9 \n]*
# humidity-to-location map:\n[0-9 \n]*
    

    def _parse_alamanac(self):

        if self.expand:
            print('expanding')
            print([int(x) for x in re.search(r'seeds: [0-9 ]*', self.input).group(0).split(':')[1].strip().split(' ')])
            self.seeds = expand_ranges([int(x) for x in re.search(r'seeds: [0-9 ]*', self.input).group(0).split(':')[1].strip().split(' ')])
        else:
            self.seeds = [int(x) for x in re.search(r'seeds: [0-9 ]*', self.input).group(0).split(':')[1].strip().split(' ')]
        self.seed_to_soil = [[int(y) for y in x.split(' ')] for x in re.search(r'seed-to-soil map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]
        self.soil_to_fert = [[int(y) for y in x.split(' ')] for x in re.search(r'soil-to-fertilizer map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]
        self.fert_to_water = [[int(y) for y in x.split(' ')] for x in re.search(r'fertilizer-to-water map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]
        self.water_to_light = [[int(y) for y in x.split(' ')] for x in re.search(r'water-to-light map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]
        self.light_to_temp = [[int(y) for y in x.split(' ')] for x in re.search(r'light-to-temperature map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]
        self.temp_to_humd = [[int(y) for y in x.split(' ')] for x in re.search(r'temperature-to-humidity map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')] 
        self. humd_to_loc = [[int(y) for y in x.split(' ')] for x in re.search(r'humidity-to-location map:\n[0-9 \n]*', self.input).group(0).split(':')[1].strip().split('\n')]

    def get_mapping(self, target, amap):
        for line in amap:
            if target in range(line[1], line[1] + (line[2])):
                offset = abs(target - line[1])
                return  line[0] + offset
        return target

    def get_seed_locs(self):
        locations = {}
        for seed in self.seeds:
            soil = self.get_mapping(seed, self.seed_to_soil)
            fert = self.get_mapping(soil, self.soil_to_fert)
            water = self.get_mapping(fert, self.fert_to_water)
            light = self.get_mapping(water, self.water_to_light)
            temp = self.get_mapping(light, self.light_to_temp)
            humd = self.get_mapping(temp, self.temp_to_humd)
            loc = self.get_mapping(humd, self.humd_to_loc)
            print(f"lookups for seed {seed}: {soil}, {fert}, {water}, {light}, {temp}, {humd}, {loc}")

            locations[seed] = loc

        return locations

def expand_ranges(numbers):
    """
    Given a list of numbers, uses every two numbers as a range,
    where the first number is the starting point and the second number 
    is the number of increments from the starting point.

    Parameters:
    numbers (list): The input list of numbers.

    Returns:
    list: A new list with expanded ranges.
    """
    result = []
    for i in range(0, len(numbers), 2):
        if i + 1 < len(numbers):
            start = numbers[i]
            increment = numbers[i + 1]
            result.extend(range(start, start + increment))
        else:
            # If it's a single number without a pair, just add it to the list
            result.append(numbers[i])
    return result
def solve_part_1(input:str):
    alamanac = Almanac(input, expand=False)
    return min(alamanac.get_seed_locs().values())

def solve_part_2(input:str):
    alamanac = Almanac(input, expand=True)
    print(alamanac.seeds)
    return min(alamanac.get_seed_locs().values())
