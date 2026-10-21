import pandas
import pandas as pd
data = pd.read_csv("004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# data.head()
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())
grey_squirrels_count=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)
data_dict={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df=pd.DataFrame(data_dict)
df.to_csv("Squirrels_count.csv")
