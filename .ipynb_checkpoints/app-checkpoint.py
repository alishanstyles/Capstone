import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler





st.set_page_config(page_title = "Obesity Risk Dataset Explorer", page_icon = ":chart:")


page = st.sidebar.selectbox("Select a Page", ["🏠Home", "🔢Data Overview", "💹EDA","⚙️Modeling" ])

df = pd.read_csv('archive/ObesityDataSet.csv')

if page == "🏠Home":
    st.title("🩺Obesity Risk Dataset Explorer App")
    st.subheader("Welcome to my Obesity Risk dataset explorer app")
    st.write(" This app is designed to allow the user to explore the dfferent factors that can contribute to obesity and what puts people at risk of being obese.")
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Obesity-waist_circumference.svg/800px-Obesity-waist_circumference.svg.png')
    st.write("Use the sidebar to navigate between the sections!")

if page == "🔢Data Overview":
    st.title("🔢Data Overview")
    st.subheader("About the Data")
    st.write ("The data consist of the estimation of obesity levels in people from the countries of Mexico, Peru and Colombia, with ages between 14 and 61 and diverse eating habits and physical condition , data was collected using a web platform with a survey where anonymous users answered each question, then the information was processed obtaining 17 attributes to obesity and 2,111 records. This dataset was provided by Kaggle")
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAcR0diFMCx2EOt7Bm7t5DB5t3Mw76gIVfGg&usqp=CAU')
    st.link_button("Click here to view more!","https://www.kaggle.com/datasets/aravindpcoder/obesity-or-cvd-risk-classifyregressorcluster/data?select=ObesityDataSet.csv" )

    st.subheader("Quick View at the Data")
    if st.checkbox("DataFrame"):
        st.dataframe(df)
    
    if st.checkbox("Shape"):
        st.write(f"There are {df.shape[0]} rows and {df.shape[1]} columns.")
    
if page == "💹EDA":
    st.title("💹EDA")

    num_cols = df.select_dtypes(include = 'number').columns.tolist()
    obj_cols = df.select_dtypes(include ='object').columns.tolist()

    eda_type = st.multiselect("What type of Exploratory Data would you like to view?", ["Histograms","Box Plots", "Scatterplots", "Count Plots"])

    if "Histograms" in eda_type: 
        st.subheader("Histograms - Visualizing Numerical Distributions")
        h_selected_col = st.selectbox("Select a numerical column for your histogram:", num_cols, index = None)

        if h_selected_col:
            st.plotly_chart(px.histogram(df, x = h_selected_col, title = f"Distribution of {h_selected_col}", color = 'NObeyesdad', barmode = 'overlay'))

    if "Box Plots" in eda_type:
        st.subheader("Box Plots - Visualizing Numerical Distributions")
        b_selected_col = st.selectbox("Select a numerical column for your box plot:", num_cols, index = None)

        if b_selected_col:
            st.plotly_chart(px.box(df, x = b_selected_col, title = f"Distribution of {b_selected_col}", y = 'NObeyesdad', color ='NObeyesdad',))

    if "Scatterplots" in eda_type:
        st.subheader("Scatterplots- Visualizing Relationsips")
        selected_col_x = st.selectbox("Select x-axis variable:", num_cols, index = None)
        selected_col_y = st.selectbox("Select y-axis variable:", num_cols, index = None)

        if selected_col_x and selected_col_y:
            chart_title = f"Relationship of {selected_col_x} vs. {selected_col_y}"
            st.plotly_chart(px.scatter(df, x = selected_col_x, y = selected_col_y, title = chart_title))

    if "Count Plots" in eda_type:
        st.subheader("Count Plots - Visualizing Categorical Distributions")
        selected_col = st.selectbox ("Select a categorical variable:", obj_cols, index = None)
        if selected_col:
            chart_title = f"Distribution of {selected_col.title()}"
            st.plotly_chart(px.histogram(df, x = selected_col, title = chart_title, color = 'NObeyesdad'))

if page == "⚙️Modeling":
    st.title("⚙️Modeling")
    st.markdown ("View how well the **machine learning model** made predictions on Obesity Risk Dataset on this page!")

    features = ['Gender_0', 'Gender_1', 'family_history_with_overweight_no',
       'family_history_with_overweight_yes', 'FAVC_no', 'FAVC_yes',
       'CAEC_Always', 'CAEC_Frequently', 'CAEC_Sometimes', 'CAEC_no',
       'SMOKE_no', 'SMOKE_yes', 'SCC_no', 'SCC_yes', 'CALC_Always',
       'CALC_Frequently', 'CALC_Sometimes', 'CALC_no', 'MTRANS_Automobile',
       'MTRANS_Bike', 'MTRANS_Motorbike', 'MTRANS_Public_Transportation',
       'MTRANS_Walking']
    X = df[features]
    y = df['NObeyesdad']
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)

    model_option = st.selectbox("Select KNN As Model", ['KNN'], index = None)
    if model_option:
        if model_option == 'KNN':
            k_value = st.slider("Select the number of neighbors (k)", 1, 29, 5, 2)
            model = KNeighborsClassifier(n_neighbors = k_value)

        if st.button("Let's see the performance"):
            model.fit(X_train, y_train)
            sc = StandardScaler()
            X_train_sc = sc.fit_transform(X_train)
            X_test_sc = sc.transform(X_test)
            knn = KNeighborsClassifier()
            knn.fit(X_train_sc, y_train)

            st.subheader(f"{model} Evaluation")
            st.text(f"Training Accuracy: {round(model.score(X_train, y_train)*100,2)}%")
            st.text(f"Testing Accuracy: {round(model.score(X_test, y_test)*100,2)}%")

            st.subheader("Confusion Matrix:")
            fig ,ax = plt.subplots(1,1,figsize=(15,15))
            ConfusionMatrixDisplay.from_estimator(model, X_test_sc, y_test,  ax=ax)
            CM_fig = plt.gcf()
            st.pyplot(CM_fig)




        



