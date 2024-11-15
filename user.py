class User:
    """
    clutch_time: how much time is left to be valid
    clutch_points: how close the game is to be valid
    """
    def __init__(self, cluth_time, clutch_points):
        self.favourite_teams = []
        self.clutch_time = cluth_time
        self.clutch_points = clutch_points