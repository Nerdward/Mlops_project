import json
import requests

house = {"Id":1461,
"MSSubClass":20,
"MSZoning":"RH",
"LotFrontage":80.0,
"LotArea":11622,
"Street":"Pave",
"Alley":" ",
"LotShape":"Reg",
"LandContour":"Lvl",
"Utilities":"AllPub",
"LotConfig":"Inside",
"LandSlope":"Gtl",
"Neighborhood":"NAmes",
"Condition1":"Feedr",
"Condition2":"Norm",
"BldgType":"1Fam",
"HouseStyle":"1Story",
"OverallQual":5,
"OverallCond":6,
"YearBuilt":1961,
"YearRemodAdd":1961,
"RoofStyle":"Gable",
"RoofMatl":"CompShg",
"Exterior1st":"VinylSd","Exterior2nd":"VinylSd","MasVnrType":"None","MasVnrArea":0.0,"ExterQual":"TA","ExterCond":"TA","Foundation":"CBlock","BsmtQual":"TA","BsmtCond":"TA","BsmtExposure":"No","BsmtFinType1":"Rec","BsmtFinSF1":468,"BsmtFinType2":"LwQ","BsmtFinSF2":144,"BsmtUnfSF":270,"TotalBsmtSF":882,"Heating":"GasA","HeatingQC":"TA","CentralAir":"Y","Electrical":"SBrkr","1stFlrSF":896,"2ndFlrSF":0,"LowQualFinSF":0,"GrLivArea":896,"BsmtFullBath":0,"BsmtHalfBath":0,"FullBath":1,"HalfBath":0,"BedroomAbvGr":2,"KitchenAbvGr":1,"KitchenQual":"TA","TotRmsAbvGrd":5,"Functional":"Typ","Fireplaces":0,"FireplaceQu":" ","GarageType":"Attchd","GarageYrBlt":1961.0,"GarageFinish":"Unf","GarageCars":1,"GarageArea":730,"GarageQual":"TA","GarageCond":"TA","PavedDrive":"Y","WoodDeckSF":140,"OpenPorchSF":0,"EnclosedPorch":0,"3SsnPorch":0,"ScreenPorch":120,"PoolArea":0,"PoolQC":" ","Fence":"MnPrv","MiscFeature":" ","MiscVal":0,"MoSold":6,"YrSold":2010,"SaleType":"WD","SaleCondition":"Normal"}

if __name__ == "__main__":

    host = "http://0.0.0.0:8000"
    url = f"{host}/predict"
    response = requests.post(url, json=house)
    result = response.json()

    print(result)