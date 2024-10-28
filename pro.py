import pandas as pd

df = pd.read_csv(r'c:\Users\abhis\OneDrive\Desktop\datae\final_track01.csv')

unwanted_substrings = ['xexxs', '\\xc2\\xa']

for substring in unwanted_substrings:
    df = df.apply(lambda x: x.str.replace(substring, '', regex=False) if x.dtype == "object" else x)

# Remove commas and unwanted characters from Amount_in_USD column
df['Amount_in_USD'] = df['Amount_in_USD'].str.replace(',', '', regex=False)

df['Amount_in_USD'] = pd.to_numeric(df['Amount_in_USD'], errors='coerce')

df['Date'] = df['Date'].str.replace(r'/+', '/', regex=True)

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

if df['Date'].isnull().any():
    print("The following dates could not be parsed:")
    print(df[df['Date'].isnull()])

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')


df.to_csv(r'c:\Users\abhis\OneDrive\Desktop\datae\finaltrack.csv', index=False)

print("Data cleaned and saved to 'startup.csv.csv'")

