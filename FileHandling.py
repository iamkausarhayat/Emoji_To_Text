# # # #First to make and write a file and then read the file.

# # # #Write the file
# # # f =  open("Intro.txt", 'x')
# # # f = open("Intro.txt","w")
# # # f.write("Hello Kausar Bhai")
# # # f.close()

# # # #Now read the file 
# # # f = open("Intro.txt", 'r')
# # # print(f.read())

# # file = open("Biograpy.txt",'x')
# # file.close()
# # file  = open("Biograpy.txt",'w')
# # file.write("My name is Kausar Hayat.\n I am 20 years Old.\n I have four brothers.")
# # file.close()

# # file=open("Biograpy.txt",'r')
# # for line in file:
# #     print(line.strip())
# # file.close( )
# # with open("Biograpy.txt",'w') as f:
# #     f.write("Add a comment")
# # f = open("Biograpy.txt", 'r')
# # print(f.read())    
import os
# cwd = os.getcwd()
# print("Current working directory:", cwd)
os.remove("Biograpy.txt")