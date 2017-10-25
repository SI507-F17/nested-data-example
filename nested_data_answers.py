# Import twitter_data.py in twitter_data in the current script
# 	- Note the file name does not include the extension ('.py')
#	- The * is a wildcard. It's telling python I want to import 
# 	  everything from the file twitter_data.py
from twitter_data import *
# What is the difference between the above statement and the following:
# import wtitter_data # You will need to comment the import above and uncomment this one to experiment
					  # HINT: the code below assumes we are using the first type of import: 'from twitter_data import *'



# Basic strategy:
# ========================================================================================
# 1. Check the type of the data structure
# 	 - If the data is dictionary... check the keys
#			- Check the type of the value associated to the key
#			- Check whether all keys are of the same type as the first
#			- Select a key the key that more closely aligns with the type of data you are looking for
#			- See step 2
# 	 - If the data is list...
# 			- Check its length (how many elements does it have?)
#			- Check the type of one element
#			- Check whether the other elements are of the same type as the first
# 2. Go down on elevel and repeat step 1
# ========================================================================================


# What is the type of the variable holding the twitter data?
# ----------------------------------------------------------
#print type(res) # prints a list of the keys in res


# If it's a dictionary, what are its keys?
# If it's a list, how many elements does it have?, and 
# what is the type of its first element?
# ----------------------------------------------------------
#print res.keys()
#print type(res['statuses']) 


# Why the key "search_metadata" is not relevant 
# to our purposes?
# ----------------------------------------------------------


# What is the type associated to the key 'statuses'?
# ----------------------------------------------------------
#print type(res['statuses']) 


# If it's a dictionary, what type are its keys?
# If it's a list, how many elements does it have?, and 
# what is the type of its first element?
# ----------------------------------------------------------
#print len(res['statuses']) # 3 elements
#print type(res['statuses'][0])


# Are all the elements on this sequence of the same type?
# ----------------------------------------------------------
#for i in range(len(res['statuses'])):
#	print type(res['statuses'][i])


# If it's the first element its a dictionary, 
# what are its keys?
# If it's a list, how many elements does it have?, and 
# what is the type of its first element?
# ----------------------------------------------------------
# print res['statuses'][0].keys()
# print type(res['statuses'][0].keys()[0])

# If it's a dictionary, how many keys does 
# the first dictionary have?
# ----------------------------------------------------------
#print len(res['statuses'][0].keys())


# Are all the elements in the sequences under 'statuses' the same?
# Are all the sequences nested under 'statuses' the same length'?
# ----------------------------------------------------------
#for i in range(len(res['statuses'])):
#	print res['statuses'][i].keys()
#	print len(res['statuses'][i].keys())


# Nested under 'statuses', there are dictionaries, 
# do they have a key that contains the username I am looking for?
# If so, what is the type and value associated to it?
# ----------------------------------------------------------
#print type(res['statuses'][0]['user'])
#print res['statuses'][0]['user']


# What are the keys associated to the dictionary 'user'?
# ----------------------------------------------------------
#print res['statuses'][0]['user'].keys()

# How many keys those the dictionary 'user' has?
# ----------------------------------------------------------
#print len(res['statuses'][0]['user'].keys())


# Is there a key that ressembles the username I am looking for?
# If so, which key is it, what is the type and value
# associated to it?
# ----------------------------------------------------------
# 'name'
#print type(res['statuses'][0]['user']['name']) 
#print res['statuses'][0]['user']['name']


# Since you know there are three tweets in the database
# You also know there is an equal number of usernames
# corresponding to the users who twitted
# By answerin the questions above, you have already found 
# the first name
# Can you iterate through the twitter data, so that you 
# access the other three names with a single print statement?
# ----------------------------------------------------------
#for i in range(len(res['statuses'])):
#	print res['statuses'][i]['user']['name']
