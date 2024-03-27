class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

    def score(self):
        return self.chickenwings * 5 + self.hamburgers * 3 + self.hotdogs * 2

def create_scoreboard(participants):
    scoreboard = []
    for participant in participants:
        score = participant.score()
        scoreboard.append({"name": participant.name, "score": score})
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))  
    return scoreboard


participants = [
    Participant("Habanero Hillary", 5, 17, 11),
    Participant("Big Bob", 20, 4, 11)
]

scoreboard = create_scoreboard(participants)
print(scoreboard)

