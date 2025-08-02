import numpy as np

sample_rainfall = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])

#for the total amount of rainfall in a week
total_rainfall = sample_rainfall.sum()
roundValue = round(total_rainfall, 2)

#for the average number of rainfall in a week
Avg_rainfall = np.mean(sample_rainfall)
roundValuerain = round(Avg_rainfall, 2)

#for when there was  no rain
no_rain = np.where(sample_rainfall <= 0)    

#Rain more than the 5mm
Index = np.where(sample_rainfall > 5)

#Value for the total rainfall
print("The total number of rainfall in the week is:", roundValue)

#Value for the Average rainfall
print("The average nnumber of rainfall in a week is:", roundValuerain)

#In the week where there is no rain and is equal to 0
print("The week where there is no rain where (Monday=0 and sunday=7):", no_rain[0]) 

#The index value where the rainfall is more the five
print("The index in which the rainfall is more than 5mm (monday=0 and suday=7):", Index[0])