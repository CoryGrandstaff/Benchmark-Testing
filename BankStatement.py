def display_file(record_count):
    with open ('bankstatement.xml', 'rt') as in_file:
        contents = in_file.read()
    print("*********************************************************************************NEW RECORD**********************************************************************************************")
    with open ("Output.txt", "w") as text_file:
        for i in range(int(record_count)):
            text_file.write(contents)

    print(contents)