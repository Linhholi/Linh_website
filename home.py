import streamlit as st
from streamlit_option_menu import option_menu
import project
import about

st.set_page_config(
    page_title = "Linh Nguyen",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center;'>LINH NGUYEN</h1>", unsafe_allow_html=True)

# Create navigation bar
selected_page = option_menu(
    menu_title = None,
    options = ["Home", "Projects", "About", "Contact"],
    icons=["house","search","info-circle","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Define content for each page
if selected_page == "Home":
    st.title("Home Page")
    st.write("""
    
    Welcome to Linh Nguyen website!
    
    There are 4 pages in this website including: Home page, Projects, About, and Contact.
    
    * Home page: instructs you to all the content in this website
    * Project: showcases some of the projects I am working on
    * About: describes about me
    * Contact: lists my contacts
    
    Take your time and travel the website with me!
    
    """)

elif selected_page == "Projects":
    project.project_page()

elif selected_page == "About":
    about.about_page()

elif selected_page == "Contact":
    st.title("Contact Me")
    st.markdown(""" 
    You can reach me at leslie.th.nguyen@gmail.com

    Linkedin: https://www.linkedin.com/in/nguyenthihoailinh/
    
    Github: https://github.com/Linhholi""")
