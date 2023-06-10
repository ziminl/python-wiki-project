




def create_table(headers, rows):
    header_row = "|".join(headers)
    header_separator = "|".join(["---"] * len(headers))
    table = [header_row, header_separator]
    for row in rows:
        row_data = "|".join(row)
        table.append(row_data)
    table_str = "\n".join(table)
    return table_str
table_headers = ["Column 1", "Column 2", "Column 3"]
table_rows = [
    ["Row 1 Data 1", "Row 1 Data 2", "Row 1 Data 3"],
    ["Row 2 Data 1", "Row 2 Data 2", "Row 2 Data 3"],
    ["Row 3 Data 1", "Row 3 Data 2", "Row 3 Data 3"],
]
markdown_table = create_table(table_headers, table_rows)
print(markdown_table)
file_path = "table.txt"
with open(file_path, "w") as file:
    file.write(markdown_table)
print("saved in", file_path)




