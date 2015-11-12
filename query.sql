drop table players;
drop table HitterGames;
drop table PitcherGames;
drop table HitterProfiles;
drop table PitcherProfiles;

CREATE TABLE players(
  playerId int NOT NULL,
  type Char(10) NOT NULL,
  name Char(10) NOT NULL,
  team Char(10) NOT NULL,
  position Char(10) NOT NULL,
  position_detail Char(10) NOT NULL,
  image Char(100) NOT NULL
);

CREATE TABLE HitterGames(
  type Char(10) NOT NULL,
  playerId int NOT NULL,
  year int NOT NULL,
  month int NOT NULL,
  day int NOT NULL,
  sideTeam Char(10) NOT NULL,
  AVG1 FLOAT(4,3) NOT NULL,
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
  AVG2 FLOAT(4,3) NOT NULL
);


CREATE TABLE PitcherGames(
  type Char(10) NOT NULL,
  playerId int NOT NULL,
  year int NOT NULL,
  month int NOT NULL,
  day int NOT NULL,
  sideTeam Char(10) NOT NULL,
  position Char(10) NOT NULL,
  win BOOLEAN NOT NULL,
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
  ERA2 float(3,2) NOT NULL
);

CREATE TABLE HitterProfiles(
  playerId int NOT NULL,
  Team int NOT NULL,
  AVG Float(4,3) NOT NULL,
  G int NOT NULL,
  PA int NOT NULL,
  AB int NOT NULL,
  R int NOT NULL,
  H int NOT NULL,
  B2 int NOT NULL,
  B3 int NOT NULL,
  HR int NOT NULL,
  TB int NOT NULL,
  RBI int NOT NULL,
  SB int NOT NULL,
  CS int NOT NULL,
  SAC int NOT NULL,
  SF int NOT NULL,
  BB int NOT NULL,
  IBB int NOT NULL,
  HBP int NOT NULL,
  SO int NOT NULL,
  GDP int NOT NULL,
  SLG Float(4,3) NOT NULL,
  OBP Float(4,3) NOT NULL,
  E int NOT NULL,
  SBP Float(3,1) NOT NULL,
  MH int NOT NULL,
  OPS Float(4,3) NOT NULL,
  RISP Float(4,3) NOT NULL,
  PHBA Float(4,3) NOT NULL
);



CREATE TABLE PitcherProfiles(
  playerId int NOT NULL,
  Team Char(10) NOT NULL,
  ERA Float(3,2) NOT NULL,
  G int NOT NULL,
  CG int NOT NULL,
  SHO int NOT NULL,
  W int NOT NULL,
  L int NOT NULL,
  SV int NOT NULL,
  HLD int NOT NULL,
  WPCT Float(4,3) NOT NULL,
  TBF int NOT NULL,
  NP int NOT NULL,
  IP int NOT NULL,
  H int NOT NULL,
  B2 int NOT NULL,
  B3 int NOT NULL,
  HR int NOT NULL,
  SAC int NOT NULL,
  SF int NOT NULL,
  BB int NOT NULL,
  IBB int NOT NULL,
  SO int NOT NULL,
  WP int NOT NULL,
  BK int NOT NULL,
  R int NOT NULL,
  ER int NOT NULL,
  BSV int NOT NULL,
  WHIP Float(3,2) NOT NULL,
  AVG Float(4,3) NOT NULL,
  QS int NOT NULL
);
