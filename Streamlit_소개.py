import streamlit as st # streamlit 라이브러리 임포트
st.title('지점 매출 분석 대시보드')

<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>지점 매출 분석 대시보드</title>

<style>
body{
    font-family: Arial, sans-serif;
    margin:0;
    background:#f5f5f5;
}

header{
    text-align:center;
    background:white;
    padding:20px;
    box-shadow:0 2px 5px rgba(0,0,0,0.1);
}

header img{
    width:100%;
    max-height:300px;
    object-fit:cover;
}

.container{
    max-width:1200px;
    margin:auto;
    padding:20px;
}

.card{
    background:white;
    padding:20px;
    margin-bottom:20px;
    border-radius:10px;
    box-shadow:0 2px 5px rgba(0,0,0,0.1);
}

table{
    width:100%;
    border-collapse:collapse;
}

th,td{
    border:1px solid #ddd;
    padding:10px;
    text-align:center;
}

th{
    background:#4CAF50;
    color:white;
}

.metric{
    display:flex;
    gap:20px;
}

.metric-box{
    flex:1;
    background:white;
    padding:20px;
    border-radius:10px;
    text-align:center;
    box-shadow:0 2px 5px rgba(0,0,0,0.1);
}
</style>
</head>

<body>

<header>
    <img src="banner.png" alt="배너">
    <h1>지점 매출 분석 대시보드</h1>
</header>

<div class="container">

    <div class="metric">
        <div class="metric-box">
            <h3>지점 수</h3>
            <p>5개</p>
        </div>

        <div class="metric-box">
            <h3>전체 평균</h3>
            <p>96.0</p>
        </div>

        <div class="metric-box">
            <h3>목표 달성률</h3>
            <p>60%</p>
        </div>
    </div>

    <div class="card">
        <h2>지점별 실적</h2>

        <table>
            <tr>
                <th>지점</th>
                <th>1분기</th>
                <th>2분기</th>
                <th>3분기</th>
                <th>총매출</th>
            </tr>

            <tr>
                <td>강남점</td>
                <td>150</td>
                <td>130</td>
                <td>140</td>
                <td>420</td>
            </tr>

            <tr>
                <td>홍대점</td>
                <td>90</td>
                <td>110</td>
                <td>100</td>
                <td>300</td>
            </tr>
        </table>
    </div>

    <div class="card">
        <h2>프로젝트 소개</h2>
        <p>
            본 프로젝트는 여러 지점의 분기별 매출 데이터를 분석하여
            평균 매출, 등급, 순위, 목표 달성률을 시각적으로 제공하는
            경영 분석 대시보드입니다.
        </p>
    </div>

</div>

</body>
</html>
