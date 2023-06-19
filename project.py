import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
from PIL import Image
import io
import os
import torch
import torchvision.transforms as transforms
import wget
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

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

    def load_model():
        model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
        model.eval()
        return model

    def load_labels():
        labels_path = 'https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt'
        labels_file = os.path.basename(labels_path)
        if not os.path.exists(labels_file):
            wget.download(labels_path)
        with open(labels_file, "r") as f:
            categories = [s.strip() for s in f.readlines()]
            return categories
        
    def predict(model, categories, image):
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = model(input_batch)

        probabilities = torch.nn.functional.softmax(output[0], dim=0)

        top5_prob, top5_catid = torch.topk(probabilities, 5)
        for i in range(top5_prob.size(0)):
            st.write(categories[top5_catid[i]], top5_prob[i].item())

    st.markdown(""" 
    #### The predictions based on pre-trained model resnet18 by Pytorch with classes getting from: 
    https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
    
    """)
    uploaded_file = st.file_uploader(label='Upload an image')
   
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        image = Image.open(io.BytesIO(image_data))
        model = load_model()
        categories = load_labels()
        result = st.button('Run prediction on the image')
        if result:
            st.write('Results:')
            predict(model, categories, image)


def project_page():
    st.title("Project Selection")
    project_options = ["Select a project"] + ["The Superheroes Project", "The Image Predictions"]  # Add more project options as needed
    selected_project = st.selectbox("",project_options)

    if selected_project == "The Superheroes Project":
        project_page1()
    elif selected_project == "The Image Predictions":
        project_page2()

if __name__ == "__main__":
    main()


