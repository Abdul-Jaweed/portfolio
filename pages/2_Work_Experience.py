import streamlit as st



def space():
    st.markdown("<br>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Experiance",
    page_icon="👋",
)

st.write("# Work Experience")
space()
space()
space()


st.markdown(
    """
    
    #### Innomatics Research Lab. Data Science Intern (02/2023 – present)


    - ##### Part 1 - Python Programming with Projects.
    - ##### Part 2 - Data Analysis with Case Studies
    - ##### Part 3 - Machine Learning / NLP / CV with Case Studies
    - ##### Part 4 - MLOps with End to End Projects.
    
    
    
    
    
    #### iNeuron, Project Intern (11/2022 – present)
    
    ### Project Name : Deep Autenticator
    ##### Problem statement : Is to design and Authentication system that can be installed places as where high securities and system should support faced based Authentications
    ##### Tech: Python, MongoDB, Fast-ApI, Docker, Azure Container Registry, Azure App Services, Terraform.
    - Designed API's embeddings-based remote application for a client to provide permission-based access to restricted areas.
    - Selected MTCNN for face detection and FaceNet for Embedding generation along with MongoDB as a feature store.
    - Used Fast-API as an interface for the model and checked similarly using Cosine Similarity.
    - Implemented CI/CD in monolithic architecture using GitHub actions and deployed the web application using Azure App services.
    
    ### Project Name : Sensor Fault Detection
    ###### Problem statement : The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air. 
    ##### Tech: MLFlow, Python, Mongodb, Machine Learning, CICD, Github Actions, Docker, FastAPI
    - Fetch Streaming data through Kafka and store it to mongodb.
    - Trained a Machine Learning Classification Model to predict accurate prediction.
    - Deployed a web app on AWS EC2 with cloud watch monitoring
    - Designed a continuous training pipeline using GitHub actions on remote machines and utilized an S3 bucket as a model registry.
    - Deployed dockerized application on GPU instance using GitHub actions for faster inferencing.
    
    
    
    #### The Sparks Foundation. Data Science and Business Analytics Intern (12/2022 – 01/2023)
    
    ### Project Name : Stock Market Prediction
    ##### Objective of the Task is to Create a Hybrid Model for Stock Price/ Performance Prediction Using Numerical Analysis of Historical Stock Prices and Sentimental Analysis of News Headlines.
    
    ### Project Name : IPL Dashboard using Tableau.
    ##### Objective of the Task is to Perform EDA on 'Indian Premier League' Dataset. As a Sports Analysts, Find out the Most Successful Teams, Players and Factors Contributing Win or Loss of a Team and showing a dashboard using Tableau.
    
"""
)