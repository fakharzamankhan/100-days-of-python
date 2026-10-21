"""Working with the Csv data """

# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             print(row[1])
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


#working with the pandas Library

import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
# print(data["temp"])
# it takes first row as the name of each column
# print(type(data["temp"]))
