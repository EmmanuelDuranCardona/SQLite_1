import sqlite3

connection = sqlite3.connect('Project.sqlite')
cursor = connection.cursor()

# def print_all_data():
#     cursor.execute("SELECT * FROM [MY2022 Fuel Consumption Ratings]")
#     print(cursor.fetchall())
#
# print_all_data()
#
#
# def print_specific_data():
#     cursor.execute("SELECT * FROM [MY2022 Fuel Consumption Ratings]")
#     data = cursor.fetchall()
#     for d in data:
#         print(d)
#
# print_specific_data()


# def print_column_names():
#     cursor.execute("SELECT * FROM [MY2022 Fuel Consumption Ratings]")
#     column_names = cursor.description
#     for row in column_names:
#         print(row[0])
#
# print_column_names()


import pandas, matplotlib.pyplot as plt

sql = """SELECT AVG([FuelConsumption(Comb(mpg))]) AS Combined_MPG, 
                VehicleClass, 
                Make,
                Cylinders,
                AVG([CO2Emissions(g/km)]) AS CO2Emissions,
                AVG(Cylinders) AS AVG_Cylinders
                FROM [MY2022 Fuel Consumption Ratings] 
                GROUP BY Make having ModelYear == 2022
                ORDER BY COUNT(*) DESC
                LIMIT 6"""

data = pandas.read_sql(sql, connection)
plt.style.use('seaborn')
fig, axes = plt.subplots(ncols=2)

#################################################
sorted_data1 = data.sort_values("Combined_MPG")

'''Bar Plot'''
axes[0].bar(sorted_data1.Make, sorted_data1.Combined_MPG)

# '''Line Plot'''
# axes[0].plot(data.Make, data.AVG_Cylinders)
# axes[0].scatter(data.Make, data.AVG_Cylinders)

axes[0].set_ylabel('Miles Per Gallon', fontsize=14)
axes[0].set_title("Fuel Economy", fontsize=20)

#################################################

#################################################
sorted_data2 = data.sort_values("CO2Emissions", ascending=False)

'''Bar Plot'''
axes[1].bar(sorted_data2.Make, sorted_data2.CO2Emissions)

axes[1].set_ylabel('CO2  (g / km)', fontsize=14)
axes[1].set_title('Carbon Dioxide (CO2) Emissions', fontsize=20)
#################################################


axes[0].tick_params(labelsize=14)
axes[1].tick_params(labelsize=14)


fig.suptitle("Fuel Consumption and CO2 Emissions by Make \n (Canada, Vehicles of 2022)", fontsize=25)

plt.show()