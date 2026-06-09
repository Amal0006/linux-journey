file=open("data.txt","w")
file.write("Name: Amal\n")
file.write("Course: CSE\n")
file.write("Goal: Cloud Engineer\n")
file.close()
print("File written")

file=open("data.txt","r")
content=file.read()
file.close()
print(content)

file=open("data.txt","a")
file.write("Status: learnong Python\n")
file.close()
print("File updated\n")

file=open("data.txt","r")
for line in file:
	print(line.strip())
file.close()
