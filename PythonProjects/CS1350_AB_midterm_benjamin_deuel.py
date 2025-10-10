import re
import numpy as np

def add_item(cart, item_name, price, quantity):
    if price <= 0 or quantity < 0:
        return False
    if item_name in cart:
        if cart[item_name][0] == price:
            cart[item_name][1] += quantity
        else:
            return False
    else:
        cart.update({item_name: [price, quantity]})
    return True

def calculate_total(cart):
    total = 0
    for item in cart:
        total += cart[item][0] * cart[item][1]
    return total

def apply_discount(cart, percent):
    if percent <= 0.0 or percent >= 100.0:
        return False
    for item in cart:
        cart[item][0] *= 1.0 - (percent / 100.0)
    return True

'''
if __name__ == "__main__":
    cart = {}
    print(add_item(cart, "Milk", 3.5, 2))
    print(add_item(cart, "Eggs", -1.0, 1))
    print(add_item(cart, "Bread", 2.0, 3))
    print(f"Total: {calculate_total(cart):.2f}")
    print(apply_discount(cart, 20))
    print(f"Total after discount: {calculate_total(cart):.2f}")
'''

def clean_message(txt):
    txt = " ".join(txt.lower().split())
    while txt[-1] in [".", "?", "!"]:
        txt = txt[:-1]
    return txt

def expand_abbreviations(txt):
    abbrevPairs = [["u", "you"], ["ur", "your"], ["r", "are"], ["thx", "thanks"]]
    splitTxt = txt.split()
    for i, t in enumerate(splitTxt):
        for a in abbrevPairs:
            if t == a[0]:
                splitTxt[i] = a[1]
    return " ".join(splitTxt)

def count_words(txt):
    words = {}
    for word in txt.split():
        if word in words:
            words[word] += 1
        else:
            words.update({word: 1})
    return words

def censor_numbers(txt):
    splitTxt = txt.split()
    for i, t in enumerate(splitTxt):
        if t.isdigit():
            splitTxt[i] = "XXX"
    return " ".join(splitTxt)

'''
if __name__ == "__main__":
    msg1 = "   Hello WORLD!!!"
    print(f"Original: '{msg1}'\nCleaned: '{clean_message(msg1)}'")
    
    msg2 = "thx for ur help u r awesome"
    print(f"Original: '{msg2}'\nCleaned: '{expand_abbreviations(msg2)}'")
    
    msg3 = "hello world hello python world"
    print(f"Original: '{msg3}'\nWord count: '{count_words(msg3)}'")
    
    msg4 = "Call me at 5551234567 or 999888777"
    print(f"Original: '{msg4}'\nCleaned: '{censor_numbers(msg4)}'")
'''

def validate_password(txt):
    txtLen = len(txt)
    if txtLen < 8 or txtLen > 20:
        return False
    if re.search(r"\d", txt) == None:
        return False
    if re.search(r"[A-Z]", txt) == None:
        return False
    return True

def extract_hashtags(txt):
    return re.findall(r"#[\w\d]+", txt)

def validate_time(txt):
    mat = re.search(r"^(\d{2}):(\d{2})$", txt)
    if mat == None:
        return False
    hour = int(mat.group(1))
    minute = int(mat.group(2))
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        return False
    return True

def find_dates(txt):
    return re.findall(r"\d{2}[\/-]\d{2}[\/-]\d{4}", txt)

'''
if __name__ == "__main__":
    passwords = ["Pass1234", "weakpass", "NoDigits!", "12345678", "GoodPass99"]
    for p in passwords:
        print(f"Password '{p}': {validate_password(p)}")
    
    txt = "Check out #Python3 and #MachineLearning tutorials! #AI #100DaysOfCode"
    print(f"Hashtags found: {extract_hashtags(txt)}")
    
    times = ["14:30", "09:45", "25:00", "12:60", "00:00"]
    for t in times:
        print(f"Time '{t}': {validate_time(t)}")
    
    txt = "I was born on 12/25/1999 and graduated on 06-15-2021."
    print(f"Dates found: {find_dates(txt)}")
'''

def create_score_array(num_students, num_exams):
    return np.random.randint(60, 101, size=(num_students, num_exams))

def find_struggling_students(scores, threshold):
    avgs = scores.mean(axis=1)
    return avgs < threshold

def curve_scores(scores, bonus):
    return np.minimum(scores + bonus, 100)

def get_exam_statistics(scores):
    exams = {}
    for i, exam in enumerate(scores.T):
        exams.update({f"exam{i+1}": {"mean": exam.mean(), "min": exam.min(), "max": exam.max()}})
    return exams

'''
if __name__ == "__main__":
    scores = create_score_array(6, 4)
    print(f"Original scores: {scores}")
    
    struggling = find_struggling_students(scores, 75)
    print(f"Struggling students: {struggling}")
    
    print(f"Curved scores: {curve_scores(scores, 5)}")
    
    stats = get_exam_statistics(scores)
    for exam, data in stats.items():
        print(f"{exam}: {data}")
'''

def add_student_to_club(clubs, clubName, student):
    if clubName in clubs:
        clubs[clubName].add(student)
    else:
        clubs.update({clubName: set({student})})

def get_students_in_multiple_clubs(clubs):
    students = {}
    for club in clubs:
        for name in clubs[club]:
            if name in students:
                students[name] += 1
            else:
                students.update({name: 1})
    studentSet = set()
    for student in students:
        if students[student] > 1:
            studentSet.add(student)
    return studentSet

def find_exclusive_members(clubs, club1, club2):
    if not club1 in clubs or not club2 in clubs:
        return set()
    return clubs[club1] - clubs[club2]

def merge_clubs(clubs, oldClub, newClub):
    if not oldClub in clubs:
        return False
    clubs[newClub] |= clubs[oldClub]
    del clubs[oldClub]
    return True

'''
if __name__ == "__main__":
    clubs = {}
    add_student_to_club(clubs, "Math", "Alice")
    add_student_to_club(clubs, "Math", "Bob")
    add_student_to_club(clubs, "Science", "Alice")
    add_student_to_club(clubs, "Science", "Charlie")
    add_student_to_club(clubs, "Art", "David")
    print(f"Clubs: {clubs}")
    print(f"In multiple clubs: {get_students_in_multiple_clubs(clubs)}")
    print(f"Math only: {find_exclusive_members(clubs, "Math", "Science")}")
    add_student_to_club(clubs, "Photography", "Eve")
    print(merge_clubs(clubs, "Photography", "Art"))
    print(f"Clubs: {clubs}")
'''