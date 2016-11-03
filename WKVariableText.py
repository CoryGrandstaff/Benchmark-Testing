def displayFile(recordCount):
    with open ('WKVariableText.dat', 'rt') as in_file:
        contents = in_file.read()
    with open ("Output.txt", "w") as text_file:
        for i in range(int(recordCount)):
            text_file.write(contents)
    print(contents)