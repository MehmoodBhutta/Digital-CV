from pathlib import Path

import streamlit as st  
from PIL import Image

# --- path settings--

current_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = current_dir / 'styles' / 'main.css'
resume_file = current_dir / 'assets' / 'Mehmood-Jamal-Bhutta-DS (1).pdf'
pfp = current_dir / 'assets' / 'profile-pic.png'


# Settings

PAGE_TITLE = 'Digital CV | Mehmood Bhutta'
PAGE_ICON = ':wave:'
NAME = "Mehmood Jamal Bhutta"
Description = "Dedicated and results-driven data scientist with a strong background in statistical analysis, machine learning, and data visualization. Proven ability to extract meaningful insights from complex datasets and translate them into actionable business strategies. Proficient in programming languages such as Python and R, with experience in implementing predictive models and deploying data-driven solutions. Adept at collaborating with cross-functional teams to solve real-world problems and passionate about leveraging data to drive informed decision-making"
Email = 'mehmood.bhutta55@gmail.com'
SM = {
    'LinkedIN': 'www.linkedin.com/in/mehmood-jb',
    'GitHub': 'https://github.com/MehmoodBhutta',
}

Projects = {
'🏆 Data Sciences : (Cyber Security Attacks) EDA/ ML',
'🏆 Data Sciences : Cardiovascular Disease Dataset',

} 

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# load css pdf & pff
with open(css_file) as f:
    st.markdown(('<style>{}</style>'.format(f.read())), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
pfp = Image.open(pfp)


# hero sec

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(pfp, width=200)

with col2:
    st.title(NAME)
    st.write(Description)
    st.download_button(
        label= '📄 Download Resume',
        data= PDFbyte,
        file_name= resume_file.name,
        mime='application/octet-stream',

    )
    st.write("📫", Email)

# Social links
st.write('#')
cols = st.columns(len(SM))
for index, (platform, link ) in enumerate(SM.items()):
    cols[index].write(f"[{platform}]({link})")


# Exp & quilifactions
st.write('#')
st.subheader('Experience & Qulification')
st.write ( """
    - ✅ Applied advanced data science techniques, leveraging machine learning algorithms to derive meaningful insights and solutions
    - ✅ Proficient in data preprocessing, feature engineering, and model evaluation to enhance predictive model performance.
    - ✅ Demonstrated expertise in utilizing popular machine learning libraries such as scikit-learn, TensorFlow, and PyTorch.
    - ✅ Developed and deployed machine learning models for real-world applications, showcasing a practical understanding of the end-to-end data science workflow.
    - ✅ Executed exploratory data analysis (EDA) to uncover patterns, trends, and outliers,facilitating informed decision-making processes.
"""
          )

# Skills

st.write('#')
st.subheader('Hard Skills')
st.write(
    '''
    - 🧑🏻‍💻 Programming : Python (Scikit-learn, Pandas)
    - 📊 Data Visulization: MS Excel, Plotly
    - 📚 Modeling: Logistic Regression, Liner Regression, Decition Trees, Random Forest 
    - 🗄️ Databases: MySQL
'''
)      

# Work History 
st.write('#')
st.subheader('Work History')
st.write('---')

# job

st.write ('Data Scientist at Knowledge Streams 09.2023 - 12.2023')
st.write ('Python Django 06.2023 – 09.2023')

