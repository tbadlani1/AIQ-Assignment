import requests
import pandas as pd

# Census API Key
API_KEY = "ba8e0a739f66a01e074129dd7be1f83cbb888b2f"


BASE_URL_TEMPLATE = "https://api.census.gov/data/{year}/acs/acs5"


VARIABLES = [
    "NAME", 
    "B01003_001E",  
    "B19013_001E",  
    "B19083_001E",  
    "B25064_001E",  
    "B25077_001E",  
    "B01002_001E",  
    "B23025_005E",  
    "B02001_002E", 
    "B02001_003E",  
    "B03003_003E",  
]


VARIABLE_RENAMES = {
    "NAME": "State",
    "B01003_001E": "Total Population",
    "B19013_001E": "Median Household Income",
    "B19083_001E": "Gini Index",
    "B25064_001E": "Median Gross Rent",
    "B25077_001E": "Median Home Value",
    "B01002_001E": "Median Age",
    "B23025_005E": "Unemployment Rate",
    "B02001_002E": "White Population",
    "B02001_003E": "Black Population",
    "B03003_003E": "Hispanic Population",
}


YEARS = list(range(2018, 2024))  

all_data = []

for year in YEARS:
    print(f"Fetching data for year {year}...")
    
    
    url = BASE_URL_TEMPLATE.format(year=year)
    
    
    query_params = {
        "get": ",".join(VARIABLES),  
        "for": "state:*",  
        "key": API_KEY
    }
    
    
    response = requests.get(url, params=query_params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            if len(data) > 1:  
                df = pd.DataFrame(data[1:], columns=data[0])
                df.rename(columns=VARIABLE_RENAMES, inplace=True)
                df["Year"] = year
                all_data.append(df)
            else:
                print(f"No data returned for {year}.")
        except Exception as e:
            print(f"Error processing data for {year}: {e}")
    else:
        print(f"Error fetching data for {year}: HTTP {response.status_code}")

if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)

    for col in combined_df.columns:
        if col not in ["State", "state", "Year"]: 
            combined_df[col] = pd.to_numeric(combined_df[col], errors="coerce")
    

    print(combined_df.head())

    combined_df.to_csv("us_census_data_2018_2024_debugged.csv", index=False)
else:
    print("No data fetched.")
