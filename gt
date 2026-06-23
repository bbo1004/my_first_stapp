import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="대학생 용돈 관리",
    page_icon="💰",
    layout="wide"
)

st.title("💰 대학생 용돈 관리 웹사이트")
st.markdown("월별 수입과 지출을 관리해 보세요.")

st.divider()

# 수입 입력
st.header("📈 수입 입력")

income = st.number_input(
    "이번 달 수입(원)",
    min_value=0,
    value=500000,
    step=10000
)

st.divider()

# 지출 입력
st.header("📉 지출 입력")

food = st.number_input("🍔 식비", min_value=0, value=100000, step=10000)
transport = st.number_input("🚌 교통비", min_value=0, value=50000, step=5000)
shopping = st.number_input("🛍 쇼핑", min_value=0, value=80000, step=10000)
study = st.number_input("📚 학습비", min_value=0, value=30000, step=5000)
etc = st.number_input("🎵 기타", min_value=0, value=20000, step=5000)

expenses = food + transport + shopping + study + etc
balance = income - expenses

st.divider()

# 요약
st.header("📊 이번 달 현황")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("총 수입", f"{income:,}원")

with col2:
    st.metric("총 지출", f"{expenses:,}원")

with col3:
    st.metric("잔액", f"{balance:,}원")

st.divider()

# 파이차트
data = pd.DataFrame({
    "항목": ["식비", "교통비", "쇼핑", "학습비", "기타"],
    "금액": [food, transport, shopping, study, etc]
})

fig = px.pie(
    data,
    values="금액",
    names="항목",
    title="지출 비율 분석"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# 소비 분석
st.header("💡 소비 분석")

if expenses <= income * 0.5:
    st.success("소비 관리가 매우 우수합니다!")
elif expenses <= income * 0.8:
    st.info("적절한 소비 수준입니다.")
else:
    st.warning("지출이 많습니다. 소비를 점검해 보세요.")

# 절약 팁
st.header("🎯 절약 팁")

tips = [
    "카페 이용 횟수 줄이기",
    "교통 정기권 활용하기",
    "충동구매 전 하루 고민하기",
    "가계부 작성 습관 만들기",
    "중고거래 활용하기"
]

for tip in tips:
    st.write("✅", tip)
