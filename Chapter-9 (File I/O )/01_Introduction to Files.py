# Topic: Introduction with Files in Python
# Author: Subhrangsu Sinha
# Date: 11.09.2022

'''
What is Files I/O?
A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content in to it.
Suppose, We are playing PUBG. when we are open PUBG in our phones on that time some existing files are called from memory and move to RAM(RAM is volatile memory).That means, we need some files to RUN PUBG in our phone. This is the concept of FILE INPUT / OUTPUT Segmentation.
IN PUBG, We have Kill Ratio, Highest Damage, Total Kill, Outfits,... , Lot Of Things--> All those are stored in File. When we Run the PUBG, on that time all the files are called by RAM.
There are two types of file:-
1) Text Files--> (.txt, .c, .py etc)
2) Binary Files--> (.jpg,.mp3,.mp4 etc)

File I/O contains five major oeprations:-
1) Opening a file
2) Reading a file
3) Updating a file
4) Appending a file
5) Deleting a file
Python has a lot of functions for opening, reading, updating and deleting files.

Modes of Opening a file:-
r--> open file for read
w--> open file for write
a--> open file for append
+--> open file for updating

Note:- 'rb' used for read in binary mode and 'rt' used for read in text mode
'''

# FOR OPEN A FILE:- (open("file path","Opening mode"))


file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt','r') #--> Open a existing file in Read mode
data = file_content.read() #--> Reading the content of opened file
print(data)
file_content.close() # --> The most important thing is, we should have to close the file if we have opened it. 

# Note:-  If you haven't specified any opening mode then it'll take 'r' by default

file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt') 
data = file_content.read()
print(data)
file_content.close()

# If we want to read up to specific limit:-
file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt') 
data = file_content.read(5) # --> It'll read up to 5 characters
print(data)
file_content.close()

# readline() --> This is the alternative way of read() in Python file segmentatiion.
file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt') 
# Read first line-->
data = file_content.readline() # --> It'll read one line at a time
print(data,end='')
# Read second line-->
data = file_content.readline() 
print(data,end='')
file_content.close()