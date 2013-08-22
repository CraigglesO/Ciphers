#########################################################################################
####################                 HOW TO USE                ##########################
#########################################################################################
# This takes input from the terminal so run (in the proper cd):                         #
# 'python vigenere_plaintext_decrypt.py wordsbundledtogetherwithnouppercase key'        #
#                            															#
# so obviously the first variable is the encryption with no spaces allowed              #
# and the key is an arbitrary length that was originally used to encode the words       #
#                             														    #
#																						#
#																						#
# For encrypting your code check the brother script 'vigenere_plaintext_encrypt.py'     #
#########################################################################################
#########################################################################################
#                Created by Craig O'Connor - Thursday, August 15, 2013					#
#########################################################################################




from sys import argv

script, encrypt_text, key = argv


encrypt_text_string = "%s" % encrypt_text
if ".txt" in encrypt_text_string:
	with open(encrypt_text_string, 'r') as f:
		encrypt_text_string = f.read()
encrypt_text_string = encrypt_text_string.lower()
key_string = "%s" % key
key_string = key_string.lower()
encrypt_num = []
key_num = []
plain_text_val = []
plain_text_char = ""

#Make sure the key length is long enough to convert the plaintext
while len(key_string) < len(encrypt_text_string):
	key_string += key_string

#This is our value system using a dictionary for a table
num_char = { 0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i',
			 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q',
			 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v', 22 : 'w', 23 : 'x', 24 : 'y',
			 25 : 'z' }

#lets convert the encryption and key into there character values and place each value in its own compartment
for i, c in enumerate(encrypt_text_string.lower()):
	for value, char in num_char.iteritems():
		if char == c:
			encrypt_num.append(value)

for i, c in enumerate(key_string.lower()):
	for value, char in num_char.iteritems():
		if char == c:
			key_num.append(value)

#Create the decryption values
for i in range(0,len(encrypt_num)):
	#Message_value = (Ciphertext_value - Key_value) mod 26
	plain_text_val.append((encrypt_num[i] - key_num[i]) % 26)

#Finish up, turn those values into the proper characters:
for i in range(0,len(plain_text_val)):
	for value, char in num_char.iteritems():
		if value == plain_text_val[i]:
			plain_text_char += char


print (plain_text_char)
with open('plain_text.txt', 'w') as f:
	f.write(plain_text_char)