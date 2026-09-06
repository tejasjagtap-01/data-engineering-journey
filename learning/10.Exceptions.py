# Handling Exceptions 

# 1.
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Can't Divide By Zero!")

# 2. The basic try/except error

# try:
#     p = open('the.txt')
# except FileNotFoundError: 
#     print("Error ! File Not found")
# except Exception:
#     print('Something went wrong!')
# else:
#     print(p.read())
#     p.close()
# finally:
#     print("The File is readed")


# 3. Self defined Error handling

# try:
#     i = open('sucks.txt')
#     if i.name == 'sucks.txt':
#         raise Exception  
# except FileNotFoundError:
#     print('File not found')
# except Exception as e:
#     print('Something Went Wrong!')
# else:
#     print(i.read())
#     i.close()
# finally:
#     print('The file is under process')


# 4. 

# try:
#     f = open('sucks.txt')
#     if f.name == 'sucks.txt':
#         raise Exception
# except FileNotFoundError as f:
#     print('File not found')
# except Exception as f:
#     print('File does not exist')
# else:
#     print(f.read())
#     f.close()
# finally:
#     print('Did you get what you are looking for')


# 5.

# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)


# 6. 
 
# number = 8
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)


# 7.

# try:
#     with open("file.log") as file:
#         read_data = file.read()
# except:
#     print("Couldn't open file.log")


# 8.

try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)