# These are for reading files

# file = open('text.txt', mode= 'rb')

# data = file.readlines()

# print(data)

# file.close()




# with open('text.txt', mode='r') as file:
#     data = file.readlines()

#     print(data)



# try:
#     with open('text.txt', 'r') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print("Unable to locate file: ", e) 
    

# These syntax are for creating files

# with open('text2.txt', 'w') as file:
#     file.writelines(["\n This is the first line of the text", "\n This is the second line of the text"])
#     file.write("\n Are you happy now!")

# try:
#     with open('text2.txt', 'w') as file:
#         file.writelines(["\n This is the first line of the text", "\n This is the second line of the text"])
#         file.write("\n Are you happy now!")
# except FileNotFoundError as e:
#     print("The file was not created", e)
# except FileExistsError as e:
#     print(" Hello friend this file already exist: ", e)


# These syntax is for Reading files
# with open('text.txt', 'r') as file:
#     data = file.readlines()

#     for x in data:
#     # for x in file:
#         print(x)

# how to read a list and read it randomly as well
import random
data = open("petnames.txt", "r")
f_content = data.read()
f_content_list = f_content.split("\n")
data.close()
print(random.choice(f_content_list))


# If I had multiple files in my folder, I could allow myself to pick a file
import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))