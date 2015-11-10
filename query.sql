CREATE TABLE players(
  playerId int NOT NULL,
  type Char(10) NOT NULL,
  name Char(10) NOT NULL,
  team Char(10) NOT NULL,
  postion Char(10) NOT NULL,
  position_detail Char(10) NOT NULL,
  img_url Char(100) NOT NULL,
  PRIMARY KEY (ID)
);

CREATE TABLE HitterGames(
  playerId int NOT NULL,
  year int NOT NULL,
  month int NOT NULL,
  day int NOT NULL,
  sideTeam Char(10) NOT NULL,
  AVG1 float(4,3) NOT NULL,
  AB int NOT NULL,
  R int NOT NULL,
  H int NOT NULL,
  B2 int NOT NULL,
  B3 int NOT NULL,
  HR int NOT NULL,
  RBI int NOT NULL,
  SB int NOT NULL,
  CS int NOT NULL,
  BB int NOT NULL,
  HBP int NOT NULL,
  SO int NOT NULL,
  GDP int NOT NULL,
  AVG2 float(4,3) NOT NULL,
  PRIMARY KEY (ID)
);


CREATE TABLE HitterGames(
  playerId int NOT NULL,
  year int NOT NULL,
  month int NOT NULL,
  day int NOT NULL,
  sideTeam Char(10) NOT NULL,
  postion Char(10) NOT NULL,
  result int NOT NULL,
  ERA1 float(3,2) NOT NULL,
  TBF int NOT NULL,
  IP int NOT NULL,
  H int NOT NULL,
  HR int NOT NULL,
  BB int NOT NULL,
  HBP int NOT NULL,
  SO int NOT NULL,
  R int NOT NULL,
  ER int NOT NULL,
  ERA2 float(3,2) NOT NULL,
  PRIMARY KEY (ID)
);
