import string

file1 = open('Book1.txt')
file2 = open('Book2.txt')
file3 = open('Book3.txt')

def longest_word():
 Book1 = " "
 Book2 = " "
 Book3 = " "

 for line in file1:
  for word1 in line.split():
   if len(word1) > len(Book1):
    Book1 = word1
 print('longest word in book1 is :',Book1) 

 for line in file2:
  for word2 in line.split():
   if len(word2) > len(Book2):
    Book2 = word2
 print('longest word in book2 is :',Book2)

 for line in file3:
  for word3 in line.split():
   if len(word3) > len(Book3):
    Book3 = word3
 print('longest word in book3 is :',Book3)


longest_word()
