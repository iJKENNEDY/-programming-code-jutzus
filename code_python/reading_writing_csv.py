 import csv

 num = int(input("how many books do you want to add to the list? "))
 file = open("Books.csv", "a")
 for x in range(0, num):
 	title = input("Enter a title: ")
 	author = input("Enter author: ")
 	year = input("Enter the year it was released: ")
 	newrecord = title + ","+ author + ", " + year + "\n"
 	file.write(str(newrecord))
 file.close()

 searchauthor = input("Enter an authors name to search for: ")

 file = open("Books.csv", "r")
 count = 0
 for row in file:
 	if searchauthor in str(row):
 		print(row)
 		count = count + 1
 if count == 0:
 	print("There are no books by that author in this list.")
 	file.close()