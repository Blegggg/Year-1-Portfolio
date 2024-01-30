import pandas as pd      #imports to panda and reads it
pd.read_csv('data.csv')
df = pd.read_csv('data.csv')  #reads the data.csv file
pd.options.display.max_rows = 9999 #increases the number of rows that could be shown
print(df) 

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,             # the data
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300   #the five limits amount of rows to 5
  }
}

df.dropna(inplace = True)

print(df.to_string())  #removes rows with no values


x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)  #calculates mean mode median
df = pd.DataFrame(data)

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)



x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)


print(df) 


