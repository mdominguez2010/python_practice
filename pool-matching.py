# You’re given a list of people to match together in a pool of candidates.
# We want to match up people based on two ways:

# 1. A hard filter on scheduled availability
# 2. A closest match based on similar interests

# First - optimize total number of matches
# Second - optimize on matching based on interests

# Example Output:
# matches = [
#     {
#         'match': ('Bob', 'Joe'),
#         'scheduled_date': '2021-01-10',
#         'overlapping_interests': ['rock climbing', 'data science'],
#     },
#     {
#         'match': ('Carolyn', 'Dan'),
#         'scheduled_date': '2021-01-12',
#         'overlapping_interests': []
#     },
# ]

# no_matches = []

people = [
    {
        'name': 'Bob',
        'availability': ['2021-01-10', '2021-01-11'],
        'interests': ['rock climbing', 'tech', 'data science'],
    },
    {
        'name': 'Joe',
        'availability': ['2021-01-10', '2021-01-09'],
        'interests': ['rock climbing', 'swimming', 'data science'],
    },
    {
        'name': 'Carolyn',
        'availability': ['2021-01-11', '2021-01-12'],
        'interests': ['data science'],
    },
    {
        'name': 'Dan',
        'availability': ['2021-01-12'],
        'interests': ['rock climbing'],
    },
]

def match(people_list):

    matches = []
    for i in range(len(people_list)):
        # compare first person and second person
            # append dictionary to matches
                # 'match': (first_person_name, second_person_name),
                # 'schedules_date': matching dates
                # 'overlapping_interests': ['overlapping_intr_1', 'overlapping_intr_2']
        # compare first person and third person
        # compare first person and fourth person
        # ...
        # compare last person and second to last person
