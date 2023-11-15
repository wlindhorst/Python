input_file = input("Enter the name of the file: ")

fin = open(input_file,'rt')
records = list()
d_item = {}

# read one line - see if it's blank - if blank then it's a new record, and read a new line
for file_line in fin:
    print(f"------\nFile line: {file_line}")
    print(len(file_line))
        
    file_line = file_line.strip("\n")  # remove new lines because they're annoying and messing things up
    
    if len(file_line) <= 1:
        records.append(d_item)         #if we got here we got an empty line, so the record should be complete
        d_item = {}                    #create new dictionary item
        
    #if not file_line:  # if end of file - exit while loop
    #    break
    if file_line:  # if line has text add a dictionary to a list
        record_items = file_line.split(' ')

        for data in record_items:
            data_item = data.split(':')
            #print(f"Data Item: {data_item}")
            d_item[data_item[0]] = data_item[1]

        print(d_item)
    

    
fin.close()
print(f"Records: {records}")  #each "passport" information is in a dictionary - in a list

valid_count = 0
invalid_count = 0

for record in records:    # records is a list of dictionaries
    current_record_valid = True
    print(f"byr: {record["byr"]}\n")
    
    # check to see there is required data in the required fields
    if len(record) != 8 and 'ecl' in record['ecl'] :
        current_record_valid = False
    elif not record['byr']:
        current_record_valid = False
    elif not record['iyr']:
        current_record_valid = False
    elif not record['eyr']:
        current_record_valid = False
    elif not record['hgt']:
        current_record_valid = False
    elif not record['hcl']:
        current_record_valid = False
    elif not record['pid']:
        current_record_valid = False
    elif not record['cid']:
        current_record_valid = False
    elif int(record['byr']) < 1920 and int(record['byr']) > 2007 :
        current_record_valid = False
    elif int(record['iyr']) < 2013 and int(record['iyr']) > 2023 :
        current_record_valid = False
    elif int(record["eyr"]) < 2023 and int(record['eyr']) > 2033 :
        current_record_valid = False
    elif len(record['pid']) != 9 :
        current_record_valid = False
    elif len(record['cid'].replace('0', '')) != 3 :
        current_record_valid = False
    
    if record['hgt'].endswith('cm') :
        if int(record['hgt'].replace('cm', '')) < 150 and  int(record['hgt'].replace('cm', '')) > 193 :
            current_record_valid = False
    elif record['hgt'].endswith('in') :
        if int(record['hgt'].replace('in', '')) < 59 and  int(record['hgt'].replace('in', '')) > 76 :
            current_record_valid = False
            
    # no need to check record['ecl'] as it's optional
    
    # if after all this we're still valid up the count!
    if current_record_valid :
        valid_count += valid_count 
    else:
        invalid_count += invalid_count
        
print(f"There are {valid_count} valid passports")
print(invalid_count)