# with open("weather_data.csv") as csv_data:
#     formatted_data = csv_data.readlines()
#     print(formatted_data)

# Output : ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# import csv
#
# with open("weather_data.csv") as csv_data_1:
#     data = csv.reader(csv_data_1)
#     tempo_list = []
#     for row in data:
#         if row[1] != 'temp':
#             tempo_list.append(int(row[1]))
# print(tempo_list)

# Output : [12, 14, 15, 14, 21, 22, 24]

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)  # Prints out the data in tabular form
# print(data["temp"])  # Prints out the data of that specific column
# print(type(data["temp"]))  # Every column is a series
# data_dict = data.to_dict()   #Makes tabular dataframe to dictionary
# data_list = data["temp"].to_list()   #Cant make whole data into list. This can make only a series (a single column) as a list.
# data_mean = data["temp"].mean()   #Gives the mean of a particular column
# print(data_mean)
# print(data.condition) #Pandas on reading the data, automatically sets column names as attributes of the whole data.
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])


#Creating a datframe from scratch

data_frame = {'Name': ['John', 'Emily', 'Mike', 'Jessica'],
              'Age': [25, 30, 35, 28],
              'City': ['New York', 'Los Angeles', 'Chicago', 'Boston']}
new_data = pandas.DataFrame(data_frame)
# print(new_data)

new_data.to_csv("CSV_New_data")