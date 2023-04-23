# Topic: Write Files in Python
# Author: Subhrangsu Sinha
# Date: 11.09.2022

# FOR Write A FILE:- 
# (open("file path","Opening mode")) --> use write() --> close the file

file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt','w') #--> Open a existing file in write mode
data = file_content.write('I want to be Vice President of Alphabet Inc.') #--> writing the content of opened file
print(data)
file_content.close() # --> The most important thing is, we should have to close the file if we have opened it. 

######## Very Very Important Note #########
# Write mode / write() always overwrites the existing file. That means, if we're used write() then existing data must be deleted.
# That's why we are preffered append() instead of write()


file_content = open('C:\\Users\\subhr\\Desktop\\PYTHON BASICS\\Chapter-9 (File I\O )\\sample.txt','a') #--> Open a existing file in append mode
data = file_content.write('\n I wanna be a part of Apphabet Inc.') #--> appending the content of opened file
file_content.close() # --> The most important thing is, we should have to close the file if we have opened it. 


'''
The most important question is when we need to use write() because I've said earlier, write() overwrites on existing data!!

--> Let's assume, We're playing Temple Run / Subway Surfer/.../ any game and my current high score is 10000. after half an hour, again we're playing that game and this time my high score is 100000. In that case, We don't need to show the existing high score. We need to overwrite the new high score instead of old high score. In this time, We can use write(). 
'''