
class Team:

    def __init__(self, dict_team):
        self.tri_code = dict_team["teamTricode"]
        self.score = dict_team["score"]
        self.name = dict_team["teamName"]
        self.city = dict_team["teamCity"]
    

    def __str__(self):
        return f"{self.city} {self.name} {self.score}"