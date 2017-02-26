import messytables
import tabulate

tableset = messytables.html.HTMLTableSet(filename="./wiki_sig_table.html")

table = tableset.tables[0]

# get data
data = []
for row in table:
    temp_row = []
    for col in row:
        if len(col.value.split('\n')) > 1:
            temp_cell = []
            for val in col.value.split('\n'):
                if val != '':
                    temp_cell.append(val)
            temp_row.append(temp_cell)
        else:
            temp_row.append(col.value)
    data.append(temp_row)

headers = data.pop(0)

#new_headers = [headers[0], headers[2], headers[4]]

#new_data = []
#for row in data:
#    new_row = [row[0], row[2], row[4]]
#    new_data.append(new_row)
        
#print(tabulate.tabulate(new_data, new_headers))
import csv

with open("wiki_file_sigs.csv", "w+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(data)