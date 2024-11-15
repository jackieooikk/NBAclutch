from .team import Team

class LiveGame:
    """
    homeCode/awayCode: tricode for home team e.g(DEN, GSW)

    """
    def __init__(self, live_game_dict):
        self.home_team = Team(live_game_dict["homeTeam"])
        self.away_team = Team(live_game_dict["awayTeam"])

        self.game_status = live_game_dict["gameStatus"]
        self.period = live_game_dict["period"]
        self.game_clock = live_game_dict["gameClock"]

        self.minutes_left = self.clock_to_min()

        self.game_status_text = live_game_dict["gameStatusText"]

    def clock_to_min(self):
        if (self.game_clock[0] == 'P'):
            return int(self.game_clock[2:4])
        else:
            return int(self.game_clock[0:2])
        

    def is_close(self, points):
        difference = abs(self.home_team.getPoints() - self.away_team.getPoints())
        return difference <= points
    
    def under(self, time):
        return self.minutes_left < time


    def __str__(self):
        return f"{self.home_team} : {self.away_team}"

    def __repr__(self):
        return f"{self.home_team} : {self.away_team}"