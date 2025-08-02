import numpy as np

Temperature_celius = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

Avg_temp = np.mean(Temperature_celius)

max_value = np.max(Temperature_celius)

min_value = np.min(Temperature_celius)

fahrenheit = Temperature_celius * 9/5 +32

Days = np.where(Temperature_celius > 20)

#for the average temperature
print("The avareage temperature is:", Avg_temp)

#List all the array present
print("Temperature given", Temperature_celius)

#for the max value
print("The maximun Temperature in given array is:", max_value)

#for the minimun value
print("The minimun temperature in teh array is:", min_value)

#for the fahrenheit
print("The converted temperatue are:", fahrenheit)

#printing the value for the temperature
print("The days where the temperature execeeds 20 (0=mon, 6=sun):", Days[0])
