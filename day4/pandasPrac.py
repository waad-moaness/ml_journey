import pandas as pd 
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
df = pd.DataFrame({
     "name" : ["waad" , "mayan" , "ali" , "alaa"],
     "age"  : [21 , 7, 16 , 23],
     "job"  : ["sw engineer" , "student" , "student" ,"pharmasist"]
}
)

# df = df.set_inprint(data.at[200,"MedInc"])dex("name")
# # print(df.loc["waad"])
# df.to_csv("datafile.csv")

# print(pd.read_csv("datafile.csv"))

# data = fetch_california_housing(as_frame=True).frame 
# print(data)
# print(data.head())
# print(data.sample(5))
# print(list(data.columns))
# data.info()
# pd.options.display.max_columns =5
# pd.options.display.max_rows =5
# print(data)
# print(data.describe())
# print(data.MedInc)
# print(data["MedInc"])
# print(data["MedInc"].max())
# data["MedInc"].hist() #creates the histogram plot using matplotlib under the hood
# plt.show()
#access data 
# print(data.iat[200,7])
# print(data.at[200,"MedInc"])
# print(df.iloc[0:3])
#add row
df.loc[4]= ["hadeer" , 21, "frontend"]  #.iloc[] is strictly positional — it expects that the row at position 4 already exists so we don;t use it here
# print(df)
# print(df.age *2)

#applying functions to df

# df.age= df.age.apply(lambda x: x if x>20 else 0)
# print(df)

#add new column 
df["summary"] = df.apply(lambda r: f"name: {r["name"]} age: {r["age"]}" , axis=1)

#handling missing values 
df.iat[1,1] = None
df.iat[3,2] = None
#1 drop the row 
# df= df.dropna() #deop all nan values 
df.age= df.age.fillna(df.age.mean()) #fill nan values of a specific row of an spesific value like mean or 0 
#if i don't spicify age it will fill the nan in job as the mean age too and this is so wrong 
# print(df)

# print(df.notna())
# print(df[df.job.notna()])

# iterating through data
# for i,r in df.iterrows():
#     # print(r)
#     print(f"{r["name"] }, {r["age"] }, {r["job"]} ,{ r["summary"]}")
 
# for i, col in df.items():
#     print(col[1])
#to index by name here
df= df.set_index("name")
for i, col in df.items():
    print(col["waad"])


