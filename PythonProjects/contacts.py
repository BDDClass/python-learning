contact = {
	"firstName" : "Example",
	"lastName" : "Example",
	"phoneNumber" : "555-555-5555",
	"email" : "example@example.ex",
	"tags" : ["tag1", "tag2", "tag3"],
	"dateMade" : "05/24/2020",
	"dateModified" : "05/24/2020",
	"notes" : "Sample text",
	"address" : {
		"street" : "1234 Example St.",
		"city" : "Fort Wayne",
		"state" : "Ohio",
		"zip" : 44444
	}
}

contacts = {}

#========================================================================================================================
#===== VALIDATION FUNCTIONS =============================================================================================
#========================================================================================================================

lettersUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettersLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

#returns true if only valid chars are found
def charWhitelist(txt, exceptions=[]):
	for ch in txt:
		if not (ch in lettersLower or ch in lettersUpper or ch in numbers or ch in exceptions):
			return False
	return True

#does not accept negative numbers
def isIntegral(txt):
	for ch in txt:
		if not ch in numbers:
			return False
	return True

#accepts both x-xxx-xxx-xxxx and xxx-xxx-xxxx numbers
def isPhoneNumber(txt):
	if len(txt) == 12:
		if not (txt[3] == '-' and txt[7] == '-'):
			return False
		txt = txt[:3] + txt[4:7] + txt[8:]
		return isIntegral(txt)
	elif len(txt) == 14:
		if not (txt[1] == '-' and txt[5] == '-' and txt[9] == '-'):
			return False
		txt = txt[0] + txt[2:5] + txt[6:9] + txt[10:]
		return isIntegral(txt)
	return False

#normally emails are allowed to have certain symbols in certain circumstances, but this implementation only allows very basic emails.
#For example, "bdd(.-01_"@google.com is technically a valid email, but this program does not accept it.
def isEmail(txt):
	if txt.count('@') != 1 or txt.count('.') < 1:
		return False
	atLocation = txt.find('@')
	#a '.' must be present after the '@'
	if txt.rfind('.') < atLocation:
		return False
	#filter out invalid '@' locations
	if atLocation == 0 or atLocation == len(txt)-1:
		return False
	#filter out invalid '.' locations
	invalidDotLocations = [0, len(txt)-1, atLocation-1, atLocation+1]
	previousIsDot = False
	for index in range(len(txt)):
		if txt[index] == '.':
			#consecutive '.'s are not allowed
			if previousIsDot:
				return False
			previousIsDot = True
			if index in invalidDotLocations:
				return False
		else:
			previousIsDot = False
	#final filter for invalid characters
	return charWhitelist(txt, ['@', '.'])

#follows the format MM/DD/YYYY
def isDate(txt):
	if len(txt) == 10:
		if not (txt[2] == '/' and txt[5] == '/'):
			return False
		txt = txt[:2] + txt[3:5] + txt[6:]
		if not isIntegral(txt):
			return False
		month = int(txt[:2])
		day = int(txt[2:4])
		if month > 12 or month < 1 or day > 31 or day < 1:
			return False
		return True
	return False

#must start with a number and a space
def isStreet(txt):
	if txt.count(' ') < 1:
		return False
	spaceLocation = txt.find(' ')
	if spaceLocation == len(txt)-1:
		return False
	num = txt[:spaceLocation]
	if not isIntegral(num):
		return False
	street = txt[spaceLocation+1:]
	validStreetChars = [' ', '.', '\'']
	if not charWhitelist(street, validStreetChars):
		return false
	#whether or not the previous char was their validStreetChars equivilant
	previousStreetChars = [False, False, False]
	for index in range(len(txt)):
		#".'" and "'." are not allowed
		if txt[index] in ['.', '\''] and (previousStreetChars[1] or previousStreetChars[2]):
			return False
		#" ." is not allowed
		if txt[index] == '.' and previousStreetChars[0]:
			return False
		for chIndex in range(len(validStreetChars)):
			if txt[index] == validStreetChars[chIndex]:
				#consecutive characters are not allowed ("  ", "..", "''")
				if previousStreetChars[chIndex]:
					return False
				previousStreetChars[chIndex] = True
			else:
				previousStreetChars[chIndex] = False
	return True

#========================================================================================================================
#===== CONTACT FUNCTIONS ================================================================================================
#========================================================================================================================

def contactInBounds(id):
	return len(contacts) > id

def contactCreate():
	input()

def contactShow():
	input()

def contactShowAll():
	input()

def contactShowStats():
	input()

def contactChange():
	input()

def contactMerge():
	input()

def contactDelete():
	input()

def contactSearchName():
	input()

def contactSearchPhone():
	input()

def contactSearchTag():
	input()

def contactSearchDuplicate():
	input()

#will use contactSearchTag()'s output
def contactExport():
	input()