input_file = input("Enter the name of the file: ")

fin = open(input_file,'rt')
records = list()
d_item = {}

# read one line - see if it's blank - if blank then it's a new record, and read a new line
for file_line in fin:

    print(f"------\nFile line: {file_line}")
    file_line = file_line.strip("\n")  # remove new lines because they're annoying and messing things up
    if file_line:  # if line has text add a dictionary to a list
        record_items = file_line.split(' ')

        for data in record_items:
            data_item = data.split(':')

            d_item[data_item[0]] = data_item[1]
        print(d_item)
    records.append(d_item)
    
fin.close()
print(f"Records: {records}")  #each "passport" information is in its own dictionary - in a list

