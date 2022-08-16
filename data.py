# the distances to each adjacent vertex
delivery_map = {
    1: {
        21: 1.9,
        25: 2.4,
        23: 2.4,
        5: 2.2,
        18: 2,
        12: 3.2,
        10: 2.8,
        3: 3.8
    },
    2: {
        7: 1.6,
        20: 4.8,
        6: 4.8,
        19: 5,
        15: 4.6,
        14: 3,
        8: 2.8
    },
    3: {
        22: 5,
        21: 3.3,
        1: 3.8,
        26: 2.8
    },
    4: {
        11: 1,
        24: 0.6,
        17: 7.2,
        14: 3.9,
        15: 4.3,
        16: 4.4,
        5: 5.6,
        23: 4.7
    },
    5: {
        4: 5.6,
        16: 2.7,
        19: 1.7,
        12: 1.5,
        18: 0.5,
        1: 2.2,
        23: 2.5
    },
    6: {
        19: 1.1,
        2: 4.8,
        20: 3.5,
        10: 1.5,
        12: 0.8
    },
    7: {
        9: 4.2,
        13: 4.2,
        20: 3.2,
        2: 1.6,
        8: 4
    },
    8: {
        7: 4,
        2: 2.8,
        14: 1.6,
        17: 3.1
    },
    9: {
        7: 4.2,
        13: 0.6,
        26: 2.8
    },
    10: {
        12: 1.1,
        6: 1.5,
        20: 4.1,
        26: 3.2,
        3: 1.6,
        1: 2.8,
        18: 2.3
    },
    11: {
        24: 0.4,
        4: 1
    },
    12: {
        19: 1,
        6: 0.8,
        10: 1.1,
        1: 3.2,
        18: 1.2,
        5: 1.5
    },
    13: {
        7: 4.2,
        9: 0.6,
        26: 2.8,
        20: 1
    },
    14: {
        8: 1.6,
        2: 3,
        15: 1.3,
        4: 3.9,
        17: 4
    },
    15: {
        14: 1.3,
        2: 4.6,
        19: 2.2,
        16: 0.6,
        4: 4.3
    },
    16: {
        4: 4.4,
        15: 0.6,
        19: 1.7,
        5: 2.7
    },
    17: {
        8: 3.1,
        14: 4,
        4: 7.2,
        24: 7.5
    },
    18: {
        5: 0.5,
        19: 1.6,
        12: 1.2,
        10: 2.3,
        1: 2
    },
    19: {
        2: 5,
        6: 1.1,
        12: 1,
        18: 1.6,
        5: 1.7,
        16: 1.7,
        15: 2.2
    },
    20: {
        13: 1,
        26: 1.8,
        10: 4.1,
        6: 3.5,
        2: 4.8,
        7: 3.2
    },
    21: {
        1: 1.9,
        3: 3.3,
        22: 2,
        27: 4.1,
        25: 2.8,
        23: 2.9
    },
    22: {
        27: 4.7,
        25: 3.4,
        21: 2,
        3: 5
    },
    23: {
        4: 4.7,
        5: 2.5,
        1: 2.4,
        21: 2.9,
        25: 1.7
    },
    24: {
        17: 7.5,
        4: 0.6,
        11: 0.4
    },
    25: {
        23: 1.7,
        1: 2.4,
        21: 2.8,
        22: 3.4,
        27: 1.3
    },
    26: {
        3: 2.8,
        10: 3.2,
        20: 1.8,
        13: 2.8,
        9: 2.8
    },
    27: {
        25: 1.3,
        21: 4.1,
        22: 4.7
    }
}

# the information for each hub or stop
hub_info = {
    1: {
        "street": "4001 South 700 East",
        "city": "South Lake City",
        "postal": "84104"
    },
    2: {
        "street": "1060 Dalton Ave S",
        "city": "Salt Lake City",
        "postal": "84104"
    },
    3: {
        "street": "1330 2100 S",
        "city": "Salt Lake City",
        "postal": "84106"
    },
    4: {
        "street": "1488 4800 S",
        "city": "Salt Lake City",
        "postal": "84123"
    },
    5: {
        "street": "177 W Price Ave",
        "city": "Salt Lake City",
        "postal": "84115"
    },
    6: {
        "street": "195 W Oakland Ave",
        "city": "Salt Lake City",
        "postal": "84115"
    },
    7: {
        "street": "2010 W 500 S",
        "city": "Salt Lake City",
        "postal": "84104"
    },
    8: {
        "street": "2300 Parkway Blvd",
        "city": "West Valley City",
        "postal": "84119"
    },
    9: {
        "street": "233 Canyon Rd",
        "city": "Salt Lake City",
        "postal": "84103"
    },
    10: {
        "street": "2530 S 500 E",
        "city": "Salt Lake City",
        "postal": "84106"
    },
    11: {
        "street": "2600 Taylorsville Blvd",
        "city": "Salt Lake City",
        "postal": "84118"
    },
    12: {
        "street": "2835 Main St",
        "city": "Salt Lake City",
        "postal": "84115"
    },
    13: {
        "street": "300 State St",
        "city": "Salt Lake City",
        "postal": "84103"
    },
    14: {
        "street": "3060 Lester St",
        "city": "West Valley City",
        "postal": "84119"
    },
    15: {
        "street": "3148 S 1100 W",
        "city": "Salt Lake City",
        "postal": "84119"
    },
    16: {
        "street": "3365 S 900 W",
        "city": "Salt Lake City",
        "postal": "84119"
    },
    17: {
        "street": "3575 W Valley Central Station Bus Loop",
        "city": "West Valley City",
        "postal": "84119"
    },
    18: {
        "street": "3595 Main St",
        "city": "Salt Lake City",
        "postal": "84115"
    },
    19: {
        "street": "380 W 2880 S",
        "city": "Salt Lake City",
        "postal": "84115"
    },
    20: {
        "street": "410 S State St",
        "city": "Salt Lake City",
        "postal": "84111"
    },
    21: {
        "street": "4300 S 1300 E",
        "city": "Millcreek",
        "postal": "84117"
    },
    22: {
        "street": "4580 S 2300 E",
        "city": "Holladay",
        "postal": "84117"
    },
    23: {
        "street": "5025 State St",
        "city": "Murray",
        "postal": "84107"
    },
    24: {
        "street": "5100 South 2700 West",
        "city": "Salt Lake City",
        "postal": "84118"
    },
    25: {
        "street": "5383 S 900 East #104",
        "city": "Salt Lake City",
        "postal": "84117"
    },
    26: {
        "street": "600 E 900 South",
        "city": "Salt Lake City",
        "postal": "84105"
    },
    27: {
        "street": "6351 South 900 East",
        "city": "Murray",
        "postal": "84121"
    }
}

# the relevant information for each package
pkg_info = {
    1: {
        "destination": 6,
        "deadline": "10:30",
        "mass": 21
    },
    2: {
        "destination": 10,
        "deadline": "EOD",
        "mass": 44
    },
    3: {
        "destination": 9,
        "deadline": "EOD",
        "mass": 2
    },
    4: {
        "destination": 19,
        "deadline": "EOD",
        "mass": 4
    },
    5: {
        "destination": 20,
        "deadline": "EOD",
        "mass": 5
    },
    6: {
        "destination": 14,
        "deadline": "10:30",
        "mass": 88
    },
    7: {
        "destination": 3,
        "deadline": "EOD",
        "mass": 8
    },
    8: {
        "destination": 13,
        "deadline": "EOD",
        "mass": 9
    },
    9: {
        "destination": 20,
        "deadline": "EOD",
        "mass": 2
    },
    10: {
        "destination": 26,
        "deadline": "EOD",
        "mass": 1
    },
    11: {
        "destination": 11,
        "deadline": "EOD",
        "mass": 1
    },
    12: {
        "destination": 17,
        "deadline": "EOD",
        "mass": 1
    },
    13: {
        "destination": 7,
        "deadline": "10:30",
        "mass": 2
    },
    14: {
        "destination": 21,
        "deadline": "10:30",
        "mass": 88
    },
    15: {
        "destination": 22,
        "deadline": "9:00",
        "mass": 4
    },
    16: {
        "destination": 22,
        "deadline": "10:30",
        "mass": 88
    },
    17: {
        "destination": 15,
        "deadline": "EOD",
        "mass": 2
    },
    18: {
        "destination": 4,
        "deadline": "EOD",
        "mass": 6
    },
    19: {
        "destination": 5,
        "deadline": "EOD",
        "mass": 37
    },
    20: {
        "destination": 18,
        "deadline": "10:30",
        "mass": 37
    },
    21: {
        "destination": 18,
        "deadline": "EOD",
        "mass": 3
    },
    22: {
        "destination": 27,
        "deadline": "EOD",
        "mass": 2
    },
    23: {
        "destination": 24,
        "deadline": "EOD",
        "mass": 5
    },
    24: {
        "destination": 23,
        "deadline": "EOD",
        "mass": 7
    },
    25: {
        "destination": 25,
        "deadline": "10:30",
        "mass": 7
    },
    26: {
        "destination": 25,
        "deadline": "EOD",
        "mass": 25
    },
    27: {
        "destination": 2,
        "deadline": "EOD",
        "mass": 5
    },
    28: {
        "destination": 12,
        "deadline": "EOD",
        "mass": 7
    },
    29: {
        "destination": 3,
        "deadline": "10:30",
        "mass": 2
    },
    30: {
        "destination": 13,
        "deadline": "10:30",
        "mass": 1
    },
    31: {
        "destination": 16,
        "deadline": "10:30",
        "mass": 1
    },
    32: {
        "destination": 16,
        "deadline": "EOD",
        "mass": 1
    },
    33: {
        "destination": 10,
        "deadline": "EOD",
        "mass": 1
    },
    34: {
        "destination": 22,
        "deadline": "10:30",
        "mass": 2
    },
    35: {
        "destination": 2,
        "deadline": "EOD",
        "mass": 88
    },
    36: {
        "destination": 8,
        "deadline": "EOD",
        "mass": 88
    },
    37: {
        "destination": 20,
        "deadline": "10:30",
        "mass": 2
    },
    38: {
        "destination": 20,
        "deadline": "EOD",
        "mass": 9
    },
    39: {
        "destination": 7,
        "deadline": "EOD",
        "mass": 9
    },
    40: {
        "destination": 19,
        "deadline": "10:30",
        "mass": 45
    }
}
