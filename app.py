import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📖 Netflix Data Storytelling App")

df = pd.read_csv("netflix_titles.csv")

st.header("Dataset Introduction")
st.write("This dataset contains Netflix Movies and TV Shows from different countries and years.")

st.header("Dataset Preview")
st.dataframe(df.head())

st.header("Exploratory Data Analysis")

fig1 = px.pie(df, names="type", title="Movies vs TV Shows")
st.plotly_chart(fig1)

fig2 = px.histogram(df, x="rating", title="Ratings Distribution")
st.plotly_chart(fig2)

fig3 = px.histogram(df, x="release_year", title="Release Year Trend")
st.plotly_chart(fig3)

st.header("Insights and Findings")

st.write("""
1. Movies are more common than TV Shows.
2. Most content was released after 2010.
3. TV-MA is the most common rating.
4. Netflix content grew rapidly after 2015.
""")

st.header("Conclusion")

st.write("""
Netflix focuses heavily on movies and mature audience content.
The platform experienced major content growth in recent years.
""")