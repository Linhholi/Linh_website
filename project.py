import streamlit as st
import pandas as pd
from datetime import datetime
# import cv2
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import numpy as np

def project_page1():
    st.title("The Superheroes Project")

    # Load the CSV data
    data = pd.read_csv('data.csv',index_col=False)

    # Get unique citizenship values
    citizenship_options = ['All'] + data['Citizenship'].unique().tolist()

    # Convert 'First Appearance' column to datetime type
    data['First Appearance'] = pd.to_datetime(data['First Appearance'], format='%m/%Y')

    # Set default values for start date, end date, and citizenship
    if 'start_date' not in st.session_state:
        st.session_state.start_date = datetime(1900, 1, 1)
    if 'end_date' not in st.session_state:
        st.session_state.end_date = datetime(2024, 1, 1)

    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    # Create search boxes
    with col1:
        search_query1 = st.text_input('Search by Name')
    with col2:
        # Date range input for First Appearance
        search_query2_start = st.date_input('Start Date of First Appearance', value=st.session_state.start_date)
        search_query2_end = st.date_input('End Date of First Appearance', value=st.session_state.end_date)
    with col3:
        # Dropdown menu for selecting citizenship
        selected_citizenship = st.selectbox("Select Citizenship", citizenship_options)
        if pd.isnull(selected_citizenship):
            selected_citizenship = "No Information"
        if selected_citizenship == 'All':
            selected_citizenship = data['Citizenship']
    # Convert start and end dates to datetime objects
    start_date = datetime.combine(search_query2_start, datetime.min.time())
    end_date = datetime.combine(search_query2_end, datetime.min.time())

    # Filter data based on search queries
    filtered_data = data[
        data['Name'].str.contains(search_query1, case=False) &
        ((data['First Appearance'] >= start_date) & (data['First Appearance'] <= end_date)) &
        (data['Citizenship'].fillna("No Information") == selected_citizenship)

    ]

    # Format 'First Appearance' column as 'MM/YYYY'
    filtered_data['First Appearance'] = filtered_data['First Appearance'].dt.strftime('%m/%Y')

    # Display the filtered results in a table format
    table_data = filtered_data.head(10)[["Name","link","Align","Eye","Hair","Sex","Alive","First Appearance","Citizenship"]].copy()
    table_data['Name'] = table_data.apply(lambda row: f'<a href="{row["link"]}">{row["Name"]}</a>', axis=1)
    table_data = table_data.drop(columns=['link']).reset_index(drop=True)

    st.write(table_data.to_html(index=False,escape=False), unsafe_allow_html=True)

def project_page2():
    # # Load the pre-trained emotion detection model
    # model = load_model('model.h5')

    # # Define the emotion labels
    # emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

    # # Initialize the webcam
    # cap = cv2.VideoCapture(0)

    # while True:
    #     # Read a frame from the webcam
    #     ret, frame = cap.read()

    #     # Preprocess the frame for emotion detection
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     resized = cv2.resize(gray, (48, 48))
    #     normalized = resized / 255.0
    #     reshaped = np.reshape(normalized, (1, 48, 48, 1))

    #     # Perform emotion prediction
    #     result = model.predict(reshaped)
    #     emotion_index = np.argmax(result)
    #     emotion = emotion_labels[emotion_index]

    #     # Display the emotion prediction on the frame
    #     cv2.putText(frame, emotion, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    #     cv2.imshow('Emotion Detection', frame)

    #     # Exit the loop if 'q' is pressed
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    # # Release the webcam and close all windows
    # cap.release()
    # cv2.destroyAllWindows()
    st.write("Here")
    



def project_page():
    st.title("Project Selection")
    project_options = ["Select a project"] + ["The Superheroes Project", "Detect Emotions"]  # Add more project options as needed
    selected_project = st.selectbox("",project_options)

    if selected_project == "The Superheroes Project":
        project_page1()
    elif selected_project == "Detect Emotions":
        project_page2()

if __name__ == "__main__":
    main()


