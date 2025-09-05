'''
Sources:
https://www.geeksforgeeks.org/python/python-program-to-print-current-year-month-and-day/
https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
'''

import os
from datetime import date

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
# ", [], and {} are not allowed since it would mess up importing contacts like SQL injections
symbols = [' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '\\', '|', ';', ':', '\'', ',', '.', '<', '>', '/', '?']
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
	if not contactId1 in contactDb or not contactId2 in contactDb:
		print("Error: Contact not found.")
		return None
	contact1 = contactDb[contactId1]
	contact2 = contactDb[contactId2]
	uniqueKeys = set(contactDb[contactId1].keys()) | set(contactDb[contactId2].keys())

	c1Date = contact1["dateModified"]
	c2Date = contact2["dateModified"]
	c1Year = int(c1Date[-4:])
	c1Month = int(c1Date[:2])
	c1Day = int(c1Date[3:5])
	c2Year = int(c2Date[-4:])
	c2Month = int(c2Date[:2])
	c2Day = int(c2Date[3:5])

	newerContact = -1 #this stays -1 if both dates are the same
	if c1Year > c2Year:
		newerContact = 0
	elif c2Year > c1Year:
		newerContact = 1
	else:
		if c1Month > c2Month:
			newerContact = 0
		elif c2Month > c1Month:
			newerContact = 1
		else:
			if c1Day > c2Day:
				newerContact = 0
			elif c2Day > c1Day:
				newerContact = 1
	promptChanges = newerContact == -1
	if promptChanges:
		print("Both contacts have the same date.\nFor each field, enter which contact will be merged.\n1 = Contact 1, 2 = Contact 2.")

	contactOrder = [contact1, contact2]
	if newerContact == 1:
		contactOrder = [contact2, contact1]
	#contact order will always have the newer contact first
	
	mergedContact = {}
	newContact = contactOrder[0]
	oldContact = contactOrder[1]
	newKeys = newContact.keys()
	oldKeys = oldContact.keys()

	for key in uniqueKeys:
		bothHasKey = key in contactDb[contactId1].keys() and key in contactDb[contactId2].keys()
		if key != "address":
			if promptChanges and bothHasKey:
				answer = input(key + ": ") #TODO: VALIDATE THIS
				answer = contactOrder[int(answer)-1][key]
				mergedContact.update({key: answer})
			elif not promptChanges and bothHasKey:
				mergedContact.update({key: newContact[key]})
			else:
				if key in newKeys:
					mergedContact.update({key: newContact[key]})
				else:
					mergedContact.update({key: oldContact[key]})
		else:
			if not bothHasKey:
				if key in newKeys:
					mergedContact.update({key: newContact[key]})
				else:
					mergedContact.update({key: oldContact[key]})
			else:
				mergedContact.update({key: dict({})})
				newAddress = newContact["address"]
				oldAddress = oldContact["address"]
				newAddressKeys = newContact.keys()
				oldAddressKeys = oldContact.keys()
				uniqueAddressKeys = set(newKeys) | set(oldKeys)
				for addressKey in uniqueAddressKeys:
					bothHasAddressKey = addressKey in newKeys and addressKey in oldKeys
					if promptChanges and bothHasAddressKey:
						input() #TODO
					elif not promptChanges and bothHasAddressKey:
						input() #TODO
					else:
						input() #TODO

	mergeValid = contactValidate(mergedContact)
	if mergeValid:
		#TIMESTAMP, REPLACE DUPLICATE NICKNAME WITH MERGED CONTACT
		input() #TODO
	else:
		return None

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
    
	answer = input("Insert contact tags, separated by one space instead of commas: ")
	if answer != "":
		contact.update({"tags": answer.split(" ")})
    
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
		tagText = ""
		if fieldsChanging[field] == "tags":
			tagText = ". Enter each tag separated by one space, not a comma"
  		#these responses are validated in contactValidate(), not here
		answer = input("Enter the new value for " + fieldsChanging[field] + tagText + ": ")
		if fieldsChanging[field] == "tags":
			answer = answer.split(" ")
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
	stats = {
		"contactTotal": 0,
		"contactsByTag": {},
		"contactsByState": {},
		"contactTagAverage": 0.0,
		"commonAreaCode": "",
		"contactCountNoEmail": 0
	}
	
	keys = contactDb.keys()
	values = contactDb.values()
	
	stats.update({"contactTotal": len(keys)})

	noEmailCount = 0
	tagCount = 0.0
	areaCodeCounts = {}
	for value in values:
		valueKeys = value.keys()
		if not "email" in valueKeys:
			noEmailCount += 1
		if "tags" in valueKeys:
			tagCount += len(value["tags"])
		areaCode = ""
		if len(value["phoneNumber"]) == 14:
			areaCode = value["phoneNumber"][2:4]
		else:
			areaCode = value["phoneNumber"][:3]
		if not areaCode in areaCodeCounts.keys():
			areaCodeCounts.update({areaCode: 1})
		else:
			areaCodeCounts[areaCode] += 1
	stats.update({"contactCountNoEmail": noEmailCount})
	stats.update({"contactTagAverage": tagCount/len(keys)})
	#get most common area code
	commonCodeIndex = ""
	commonCodeValue = 0
	for code in areaCodeCounts.keys():
		if areaCodeCounts[code] > commonCodeValue:
			commonCodeIndex = code
	stats.update({"commonAreaCode": commonCodeIndex})
	#get unique tags and states
	uniqueTags = []
	uniqueStates = []
	for value in values:
		contactKeys = value.keys()
		if "tags" in contactKeys:
			for tag in value["tags"]:
				if not tag in uniqueTags:
					uniqueTags.append(tag)
		if "address" in contactKeys:
			if "state" in value["address"].keys():
				state = value["address"]["state"]
				if not state in uniqueStates:
					uniqueStates.append(state)
	#sort contacts by tag
	for tag in uniqueTags:
		matches = []
		for value in values:
			contactKeys = value.keys()
			if "tags" in contactKeys:
				if tag in value["tags"]:
					matches.append(value["nickname"])
		stats["contactsByTag"].update({tag: matches})
	#sort contacts by state
	for state in uniqueStates:
		matches = []
		for value in values:
			if "address" in value.keys():
				if "state" in value["address"].keys():
					if state == value["address"]["state"]:
						matches.append(value["nickname"])
		stats["contactsByState"].update({state: matches})
	return stats

def contactSearchName(contactDb, contactName):
	filteredContacts = {}
	searchName = contactName.lower()
	for value in contactDb.values():
		foundFirstName = value["firstName"].lower().find(searchName) > -1
		foundLastName = value["lastName"].lower().find(searchName) > -1
		if foundFirstName or foundLastName:
			filteredContacts.update({value["nickname"]: value})
	return filteredContacts

def contactSearchPhone(contactDb, contactPhone):
	for value in contactDb.values():
		if value["phoneNumber"] == contactPhone:
			return (value["nickname"], value)
	return (None, None)

def contactSearchTag(contactDb, contactTag):
	filteredContacts = {}
	for value in contactDb.values():
		if contactTag in value["tags"]:
			filteredContacts.update({value["nickname"]: value})
	return filteredContacts

def contactSearchDuplicates(contactDb):
	matchesNickname = []
	matchesName = []
	matchesPhone = []
	matchesEmail = []
	
	uniqueNicknames = []
	uniqueNames = []
	uniquePhones = []
	uniqueEmails = []
	for value in contactDb.values():
		if not value["nickname"] in uniqueNicknames:
			uniqueNicknames.append(value["nickname"])
		if not (value["firstName"] + value["lastName"]) in uniqueNames:
			uniqueNames.append(value["firstName"] + value["lastName"])
		if not value["phoneNumber"] in uniquePhones:
			uniquePhones.append(value["phoneNumber"])
		if not value["email"] in uniqueEmails:
			uniqueEmails.append(value["email"])
	
	dbSize = len(contactDb.keys())
	
	#find duplicate nicknames
	if len(uniqueNicknames) != dbSize:
		for nickname in uniqueNicknames:
			idMatches = []
			for value in contactDb.values():
				if value["nickname"] == nickname:
					idMatches.append(value["nickname"])
			if len(idMatches) > 1:
				matchesNickname.append(idMatches)
	#find duplicate names
	if len(uniqueNames) != dbSize:
		for name in uniqueNames:
			idMatches = []
			for value in contactDb.values():
				if (value["firstName"] + value["lastName"]) == name:
					idMatches.append(value["nickname"])
			if len(idMatches) > 1:
				matchesName.append(idMatches)
	#find duplicate phone numbers
	if len(uniquePhones) != dbSize:
		for phone in uniquePhones:
			idMatches = []
			for value in contactDb.values():
				if value["phoneNumber"] == phone:
					idMatches.append(value["nickname"])
			if len(idMatches) > 1:
				matchesPhone.append(idMatches)
	#find duplicate emails
	if len(uniqueEmails) != dbSize:
		for email in uniqueEmails:
			idMatches = []
			for value in contactDb.values():
				if value["email"] == email:
					idMatches.append(value["nickname"])
			if len(idMatches) > 1:
				matchesEmail.append(idMatches)
	
	duplicateContacts = {}
	duplicateContacts.update({"duplicateNicknames": matchesNickname})
	duplicateContacts.update({"duplicateNames": matchesName})
	duplicateContacts.update({"duplicatePhones": matchesPhone})
	duplicateContacts.update({"duplicateEmails": matchesEmail})
	return duplicateContacts

def contactStringForm(contactInfo):
	keys = contactInfo.keys()
	stream = ""
	stream += "{ [\"nickname\"]: " + contactInfo["nickname"] + " "
	stream += ", [\"firstName\"]: " + contactInfo["firstName"] + " "
	stream += ", [\"lastName\"]: " + contactInfo["lastName"] + " "
	stream += ", [\"phoneNumber\"]: " + contactInfo["phoneNumber"] + " "
	if "email" in keys:
		stream += ", [\"email\"]: " + contactInfo["email"] + " "
	if "dateMade" in keys:
		stream += ", [\"dateMade\"]: " + contactInfo["dateMade"] + " "
	if "dateModified" in keys:
		stream += ", [\"dateModified\"]: " + contactInfo["dateModified"] + " "
	if "notes" in keys:
		stream += ", [\"notes\"]: " + contactInfo["notes"] + " "
	if "tags" in keys:
		stream += ", [\"tags\"]: ["
		for tag in range(len(contactInfo["tags"])):
			stream += "\"" + contactInfo["tags"][tag] + "\""
			if tag != len(contactInfo["tags"]) - 1:
				stream += ", "
		stream += "] "
	if "address" in keys:
		address = contactInfo["address"]
		addressKeys = address.keys()
		stream += ", [\"address\"]: { "
		firstAttribute = True
		if "street" in addressKeys:
			if not firstAttribute:
				stream += ", "
			stream += "[\"street\"]: " + address["street"]
			firstAttribute = False
		if "city" in addressKeys:
			if not firstAttribute:
				stream += ", "
			stream += "[\"city\"]: " + address["city"]
			firstAttribute = False
		if "state" in addressKeys:
			if not firstAttribute:
				stream += ", "
			stream += "[\"state\"]: " + address["state"]
			firstAttribute = False
		if "zip" in addressKeys:
			if not firstAttribute:
				stream += ", "
			stream += "[\"zip\"]: " + address["zip"]
			firstAttribute = False
		stream += " } "
	stream += "}"
	return stream

def contactExport(contactDb, contactTag):
	entries = contactSearchTag(contactDb, contactTag)
	stream = "{ "
	firstAttribute = True
	for key in entries.keys():
		if not firstAttribute:
			stream += ", "
		contactText = contactStringForm(entries[key])
		stream += "[\"" + key + "\"]: " + contactText
	stream += " }"
	return stream

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
				else:
					input()
			case "7":
				contactsShown = contactShowAll(contacts)
				if not contactsShown:
					input("Contacts failed to show.")
				else:
					input()
			case "8":
				input()
			case "9":
				input()

mainMenu()