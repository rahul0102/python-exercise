
file_data = input("Enter data you want to write: ")
file_name = input("Enter file name with extension(a.txt): ")

open_file = open(file_name,"w")
open_file.write(file_data)
open_file.close()
