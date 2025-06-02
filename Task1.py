import pandas as pd

#  LOAD THE DATA OF MALL CUSTOMER FROM KEGGLE......
df = pd.read_csv('Mall_Customers.csv')

print(df.info())
print(df.head())

# IDENTIFY OR HANDLE THE MISSING VALUES.....
print(df.isnull().sum())
df = df.dropna()


# REMOVE DUPLICATE VALUES FROM THR DATA...
df = df.drop_duplicates()

# STANDARDIZE THE TEXT VALUES...
df['Gender'] = df['Gender'].str.strip().str.lower().replace({'m': 'male', 'f': 'female'})

# REMOVE COLUMN HEADERS TO UNIFORM AND CLEAN (e.g. lowercase , no spaces)....
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


df['age'] = pd.to_numeric(df['age'], errors='coerce')  
df['age'] = df['age'].fillna(0).astype(int)  
