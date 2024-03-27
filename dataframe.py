# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv("gapminder.tsv", sep="\t") 
    # 데이터 프레임으로 반환(표로 반환한다는 뜻)구분자를 이용해서 데이터 저장
    return df

def plot_matplotlib():
    st.title("**Bar Plot** with Seaborn") # title 사용해서 크게 표시
    df = load_data() # 테이터 불러오기 테이터 프레임으로 구보 변환
    fig, ax = plt.subplots() # 시각화 하는 것 fig ->그림 ax ->도화지
    
    # Using Seaborn's barplot function
    sns.barplot(x=df['year'], y=df['lifeExp'], data=df, ax=ax)
    
    # Labeling axes and title
    ax.set_xlabel("year")
    ax.set_ylabel("lifeExp")
    ax.set_title("yer vs lifeExp")
        
    st.pyplot(fig) #웹상에 즉 streamlit에 그리는 것을 의미함

def main():
    st.title("Data Display st.dataframe()") #웹페이지 타이틀
    st.checkbox("Use container width", value=False, key = 'use_container_width')
    
    df = load_data()
    st.dataframe(df, use_container_width=True)

    #pandas style
    st.dataframe(df.iloc[:5,2:].style.highlight_max(axis=0))

    plot_matplotlib()
    
    
if __name__ == "__main__":
    main()