# Competitive Eating Competition Scoreboard

This project implements a Python script to calculate scores for participants in a competitive eating competition based on the number of chicken wings, hamburgers, and hotdogs consumed. The script then generates a scoreboard sorted by score and participant name.

## How to Use

1. Clone the repository:

> git clone git@github.com:khalidka/CompetitiveEatingScoreboard.git

[x] Navigate to the project directory:

> cd CompetitiveEatingScoreboard 

# Participant Data Format
## Participants are represented as objects with the following properties:

name: Participant's name
chickenwings: Number of chicken wings consumed
hamburgers: Number of hamburgers consumed
hotdogs: Number of hotdogs consumed

# Example

participants = [
    Participant("Habanero Hillary", 5, 17, 11),
    Participant("Big Bob", 20, 4, 11)
]

scoreboard = create_scoreboard(participants)
print(scoreboard)


## License
> This project is licensed under the MIT License. See the LICENSE file for details.