
writefile = open("write_test.txt", "w")

writefile.write("1. This is a text file")
writefile.write("\n2. It was created using python")
writefile.write("\n3. It was written to using python as well")


writefile = open("write_test.txt", "r")

# reads the first line of the file
print(writefile.readline())
print("================================================================================")
# reads 16 characters from the file, after the first line
print(writefile.read(16))
print("================================================================================")
# reads the remainder of the file, after the 16 characters
print(writefile.read())

writefile.close()

writefile = open("write_test.txt", "a+")

writefile.write("\nX. Appended line.")

print(writefile.read())
