class Player(object):

    def __init__(self, playerId, name, team, postion):
        self.type = "Hitter"
        self.name = name
        self.playerId = playerId
        self.team = team
        self.position = postion
        self.games = []
        self.pitcherGames =[]
