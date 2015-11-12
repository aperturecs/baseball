#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def codeParsing(html):

    # teams = ['SS','WO','NC','LG','SK','OB','LT','HT','HH','KT']
    player_codes = []
    soup = BeautifulSoup(html, 'html.parser')

    try:
        tables = soup.findAll("table",{"class" : "tNData"})
    except Exception,e:
        print e

    player_tr = []

    for i in range(2,6):
        trs = tables[i].find("tbody").findAll("tr")
        for tr in trs:
            player_tr.append(tr)

    for tr in player_tr:
        player_codes.append(int(tr.find("a")["href"].split("playerId=")[1]))

    print player_codes


html ="""
<html xmlns="http://www.w3.org/1999/xhtml"><head><link rel="shortcut icon" href="//image.koreabaseball.com/client/images/common/favicon.ico"><meta http-equiv="content-type" content="text/html; charset=utf-8"><meta name="keywords" content="kbo"><meta name="author-date" content="20130308"><meta http-equiv="x-ua-compatible" content="IE=9, Chrome"><title>선수등록현황 | 선수현황 | KBO</title><link type="text/css" rel="stylesheet" href="//image.koreabaseball.com/client/css/reset.css?version=201503111"><link type="text/css" rel="stylesheet" href="//image.koreabaseball.com/client/css/common.css?version=20151109"><link type="text/css" rel="stylesheet" href="//image.koreabaseball.com/client/css/jquery-ui.css"><link type="text/css" rel="stylesheet" href="//image.koreabaseball.com/client/css/jquery.bxslider.css?version=20151006">

	<script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript" src="//image.koreabaseball.com/client/js/jquery-1.11.1.min.js"></script>
	<script type="text/javascript" src="//image.koreabaseball.com/client/js/jquery-ui.js"></script>
	<script type="text/javascript" src="//image.koreabaseball.com/client/js/jquery.bxslider.min.js"></script>
	<script type="text/javascript" src="//image.koreabaseball.com/client/js/common.js?version=20150724"></script>
    <script type="text/javascript" src="//image.koreabaseball.com/client/js/rolling.js?version=20150305"></script>

<link type="text/css" rel="stylesheet" href="http://image.koreabaseball.com/client/css/sub.css?version=20150311">
<link type="text/css" rel="stylesheet" href="http://image.koreabaseball.com/client/css/player.css?version=20150514">
<link type="text/css" rel="stylesheet" href="http://image.koreabaseball.com/client/css/jquery-ui-theme.css">

<script type="text/javascript">
    function fnSearchChange(teamId) {
        $("#cphContainer_cphContents_hfSearchTeam").val(teamId);
        __doPostBack('ctl00$ctl00$cphContainer$cphContents$btnCalendarSelect','')
	}
</script>


    <script type="text/javascript">
        function setPlayerSearch() {
            var searchWord = encodeURI($('#txtSearchWord').val());

            if (searchWord != "") {
                location.href = "/Player/Search.aspx?searchWord=" + searchWord;
            }
        }
    </script>
    <script type="text/javascript">
        (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date(); a = s.createElement(o),
            m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-15700655-14', 'auto');
        ga('send', 'pageview');
    </script>
<script type="text/javascript">jQuery(function ($) {$('[data-id=WO]').parent().children().filter(':last').addClass('last');$('[data-id=WO]').addClass('on');$('[data-id=WO]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=SS]').parent().children().filter(':last').addClass('last');$('[data-id=SS]').addClass('on');$('[data-id=SS]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=WO]').parent().children().filter(':last').addClass('last');$('[data-id=WO]').addClass('on');$('[data-id=WO]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=NC]').parent().children().filter(':last').addClass('last');$('[data-id=NC]').addClass('on');$('[data-id=NC]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=LG]').parent().children().filter(':last').addClass('last');$('[data-id=LG]').addClass('on');$('[data-id=LG]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=SK]').parent().children().filter(':last').addClass('last');$('[data-id=SK]').addClass('on');$('[data-id=SK]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=OB]').parent().children().filter(':last').addClass('last');$('[data-id=OB]').addClass('on');$('[data-id=OB]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=LT]').parent().children().filter(':last').addClass('last');$('[data-id=LT]').addClass('on');$('[data-id=LT]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=HT]').parent().children().filter(':last').addClass('last');$('[data-id=HT]').addClass('on');$('[data-id=HT]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=HH]').parent().children().filter(':last').addClass('last');$('[data-id=HH]').addClass('on');$('[data-id=HH]').siblings().removeClass('on');});</script><script type="text/javascript">jQuery(function ($) {$('[data-id=KT]').parent().children().filter(':last').addClass('last');$('[data-id=KT]').addClass('on');$('[data-id=KT]').siblings().removeClass('on');});</script></head>
<body>
    <form method="post" action="Register.aspx" id="mainForm">
<div class="aspNetHidden">



</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['mainForm'];
if (!theForm) {
    theForm = document.mainForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=svPT2SWo_OysBNOXHKqqfat8pYk89GZeLS4S2PJhj91dcYLQFDICr-RhNxegR7MIqboQss36WisDLNPQV195pnv-ohxI__rntw8986GX--c1&amp;t=635586541120000000" type="text/javascript"></script>


<script src="/ScriptResource.axd?d=TeE6n-7kls760uhe3f05Yr4Z-dl_2EMYx9L1wbBSB7lAHiRkTuCizJkGiRLaIqSEGuR1mtFXCFtHPrSyjnslZFLjsq252WMTGDwql5obSe7KhJGzvrYLwmZMuoDKlP1GfsczF_IN01sDboNRbYMKpaKk2wAYddG9aDyfRuuF1sZ0t2uO2TrIBiIIRxEAg6DL0&amp;t=7b689585" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
if (typeof(Sys) === 'undefined') throw new Error('ASP.NET Ajax 클라이언트 쪽 프레임워크를 로드하지 못했습니다.');
//]]>
</script>

<script src="/ScriptResource.axd?d=Rsf7zs4BUjjXrUTHU74LEnwL5MuISmQsMGr1OIIjxqtI7z29x0GbQfnJHXDad5oc8xsAJj_0oOaOSpowXjIW0tmKI6Tmn6fRwWKcQ7j8aTzTF1jgeFDzEPo1P2oc49U7ldam_iWpt4nTE2ouYxZD5-7A10NPRr3ugDIBHdqQHJvdf0ZfhDMYlOl5jAO2asER0&amp;t=7b689585" type="text/javascript"></script>
<div class="aspNetHidden">



</div>
        <div id="wrap">
	        <!-- header -->

	        <div id="header">
		        <div class="row ">
			        <div class="top_area">
				        <ul class="top_menu">
					        <li class="first-child"><a href="/" title="home"><img src="//image.koreabaseball.com/client/images/common/btn_home.png" alt="home"></a></li>

					            <li><a href="/Member/Login.aspx" title="로그인">로그인</a></li>
					            <li><a href="/Member/Join/Accessterms.aspx" title="회원가입">회원가입</a></li>

					        <li class="last"><a href="//eng.koreabaseball.com/" title="ENGLISH">ENGLISH</a></li>
				        </ul>
				        <span class="srch_player">
                            <input name="ctl00$ctl00$txtSearchWord" type="text" id="txtSearchWord" placeholder="선수검색" class="input01">
					        <input type="image" alt="선수검색하기" src="//image.koreabaseball.com/client/images/common/btn_srch.png" class="btn_srch" onclick="setPlayerSearch();return false;">
				        </span>
			        </div>
		        </div>
		        <div class="row">
			        <div class="wrapper03">

				        <h1 class="logo"><a href="/Default.aspx">KBO</a></h1>
                        <div class="kbo_history mgt30">
					        <div class="row">
					            <span class="title"><b>KBO</b> 역사속 오늘 | </span>
					            <span class="date">11월 12일</span>
					        </div>
					        <div class="row flow_text bg_black mgt10">
						        <ul id="HistoryItem" style="position: relative; overflow: hidden; white-space: nowrap;"><li style="position: relative; display: inline; top: 0px; left: -108px;"><a href="/Etc/TodayHistory.aspx?searchDate=2012-11-12"><span class="point">12'</span>&nbsp;<b>제3회 WBC 대표...</b> </a>&nbsp;</li><li style="position: relative; display: inline; top: 0px; left: -108px;"><a href="/Etc/TodayHistory.aspx?searchDate=2014-11-12"><span class="point">14'</span>&nbsp;<b> KBO, SK 와...</b> </a>&nbsp;</li><li style="position: relative; display: inline; top: 0px; left: -108px;"><a href="/Etc/TodayHistory.aspx?searchDate=2000-11-12"><span class="point">00'</span>&nbsp;<b>박용오 총재 일본 ...</b> 박용오 총재는 12일 일본 ...</a>&nbsp;</li></ul>
						        <div class="btnControl">
							        <a href="#" class="left"><img src="//image.koreabaseball.com/client/images/main/roll_prev.png" alt="Left"></a>
							        <a href="#" class="stop"><img src="//image.koreabaseball.com/client/images/main/roll_stop.png" alt="Stop"></a>
							        <a href="#" class="right"><img src="//image.koreabaseball.com/client/images/main/roll_next.png" alt="Right"></a>
						        </div>
					        </div>
				        </div>
			        </div>

		        </div>
		        <div class="row">
			        <div class="wrapper03">
                        <!-- gnb -->
				        <div class="gnb">
					        <ul class="main">
						        <li><a href="/Schedule/ScoreBoard/ScoreBoard.aspx" style="width:86px">경기일정/결과</a>
							        <ul class="sub por01">
								        <li><a href="/Schedule/ScoreBoard/ScoreBoard.aspx">스코어보드</a></li>
								        <li><a href="/Schedule/GameList/General.aspx">경기일정/결과</a></li>
                                        <li><a href="/Schedule/GameList/CalendarSchedule.aspx">월별일정/결과</a></li>


							        </ul>
						        </li>
						        <li><a href="/TeamRank/TeamRank.aspx">팀순위</a>
							        <ul class="sub">
								        <li><a href="/TeamRank/TeamRank.aspx">팀순위</a></li>
								        <li><a href="/TeamRank/GraphDaily.aspx">팀별 순위변동 그래프</a></li>
							        </ul>
						        </li>
						        <li><a href="/Record/Main.aspx">기록실</a>
							        <ul class="sub">
                                        <li><a href="/Record/Main.aspx">TOP5</a></li>
								        <li><a href="/Record/Player/HitterBasic/Basic1.aspx">기록실</a></li>
			                            <li><a href="/Record/Etc/HitVsPit.aspx">투수 vs 타자</a></li>

			                            <li><a href="/Record/Crowd/GraphTeam.aspx">관중현황-KBO 정규시즌</a></li>
			                            <li><a href="/Record/Crowd/History.aspx">역대 관중현황</a></li>
							        </ul>
						        </li>
						        <li><a href="/Futures/Schedule/GameList.aspx" style="width:65px">퓨처스리그</a>
							        <ul class="sub">
								        <li><a href="/Futures/Schedule/GameList.aspx">경기일정/결과</a></li>
								        <li><a href="/Futures/TeamRank/North.aspx">팀순위</a></li>
								        <li><a href="/Futures/Main/Main.aspx">TOP5</a></li>
			                            <li><a href="/Futures/Player/Hitter.aspx">기록실</a></li>
							        </ul>
						        </li>
						        <li><a href="/History/Top/Hitter.aspx" style="width:65px">역대기록실</a>
							        <ul class="sub">
								        <li><a href="/History/Top/Hitter.aspx">역대 최고기록 10걸</a></li>
								        <li><a href="/History/Team/Year2010.aspx">역대 구단성적</a></li>
								        <li><a href="/History/Player/Hitter.aspx">역대 타자</a></li>
								        <li><a href="/History/Player/Pitcher.aspx">역대 투수</a></li>
								        <li><a href="/History/Etc/Award.aspx">역대 개인수상</a></li>
                                        <li><a href="/History/Etc/GoldenGlobe.aspx">역대 골든글러브</a></li>
								        <li><a href="/History/Etc/Amazing.aspx">진기록 명기록</a></li>
								        <li><a href="/History/Ebook/Ebook2015.aspx">E-BOOK</a></li>
								        <li><a href="/History/International/Asia.aspx">국제대회</a></li>
							        </ul>
						        </li>
						        <li class=""><a href="/News/Main.aspx">NEWS</a>
							        <ul class="sub" style="display: none; height: 1px; padding-top: 0px; margin-top: 0px; padding-bottom: 0px; margin-bottom: 0px;">
								        <li><a href="/News/Main.aspx">NEWS</a></li>
			                            <li><a href="/News/Notice/List.aspx">KBO 보도자료</a></li>
			                            <li><a href="/News/Preview/List.aspx">프리뷰</a></li>
			                            <li><a href="/News/BreakingNews/List.aspx">KBO 리그 속보</a></li>
			                            <li><a href="/News/Interview/List.aspx">스타 인터뷰</a></li>
			                            <li><a href="/News/KboPhoto/List.aspx">KBO PHOTO</a></li>
			                            <li><a href="/News/ExpectationWeek/List.aspx">주간 예상 달성기록</a></li>
			                            <li><a href="/News/ExpectationDaily/List.aspx">일간 예상 달성기록</a></li>
							        </ul>
						        </li>
						        <li class=""><a href="/KboTv/Highlight/List.aspx" style="width:52px">KBO TV</a>
							        <ul class="sub" style="display: none; height: 1px; padding-top: 0px; margin-top: 0px; padding-bottom: 0px; margin-bottom: 0px;">
								        <li><a href="/KboTv/Highlight/List.aspx">하이라이트</a></li>
			                            <li><a href="/KboTv/MonthMvp/List.aspx">월간 MVP</a></li>
                                        <li><a href="/KboTv/ADTCaps/List.aspx">월간 ADT캡스플레이</a></li>
			                            <li><a href="/KboTv/Legend/List.aspx">레전드 올스타 동영상</a></li>
			                            <li><a href="/KboTv/Naver.aspx">NAVER 스포츠</a></li>
			                            <li><a href="/KboTv/Daum.aspx">Daum 스포츠</a></li>
			                            <li><a href="/KboTv/Crowd/List.aspx">KBO 영상</a></li>
			                            <li><a href="/KboTv/VeteranInterview/List.aspx">야구 원로 인터뷰</a></li>
							        </ul>
						        </li>
						        <li><a href="/Player/Search.aspx" style="width:52px">선수현황</a>
							        <ul class="sub">
								        <li><a href="/Player/Search.aspx">선수조회</a></li>
								        <li><a href="/Player/Register.aspx">선수등록현황</a></li>
                                        <li><a href="/Player/RegisterAll.aspx">전체등록현황</a></li>
							        </ul>
						        </li>
						        <li class=""><a href="/Board/Faq/List.aspx">게시판</a>
							        <ul class="sub" style="display: none; height: 100px; padding-top: 15px; margin-top: 0px; padding-bottom: 15px; margin-bottom: 0px;">
								        <li><a href="/Board/Faq/List.aspx">자주하는 질문</a></li>
			                            <li><a href="/Board/Qna/List.aspx">Q&amp;A 게시판</a></li>
			                            <li><a href="/Board/Free/List.aspx">자유 게시판</a></li>
								        <li><a href="/Board/Committee/List.aspx">기록위원회 Q&amp;A 게시판</a></li>
							        </ul>
						        </li>
					        </ul>
					        <ul class="special">
						        <li><a href="/About/Safe.aspx" class="gnb_about">ABOUT <strong>KBO</strong></a>
							        <ul class="sub">
                                        <li><a href="/About/Safe.aspx">SAFE 캠페인</a></li>
                                        <li><a href="/Event/DreamSave05.aspx">Dream Save</a></li>
								        <li><a href="/About/TeamInfo.aspx">구단소개</a></li>
                                        <li><a href="/About/Group/Activity.aspx">조직 및 활동</a></li>
								        <li><a href="/About/Kbop.aspx">KBOP</a></li>
								        <li><a href="/About/KboCi.aspx">KBO CI</a></li>
								        <li><a href="/About/CatchPhrase.aspx">KBO 캐치프레이즈</a></li>
								        <li><a href="/About/GameManage.aspx">경기운영체제</a></li>
								        <li><a href="/About/Map.aspx">약도/관람료</a></li>
								        <li><a href="/About/GameRule.aspx">경기규칙</a></li>
								        <li><a href="/About/TeamHistory.aspx">각 구단 변천사</a></li>
								        <li><a href="/About/Change2015.aspx">2015 달라지는 점</a></li>
								        <li><a href="/About/Service2015.aspx">KBO 사회공헌 사업</a></li>
								        <li><a href="/Committee/Organizationchart.aspx">기록위원회</a></li>
                                        <li><a href="/Allstar/AllstarEvent.aspx">2015 KBO 올스타전 </a></li>
							        </ul>
						        </li>
						        <li class="last"><a href="/Mobile/Kboapp.aspx" class="gnb_mobile">MOBILE</a></li>
					        </ul>
				        </div>

                    <!-- 아시아시리즈 -->
                    <!--
                    <div class="gnb asia">
                        <a href="#" class="s_menu"><strong>아시아</strong> 시리즈</a>
					        <ul class="main">
						        <li><a href="/Schedule/ScoreBoard/ScoreBoard.aspx"style="width:86px">경기일정/결과</a>
							        <ul class="sub por01">
								        <li><a href="/Schedule/ScoreBoard/ScoreBoard.aspx">스코어보드</a></li>
								        <li><a href="/Schedule/GameList/General.aspx">경기일정/결과</a></li>
								        <li><a href="/Schedule/Analysis/Main.aspx">전력분석</a></li>
							        </ul>
						        </li>
						        <li><a href="/TeamRank/TeamRank.aspx">팀순위</a>
							        <ul class="sub">
								        <li><a href="/TeamRank/TeamRank.aspx" >팀순위</a></li>
								        <li><a href="/TeamRank/GraphDaily.aspx" >팀별 순위변동 그래프</a></li>
							        </ul>
						        </li>
						        <li><a href="/Record/Main.aspx">기록실</a>
							        <ul class="sub">
								        <li><a href="/Record/Main.aspx" >기록실</a></li>
			                            <li><a href="/Record/Etc/HitVsPit.aspx" >투수 vs 타자</a></li>

			                            <li><a href="/Record/Crowd/GraphTeam.aspx" >관중현황-KBO 정규시즌</a></li>
			                            <li><a href="/Record/Crowd/History.aspx" >역대 관중현황</a></li>
							        </ul>
						        </li>
						        <li><a href="/Futures/Schedule/GameList.aspx" style="width:65px">퓨처스리그</a>
							        <ul class="sub">
								        <li><a href="/Futures/Schedule/GameList.aspx" >퓨처스 경기 일정/결과</a></li>
								        <li><a href="/Futures/TeamRank/North.aspx" >퓨처스 팀순위</a></li>
								        <li><a href="/Futures/Main/North.aspx" >퓨처스 기록실</a></li>
							        </ul>
						        </li>
						        <li><a href="/History/Top/Hitter.aspx" style="width:65px">역대기록실</a>
							        <ul class="sub">
								        <li><a href="/History/Top/Hitter.aspx" >역대 최고기록 10걸</a></li>
								        <li><a href="/History/Team/Year2010.aspx" >역대 구단성적</a></li>
								        <li><a href="/History/Player/Hitter.aspx" >역대 타자</a></li>
								        <li><a href="/History/Player/Pitcher.aspx" >역대 투수</a></li>
								        <li><a href="/History/Etc/Award.aspx" >역대 개인수상</a></li>
                                        <li><a href="/History/Etc/GoldenGlobe.aspx" >역대 골든글로브</a></li>
								        <li><a href="/History/Etc/Amazing.aspx" >진기록 명기록</a></li>
								        <li><a href="/History/Ebook/Ebook2014.aspx" >E-BOOK</a></li>
								        <li><a href="/History/International/Asia.aspx" >국제대회</a></li>
							        </ul>
						        </li>
						        <li><a href="/News/Main.aspx">NEWS</a>
							        <ul class="sub">
								        <li><a href="/News/Main.aspx" >NEWS</a></li>
			                            <li><a href="/News/Notice/List.aspx" >KBO 보도자료</a></li>
			                            <li><a href="/News/Preview/List.aspx">프리뷰</a></li>
			                            <li><a href="/News/BreakingNews/List.aspx" >KBO 리그 속보</a></li>
			                            <li><a href="/News/Interview/List.aspx" >스타 인터뷰</a></li>
			                            <li><a href="/News/KboPhoto/List.aspx" >KBO PHOTO</a></li>
			                            <li><a href="/News/ExpectationWeek/List.aspx" >주간 예상 달성기록</a></li>
			                            <li><a href="/News/ExpectationDaily/List.aspx" >일간 예상 달성기록</a></li>
							        </ul>
						        </li>
						        <li><a href="/KboTv/Highlight/List.aspx" style="width:47px">KBO TV</a>
							        <ul class="sub">
								        <li><a href="/KboTv/Highlight/List.aspx" >하이라이트</a></li>
			                            <li><a href="/KboTv/MonthMvp/List.aspx" >월간 MVP</a></li>
			                            <li><a href="/KboTv/Legend/List.aspx" >레전드 올스타 동영상</a></li>
			                            <li><a href="/KboTv/Naver.aspx" >NAVER 스포츠</a></li>
			                            <li><a href="/KboTv/Daum.aspx" >DAUM스포츠</a></li>
			                            <li><a href="/KboTv/Crowd/List.aspx" >관중 돌파 감사영상</a></li>
			                            <li><a href="/KboTv/VeteranInterview/List.aspx" >야구 원로 인터뷰</a></li>
							        </ul>
						        </li>
						        <li><a href="/Player/Search.aspx" style="width:52px">선수현황</a>
							        <ul class="sub">
								        <li><a href="/Player/Search.aspx" >선수조회</a></li>
								        <li><a href="/Player/Register.aspx" >선수등록현황</a></li>
							        </ul>
						        </li>
						        <li><a href="/Board/Faq/List.aspx">게시판</a>
							        <ul class="sub">
								        <li><a href="/Board/Faq/List.aspx">자주하는 질문</a></li>
			                            <li><a href="/Board/Qna/List.aspx">Q&amp;A 게시판</a></li>
			                            <li><a href="/Board/Free/List.aspx">자유 게시판</a></li>
								        <li><a href="/Board/Committee/List.aspx" >기록위원회 Q&amp;A 게시판</a></li>
							        </ul>
						        </li>
					        </ul>
					        <ul class="special">
						        <li><a href="/About/TeamInfo.aspx" class="gnb_about">About <strong>KBO</strong></a>
							        <ul class="sub">
								        <li><a href="/About/TeamInfo.aspx" >구단소개</a></li>
                                        <li><a href="/About/Group/Activity.aspx" >조직 및 활동</a></li>
								        <li><a href="/About/Kbop.aspx" >KBOP</a></li>
								        <li><a href="/About/KboCi.aspx" >KBO CI</a></li>
								        <li><a href="/About/CatchPhrase.aspx" >2015 캐치프레이즈</a></li>
								        <li><a href="/About/GameManage.aspx" >경기운영체제</a></li>
								        <li><a href="/About/Map.aspx" >약도,관람료</a></li>
								        <li><a href="/About/GameRule.aspx" >경기규칙</a></li>
								        <li><a href="/About/TeamHistory.aspx" >각 구단 변천사</a></li>
								        <li><a href="/About/Change2015.aspx" >2015달라지는 점</a></li>
								        <li><a href="/About/Service2014.aspx" >KBO 사회공헌 사업</a></li>
								        <li><a href="/Committee/Organizationchart.aspx" >기록위원회</a></li>
							        </ul>
						        </li>
						        <li class="last"><a href="/Mobile/Baseball2015.aspx" class="gnb_mobile">Mobile</a></li>
					        </ul>
				        </div>
                        -->
			         	<!-- 아시아 시리즈 -->
			        </div>
		        </div>
	        </div>

	        <!-- // header-->

	        <!-- container -->
	        <div id="container">

<div class="wrap">
	<div id="lnb">
		<h3 class="title"><img src="http://image.koreabaseball.com/client/images/common/lnb_title08.png" alt="선수현황"></h3>
		<ul>
			<li><a href="/Player/Search.aspx">선수조회</a></li>
			<li><a href="/Player/Register.aspx">선수등록현황</a></li>
            <li><a href="/Player/RegisterAll.aspx">전체등록현황</a></li>
		</ul>
	</div>
	<!--lnb-->

    <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ctl00$cphContainer$ScriptManager1', 'mainForm', ['tctl00$ctl00$cphContainer$cphContents$udpRecord','cphContainer_cphContents_udpRecord'], ['ctl00$ctl00$cphContainer$cphContents$btnCalendarSelect','cphContainer_cphContents_btnCalendarSelect','ctl00$ctl00$cphContainer$cphContents$btnPreDate','cphContainer_cphContents_btnPreDate','ctl00$ctl00$cphContainer$cphContents$btnNextDate','cphContainer_cphContents_btnNextDate'], [], 90, 'ctl00$ctl00');
//]]>
</script>




<div id="contents" class="content01">
	<!--sub title & location -->
	<h3 class="sub_title"><img src="http://image.koreabaseball.com/client/images/common/img_sub_playereg.png" alt="선수등록현황"></h3>
	<div class="location">
		<span><a href="/"><img src="http://image.koreabaseball.com/client/images/common/location_home.jpg" alt="홈"></a></span>
		<span><img src="http://image.koreabaseball.com/client/images/common/location_next_level.jpg" alt=">"></span>
		<span class="f_depth"><a href="/Player/Search.aspx">선수현황</a></span>
		<span><img src="http://image.koreabaseball.com/client/images/common/location_next_level.jpg" alt=">"></span>
		<span class="l_depth">선수등록현황</span>
	</div>
	<!-- // sub title & location -->
    <!-- banner -->


<div class="com_banner">
    <div class="bx-wrapper" style="max-width: 100%; margin: 0px auto;"><div class="bx-viewport" style="width: 100%; overflow: hidden; position: relative; height: 89px;"><ul class="sub_banner" style="width: auto; position: relative; transition-duration: 0s; transform: translate3d(0px, -86px, 0px);"><a href="http://www.legend2i.com/community/noticeView.aspx?p_boardSe=78262&amp;p_currentPage=1&amp;p_searchSc=%EC%A0%9C%EB%AA%A9&amp;p_searchVa=" target="_blank" style="float: none; list-style: none; position: relative; width: 791px;" class="bx-clone"><img src="http://image.koreabaseball.com/client/images/common/img_banner_postadd.jpg" alt="포스트시즌 배너"></a>
        <li style="float: none; list-style: none; position: relative; width: 791px;"><a href="http://www.legend2i.com/community/noticeView.aspx?p_boardSe=62912&amp;p_currentPage=1&amp;p_searchSc=%EC%A0%9C%EB%AA%A9&amp;p_searchVa=" target="_blank"><img src="http://image.koreabaseball.com/client/images/common/img_banner_combo.jpg?version=201508171" alt=""></a></li>
		 <a href="/Mobile/Baseball2015.aspx" style="float: none; list-style: none; position: relative; width: 791px;"><img src="//image.koreabaseball.com/client/images/common/img_banner_post.jpg?version=201508172" alt=""></a>
         <a href="/Mobile/Kboapp.aspx" style="float: none; list-style: none; position: relative; width: 791px;"><img src="//image.koreabaseball.com/client/images/common/img_banner_app.jpg?version=20150407" alt=""></a>

         <a href="http://www.legend2i.com/community/noticeView.aspx?p_boardSe=78262&amp;p_currentPage=1&amp;p_searchSc=%EC%A0%9C%EB%AA%A9&amp;p_searchVa=" target="_blank" style="float: none; list-style: none; position: relative; width: 791px;"><img src="http://image.koreabaseball.com/client/images/common/img_banner_postadd.jpg" alt="포스트시즌 배너"></a>

    <li style="float: none; list-style: none; position: relative; width: 791px;" class="bx-clone"><a href="http://www.legend2i.com/community/noticeView.aspx?p_boardSe=62912&amp;p_currentPage=1&amp;p_searchSc=%EC%A0%9C%EB%AA%A9&amp;p_searchVa=" target="_blank"><img src="http://image.koreabaseball.com/client/images/common/img_banner_combo.jpg?version=201508171" alt=""></a></li></ul></div><div class="bx-controls bx-has-controls-direction bx-has-controls-auto"><div class="bx-controls-direction"><a class="bx-prev" href="">Prev</a><a class="bx-next" href="">Next</a></div><div class="bx-controls-auto"><div class="bx-controls-auto-item"><a class="bx-start active" href="">Start</a></div><div class="bx-controls-auto-item"><a class="bx-stop" href="">Stop</a></div></div></div></div>
    <div class="contron_area">
			<span id="sp_prev10" class="sp_prev"></span>
			<span id="sp_stop10" class="sp_stop"></span>
			<span id="sp_next10" class="sp_next"></span>
	</div>
</div>
<script type="text/javascript">
    $('.sub_banner').bxSlider({
        auto: true,
        autoControls: true,
        mode: 'vertical',
        speed: 1000
    });
</script>
    <!-- // banner -->

    <div id="cphContainer_cphContents_udpRecord">

    <script type="text/javascript">
    var request = Sys.WebForms.PageRequestManager.getInstance();
    request.add_pageLoaded(PageLoadedHandler);

    function PageLoadedHandler(sender, args)
    {
        var cntTeam = $(".teams ul li").length;
        var boxWidth = $(".teams ul").innerWidth();
        var rWidth = boxWidth / cntTeam;
        $(".teams ul li a").css("width", rWidth + "px");
        $(".teams ul li.last a").css("width", rWidth - cntTeam + "px");

        $(function () {
            $(".tNData th:last-child,.tNData td:last-child").css("border-right", "0");

            $(".calendar").datepicker({
                showOn: "button",
                buttonImage: "http://image.koreabaseball.com/client/images/common/calendar.jpg",
                buttonImageOnly: true,
                buttonText: "Select date",
                dateFormat: 'yy-mm-dd',
                defaultDate: $("#cphContainer_cphContents_hfSearchDate").val(),
                maxDate: 'today',
                beforeShow: function (e) {
                    var i_offset = $(e).offset(); //클릭된 input의 위치값 체크
                    //console.log(i_offset);
                    setTimeout(function () {
                        $('#ui-datepicker-div').css({ 'z-index': 9999 });
                    })
                },
                onSelect: function (selectedDate) {
                    $("#cphContainer_cphContents_hfSearchDate").val(selectedDate);
                    __doPostBack('ctl00$ctl00$cphContainer$cphContents$btnCalendarSelect','')
                }
            });
        });

    }
    </script>
        <div class="teams">
            <ul>

                    <li class="" data-id="SS"><a href="javascript:fnSearchChange('SS');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_SS.png" alt="삼성"><span>삼성</span></a></li>

                    <li class="" data-id="WO"><a href="javascript:fnSearchChange('WO');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_WO.png" alt="넥센"><span>넥센</span></a></li>

                    <li class="" data-id="NC"><a href="javascript:fnSearchChange('NC');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_NC.png" alt="NC"><span>NC</span></a></li>

                    <li class="" data-id="LG"><a href="javascript:fnSearchChange('LG');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_LG.png" alt="LG"><span>LG</span></a></li>

                    <li class="" data-id="SK"><a href="javascript:fnSearchChange('SK');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_SK.png" alt="SK"><span>SK</span></a></li>

                    <li class="" data-id="OB"><a href="javascript:fnSearchChange('OB');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_OB.png" alt="두산"><span>두산</span></a></li>

                    <li class="" data-id="LT"><a href="javascript:fnSearchChange('LT');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_LT.png" alt="롯데"><span>롯데</span></a></li>

                    <li class="" data-id="HT"><a href="javascript:fnSearchChange('HT');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_HT.png" alt="KIA"><span>KIA</span></a></li>

                    <li class="" data-id="HH"><a href="javascript:fnSearchChange('HH');" style="width: 79.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_HH.png" alt="한화"><span>한화</span></a></li>

                    <li class="last on" data-id="KT"><a href="javascript:fnSearchChange('KT');" style="width: 69.1px;"><img src="http://image.koreabaseball.com/client/images/common/emblem/emblemN_KT.png" alt="kt"><span>kt</span></a></li>

            </ul>
        </div>

        <!-- 날짜선택 -->
        <div class="yeardate">
		    <span class="date_prev"><input type="image" name="ctl00$ctl00$cphContainer$cphContents$btnPreDate" id="cphContainer_cphContents_btnPreDate" src="http://image.koreabaseball.com/client/images/common/date_prev.jpg" alt="이전날짜"></span>
		    <span class="date"><span id="cphContainer_cphContents_lblGameDate">2015.10.06(화)</span></span>
		    <span><input type="text" class="calendar blind02 hasDatepicker" id="dp1447301013862"><img class="ui-datepicker-trigger" src="http://image.koreabaseball.com/client/images/common/calendar.jpg" alt="Select date" title="Select date"></span>
		    <span class="date_next"><input type="image" name="ctl00$ctl00$cphContainer$cphContents$btnNextDate" id="cphContainer_cphContents_btnNextDate" src="http://image.koreabaseball.com/client/images/common/date_next.jpg" alt="다음날짜"></span>
	    </div>
        <!-- // 날짜선택 -->

        <!--선수 등록명단-->
        <div class="row">
            <h4 class="bul_history">kt wiz 선수등록명단</h4>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>감독</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>70</td>
                            <td>조범현</td>
                            <td>우투우타</td>
                            <td>1960-10-01</td>
                            <td style="border-right-width: 0px;">177cm, 80kg</td>
                        </tr>


                </tbody>
            </table>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>코치</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>71</td>
                            <td>이숭용</td>
                            <td>좌투좌타</td>
                            <td>1971-03-10</td>
                            <td style="border-right-width: 0px;">185cm, 86kg</td>
                        </tr>

                        <tr>
                            <td>74</td>
                            <td>정명원</td>
                            <td>우투우타</td>
                            <td>1966-06-14</td>
                            <td style="border-right-width: 0px;">189cm, 89kg</td>
                        </tr>

                        <tr>
                            <td>79</td>
                            <td>김민재</td>
                            <td>우투우타</td>
                            <td>1973-01-03</td>
                            <td style="border-right-width: 0px;">181cm, 84kg</td>
                        </tr>

                        <tr>
                            <td>80</td>
                            <td>전병호</td>
                            <td>좌투좌타</td>
                            <td>1973-03-23</td>
                            <td style="border-right-width: 0px;">186cm, 86kg</td>
                        </tr>

                        <tr>
                            <td>81</td>
                            <td>장재중</td>
                            <td>우투우타</td>
                            <td>1971-05-19</td>
                            <td style="border-right-width: 0px;">172cm, 78kg</td>
                        </tr>

                        <tr>
                            <td>85</td>
                            <td>박계원</td>
                            <td>우투우타</td>
                            <td>1970-02-04</td>
                            <td style="border-right-width: 0px;">186cm, 85kg</td>
                        </tr>

                        <tr>
                            <td>87</td>
                            <td>황병일</td>
                            <td>우투우타</td>
                            <td>1960-03-22</td>
                            <td style="border-right-width: 0px;">180cm, 86kg</td>
                        </tr>


                </tbody>
            </table>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>투수</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>15</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=60264">정대현</a></td>
                            <td>좌투좌타</td>
                            <td>1991-07-19</td>
                            <td style="border-right-width: 0px;">186cm, 97kg</td>
                        </tr>

                        <tr>
                            <td>32</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=77199">옥스프링</a></td>
                            <td>우투좌타</td>
                            <td>1977-05-13</td>
                            <td style="border-right-width: 0px;">183cm, 90kg</td>
                        </tr>

                        <tr>
                            <td>34</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=64017">심재민</a></td>
                            <td>좌투좌타</td>
                            <td>1994-02-18</td>
                            <td style="border-right-width: 0px;">182cm, 92kg</td>
                        </tr>

                        <tr>
                            <td>37</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=61434">저마노</a></td>
                            <td>우투우타</td>
                            <td>1982-08-06</td>
                            <td style="border-right-width: 0px;">190cm, 95kg</td>
                        </tr>

                        <tr>
                            <td>39</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=64001">고영표</a></td>
                            <td>우언우타</td>
                            <td>1991-09-16</td>
                            <td style="border-right-width: 0px;">187cm, 88kg</td>
                        </tr>

                        <tr>
                            <td>41</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=64041">안상빈</a></td>
                            <td>우언우타</td>
                            <td>1995-03-23</td>
                            <td style="border-right-width: 0px;">187cm, 85kg</td>
                        </tr>

                        <tr>
                            <td>42</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65042">홍성무</a></td>
                            <td>우투우타</td>
                            <td>1993-01-25</td>
                            <td style="border-right-width: 0px;">183cm, 98kg</td>
                        </tr>

                        <tr>
                            <td>51</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=75149">홍성용</a></td>
                            <td>좌투좌타</td>
                            <td>1986-11-18</td>
                            <td style="border-right-width: 0px;">180cm, 85kg</td>
                        </tr>

                        <tr>
                            <td>56</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65056">엄상백</a></td>
                            <td>우언우타</td>
                            <td>1996-10-04</td>
                            <td style="border-right-width: 0px;">187cm, 72kg</td>
                        </tr>

                        <tr>
                            <td>58</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65058">정성곤</a></td>
                            <td>좌투좌타</td>
                            <td>1996-07-10</td>
                            <td style="border-right-width: 0px;">176cm, 74kg</td>
                        </tr>

                        <tr>
                            <td>59</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=60848">최원재</a></td>
                            <td>우언좌타</td>
                            <td>1987-04-29</td>
                            <td style="border-right-width: 0px;">185cm, 84kg</td>
                        </tr>

                        <tr>
                            <td>60</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65060">주권</a></td>
                            <td>우투우타</td>
                            <td>1995-05-31</td>
                            <td style="border-right-width: 0px;">181cm, 82kg</td>
                        </tr>

                        <tr>
                            <td>62</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65062">김재윤</a></td>
                            <td>우투우타</td>
                            <td>1990-09-16</td>
                            <td style="border-right-width: 0px;">185cm, 91kg</td>
                        </tr>

                        <tr>
                            <td>67</td>
                            <td><a href="/Record/Player/PitcherDetail/Basic.aspx?playerId=65067">조무근</a></td>
                            <td>우투우타</td>
                            <td>1991-09-26</td>
                            <td style="border-right-width: 0px;">198cm, 116kg</td>
                        </tr>


                </tbody>
            </table>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>포수</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>20</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=78892">윤요섭</a></td>
                            <td>우투우타</td>
                            <td>1982-03-30</td>
                            <td style="border-right-width: 0px;">180cm, 96kg</td>
                        </tr>

                        <tr>
                            <td>22</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=78548">장성우</a></td>
                            <td>우투우타</td>
                            <td>1990-01-17</td>
                            <td style="border-right-width: 0px;">187cm, 100kg</td>
                        </tr>

                        <tr>
                            <td>84</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=62537">윤여운</a></td>
                            <td>우투우타</td>
                            <td>1990-02-22</td>
                            <td style="border-right-width: 0px;">181cm, 90kg</td>
                        </tr>


                </tbody>
            </table>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>내야수</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>3</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=63448">김영환</a></td>
                            <td>우투좌타</td>
                            <td>1993-01-31</td>
                            <td style="border-right-width: 0px;">178cm, 74kg</td>
                        </tr>

                        <tr>
                            <td>5</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=65005">마르테</a></td>
                            <td>우투우타</td>
                            <td>1983-10-21</td>
                            <td style="border-right-width: 0px;">185cm, 93kg</td>
                        </tr>

                        <tr>
                            <td>6</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=73113">박경수</a></td>
                            <td>우투우타</td>
                            <td>1984-03-31</td>
                            <td style="border-right-width: 0px;">178cm, 80kg</td>
                        </tr>

                        <tr>
                            <td>7</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=64007">문상철</a></td>
                            <td>우투우타</td>
                            <td>1991-04-06</td>
                            <td style="border-right-width: 0px;">184cm, 85kg</td>
                        </tr>

                        <tr>
                            <td>16</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=70553">박기혁</a></td>
                            <td>우투우타</td>
                            <td>1981-06-04</td>
                            <td style="border-right-width: 0px;">179cm, 77kg</td>
                        </tr>

                        <tr>
                            <td>35</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=71504">신명철</a></td>
                            <td>우투우타</td>
                            <td>1978-08-06</td>
                            <td style="border-right-width: 0px;">181cm, 77kg</td>
                        </tr>

                        <tr>
                            <td>52</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=65052">댄블랙</a></td>
                            <td>우투양타</td>
                            <td>1987-07-02</td>
                            <td style="border-right-width: 0px;">193cm, 116kg</td>
                        </tr>

                        <tr>
                            <td>66</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=60496">김선민</a></td>
                            <td>우투우타</td>
                            <td>1990-11-13</td>
                            <td style="border-right-width: 0px;">174cm, 75kg</td>
                        </tr>


                </tbody>
            </table>
            <table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="120">
                    <col width="120">
                    <col width="166">
                    <col width="157">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>외야수</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                        <tr>
                            <td>4</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=64004">김민혁</a></td>
                            <td>우투좌타</td>
                            <td>1995-11-21</td>
                            <td style="border-right-width: 0px;">181cm, 71kg</td>
                        </tr>

                        <tr>
                            <td>8</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=63088">김진곤</a></td>
                            <td>우투좌타</td>
                            <td>1987-09-10</td>
                            <td style="border-right-width: 0px;">173cm, 75kg</td>
                        </tr>

                        <tr>
                            <td>19</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=70646">김상현</a></td>
                            <td>우투우타</td>
                            <td>1980-11-12</td>
                            <td style="border-right-width: 0px;">190cm, 95kg</td>
                        </tr>

                        <tr>
                            <td>25</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=78753">김사연</a></td>
                            <td>우투우타</td>
                            <td>1988-08-09</td>
                            <td style="border-right-width: 0px;">179cm, 80kg</td>
                        </tr>

                        <tr>
                            <td>27</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=79453">오정복</a></td>
                            <td>우투우타</td>
                            <td>1986-10-13</td>
                            <td style="border-right-width: 0px;">177cm, 75kg</td>
                        </tr>

                        <tr>
                            <td>45</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=78517">하준호</a></td>
                            <td>좌투좌타</td>
                            <td>1989-04-29</td>
                            <td style="border-right-width: 0px;">174cm, 78kg</td>
                        </tr>

                        <tr>
                            <td>53</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=73153">이대형</a></td>
                            <td>좌투좌타</td>
                            <td>1983-07-19</td>
                            <td style="border-right-width: 0px;">184cm, 78kg</td>
                        </tr>

                        <tr>
                            <td>65</td>
                            <td><a href="/Record/Player/HitterDetail/Basic.aspx?playerId=64166">배병옥</a></td>
                            <td>우투우타</td>
                            <td>1995-11-21</td>
                            <td style="border-right-width: 0px;">185cm, 80kg</td>
                        </tr>


                </tbody>
            </table>
        </div>
        <!-- 등록/말소 현황-->
        <div class="row mgt35">
            <h4 class="bul_history">kt wiz 등/말소 현황</h4>
            <h5 class="bul_sub">등록</h5>
                <div id="cphContainer_cphContents_pnlEntryY">

                        </div><table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="110">
                    <col width="110">
                    <col width="110">
                    <col width="146">
                    <col width="137">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>선수명</th>
                        <th>포지션</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                            <td colspan="6" style="border-right-width: 0px;">당일 1군 등록된 선수가 없습니다.</td>
                        </tr>


                </tbody>
            </table>

            <h5 class="bul_sub">말소</h5>
            <div id="cphContainer_cphContents_pnlEntryN">

                        </div><table class="tNData" summary="선수등록명단으로 등번호,포지션,투타유형,생년월일,체격,등록일수를나타냅니다">
                <colgroup>
                    <col width="80">
                    <col width="110">
                    <col width="110">
                    <col width="110">
                    <col width="146">
                    <col width="137">
                </colgroup>
                <thead>
                    <tr>
                        <th>등번호</th>
                        <th>선수명</th>
                        <th>포지션</th>
                        <th>투타유형</th>
                        <th>생년월일</th>
                        <th style="border-right-width: 0px;">체격</th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                            <td colspan="6" style="border-right-width: 0px;">당일 1군 말소된 선수가 없습니다.</td>
                        </tr>


                </tbody>
            </table>
        </div>

        <input type="hidden" name="ctl00$ctl00$cphContainer$cphContents$hfSearchTeam" id="cphContainer_cphContents_hfSearchTeam" value="KT">
        <input type="hidden" name="ctl00$ctl00$cphContainer$cphContents$hfSearchDate" id="cphContainer_cphContents_hfSearchDate" value="2015-10-06 오전 12:00:00">
        <input type="submit" name="ctl00$ctl00$cphContainer$cphContents$btnCalendarSelect" value="" id="cphContainer_cphContents_btnCalendarSelect" style="display:none;">
    </div>
</div>


</div>

	        </div>

	        <!-- // container -->

	        <!-- footer -->
	        <div id="footer">
		        <div class="wrapper01">
			        <div class="row">
				        <div class="team_kbo">
					        <ul>
						        <li><a target="_blank" href="http://www.samsunglions.com/"><img src="//image.koreabaseball.com/client/images/common/team_lions.png" alt="삼성"></a></li>
						        <li><a target="_blank" href="http://www.heroes-baseball.co.kr/"><img src="//image.koreabaseball.com/client/images/common/team_heroes.png" alt="넥센"></a></li>
						        <li><a target="_blank" href="http://www.ncdinos.com/"><img src="//image.koreabaseball.com/client/images/common/team_dinos.png" alt="NC"></a></li>
						        <li><a target="_blank" href="http://www.lgtwins.com/"><img src="//image.koreabaseball.com/client/images/common/team_twins.png" alt="LG"></a></li>
						        <li><a target="_blank" href="http://www.sksports.net/Wyverns/main.asp"><img src="//image.koreabaseball.com/client/images/common/team_wyvurns.png" alt="SK"></a></li>
						        <li><a target="_blank" href="http://www.doosanbears.com/"><img src="//image.koreabaseball.com/client/images/common/team_bears.png" alt="두산"></a></li>
						        <li><a target="_blank" href="http://www.giantsclub.com/html/"><img src="//image.koreabaseball.com/client/images/common/team_giants.png" alt="롯데"></a></li>
						        <li><a target="_blank" href="http://www.tigers.co.kr"><img src="//image.koreabaseball.com/client/images/common/team_tigers.png" alt="기아"></a></li>
						        <li><a target="_blank" href="http://www.hanwhaeagles.co.kr/html/main/main.asp"><img src="//image.koreabaseball.com/client/images/common/team_eagles.png" alt="한화"></a></li>
						        <li><a target="_blank" href="http://www.ktwiz.co.kr/sports/site/baseball/main.do"><img src="//image.koreabaseball.com/client/images/common/team_wiz.png" alt="KT"></a></li>
					        </ul>
				        </div>
			        </div>
		        </div>
		        <div class="wrapper02">
			        <div class="row">
				        <div class="foo">
					        <h2 class="sub_logo" onclick="javascript:location.href='/Etc/PressRelease.aspx';" style="cursor:pointer;">KBO</h2>

					        <div class="copyright">
						        <div class="foo_menu">
							        <ul>
								        <li class="first"><a href="/About/TeamInfo.aspx">KBO소개</a></li>
								        <li><a href="/Schedule/ScoreBoard/ScoreBoard.aspx">문자중계</a></li>
								        <li><a href="/Board/Faq/List.aspx">고객질문</a></li>
								        <li><a href="/Etc/SiteMap.aspx">사이트맵</a></li>
								        <li><a href="/Etc/Privacy.aspx">개인정보보호정책</a></li>
								        <li class="last"><a href="/Etc/Advertising.aspx">광고문의</a></li>
							        </ul>
						        </div>
						        <div class="address">
						        <p>(사)한국야구위원회 서울특별시 강남구 강남대로 278 TEL 02) 3460-4600</p>
						        <p>본 사이트는 <strong>스포츠투아이㈜</strong>가 KBO 리그 팬을 위해 운영하는 KBO 공식 사이트입니다.</p>
						        <p>Copyrightⓒ KBO, All Rights Reserved.</p>
						        <span class="sign">
							        <img src="//image.koreabaseball.com/client/images/common/img_xhtml.png" alt="w3chtml">
							        <img src="//image.koreabaseball.com/client/images/common/img_verisign.png" alt="verisign">
						        </span>
						        </div>
					        </div>
					        <div class="verify">
					        </div>
				        </div>
			        </div>
		        </div>
	        </div>
	        <!-- // footer -->
        </div>


<script type="text/javascript">
//<![CDATA[
jQuery(function ($) {$('[data-id=SS]').parent().children().filter(':last').addClass('last');$('[data-id=SS]').addClass('on');$('[data-id=SS]').siblings().removeClass('on');});//]]>
</script>
<span style="display: none !important;"><input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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"></span><span style="display: none !important;"><input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="3CB9947C"></span><span style="display: none !important;"><input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value=""></span><span style="display: none !important;"><input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value=""></span><span style="display: none !important;"><input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEdAAewENZj2J1zZCvR0D5H0Yo3MuN4Os9LP1AFaiK4aD3ur8mhLl/VP02FtVAMo5z5IguaA+o3uafw7wp4CUJ76q33E4seC6JQTftOIuy7Cku2br0XPyMYYAm84yfpHD9ObZoQbgVBup4xAxzzUKps4Aq76rwlN08GBZZMkRb74EyNznBOvslTaJeNtU5hLR9kW9o="></span></form>

    <script type="text/javascript">
    //<![CDATA[
	    $(document).ready(function () {
	        var historybanner = new js_rolling(document.getElementById('HistoryItem'));
            historybanner.set_direction(4);
	        historybanner.time_dealy_pause = 0; //하나의 대상이 새로 시작할 때 멈추는 시간, 0 이면 적용 안함

	        function bannerTop() {
	            banner.move_up();
	            banner.set_direction(1);
	        }
	        function bannerBottom() {
	            banner.move_down();
	            banner.set_direction(3);
	        }
	        function bannerRight() {
	            banner.move_right();
	            banner.set_direction(2);
	        }
	        function bannerLeft() {
	            banner.move_left();
	            banner.set_direction(4);
	        }
	        function bannerStop() {
	            banner.stop();
	        }
	        function bannerPlay() {
	            banner.resume();
	        }

	        function historybannerTop() {
	            historybanner.move_up();
	            historybanner.set_direction(1);
	        }
	        function historybannerBottom() {
	            historybanner.move_down();
	            historybanner.set_direction(3);
	        }
	        function historybannerRight() {
	            historybanner.move_right();
	            historybanner.set_direction(2);
	        }
	        function historybannerLeft() {
	            historybanner.move_left();
	            historybanner.set_direction(4);
	        }
	        function historybannerStop() {
	            historybanner.stop();
	        }
	        function historybannerPlay() {
	            historybanner.resume();

	        }

	        //연사
	        $(".btnControl a").click(function (e) {
	            e.preventDefault();
	            if ($(this).hasClass("left")) {
	                historybannerLeft();
	            } else if ($(this).hasClass("right")) {
	                historybannerRight();
	            } else if ($(this).hasClass("playing")) {
	                historybannerPlay();
	                $(this).removeClass("playing");
	                $(this).find("img").attr({
	                    alt: "Stop",
	                    src: "//image.koreabaseball.com/client/images/main/roll_stop.png"
	                });
	            } else {
	                historybannerStop();
	                $(this).addClass("playing");
	                $(this).find("img").attr({
	                    alt: "Play",
	                    src: "//image.koreabaseball.com/client/images/main/roll_play.png"
	                });
	            }
	        });


	    });
        // ]]>
    </script>


<div id="ui-datepicker-div" class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all"></div></body></html>
"""

codeParsing(html)
