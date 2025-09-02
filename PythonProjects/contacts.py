'''
Sources:
https://www.geeksforgeeks.org/python/python-program-to-print-current-year-month-and-day/
https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
'''

import os
from datetime import date

'''
TODO:
contactCreate() and contactCreatePrompt() doesn't support tags yet.
'''

'''
CONTACT FORMAT:

contact = {
	"nickname" : "Ex",
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
		"zip" : "44444"
	}
}
'''

contacts = {}

#========================================================================================================================
#===== VALIDATION FUNCTIONS =============================================================================================
#========================================================================================================================

lettersUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettersLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '<', '>', '/', '?']
letters = lettersUpper + lettersLower
numbersAndLetters = letters + numbers
allText = numbersAndLetters + symbols

#returns true if only valid chars are found
def charWhitelist(txt, list, exceptions=[]):
	for ch in txt:
		if not (ch in list or ch in exceptions):
			return False
	return True

#does not accept negative or decimal numbers
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
#for example, "bdd(.-01_"@google.com is technically a valid email, but this program does not accept it.
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
	return charWhitelist(txt, numbersAndLetters, ['@', '.'])

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
	if not charWhitelist(street, numbersAndLetters, validStreetChars):
		return False
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
#===== CONTACT MODIFICATION FUNCTIONS ===================================================================================
#========================================================================================================================

def contactValidate(contactInfo):
	validKeys = ["nickname", "firstName", "lastName", "phoneNumber", "email", "tags", "notes", "address", "dateMade", "dateModified"]
	validAddressKeys = ["street", "city", "state", "zip"]
	#get keys, detect required keys, detect date keys
	keys = contactInfo.keys()
	if not ("firstName" in keys and "lastName" in keys and "phoneNumber" in keys):
		print("Error: Contact must contain first name, last name, and phone number.")
		return False
	hasAddress = "address" in keys
	addressKeys = []
	if hasAddress:
		addressKeys = contactInfo["address"].keys()
	#detect invalid keys
	invalidKeys = []
	for key in keys:
		if not key in validKeys:
			invalidKeys.append(key)
	if hasAddress:
		for key in addressKeys:
			if not key in validAddressKeys:
				invalidKeys.append("address["+key+"]")
	if len(invalidKeys) >= 1:
		print("Error: Contact contains one or more invalid attributes:")
		print(invalidKeys)
		return False
	#validate keys
	for key in ["nickname", "firstName", "lastName"]:
		if key in keys:
			if not charWhitelist(contactInfo[key], letters):
				print("Error: Invalid name or nickname ("+contactInfo[key]+").")
				return False
	if "tags" in keys:
		for tag in contactInfo["tags"]:
			if not charWhitelist(tag, allText):
				print("Error: Invalid tag ("+tag+").")
				return False
	if "notes" in keys:
		if not charWhitelist(contactInfo["notes"], allText):
			print("Error: Invalid notes.")
			return False
	for key in ["dateMade", "dateModified"]:
		if key in keys:
			if not isDate(contactInfo[key]):
				print("Error: Invalid date ("+contactInfo[key]+").")
				return False
	if "zip" in addressKeys:
		if not isIntegral(contactInfo["address"]["zip"]):
			print("Error: Invalid zip code.")
			return False
	if "state" in addressKeys:
		if not charWhitelist(contactInfo["address"]["state"], letters):
			print("Error: Invalid state.")
			return False
	if "city" in addressKeys:
		if not charWhitelist(contactInfo["address"]["city"], letters, ["."]):
			print("Error: Invalid city.")
			return False
	if "street" in addressKeys:
		if not isStreet(contactInfo["address"]["street"]):
			print("Error: Invalid street.")
			return False
	if "email" in keys:
		if not isEmail(contactInfo["email"]):
			print("Error: Invalid email.")
			return False
	if "phoneNumber" in keys:
		if not isPhoneNumber(contactInfo["phoneNumber"]):
			print("Error: Invalid phone number.")
			return False
	return True

def contactTimestamp(contactInfo, stampMade, stampModified):
	today = date.today()
	year = str(today.year).rjust(4, '0')
	month = str(today.month).rjust(2, '0')
	day = str(today.day).rjust(2, '0')
	dateStr = month + "-" + day + "-" + year
	keys = contactInfo.keys()
	
	if stampMade:
		contactInfo.update({"dateMade": dateStr})
	if stampModified:
		contactInfo.update({"dateModified": dateStr})

def contactCreate(contactDb, contactInfo):
	if contactValidate(contactInfo):
		contactTimestamp(contactInfo, True, True)
		contactDb.update({contactInfo["nickname"]: contactInfo})
		return contactInfo["nickname"]
	return None

def contactChange(contactDb, contactId, contactChanges):
	listKeys = contactDb.keys()
	if not contactId in listKeys:
		print("Error: Contact does not exist.")
		return False	

	oldContact = contactDb[contactId].copy()
	oldKeys = oldContact.keys()
	newKeys = contactChanges.keys()
	
	for key in range(len(newKeys)):
		if newKeys[key] != "address":
			if newKeys[key] in oldKeys:
				oldContact.pop(newKeys[key])
			oldContact.update({newKeys[key]: contactChanges[newKeys[key]]})
		else:
			if not "address" in oldKeys:
				oldContact.update({"address": dict({})})
			newAddressKeys = newKeys[key].keys()
			oldAddressKeys = oldContact["address"].keys()
			for addressKey in range(len(newAddressKeys)):
				if newAddressKeys[addressKey] in oldAddressKeys:
					oldContact["address"].pop(newAddressKeys[addressKey])
				oldContact["address"].update({newAddressKeys[addressKey]: contactChanges["address"][newAddressKeys[addressKey]]})

	newContactValid = contactValidate(oldContact)
	if newContactValid:
		nickname = oldContact["nickname"]
		contactTimestamp(oldContact, False, True)
		contactDb.pop(nickname)
		contactDb.update({nickname: oldContact})
	return newContactValid

def contactMerge(contactDb, contactId1, contactId2):
	input()

def contactDelete(contactDb, contactId):
	listKeys = contactDb.keys()
	if not contactId in listKeys:
		print("Error: Contact does not exist.")
		return False
	contactDb.pop(contactId)
	return True

#========================================================================================================================
#===== CONTACT PROMPT FUNCTIONS =========================================================================================
#========================================================================================================================

def contactCreatePrompt(contactDb):
	listKeys = contactDb.keys()
	print("For the following prompts, leave the field blank if not applicable. Prompts with \"*\" are required, and cannot be left blank.\n")
	nickname = input("*Input contact nickname: ")
	
	if nickname == "":
		print("Error: You must provide a nickname.")
		return None
	if nickname in listKeys:
		print("Error: Contact nicknames must be unique.")
		return None
	contact = {"nickname":nickname}
	
	fields = ["firstName", "lastName", "phoneNumber", "email", "notes"]
	fieldNames = ["first name", "last name", "phone number", "email", "notes"]
	fieldRequired = [True, True, True, False, False]

	for field in range(len(fields)):
		printText = "Input contact " + fieldNames[field] + ": "
		if fieldRequired[field]:
			printText = "*" + printText
		answer = input(printText)
		if answer == "" and fieldRequired[field]:
			print("Error: You must provide a " + fieldNames[field] + ".")
			return None
		if answer != "":
			contact.update({fields[field]: answer})
   
	addressFields = ["street", "city", "state", "zip"]
	addressFieldNames = ["street", "city", "state", "zip code"]
	hasAddressKey = False
	
	for field in range(len(addressFields)):
		printText = "Input contact " + addressFieldNames[field] + ": "
		answer = input(printText)
		if answer != "":
			if not hasAddressKey:
				contact.update({"address": {addressFields[field]:answer}})
				hasAddressKey = True
			else:
				contact["address"].update({addressFields[field]: answer})
	return contactCreate(contactDb, contact)

def contactChangePrompt(contactDb):
	listKeys = contactDb.keys()
	nickname = input("Enter the nickname of the contact you would like to modify: ")
	if not nickname in listKeys:
		print("Error: Contact does not exist.")
		return False

	validFields = ["firstName", "lastName", "phoneNumber", "email", "tags", "notes", "street", "city", "state", "zip"]
	print("Enter the field(s) you would like to update.\nThey should be separated by just one space instead of a comma.\nHere are the valid fields:")
	for field in validFields:
		print(field)
	answer = input()
	fieldsChanging = answer.split(" ")
	for field in fieldsChanging:
		if not field in validFields:
			print("Error: Invalid field (" + field + ").")
			return False

	changes = {}
	addressFields = ["street", "city", "state", "zip"]
	hasAddressKey = False
	for field in range(len(fieldsChanging)):
		#these responses are validated in contactValidate(), not here
		answer = input("Enter the new value for " + fieldsChanging[field] + ": ")
		if not fieldsChanging[field] in addressFields:
			changes.update({fieldsChanging[field]: answer})
		else:
			if not hasAddressKey:
				changes.update({"address": {fieldsChanging[field]:answer}})
				hasAddressKey = True
			else:
				changes["address"].update({fieldsChanging[field]: answer})

	return contactChange(contactDb, nickname, changes)

#========================================================================================================================
#===== CONTACT READING FUNCTIONS ========================================================================================
#========================================================================================================================

def contactShow(contactDb, contactId):
	dbKeys = contactDb.keys()
	if not contactId in dbKeys:
		print("Error: Contact not found.")
		return False
	contact = contactDb[contactId]
	contactKeys = contact.keys()
	print("="*25)
	print(contactId + " (" + contact["firstName"] + " " + contact["lastName"] + ")")
	emailText = ""
	if "email" in contactKeys:
		emailText = " Email: " + contact["email"]
	print("Phone: " + contact["phoneNumber"] + emailText)
	print("Date created: " + contact["dateMade"] + " Date last modified: " + contact["dateModified"])
	
	streetText = ""
	cityText = ""
	stateText = ""
	zipText = ""
	if "address" in contactKeys:
		addressKeys = contact["address"].keys()
		if "street" in addressKeys:
			streetText = "Street: " + contact["address"]["street"] + " "
		if "city" in addressKeys:
			streetText = "City: " + contact["address"]["city"] + " "
		if "street" in addressKeys:
			streetText = "State: " + contact["address"]["state"] + " "
		if "street" in addressKeys:
			streetText = "Zip: " + contact["address"]["zip"] + " "
	if not (streetText == "" and cityText == "" and stateText == "" and zipText == ""):
		print(streetText + cityText + stateText + zipText)

	if "notes" in contactKeys:
		print("Notes: " + contact["notes"])
	if "tags" in contactKeys:
		tagText = "Tags: "
		for tag in contact["tags"]:
			tagText += tag + " "
		print(tagText)

	print("="*25)
	return True

def contactShowAll(contactDb):
	for key in contactDb.keys():
		contactShown = contactShow(contactDb, key)
		if not contactShown:
			return False
	return True

def contactShowStats(contactDb):
	input()

def contactSearchName(contactDb, contactName):
	filteredContacts = [] #list of contactIds
	input()

def contactSearchPhone(contactDb, contactPhone):
	filteredContacts = [] #list of contactIds
	input()

def contactSearchTag(contactDb, contactTag):
	filteredContacts = [] #list of contactIds
	input()

def contactSearchDuplicate(contactDb):
	#attributes that will trigger duplication search:
	#nickname, firstName + lastName, phoneNumber, email
	input()

def contactStringForm(contactDb, contactId):
	input()

#will use contactSearchTag()'s output
def contactExport(contactDb, contactTag):
	input()

#========================================================================================================================
#===== PROGRAM FUNCTIONS ================================================================================================
#========================================================================================================================

def clearScreen():
    os.system("cls")

def mainMenu():
	answer = ""
	exitProgram = False
	
	while not exitProgram:
		clearScreen()
		print("Contact Manager")
		print("Type the number next to the action you want to perform.")
		print("1 - Add contact")
		print("2 - Change contact")
		print("3 - Delete contact")
		print("4 - Show contact statistics")
		print("5 - Find duplicate contacts")
		print("6 - Show contact")
		print("7 - Show all contacts")
		print("8 - Search contacts")
		print("9 - Export contacts")
		print("0 - Exit")
		answer = input()
		clearScreen()
		
		match answer:
			case "0":
				exitProgram = True
			case "1":
				contactId = contactCreatePrompt(contacts)
				if contactId == None:
					input("Contact creation failed.")
				else:
					input("Contact created successfuly.")
			case "2":
				contactChanged = contactChangePrompt(contacts)
				if not contactChanged:
					input("Contact change failed.")
				else:
					input("Contact changed successfuly.")
			case "3":
				contactId = input("Enter the nickname of the contact you would like to delete: ")
				contactDeleted = contactDelete(contacts, contactId)
				if not contactDeleted:
					input("Contact deletion failed.")
				else:
					input("Contact deleted successfuly.")
			case "4":
				input()
			case "5":
				input()
			case "6":
				contactId = input("Enter the nickname of the contact you would like to see: ")
				contactShown = contactShow(contacts, contactId)
				if not contactShown:
					input("Contact failed to show.")
			case "7":
				contactsShown = contactShowAll(contacts)
				if not contactsShown:
					input("Contacts failed to show.")
			case "8":
				input()
			case "9":
				input()

mainMenu()