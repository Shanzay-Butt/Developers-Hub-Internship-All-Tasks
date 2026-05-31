# We can use HTML , CSS ,JS but to do it fastly we can use streamlit

# import streamlit as st

# Streamlit is used to create the web interface.
# st is a short name so we can write st.title(), st.button() etc.

# import pandas as pd

# Pandas is used to handle data tables.
# Machine learning models expect data in DataFrame format.

# import joblib

# Joblib is used to load saved machine learning models and objects.


import streamlit as st
import pandas as pd
import joblib

model=joblib.load(r"E:\ML\projects_ML\Heart_Stroke_Risk\LG_heart.pkl")  # give exact path of the pickel
scaler=joblib.load(r"E:\ML\projects_ML\Heart_Stroke_Risk\scaler.pkl")
expected_columns=joblib.load(r"E:\ML\projects_ML\Heart_Stroke_Risk\columns.pkl")

st.title("Heart Stroke prediction !!! ")  # title
st.markdown("Provide the following details !!!")  # showing instructions

age=st.slider("Age",18,100,40)    # start,stop,bydefault 40 set  ( creates a  slider input)
sex=st.selectbox("Sex",['M','F'])   # creates a dropdown menu 
chest_pain=st.selectbox("Chest Pain Type",["ATA","NAP","TA","ASY"])
resting_bp=st.number_input("Resting Blood Pressure",80,200,120)   # continuous value so that using number_input that allows to enter numeric bp value
cholesterol=st.number_input("Cholesterol(mg/dL)",100,600,200)
fasting_bs=st.select_slider("Fasting Blood Sugar > 120 mg/dL",[0,1])
resting_ecg=st.selectbox("Resting ECG",["Normal","ST","LVH"])
max_hr=st.slider("Max Heart Rate",60,220,150)
exercise_angina=st.selectbox("Exercise-Induced Angina",["Y","N"])
oldpeak= st.slider("OldPeak(ST Depression)",0.0,6.0,1.0)


if st.button("Predict"): # Prediction will only run when user clicks the button.
    # collecting all inputs tha user will enter
    raw_input={
        'Age':age,
        'RestingBP':resting_bp,
        'Cholesterol':cholesterol,
        'FastingBS':fasting_bs,
        'MaxHR':max_hr,
        'Oldpeak':oldpeak,
        'Sex_ '+sex:1,  # this is manual one hot encoding if user select M it will put 1 there  'Sex_' + 'M' then python will combine it Sex_M and it will become 'Sex_M:'1
        'ChestPainType_ '+chest_pain:1,   # 'ChestPainType_' + 'ATA',ChestPainType_ATA  ,'ChestPainType_ATA':1   yai 1 hoyega baqi sab 0 put hojyengeniche for loop krega  bcz in one hot encoding selcted=1 and not selected =0

        'RestingECG_ '+resting_ecg:1,
        'ExerciseAngina_ '+exercise_angina:1
        }
    input_df=pd.DataFrame([raw_input])  #Machine learning models expect table format (DataFrame)
        #During training there were many columns.But user input might only contain some of them.So missing columns are filled with 
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0

    input_df=input_df[expected_columns]

    scaled_input=scaler.transform(input_df)
    prediction=model.predict(scaled_input)[0]   # [0] extracts the first value from the prediction array.

    if prediction==1:
        st.error("High Risk of Heart Disease!!!")

    else:
        st.success("Low risk of heart Disease!!!")