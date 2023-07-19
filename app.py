import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe=pickle.load(open('pipe.pkl','rb'))

teams = ['Australia',
 'India',
 'Bangladesh',
 'New Zealand',
 'South Africa',
 'England',
 'West Indies',
 'Afghanistan',
 'Pakistan',
 'Sri Lanka']

cities = ['Colombo',
 'Mirpur',
 'Johannesburg',
 'Dubai',
 'Auckland',
 'Cape Town',
 'London',
 'Pallekele',
 'Barbados',
 'Sydney',
 'Melbourne',
 'Durban',
 'St Lucia',
 'Wellington',
 'Lauderhill',
 'Hamilton',
 'Centurion',
 'Manchester',
 'Abu Dhabi',
 'Mumbai',
 'Nottingham',
 'Southampton',
 'Mount Maunganui',
 'Chittagong',
 'Kolkata',
 'Lahore',
 'Delhi',
 'Nagpur',
 'Chandigarh',
 'Adelaide',
 'Bangalore',
 'St Kitts',
 'Cardiff',
 'Christchurch',
 'Trinidad']

st.title('Cricket Score Predictor')

# col1, col2 = st.beta_columns(2)
col1, col2 = st.columns(2)


with col1:
    batting_team=st.selectbox('Select batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select bowling team',sorted(teams))    

city=st.selectbox('Select city',sorted(cities))

col3,col4,col5=st.columns(3)

with col3:
    current_score=st.number_input('Current Score')
with col4:
    overs_done=st.number_input('Overs done(works for over>5)') 
with col5:
    wickets=st.number_input('Wickets out')  

last_five=st.number_input('Runs scored in last 5 overs')

# if st.button('Predict Score'):
#     balls_left = 120 - overs_done * 6
#     wickets_left = 10 - wickets
#     crr = current_score / overs_done

#     # Perform checks
#     if wickets_left < 0:
#         st.error("Wickets cannot be greater than 10.")
#     elif last_five > current_score:
#         st.error("Last five runs cannot be greater than the current score.")
#     else:
#         input_df = pd.DataFrame({
#             'batting_team': [batting_team],
#             'bowling_team': [bowling_team],
#             'city': [city],
#             'current_score': [current_score],
#             'balls_left': [balls_left],
#             'wickets_left': [wickets_left],
#             'crr': [crr],
#             'last_five': [last_five]
#         }) 

#         st.table(input_df)

#         result = pipe.predict(input_df)

#         st.header("Predicted Score: " + str(int(result[0])))
if st.button('Predict Score'):
    balls_left = 120 - overs_done * 6
    wickets_left = 10 - wickets
    crr = current_score / overs_done

    # Perform checks
    if wickets_left < 0:
        st.error("Wickets cannot be greater than 10.")
    elif last_five > current_score:
        st.error("Last five runs cannot be greater than the current score.")
    else:
        input_df = pd.DataFrame({
            'batting_team': teams,  # List of all batting teams
            'bowling_team': [bowling_team] * len(teams),  # Selected bowling team for comparison
            'city': [city] * len(teams),  # Same city for all teams
            'current_score': [current_score] * len(teams),  # Same current score for all teams
            'balls_left': [balls_left] * len(teams),  # Same balls left for all teams
            'wickets_left': [wickets_left] * len(teams),  # Same wickets left for all teams
            'crr': [crr] * len(teams),  # Same crr for all teams
            'last_five': [last_five] * len(teams)  # Same last five runs for all teams
        }) 

        # st.table(input_df)

        result = pipe.predict(input_df)

        # Create a bar chart of predicted scores for all teams except the selected bowling team
        # teams_except_bowling = [team for team in teams if team != bowling_team]
        # predicted_scores_except_bowling = [int(score) for score in result if score != result[teams.index(bowling_team)]]

        # fig, ax = plt.subplots()
        # ax.bar(teams_except_bowling, predicted_scores_except_bowling)
        # ax.set_xlabel('Batting Teams')
        # ax.set_ylabel('Predicted Scores')
        # ax.set_title('Predicted Scores vs. Bowling Team')
        # st.pyplot(fig)

        st.header("Predicted Score: " + str(int(result[teams.index(bowling_team)])))

   
