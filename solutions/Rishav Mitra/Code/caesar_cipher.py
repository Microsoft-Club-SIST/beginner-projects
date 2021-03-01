# This is a command-line application
import string

# Getting the list of alphabets
UPPERCASE_LETTERS = string.ascii_uppercase
LOWERCASE_LETTERS = string.ascii_lowercase

# function to encrypt the message
def encrypt(message, shift):
	encrypted_message = ""
	# Algorithm for encryption
	for char in message:
		if char in UPPERCASE_LETTERS:
			new_char = UPPERCASE_LETTERS[(UPPERCASE_LETTERS.index(char) + shift) % 26]
		elif char in LOWERCASE_LETTERS:
			new_char = LOWERCASE_LETTERS[(LOWERCASE_LETTERS.index(char) + shift) % 26]
		else:
			new_char = char

		encrypted_message += new_char
	
	return encrypted_message

# function to decrypt the message
def decrypt(message, shift):
	decrypted_message = ""
	# Algorithm for decryption
	for char in message:
		if char in UPPERCASE_LETTERS:
			new_char = UPPERCASE_LETTERS[(UPPERCASE_LETTERS.index(char) - shift) % 26]
		elif char in LOWERCASE_LETTERS:
			new_char = LOWERCASE_LETTERS[(LOWERCASE_LETTERS.index(char) - shift) % 26]
		else:
			new_char = char

		decrypted_message += new_char
	
	return decrypted_message

if __name__ == '__main__':
	option = input("Do you want to [e]ncrypt or [d]ecrypt your message ? ")

	if option in ['e', 'd']:
		message = input("Enter your message : ")

		print("Enter the shift of the cipher \nPositive values => Right shift \nNegative values => Left shift")
		shift = int(input())

		if option == 'e':
			print(encrypt(message, shift))
		elif option == 'd':
			print(decrypt(message, shift))
			
	else:
		print("Please enter a valid option !")
