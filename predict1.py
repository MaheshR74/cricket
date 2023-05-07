import streamlit as st
import numpy as np
import joblib

# load the trained model
lr_regressor = joblib.load('lr-model.pkl')

# team names
teams = ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders',
         'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']

# initialize input values
batting_team = bowling_team = teams[0]
overs = runs = wickets = runs_in_prev_5 = wickets_in_prev_5 = 0

# user input form
st.title('Cricket Score Prediction')
batting_team = st.selectbox('Batting Team', teams)
bowling_team = st.selectbox('Bowling Team', teams)
overs = st.number_input('Overs', min_value=0, max_value=50, step=1, value=overs)
runs = st.number_input('Runs', min_value=0, value=runs)
wickets = st.number_input('Wickets', min_value=0, value=wickets)
runs_in_prev_5 = st.number_input('Runs in Previous 5 Overs', min_value=0, value=runs_in_prev_5)
wickets_in_prev_5 = st.number_input('Wickets in Previous 5 Overs', min_value=0, value=wickets_in_prev_5)
submit_button = st.button('Predict')

# prediction
if submit_button:
    # create input array
    input_array = np.zeros(21)
    input_array[teams.index(batting_team)] = 1
    input_array[8 + teams.index(bowling_team)] = 1
    input_array[16] = overs
    input_array[17] = runs
    input_array[18] = wickets
    input_array[19] = runs_in_prev_5
    input_array[20] = wickets_in_prev_5
    # predict the score range
    my_prediction = int(lr_regressor.predict([input_array])[0])
    lower_limit, upper_limit = my_prediction-10, my_prediction+5

    # display the result
    st.write(f"The predicted score is between {lower_limit} and {upper_limit}.")
