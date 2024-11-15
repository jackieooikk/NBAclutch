from nba_api.live.nba.endpoints import scoreboard
from .live_game import LiveGame
from .team import Team


class Data:
    def __init__(self):
        self.todays_games = []
        self.live_games = []
        self.update_data()


    def update_data(self):
        games = scoreboard.ScoreBoard().get_dict()["scoreboard"]["games"]

        self.todays_games = []
        self.live_games = []

        for game in games:
            self.todays_games.append(LiveGame(game))

        for game in self.todays_games:
            # 1: not started
            # 2: live
            # 3: completed
            if (game.game_status == 2):
                self.live_games.append(game)


    def __str__(self):
        result = ""
        for game in self.live_games:
            result += str(game)
            result += "\n"
        return result





    
if __name__ == "__main__":
    Data()