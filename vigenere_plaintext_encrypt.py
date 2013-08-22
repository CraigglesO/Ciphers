#########################################################################################
####################                 HOW TO USE                ##########################
#########################################################################################
# This takes input from the terminal so run (in the proper cd):                         #
# 'python vigenere_plaintext_encrypt.py textFile.txt key'                               #
# Make sure the file is in the same folder as this script                               #
# You can also directly input the plain text:                                           #
# 'python vigenere_plaintext_encrypt.py ThisIsPlainTextCamelCasing key'                 #
#                            															#
# so obviously the first variable is the plaintext with no spaces allowed               #
# and the key is an arbitrary length you use to encode the words                        #
#                             														    #
#																						#
#																						#
# For decrypting your code check the brother script 'vigenere_plaintext_decrypt.py'     #
#########################################################################################
#########################################################################################
#                Created by Craig O'Connor - Thursday, August 15, 2013					#
#########################################################################################




from sys import argv

script, plain_text, key = argv


plain_text_string = "%s" % plain_text
if ".txt" in plain_text_string:
	with open(plain_text_string, 'r') as f:
		plain_text_string = f.read()
plain_text_string = plain_text_string.lower()
key_string = "%s" % key
key_string = key_string.lower()
plain_text_num = []
key_num = []
encryption_val = []
encryption_char = ""

#Make sure the key length is long enough to convert the plaintext
while len(key_string) < len(plain_text_string):
	key_string += key_string

#This is our value system using a dictionary for a table
num_char = { 0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i',
			 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q',
			 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y',
			 25 : 'z' }

#lets convert the plain_text and key into there character values and place each value in its own compartment
for i, c in enumerate(plain_text_string):
	for value, char in num_char.iteritems():
		if char == c:
			plain_text_num.append(value)
for i, c in enumerate(key_string):
	for value, char in num_char.iteritems():
		if char == c:
			key_num.append(value)

#Create encryption values
for i in range(0,len(plain_text_num)):
	#Cipher_value = (Message_value + Key_value) mod 26
	encryption_val.append((plain_text_num[i] + key_num[i]) % 26)

#Finish up, turn those values into the proper characters:
for i in range(0,len(encryption_val)):
	for value, char in num_char.iteritems():
		if value == encryption_val[i]:
			encryption_char += char


print (encryption_char)
with open('cipher_text.txt', 'w') as f:
	f.write(encryption_char)