import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df= pd.read_excel(r"C:\Users\laaru\Downloads\pandas-python\Customer Call List.xlsx")

df= df.drop_duplicates()

print(df)

df.drop(columns="Not_Useful_Column", inplace=True)

print(df)

df["Last_Name"] = df["Last_Name"].str.strip("...")
print(df)

df["Last_Name"] = df["Last_Name"].str.lstrip("/")
print(df)

df["Last_Name"] = df["Last_Name"].str.rstrip("_")
print(df)

df["Last_Name"] = df["Last_Name"].str.strip("123._/")
print(df)

df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]", "", regex=True)
print(df)

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
print(df)

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])
print(df)

df["Phone_Number"] = df["Phone_Number"].str.replace("nan--","")
print(df)

df["Phone_Number"] = df["Phone_Number"].str.replace("Na--","")
print(df)

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(",",n= 2 , expand=True)
print(df)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes","Y")
print(df)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No","N")
print(df)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("N","No")
print(df)

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Y","Yes")
print(df)

df["Paying Customer"] = df["Paying Customer"].str.replace("Yes","Y")
print(df)

df["Paying Customer"] = df["Paying Customer"].str.replace("No","N")
print(df)

df["Paying Customer"] = df["Paying Customer"].str.replace("N","No")
print(df)

df["Paying Customer"] = df["Paying Customer"].str.replace("Y","Yes")
print(df)


df= df.fillna("")
print(df)


for x in df.index:
        if df.loc[x, "Do_Not_Contact"] == "Yes":
            df.drop(x, inplace=True)

print(df)


for x in df.index:
        if df.loc[x, "Phone_Number"] == "":
            df.drop(x, inplace=True)

print(df)

df = df.reset_index(drop=True)
print(df)
