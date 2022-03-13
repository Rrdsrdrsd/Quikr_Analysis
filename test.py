import pickle
import numpy as np

pipe = pickle.load(open('LinearRegressionModel.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))



name = 'Hyundai Santro Xing'
company = 'Hyundai'

year = 2007

kmsdriven = 10000

fueltype = 'Petrol'


 
query = np.array([name,company,year,kmsdriven,fueltype])

query = query.reshape(1,5)
print("OM IS NIGGA BITCH========================================")
print(query)
print(pipe.predict(query))
    