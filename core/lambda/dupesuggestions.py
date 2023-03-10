"""This script reads a .csv file, checks if there are
any duplicates in the file, returns True or False, returns
 the duplicate dataset based on the first column, and then
 saves the duplicates to a file."""

import pandas as pd

df = pd.read_csv('dupesuggestions.csv')
df.head()  # using head() to view the first 5 rows

COL = 'suggestion_external_id_vod_c'

# Using Lambda 'apply' function to find duplicate suggestions
np2 = df.apply(lambda x: x.astype(str).str.lower()).duplicated(COL)
print(np2)

# Total count of duplicate suggestions
duplicates = np2[np2].duplicated().sum()
print("Total number of duplicate suggestions are:", duplicates)

# Display the suggestions ids that are duplicated
print(df[df.duplicated(COL)])

# Get the index of the duplicates
index = df.index

# Save duplicate suggestions records to a file
df.to_csv('newdupeSuggestions.csv')

# Send and email with attachment using smtp


# Send file with duplicates to ServiceNow

# Remove the duplicates after saving duplicates to a file
# np2 = df.apply(lambda x: x.astype(str).str.lower()).drop_duplicates(COL)
# print(np2)

# Save file with no duplicates
# df.to_csv('No_More_Duplicates')
