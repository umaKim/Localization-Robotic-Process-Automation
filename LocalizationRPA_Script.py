import gspread
import pandas as pd

# Service account key path - replace with your JSON file path
service_account_file = '' #ex) sample-406015-31f157455f19.json

# Spreadsheet details
spreadsheet_name = '' # ex) MAFIA42_Localization
worksheet_name = '' # ex) Sheet1

# Authenticate with the Google Sheets API
gc = gspread.service_account(filename=service_account_file)

# Open the spreadsheet and the specific worksheet
spreadsheet = gc.open(spreadsheet_name)
worksheet = spreadsheet.worksheet(worksheet_name)

# Get all values in the worksheet
values = worksheet.get_all_values()

# Convert to a DataFrame, setting the first row as the header
df = pd.DataFrame(values[1:], columns=values[0])

# Function to replace %s with %@마ㅈ
def replace_percent_s(text):
    return text.replace('%s', '%@')

# Iterate through the DataFrame to create localization strings with replaced %s
# Add more language you wish too
localization_strings_ko = [f'"{replace_percent_s(row["key"])}" = "{replace_percent_s(row["korValue"])}";' 
                           for index, row in df.iterrows()]
localization_strings_en = [f'"{replace_percent_s(row["key"])}" = "{replace_percent_s(row["engValue"])}";' 
                           for index, row in df.iterrows()]
localization_strings_ar = [f'"{replace_percent_s(row["key"])}" = "{replace_percent_s(row["arValue"])}";' 
                           for index, row in df.iterrows()]
localization_strings_jp = [f'"{replace_percent_s(row["key"])}" = "{replace_percent_s(row["jpValue"])}";' 
                           for index, row in df.iterrows()]

# Save to a .strings file (Korean version)
with open('Localizable_ko.strings', 'w', encoding='utf-8') as f:
    for line in localization_strings_ko:
        f.write(line + '\n')

# Save to a .strings file (English version)
with open('Localizable_en.strings', 'w', encoding='utf-8') as f:
    for line in localization_strings_en:
        f.write(line + '\n')

# Save to a .strings file (Arabic version)
with open('Localizable_ar.strings', 'w', encoding='utf-8') as f:
    for line in localization_strings_ar:
        f.write(line + '\n')

# Save to a .strings file (Japanese version)
with open('Localizable_jp.strings', 'w', encoding='utf-8') as f:
    for line in localization_strings_jp:
        f.write(line + '\n')

print("Localization files have been created.")
