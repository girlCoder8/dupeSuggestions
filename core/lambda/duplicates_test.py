"""This script performs one assertion against
the dupesuggestions.py code"""

import ge as ge
import pandas as pd

df = pd.read_csv('dupesuggestions.csv')
df.head()  # using head() to view the rows

COL = 'suggestion_external_id_vod_c'

# Using Lambda 'apply' function to find duplicate suggestions
np2 = df.apply(lambda x: x.astype(str).str.lower()).duplicated(COL)
# print(np2)

# Total count of duplicate suggestions
duplicates = np2[np2].duplicated().sum()
print("Total number of duplicate suggestions are:", duplicates)

# Display the suggestions ids that are duplicated
print(df[df.duplicated(COL)])

# Get the index of the duplicates
index = df.index

# Save duplicate suggestions records to a file
df.to_csv('newdupeSuggestions.csv')

# load the dataframe in Great Expectations
df_ge = ge.dataset.PandasDataset(df)

# external_suggestions_vod_c column should NEVER be null
df_ge.expect_column_values_to_not_be_null('suggestion_external_id_vod_c')

validation_results = df_ge.validate()

print('')  # printing a blank line

# Validate the data
if validation_results["success"]:
    print('Assertion passed, the suggestion_external_id_vod_c column is not null! :)')
else:
    print('Assertion failed, the suggestion_external_id_vod_c column is not null! :(')
