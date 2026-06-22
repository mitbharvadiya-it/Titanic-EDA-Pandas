import pandas as pd
import numpy as np

# 1. Load Dataset
df=pd.read_csv("Titanic-Dataset.csv")

# 2. Dataset Overview
print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

print("\nDescription:")
print(df.describe())

# 3. Missing Values
print(df.isnull().sum())
missing_percent = (df.isnull().sum()/len(df))*100

print(missing_percent)

# 4.  Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean()) # Fill Age with Mean
df["Embarked"] = df["Embarked"].fillna(  #Fill Embarked with Mode
    df["Embarked"].mode()[0]
)
df["Cabin"] = df["Cabin"].fillna("Unknown") #Fill Cabin with Unknown
print(df.isnull().sum())  # Check Again

# 5. Duplicate Rows
print("Duplicate Rows:")

print(df.duplicated().sum())
df = df.drop_duplicates() # remove duplicate rows

# 6. Filtering
female = df[df["Sex"]=="female"]

print(female.head())

male = df[df["Sex"]=="male"]

print(male.head())
  # Passengers older than 50
old = df[df["Age"]>50]

print(old.head())
  # Female passengers who survived
female_survived = df[
    (df["Sex"]=="female")
    &
    (df["Survived"]==1)
]

print(female_survived.head())

# 7. Sorting
  # Oldest Passengers

print(

df.sort_values(
    "Age",
    ascending=False
).head(10)

)
   # Highest Fare
print(

df.sort_values(
    "Fare",
    ascending=False
).head(10)

)

# Value Counts
   # Male vs Female
print(

df["Sex"].value_counts()

)
   # Passenger Class Count
print(

df["Pclass"].value_counts()

)
   # Embarked Count
print(

df["Embarked"].value_counts()

)

# 8. GroupBy Operations

   # Average Age by Gender
print(

df.groupby("Sex")["Age"].mean()

)
   # Survival Rate by Gender
print(

df.groupby("Sex")["Survived"].mean()

)
   # Average Fare by Passenger Class
print(

df.groupby("Pclass")["Fare"].mean()

)
   # Number of Passengers in Each Class
print(

df.groupby("Pclass")["PassengerId"].count()

)

# 9. Create Age Group Column
def age_group(age):

    if age <= 12:
        return "Child"

    elif age <= 19:
        return "Teen"

    elif age <= 59:
        return "Adult"

    else:
        return "Senior"


df["Age_Group"] = df["Age"].apply(age_group)

print(

df[["Age","Age_Group"]].head()

)
   # Count Age Groups
print(

df["Age_Group"].value_counts()

)

# 10. Create Family Size
df["Family_Size"] = (

    df["SibSp"]

    +

    df["Parch"]

    +

    1

)

print(

df[["SibSp","Parch","Family_Size"]].head()

)

# 11. Create Status Column
def status(size):

    if size==1:

        return "Alone"

    else:

        return "With Family"


df["Status"] = df["Family_Size"].apply(status)


print(

df[["Family_Size","Status"]].head()

)
   # Count Alone vs With Family
print(

df["Status"].value_counts()

)

# 12. Pivot Table
   # Survival by Gender and Class
pivot = pd.pivot_table(

    df,

    index="Sex",

    columns="Pclass",

    values="Survived",

    aggfunc="mean"

)

print(pivot)

# 13. Top 10 Highest Fare Passengers
top10 = df.sort_values(

    "Fare",

    ascending=False

).head(10)


print(

top10[

    [

    "Name",

    "Sex",

    "Age",

    "Fare",

    "Pclass"

    ]

]

)

# 14. Save Cleaned Dataset
df.to_csv(

    "titanic_cleaned.csv",

    index=False

)