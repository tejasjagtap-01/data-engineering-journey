# number = 6
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)


# def linux_interaction():
#     import sys
#     if "linux" not in sys.platform:
#         raise RuntimeError("Function can only run on Linux systems.")
#     print("Doing Linux things.")

# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
#     print("The linux_interaction() function wasn't executed.")    




# try:
#     linux_interaction()
# except:
#     print("Linux function wasn't executed.")



# try:
#     with open("employee.log") as file:
#         read_data = file.read()
# except:
#     print("Couldn't open file.log")




# try:
#     linux_interaction()
#     with open("file.log") as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except RuntimeError as error:
#     print(error)
#     print("Linux linux_interaction() function wasn't executed.")



# import sys
# def linux_interaction():
#     if "linux" not in sys.platform:
#         raise RuntimeError("Function can only run on Linux systems.")
# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
# else:
#     print("Doing even more Linux things.")




# import sys
# def linux_interaction():
#     try:
#         linux_interaction()
#     except RuntimeError as error:
#         print(error)
#     else:
#         try:
#             with open("file.log") as file:
#                 read_data = file.read()
#         except FileNotFoundError as fnf_error:
#             print(fnf_error)    




def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")