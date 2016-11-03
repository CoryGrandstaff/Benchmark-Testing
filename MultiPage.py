def displayFile(recordCount):
    with open ('MultiPage.DAT', 'rt') as in_file:
        for line in in_file:
            print(line)
    with open ("Output.txt", "w") as text_file:
        for i in range(int(recordCount)):
            text_file.write(line)
    print(line)