class Player(object):

    def __init__(self, playerId, name, team, postion, position_detail, img_url):
        self.type = "Hitter"
        self.image = img_url
        self.name = name
        self.playerId = playerId
        self.team = team
        self.position = postion
        self.position_detail = position_detail
        self.hitterGames = []
        self.pitcherGames =[]
        self.finalscore = None
