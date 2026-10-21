import pandas
data=pandas.read_csv("weather_data.csv")
print(data)

# data as a Dictionary
data_dict= data.to_dict()
print(data)

#Data As a list
temp_list=data["temp"].to_list()
print(temp_list)

"""find average of all the temperatures"""
average= sum(temp_list) /len(temp_list)
print(f"The average is {average}")

"""Another Method to find the average temperatures """
# avg=0
# for temp in temp_list:
#     total=len(temp_list)
#     add=sum(temp_list)
#     avg=int(add/total)
# print(avg)

"""Another Method"""
# print(data["temp"].mean())

"""Get the maximum temperatures"""
# print(data["temp"].max ())

"""Get the Data in Columns"""
"""Pandas takes each of the columns as the attributes and then call with the object"""
# print(data.condition)

"""Treating the dataframe as the dictionary and each column acts as the key"""
# print(data["condition"])

"""Get the data in the row"""
# print(data[data.day == "Monday"])

"""Which row has the maximum temperature"""
"""In this case we will get the row instead of the single column"""
# print(data[data.temp==data.temp.max()])

monday =data[data.day == "Monday"]
print(monday.condition)

"""Print the mondays temperature in fh"""
# monday_temp = int(monday.temp)
# monday_temp_f=monday_temp * 9/5 + 32
# print(monday_temp_f)

"""Create the Dataframe from the Dictionary"""

data_dict={
    "Students":["Ali","shan","Nimra"],
    "scores":[76,56,65]
}

data=pandas.DataFrame(data_dict)
print(data)
"""Convert the Dataframe into the CSV file"""
# data.to_csv("new_data.csv")







