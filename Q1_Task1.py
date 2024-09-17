import pandas as pd

# Paths to the CSV files
csv_files = ["CSV1.csv", "CSV2.csv", "CSV3.csv", "CSV4.csv"]
combined_text = ""

# Iterate over each file, read the content, and extract the 'text' column
for file in csv_files:
    df = pd.read_csv(file)

    # Print the columns for debugging purposes
    print(f"Columns in {file}: {df.columns.tolist()}")

    # Check for 'text' column ignoring case sensitivity
    possible_columns = [col for col in df.columns if col.lower() == 'text']
    if possible_columns:
        combined_text += " ".join(df[possible_columns[0]].dropna().tolist()) + "\n"
    else:
        print(f"No 'text' column found in {file}")

# Write the combined text into a single .txt file
with open("combined_text.txt", "w") as f:
    f.write(combined_text)

print("Text from CSV files extracted and stored into combined_text.txt")
