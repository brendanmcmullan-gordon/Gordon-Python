arrayfile = open("arrays.txt", "w")

arrayfile.write("A tuple is a collection of data that is immutable")
arrayfile.write("\nA list is a collection of data that is mutable")
arrayfile.write("\nA dictionary is collection of data that uses key/value pairs")

arrayfile = open("arrays.txt", "r")

print(arrayfile.read())

arrayfile.close()
