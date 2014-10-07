import os
import shutil

def create_alphabet_directories():
	"""Creates 26 directories in the current directory, one for each letter of the alphabet"""
	# Print our current directory
	# print os.getcwd()

	# Create a for loop that iterates through the alphabet, create a dictionary for each
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in alphabet:
		# if the directory for that letter doesn't exist yet, create one
		if os.path.exists(letter) == False:
			os.makedirs(letter)

def put_originalfiles_into_directories():
	"""Loops through the files in the original_files directory, moves them into the appropriate directory"""
	# put all the files in original_files into a list
	list_of_files = os.listdir("/Users/mfb279/Documents/HackbrightHW_and_Projects/Week_1_Project/original_files")
	# print list_of_files

	for the_file in list_of_files:
		# get the first letter of the file name
		first_letter = the_file[0]

		source_path = "/Users/mfb279/Documents/HackbrightHW_and_Projects/Week_1_Project/original_files/%s" % the_file
		destination_path = "/Users/mfb279/Documents/HackbrightHW_and_Projects/Week_1_Project/%s" % first_letter

		# print source_path
		# print destination_path

		# move each file in the list to its appropriate directory
		shutil.move(source_path, destination_path)



def main():
	# Change the current directory so that we're in the right one
	os.chdir("/Users/mfb279/Documents/HackbrightHW_and_Projects/Week_1_Project")
	
	create_alphabet_directories()
	put_originalfiles_into_directories()

if __name__ == '__main__':
	main()