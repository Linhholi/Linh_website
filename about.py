import streamlit as st
import pandas as pd


def about_page():
#     with open('style.css') as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.subheader("Personal statement")
    st.write("Data holds layers of meaning that can be used to drive business improvements, which is what makes the field so fascinating to me. This is what motivated me to choose data science as my major. The thrill of discovering innovative solutions and seeing the positive impact of my work is what drives me to pursue a career in this exciting industry.")
    col1, col2 = st.columns(2)
    col1.subheader("Education")
    # Define the table data
    table_edu = [
        ['<b>Master of Data Science</b><br>Swinburne University of Technology','<br>Distinction average 87.5% <br> Current GPA: 3.125 '],
        ['<b>Bachelor of Finance and Banking</b><br>Foreign Trade University','<br> GPA: 3.23']
    ]
     # Convert table_data to a DataFrame
    df_edu = pd.DataFrame(table_edu)
    # Convert the DataFrame to an HTML table
    table_edu_html = df_edu.to_html(index=False, header=False, escape=False)
    # Display the HTML table
    col1.write(table_edu_html, unsafe_allow_html=True)

    col2.subheader("Technical Skills")   
    table_skills = [
        ['<b>Programming</b>','Python'],
        ['<b>Databases</b>','MySQL, MongoDB, CSV'],
        ['<b>Web</b>','ERN stack: Express.JS, React.JS, Node.JS'],
        ['<b>Visualisation</b>','Tableau, Matplotlib'],
        ['<b>Clouds</b>','Microsoft Azure, Amazon Web Services AWS, Oracle Cloud OCI'],
        ['<b>Office</b>','Microsoft Office: Word, PowerPoint, Excel, Outlook, Visio']
    ]
    # Convert table_data to a DataFrame
    df_skills = pd.DataFrame(table_skills)
    # Convert the DataFrame to an HTML table
    table_skills_html = df_skills.to_html(index=False, header=False, escape=False)
    # Display the HTML table
    col2.write(table_skills_html, unsafe_allow_html=True)

    st.subheader("Employment")
    table_emp =[
        ['<b>Business Analyst/Premium Technology Inc./<em>2021-2022</em></b><br>* Work with internal teams: <br>- Collaborate with PM to timely all documents (business requirement analysis, business workflow, presentation, etc.)<br>- Support production team doing system testing to improve customers’ experiences<br>* Work with customers:<br>- Control timeline and communicate closely with customers including Business and Technical team at the banks to understand business requirements and working processes.<br>- Be the first solving point to any of customers’ issues with system<br>- Conduct end-user training, train-the-trainers training.'],
        ['<b>Auditor/LG Electronics Vietnam/Vinfast LCC/<em>2018-2021</em></b><br>*Mistakes/Frauds findings:<br>- Analyze data through projects with targeted objects are from both internal and external.<br>- Reduce risks by working with related departments to understand their process before concentration on finding mistakes/ risks <br>* Process improvement:<br>- Propose any recommendations for changing or enhancements through reports presentation<br>- Apply penalties if any to prevent any futures mistakes. Apply new process if required.'],
        ['<b>Accountant/Toyota Motor Vietnam/<em>2015-2017</em></b><br>* Cost accountant:<br>- Calculate car cost (both imported (CBU) and manufactured vehicles (CKD)) by collecting related expenses to build a completed car <br>- Leader of half-year and year-end stock-taking in both North and South branches <br>* AP accountant:<br>- Receive and check documents of all payments made by cash and some specific payments made by transfer through the banks of assigned departments and input data on Oracle system based on accounting standards <br>- Create VAT report to support AP manager monthly.']
    ]
    # Convert table_data to a DataFrame
    df_emp = pd.DataFrame(table_emp)
    # Convert the DataFrame to an HTML table
    table_emp_html = df_emp.to_html(index=False, header=False, escape=False)
    # Display the HTML table
    st.write(table_emp_html, unsafe_allow_html=True)

    st.subheader("Professional Development")
    st.write("Microsoft Azure Fundamentals (AZ 900)")
