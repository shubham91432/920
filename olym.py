import streamlit as st
import pandas as pd
import preprocessor
import helper
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

st.sidebar.title("Olympics Analysis")
df = preprocessor.preprocess(df,region_df)
user_menu = st.sidebar.radio(
    'Select an Option',
  ('Medal Tally',' Overall Anlaysis','Country-wise Analysis','Athlete wise Analysis')
)

st.dataframe(df)

if user_menu == 'Medal Tally':
    medal_tally = helper.medal_tally(df)
    st.dataframe(medal_tally)

   # st.sidebar.title("Olympics Analysis")

    st.sidebar.image(
        'https://e7.pngegg.com/pngimages/1020/402/png-clipart-2024-summer-olympics-brand-circle-area-olympic-rings-olympics-logo-text-sport.png')
    user_menu = st.sidebar.radio(
        'Select an Option',
        ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis')
    )

    if user_menu == 'Medal Tally':
        st.sidebar.header("Medal Tally")
        years, country = helper.country_year_list(df)

        selected_year = st.sidebar.selectbox("Select Year", years)
        selected_country = st.sidebar.selectbox("Select Country", country)

        medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
        if selected_year == 'Overall' and selected_country == 'Overall':
            st.title("Overall Tally")
        if selected_year != 'Overall' and selected_country == 'Overall':
            st.title("Medal Tally in " + str(selected_year) + " Olympics")
        if selected_year == 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " overall performance")
        if selected_year != 'Overall' and selected_country != 'Overall':
            st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

   # st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
