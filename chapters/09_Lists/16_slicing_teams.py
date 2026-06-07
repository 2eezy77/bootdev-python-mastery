"""
You work at NCAA and need to organize tournament matches
Give 3 different options for how to draft what teams play each other (no names just number of orientation):
- Start with the third team.
- Ignore all with the exception of the last 3.
- Only every other (even only)
"""


def tournament_orientation(team_names):
    return team_names[3:], team_names[-3::], team_names[::2]


def test():
    how_to_call = tournament_orientation([0, 1, 2, 3, 4, 5, 6, 7])
    print(how_to_call)

def main():
    test()

main()
