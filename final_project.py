import numpy as np
import matplotlib.pyplot as plt
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

    

    # ~~~SECTION 1.1: Reading the CSV file~~~ #
    df = pd.read_csv(dataset) # Reads the .csv file
    #print(df) # For debugging

    # The following variables below are used for encoding non-numerical values to fit into the covariance matrix
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

    # Mapping the codes to their own dictionaries
    encodeAge = {}
    for i in range(len(ageList)):
        encodeAge.update({ageList[i]:i})
    #print(encodeAge) # For debugging

    encodeProduct = {}
    for i in range(len(productList)):
        encodeProduct.update({productList[i]:i})
    #print(encodeProduct) # For debugging

    encodeCountry = {}
    for i in range(len(countryList)):
        encodeCountry.update({countryList[i]:i})
    #print(encodeCountry) # For debugging

    encodeResidence = {}
    for i in range(len(residenceList)):
        encodeResidence.update({residenceList[i]:i})
    #print(encodeResidence) # For debugging

    encodeSex = {}
    for i in range(len(sexList)):
        encodeSex.update({sexList[i]:i})
    #print(encodeSex) # For debugging

    disaggDim = df["DisaggregatingDimension1"].tolist()
    disaggDim = list(set(disaggDim))
    encodeDisaggDim = {}
    for i in range(len(disaggDim)):
        encodeDisaggDim.update({disaggDim[i]:i})
    #print(encodeDisaggDim) # For debugging


    # ~~~SECTION 1.2: Preparing/Cleaning the data (i.e., check for NaNs and duplicates, incorrect labels, etc.)~~~ #
    tempDF = df # This temporary dataframe will copy the dataframe. Its purpose is to perform EDA.
    #print(tempDF) # For debugging

    tempDF.drop_duplicates() # Drops any duplicates from the dataset
    tempDF = tempDF.drop(columns=['Id','IndicatorCode','TimeDimension','Comments','SpatialDimension', 'TimeDim','TimeDimensionBegin','TimeDimensionEnd','Value','Date','DisaggregatingDimension2','DisaggregatingDimension2ValueCode']) # Drop the columns that have constant values or aren't that meaningful.
    #print(tempDF.columns) # For debugging

    emptyCol = tempDF.columns[tempDF.isnull().all()] # Checks if the entire column is empty
    tempDF = tempDF.drop(columns=emptyCol)  # Drops all the columns that are completely empty
    #print(tempDF.columns) # For debugging
    #print(tempDF) # For debugging

    # Encoding non-numerical values (USE AS TEMPLATE FOR ENCODING: newDF['Class']= newDF['Class'].map(class_Labels))
    tempDF["DisaggregatingDimension1"] = tempDF["DisaggregatingDimension1"].map(encodeDisaggDim) # Encoding the disaggregate dimensions
    tempDF["SpatialDimensionValueCode"] = tempDF["SpatialDimensionValueCode"].map(encodeCountry) # Encoding the countries

    multi_Dictionary = {**encodeProduct, **encodeResidence, **encodeAge, **encodeSex}
    tempDF["DisaggregatingDimension1ValueCode"] = tempDF["DisaggregatingDimension1ValueCode"].map(multi_Dictionary)
    #print(tempDF) # For debugging
    
    finalDF = tempDF # Sets the new dataframe to the cleaned dataframe from the temporary dataframe.
    #print(finalDF) # For debugging



    # ~~~SECTION 1.3: Identifying the target variable and features~~~ #
    corr_Matrix= finalDF.corr()
    print('\nCorrelation Matrix:\n', corr_Matrix, '\n\n')
    #print('\n',newDF)      # For debugging
    plt.imshow(corr_Matrix, cmap=None, norm=None)
    plt.title('Correlation Matrix')
    plt.show()
    


    # ~~~FINAL SECTION: Final dataframe for EDA Update Presentation on April 18, 2025~~~ #
    #print(finalDF)
    features = []
    for feature in finalDF.columns:
        # The top strongest features based off the correlation matrix analysis
        if feature == 'DisaggregatingDimension1' or feature == 'DisaggregatingDimension1ValueCode' or 'TimeDimensionValue' or 'SpatialDimensionValueCode':
            features.append(feature)

        # Otherwise, ignore the other features
        else:
            continue




    # ----- PHASE 2: MACHINE LEARNING MODEL TRAINING (CPU) ----- #

    # 'Is it just me or does President Callahan exude insane aura and hype whenever he pulls up to an event?' -Winstar


    # ----- PHASE 3: MACHINE LEARNING MODEL TRAINING (GPU) ----- #

    # 'AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!' -Winstar


    # ----- PHASE 4: LINEAR REGRESSION ANALYSIS ----- #

    # 'I understand it now. Lock. In.' -Winstar


if __name__ == '__main__':
    SystemExit(main())