import csv
import numpy as np

# Read dataframe in from csv
df = pd.read_csv('CT_unclean.csv', names=["IND", "TOWN", "NAME", "BEDS", "CASES", "1", "2", "3", "4", "5"])
# Drop first 7 rows, which do not include nursing home data
df = pd.DataFrame(df.iloc[7:,]).dropna(how="all").reset_index(drop=True)

# Seperate out left columns, since they are largely consistent
left_info = df.iloc[:,:5]

# Combine all columns with death data using spaces, delete empty data, and then expand into two columns (confirmed and probable) 
deaths = df.iloc[:,5:].astype(str).agg(" ".join, axis=1).str.replace("\s*nan\s*", "", regex=True).str.split(" ", expand=True)
deaths.columns = ["CONFIRMED DEATHS", "PROBABLE DEATHS"]

# Get totals confirmed/probable deaths from bottom row to check later
total_confirmed = float(deaths.iloc[-1]["CONFIRMED DEATHS"].replace(",", ""))
total_probable = float(deaths.iloc[-1]["PROBABLE DEATHS"])

# Combine left columns and death columns, and remove total row at bottom
df2 = pd.concat([left_info, deaths], axis=1).iloc[:-1,]

# Look for names split across multiple rows and combine them
for i, row in df2.iterrows():
    if str(row["TOWN"]) == "nan":
        df2.at[i+1, "NAME"] = row["NAME"] + " " + df2.iloc[i+1]["NAME"]

# Drop rows that only had partial names and no data
final_df = df2.dropna().reset_index(drop=True)

# Replace line breaks in cells with spaces
final_df["NAME"] = final_df["NAME"].astype(str).replace("\\r", " ", regex=True)

# Check death counts and row counts against totals/indices from data
if final_df["PROBABLE DEATHS"].astype(float).sum() != total_probable:
    print("Probable deaths do not match total")
    
if final_df["CONFIRMED DEATHS"].astype(float).sum() != total_confirmed:
    print("Confirmed deaths do not match total")

if final_df.iloc[-1]["IND"] != str(final_df.shape[0]):
    print("Row count doesn't match index")

# Write to csv
final_df.to_csv("CT_clean.csv", index=False)
