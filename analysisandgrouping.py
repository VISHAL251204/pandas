import pandas as pd

data={
    "name": ["Alice", "Bob", "Charlie","Vishal", "david", "Eve", "Frank", "Grace", "Heidi", "Ivan"],
    "department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"],
    "gender": ["F", "M", "M", "M", "M", "F", "M", "F", "M", "M"],
    "age": [25, 30, 35, 28, 32, 27, 40, 29, 31, 26],
    "salary": [50000, 60000, 70000, 55000, 62000, 58000, 75000, 52000, 68000, 61000],
    "years_experience": [2, 5, 10, 3, 6, 4, 12, 3, 8, 2],
    "joined date": ["2020-01-15", "2018-03-22", "2015-07-30", "2019-11-05", "2017-06-12", 
                    "2021-02-20", "2014-09-10", "2020-05-18", "2016-12-01", "2021-08-25"],
    "performance_rating": [4.5, 4.0, 4.8, 4.2, 4.6, 4.1, 4.9, 4.3, 4.7, 4.4]    
}
dataframe = pd.DataFrame(data)
#print(dataframe)

#groupby
avg_salary = dataframe.groupby("department")["salary"].mean()
count_employees = dataframe.groupby("department")["name"].count()
sum_salary = dataframe.groupby("department")["salary"].sum()

#print(count_employees)
#print(avg_salary)
#print(sum_salary)

multiple_aggregations = dataframe.groupby("department").agg({"salary": ["mean", "sum", "count"]})
#print(multiple_aggregations)


#merging and joining
incentive ={
    "name": ["Alice", "Bob", "Charlie","Vishal", "david", "Eve", "Frank", "Grace", "Heidi", "Ivan"],
    "incentive": [5000, 6000, 7000, 5500, 6200, 5800, 7500, 5200, 6800, 6100]

}
incentive_df = pd.DataFrame(incentive)
#print(incentive_df)

merged_df = pd.merge(dataframe, incentive_df, on="name")
#print(merged_df)

#concatination

concatinated_df = pd.concat([dataframe, incentive_df])
#print(concatinated_df)

#changing date format
dataframe["joindate"]=pd.to_datetime(dataframe["joined date"] )
dataframe["year"]=dataframe["joindate"].dt.year
dataframe["month"]=dataframe["joindate"].dt.month

#correlation analysis
correlation_matrix = dataframe[["age", "salary", "years_experience", "performance_rating"]].corr()
print(correlation_matrix)
