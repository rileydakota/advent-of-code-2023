from modules import day_5

test_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

def test_parse_almanac():
    almanac = day_5.Almanac(test_input)
    assert len(almanac.seeds) == 4

    #assert almanac.get_seed_locs() == 5
    #assert almanac.soil_to_fert[81] == 81
    #assert almanac.fert_to_water[81] == 81
    #assert almanac.water_to_light[81] == 74

    #assert almanac.get_seed_locs()[13] == 35

def test_get_mapping():
    almanac = day_5.Almanac(test_input)
    assert almanac.get_mapping(14, [[50, 98, 2]]) == 14
    assert almanac.get_mapping(53, [[52, 50, 48]]) == 55
    assert almanac.get_mapping(14, [[39, 0, 15]]) ==  53

def test_get_locs():
    almanac = day_5.Almanac(test_input)
    assert almanac.get_seed_locs()[14] == 43
    assert almanac.get_seed_locs()[13] == 35
    assert almanac.get_seed_locs()[79] == 82
    assert almanac.get_seed_locs()[55] == 86
