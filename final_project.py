import numpy as np
import matplotlib as plt
import pandas as pd
import seaborn as sb
import statsmodels as sts
import os

#GPU Kernel here


#def linearRegression_Model():

#def ML_classifier1():
#def ML_classifier2():
#def ML_classifier3():
#def ML_classifier4():
#def ML_classifier5():

def main():
    # ----- PHASE 1: EXPLORATORY DATA ANALYSIS ----- #

    # 'And so it begins... war...' -Winstar
    dataset = "ASSISTIVETECH_TOTALNEED.csv"
    
    # These following variables below are used for encoding non-numerical values to fit into the covariance matrix

    age_group = "AGEGROUP.csv"
    ageGroup = pd.read_csv(age_group)
    ageList = ageGroup["Code"].tolist()
    #print(ageList) # For debugging

    assistive_product = "ASSISTIVETECHPRODUCT.csv"
    assistiveProd = pd.read_csv(assistive_product)
    productList = assistiveProd["Code"].tolist()
    #print(productList) # For debugging

    country = "COUNTRY.csv"
    countryCSV = pd.read_csv(country)
    countryList = countryCSV["Code"].tolist()
    #print(countryList) # For debugging

    residence_area_type = "RESIDENCEAREATYPE.csv"
    residenceType = pd.read_csv(residence_area_type)
    residenceList = residenceType["Code"].tolist()
    #print(residenceList) # For debugging

    sexes = "SEX.csv"
    sexesCSV = pd.read_csv(sexes)
    sexList = sexesCSV["Code"].tolist()
    #print(sexList) # For debugging

    # ~~~SECTION 1.1: Reading the CSV file~~~ #
    df = pd.read_csv(dataset) # Reads the .csv file
    #print(df) # For debugging



    # ~~~SECTION 1.2: Preparing/Cleaning the data (i.e., check for NaNs and duplicates, incorrect labels, etc.)~~~ #
    tempDF = df # This temporary dataframe will copy the dataframe. Its purpose is to perform EDA.
    #print(tempDF) # For debugging

    tempDF.drop_duplicates() # Drops any duplicates from the dataset
    tempDF = tempDF.drop(columns=['Id','IndicatorCode','TimeDimension','Comments','SpatialDimension']) # Drop the columns that have constant values or aren't that meaningful.
    #print(tempDF.columns) # For debugging

    emptyCol = tempDF.columns[tempDF.isnull().all()] # Checks if the entire column is empty
    tempDF = tempDF.drop(columns=emptyCol)  # Drops all the columns that are completely empty
    #print(tempDF.columns) # For debugging
    #print(tempDF) # For debugging

    # Encoding non-numerical values



    newDF = tempDF # Sets the new dataframe to the cleaned dataframe from the temporary dataframe.
    #print(newDF) # For debugging



    # ~~~SECTION 1.3: Identifying the target variable and features~~~ #



    # ~~~FINAL SECTION: Final dataframe for EDA Update Presentation on April 18, 2025~~~ #
    




    # ----- PHASE 2: MACHINE LEARNING MODEL TRAINING (CPU) ----- #

    # 'Is it just me or does President Callahan exude insane aura and hype whenever he pulls up to an event?' -Winstar


    # ----- PHASE 3: MACHINE LEARNING MODEL TRAINING (GPU) ----- #

    # 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!' -Winstar


    # ----- PHASE 4: LINEAR REGRESSION ANALYSIS ----- #

    # 'I understand it now. Lock. In.' -Winstar


if __name__ == '__main__':
    SystemExit(main())