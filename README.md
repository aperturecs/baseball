#BaseBall API

##API

| status code | reason |
|:-----------:|:------:|
| 200 | 선수조회 성공 |
| 404 | 해당 선수가 없을 경우 |


###```GET     /profile/<선수ID>```
선수의 정보를 보여줍니다.
```json
{
  "name":"김준성",
  "playerID":333333,
  "team":"두산",
  "position":"내야수",
  "position_detail":"우투좌타",
  "image":"http://.../.jpg"
}

```

###```GET  /stat/<선수ID>```
선수의 능력치를 보여줍니다.
```json
{
  "power":255,
  "scoring":255,
  "running":255,
  "error":255,
  "contribute":255
}
```

###```GET  /growth/<선수ID>```
선수의 성장율을 얻습니다.
```json
{
  "date":[[2010,10],[2011,3],[2011,4]],
  "points":[20,30,10]
}
```
###```GET  /similar/<선수ID>```
이 선수와 유사한 선수를 추천해 줍니다.
```json
{
  "similar_players":[101111,131111,13333]
}
```

###```GET  /playerId/<선수이름>```
선수이름을 기입하여 playerId를 얻습니다.
```json
{
  "playerId":139888
}
```
