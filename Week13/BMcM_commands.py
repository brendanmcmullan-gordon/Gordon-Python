commandfile = open("commands.txt", "w")

commandfile.write("'r' Open a file for reading. (default)")
commandfile.write("\n'w' Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.")
commandfile.write("\n'x' Open a file for exclusive creation. If the file already exists, the operation fails.")
commandfile.write("\n'a' Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.")
commandfile.write("\n't' Open in text mode. (default)")
commandfile.write("\n'b' Open in binary mode.")
commandfile.write("\n'+' Open a file for updating (reading and writing)")

commandfile = open("commands.txt", "a+")

commandfile.write("\n\n Appended line.")

commandfile = open("commands.txt", "r")

print(commandfile.read())

commandfile.close()
