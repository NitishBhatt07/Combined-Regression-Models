import streamlit as st
import pandas as pd
import pickle

## sidebar
st.sidebar.title("Pricer Predictor")
list_product = ['Car Price Predict','Laptop Price Predict']

selected_model = st.sidebar.selectbox("Select Model: ",list_product)

if selected_model == 'Car Price Predict':   

    st.title("Car Price Predict")

    ## loading csv file  
    car = pd.read_csv('car cleaned data.csv')

    rfmodel_car = pickle.load(open('RFRegressor_Car_model.pkl','rb'))

    ## getting all the companies name
    companies = sorted(car['company'].unique())
    ## drop down for all the company names
    company_name = st.selectbox('Select the Company',companies)

    ## drop down for model name
    models_ac_company = []
    ## getting all model names
    all_model_names = sorted(car['name'].unique())
    ## getting all the model names a/c to company
    for model in all_model_names:
        if company_name in model:
            models_ac_company.append(model)
    model_name = st.selectbox("Select Model",models_ac_company)


    ## select years
    years = sorted(car['year'].unique(),reverse=True)
    ## disply drop down
    year_of_buy = st.selectbox("Select year of Buy",years)

    ## select km driven
    kms = st.text_input("Total run time ?")
    #kms = st.number_input(label="How much kilometer run ?")

    ## select years
    fuel_types = sorted(car['fuel_type'].unique())
    ## disply drop down
    fuel = st.selectbox("Select Fuel Type",fuel_types)


    # botton predict
    if st.button("Predict Price"):
        predicted_price = rfmodel_car.predict(pd.DataFrame([[model_name,company_name,year_of_buy,kms,fuel]],
                            columns=['name','company','year','kms_driven','fuel_type']))
        st.write("Price of Car : ",str(predicted_price[0]))

elif selected_model == 'Laptop Price Predict':
    st.title("Laptop Price Predict")

    ## loading csv file  
    laptop = pd.read_csv('laptop cleaned data.csv')

    rfmodel_laptop = pickle.load(open('RFRegressor_Laptop_model.pkl','rb'))

    ## getting all the companies name
    companies = sorted(laptop['Company'].unique())
    company_name = st.selectbox('Select the Company',companies)

    ## getting all the type name
    typename_list = sorted(laptop['TypeName'].unique())
    type_name = st.selectbox('Select the Type ',typename_list)

    ## getting all the inches
    inches_list = sorted(laptop['Inches'].unique())
    inches = st.selectbox('Select the Inches',inches_list)

    ## getting all the os
    os_list = sorted(laptop['OpSys'].unique())
    os = st.selectbox('Select the Operating System',os_list)

    ## getting all the Resolution
    Resolution_list = sorted(laptop['Resolution'].unique())
    Resolution = st.selectbox('Select the Resolution',Resolution_list)

    ## getting all the Screen
    Screen_list = sorted(laptop['Screen'].unique())
    Screen = st.selectbox('Select the Screen Type',Screen_list)

    ## getting all the Cpu Company
    Cpu_Company_list = sorted(laptop['Cpu Company'].unique())
    Cpu_Company = st.selectbox('Select the CPU Company',Cpu_Company_list)

    ## getting all the Cpu Core
    Cpu_Core_list = sorted(laptop['Cpu Core'].unique())
    Cpu_Core = st.selectbox('Select the CPU Core',Cpu_Core_list)

    ## getting all the Memory Size
    Memory_Size_list = sorted(laptop['Memory Size'].unique())
    Memory_Size = st.selectbox('Select the Memory Size',Memory_Size_list)

    ## getting all the Memory Type
    Memory_Type_list = sorted(laptop['Memory Type'].unique())
    Memory_Type = st.selectbox('Select the Memory Type',Memory_Type_list)

    ## getting all the Gpu Company
    Gpu_Company_list = sorted(laptop['Gpu Company'].unique())
    Gpu_Company = st.selectbox('Select the GPU Company',Gpu_Company_list)

    ## getting all the Weight Range
    Weight_Range_list = sorted(laptop['Weight Range'].unique())
    Weight_Range = st.selectbox('Select the Weight Range',Weight_Range_list)

     ## getting all the Ram Size
    Ram_Size_list = sorted(laptop['Ram Size'].unique())
    Ram_Size = st.selectbox('Select the Ram Size',Ram_Size_list)

    ## getting all the Weight Range
    GHZ_Size_list = sorted(laptop['GHZ Size'].unique())
    GHZ_Size = st.selectbox('Select the Ghz',GHZ_Size_list)

    if st.button("Predict Price"):

        predicted_price = rfmodel_laptop.predict(pd.DataFrame([[company_name,type_name,inches,os,Resolution,
        Screen,Cpu_Company,Cpu_Core,Memory_Size,Memory_Type,Gpu_Company,Weight_Range,Ram_Size,GHZ_Size]],
                          columns=['Company', 'TypeName', 'Inches', 'OpSys', 'Resolution', 'Screen',
       'Cpu Company', 'Cpu Core', 'Memory Size', 'Memory Type', 'Gpu Company',
       'Weight Range', 'Ram Size', 'GHZ Size']))

        st.write("Price of Car : ",str(predicted_price[0]))



    

    
