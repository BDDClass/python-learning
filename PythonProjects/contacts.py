contact = {
    "firstName" : "Example",
    "lastName" : "Example",
    "phoneNumber" : "555-555-5555",
    "email" : "example@example.ex",
    "tags" : ["tag1", "tag2", "tag3"],
    "dateMade" : "5-24-2020",
    "dateModified" : "5-24-2020",
    "address" : {
        "street" : "1234 Example St."
        "city" : "Fort Wayne",
        "state" : "Ohio",
        "zip" : 44444
    }
}

lettersUpper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lettersLower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

#returns true if only valid chars are found
def charWhitelist(txt, exceptions=[]):
    for ch in txt:
        if not (ch in lettersLower or ch in lettersUpper or ch in numbers or ch in exceptions):
            return False
    return True

def isIntegral(txt):
    for ch in txt:
        if not ch in numbers:
            return False
    return True

def isPhoneNumber(txt):
    #

def isEmail(txt):
    #

def isDate(txt):
    #

def isStreet(txt):
    #