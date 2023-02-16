import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl', "rb"))

st.title('ipl win predictor')

teams = ['Gujarat Lions', 'Kings XI Punjab', 'Sunrisers Hyderabad',
       'Deccan Chargers', 'Mumbai Indians', 'Chennai Super Kings',
       'Rajasthan Royals', 'Delhi Daredevils', 'Kolkata Knight Riders',
       'Royal Challengers Bangalore', 'Delhi Capitals',
       'Rising Pune Supergiant', 'Rising Pune Supergiants',
       'Kochi Tuskers Kerala', 'Pune Warriors']

city = ['Rajkot', 'Delhi', 'Hyderabad', 'Indore', 'Kolkata', 'Mumbai',
       'Chennai', 'Jaipur', 'Pune', 'Bengaluru', 'Chandigarh',
       'Abu Dhabi', 'Bangalore', 'Port Elizabeth', 'Centurion',
       'Visakhapatnam', 'Durban', 'Mohali', 'Ranchi', 'Ahmedabad',
       'Kimberley', 'Nagpur', 'Dharamsala', 'Raipur', 'Kochi',
       'Johannesburg', 'Bloemfontein', 'Cuttack', 'Cape Town', 'Kanpur',
       'Sharjah', 'East London']

col1, col2 = st.columns(2)

with col1:
    batting = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowling = st.selectbox('Slect Bowling Team', sorted(teams))

city = st.selectbox('Slect Host City', sorted(city))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
       score = st.number_input('Score')
with col4:
       overs = st.number_input('Overs Completed')
with col5:
       wickets = st.number_input('Wickets Down')

if st.button('Predict Win Probability'):
       runs_left = target - score
       balls_left = 120 - overs * 6
       wickets_left = 10 - wickets
       crr = score / overs
       rrr = (runs_left * 6) / balls_left

       input_data = pd.DataFrame({'batting_team': [batting], 'bowling_team': [bowling], 'city': [city],
                                  'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets_left': [wickets_left],
                                  'total_runs_y': [target], 'crr': [crr], 'rrr': [rrr]

       })
       result = pipe.predict_proba(input_data)
       loss = result[0][0]
       win = result[0][1]

       st.header(batting + "-" + str(round(win * 100)) + "%")
       st.header(bowling + "-" + str(round(loss * 100)) + "%")