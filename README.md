#BaseBall API

##API

| status code | reason |
|:-----------:|:------:|
| 200 | 선수조회 성공 |
| 404 | 해당 선수가 없을 경우 |


###```GET     /player/<선수이름>```

```json
{
  "name":"김준성",
  "playerID":333333,
  "team":"두산",
  "position":"내야수",
  "position_detail":"우투좌타",
  "back_number":13,
  "player_image":"http://.../.jpg"
}

```

###```GET  /player/<선수ID>/stat```

```json
{
  "power":255,
  "scoring":255,
  "running":255,
  "error":255,
  "contribute":255
}
```

###```GET  /player/<선수ID>/OPS```

```json
{
  "start_time":"2015.10",
  "end_time":"2020.10",
  "player_ops":[33,33,333,33,33,33],
  "avg_ops":[33,33,33,33,33,33,33]
}
```

###```GET  /player/<선수ID>/growth```
```json
{
  "start_time":"2015.10",
  "end_time":"2020.10",
  "player_growth":[33,33,333,33,33,33]
}
```

###```GET  /player/<선수ID>/wOBA```
```json
{
  "start_time":"2015.10",
  "end_time":"2020.10",
  "player_wOBA":[33,33,333,33,33,33],
  "avg_wOBA":[33,33,33,33,33,33,33]
}
```

##파싱해야할 내용

1. 선수 프로필
2. 기본 기록 - 2015년도 성적
3. **일자별 기록 - 2010~2015년도 경기 기록**<완료> 



##KBO 선수정보 구조

- 선수
	- 타자
	- 투수

- 타자
	- 기본 기록
		- **2015년도 성적**
		- 최근 10경기
		- 연도별 TOP 10
	- 통산 기록
		- 선수 생활 전체 통계
	- 일자별 기록
		- **일자별 성적**
	- 경기별 기록
		- 상대팀별
		- 구장별
		- 월별
		- 요일별
		- 홈/방문별
		- 주/야간별
		- 기간별
	- 상황별 기록
		- 주자상황별
		- 볼카운트별
		- 이닝별
		- 타순별
		- 투수유형별
		- 아웃카운트별	

- 투수
	- 기본기록
		- **2015년도 성적**
		- 최근 10경기
		- 연도별 TOP 10
	- 통산기록
		- 선수 생활 전체 통계
	- 일자별기록
		- **일자별 성적**
	- 경기별기록
		- 상대팀별
		- 구장별
		- 월별
		- 요일별
		- 홈/방문별
		- 주/야간별
		- 기간별
	- 상황별기록
		- 주자상황별
		- 볼카운트별
		- 이닝별
		- 타순별
		- 타자유형별
		- 아웃카운트별



## 디자인

	디자인은 수시로 변할수 있기에 완료된 부분은 파일 마지막에 co를 붙이겠음.








