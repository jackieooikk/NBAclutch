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
        """
        Final: done
        Q4 :44.3
        """
        self.game_status_text = live_game_dict["gameStatusText"]



    def __str__(self):
        return f"{self.home_team} : {self.away_team}"

    def __repr__(self):
        return f"{self.home_team} : {self.away_team}"