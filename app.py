# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pkIlQxbOf1bFm7vqa5c0ops3P6k_GNC8
"""

import streamlit as st

def main():
    st.title("Music Recommendation System")

    # Sidebar input
    song_title = st.sidebar.text_input("Enter a song title")
    number_songs = st.sidebar.slider("Number of songs to recommend", min_value=1, max_value=10, value=5)

    if st.sidebar.button("Recommend"):
        # Load the recommendation model
        recommender = joblib.load('recommendation_model.joblib')
        # Define the recommendation input
        recommendation = {'song': song_title, 'number_songs': number_songs}
        # Get recommendations
        recommendations = recommender.recommend(recommendation)

        # Display recommendations
        st.write(f"The {number_songs} recommended songs for {song_title} are:")
        for i, rec_song in enumerate(recommendations):
            st.write(f"Number {i+1}:")
            st.write(f"{rec_song[1]} by {rec_song[2]} with {round(rec_song[0], 3)} similarity score")
            st.write("--------------------")

if __name__ == '__main__':
    main()