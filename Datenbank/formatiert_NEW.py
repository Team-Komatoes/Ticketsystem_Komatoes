import json

# Load JSON data from the file
with open('komatoes.json', 'r') as file:
    data = json.load(file)

# Open the SQL file for writing
with open('proj_koma.sql', 'w') as sql_file:
    # Iterate over each table in the JSON data
    for table in data:
        if table['type'] == 'table':
            table_name = table['name']
            # Write the CREATE TABLE statement
            sql_file.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")
            # Get the first row of data to determine column names and types
            first_row = table['data'][0]
            columns = []
            for column, value in first_row.items():
                # Determine the SQL data type
                if isinstance(value, int):
                    columns.append(f"{column} INT")
                elif isinstance(value, float):
                    columns.append(f"{column} FLOAT")
                else:
                    columns.append(f"{column} VARCHAR(255)")
            # Write columns to the SQL file
            sql_file.write(",\n".join(columns))
            sql_file.write("\n);\n\n")

            # Write INSERT statements for each row of data
            for row in table['data']:
                columns = ', '.join(row.keys())
                values = ', '.join(
                    f"'{value}'" if value is not None else 'NULL' for value in row.values()
                )
                sql_file.write(f"INSERT INTO {table_name} ({columns}) VALUES ({values});\n")
            sql_file.write("\n")

print("The SQL file 'proj_koma.sql' has been successfully created!")