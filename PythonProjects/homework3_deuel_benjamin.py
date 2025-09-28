import re

def format_receipt(items, prices, quantities):
	text = "="*40+"\nItem Quantity Price\n"+"="*40
	itemCount = min(len(items), len(prices), len(quantities))
	for i in range(itemCount):
		text += f"\n{items[i].capitalize():<20} x{str(quantities[i]):^5} ${prices[i]*quantities[i]:8.2f}"
	total = 0.0
	for item in zip(quantities[:itemCount], prices[:itemCount]):
		total += item[0] * item[1]
	text += "\n"+"="*40+f"\nTotal: ${total:.2f}\n"+"="*40
	return text

def process_user_data(raw_data):
	rawKeys = raw_data.keys()
	
	name = "None"
	if "name" in rawKeys:
		name = " ".join(raw_data["name"].strip().split()).title()
	email = "None"
	if "email" in rawKeys:
		email = "".join(raw_data["email"].strip().split()).lower()
	phone = "None"
	if "phone" in rawKeys:
		phone = "".join(raw_data["phone"].strip().split()).lower()
		mat = re.search(r"^[^\d]*(\d{3})[^\d]*(\d{3})[^\d]*(\d{4})[^\d]*$", phone)
		phone = mat.group(1) + mat.group(2) + mat.group(3)
	addr = "None"
	if "address" in rawKeys:
		addr = " ".join(raw_data["address"].strip().split()).title()
	
	username = "_".join(name.split()).lower()
	return dict({"name": name, "email": email, "phone": phone, "address": addr, "username": username})

def analyze_text(text):
	totalChar = len(text.replace(" ", ""))
	totalWords = len(text.split())
	totalLines = len(text.split("\n"))
	averageWordLength = sum([len(x) for x in text.split()]) / len(text.split())
	commonWord = 
	longestLine = 
	lineWordCount = [len(x.strip().split()) for x in text.strip().split("\n")]
	capitalCount = sum([x.isupper() for x in text.strip().split("\n")])
	questionCount = sum([x.endswith("?") for x in text.strip().split()])
	exclamationCount = sum([x.endswith("!") for x in text.strip().split()])
	"""
	Perform comprehensive text analysis using string methods.
	Args:
	text: Multi-line string of text
	Returns:
	dict: Analysis results containing:
	- 'total_chars': Total character count
	- 'total_words': Total word count
	- 'total_lines': Number of lines
	- 'avg_word_length': Average word length (rounded to 2 decimal)
	- 'most_common_word': Most frequently used word (case-insensitive)
	- 'longest_line': The longest line in the text
	- 'words_per_line': List of word counts per line
	- 'capitalized_sentences': Number of sentences starting with capital
	- 'questions': Number of sentences ending with '?'
	- 'exclamations': Number of sentences ending with '!'
	Example:
	>>> text = '''Hello world! How are you?
	... This is a test. Another line here!'''
	>>> result = analyze_text(text)
	>>> result['total_words']
	11
	>>> result['questions']
	1
	"""
	# Your code here
	pass

def find_patterns(text):
	"""
	Find basic patterns in text using regex.
	Args:
	text: String to search
	Returns:
	dict: Found patterns:
	- 'integers': List of all integers
	- 'decimals': List of all decimal numbers
	- 'words_with_digits': Words containing digits
	- 'capitalized_words': Words starting with capital letter
	- 'all_caps_words': Words in all capitals (min 2 chars)
	- 'repeated_chars': Words with repeated characters (aa, ll, etc.)
	Example:
	>>> text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
	>>> result = find_patterns(text)
	>>> result['integers']
	['25']
	>>> result['decimals']
	['3.14']
	>>> result['all_caps_words']
	['HELLO']
	>>> result['words_with_digits']
	['W0RLD']
	"""
	patterns = {
	'integers': r'', # Fill in pattern
	'decimals': r'', # Fill in pattern
	'words_with_digits': r'', # Fill in pattern
	'capitalized_words': r'', # Fill in pattern
	'all_caps_words': r'', # Fill in pattern
	'repeated_chars': r'' # Fill in pattern
	}
	# Your code here
	pass

def validate_format(input_string, format_type):
	"""
	Validate if input matches specified format using regex.
	Args:
	input_string: String to validate
	format_type: Type of format to check
	Returns:
	tuple: (is_valid: bool, extracted_parts: dict or None)
	Format types:
	- 'phone': (XXX) XXX-XXXX or XXX-XXX-XXXX
	- 'date': MM/DD/YYYY (validate month 01-12, day 01-31)
	- 'time': HH:MM AM/PM or HH:MM (24-hour)
	- 'email': basic email format (username@domain.extension)
	- 'url': http:// or https:// followed by domain
	- 'ssn': XXX-XX-XXXX (just format, not validity)
	For valid inputs, extract parts (area_code, month, hour, etc.)
	Example:
	>>> validate_format("(555) 123-4567", "phone")
	(True, {'area_code': '555', 'prefix': '123', 'line': '4567'})
	>>> validate_format("13/45/2024", "date")
	(False, None)
	"""
	# Define patterns for each format type
	patterns = {
	'phone': r'', # Fill in pattern with groups
	'date': r'', # Fill in pattern with groups
	'time': r'', # Fill in pattern with groups
	'email': r'', # Fill in pattern with groups
	'url': r'', # Fill in pattern with groups
	'ssn': r'' # Fill in pattern with groups
	}
	# Your code here
	pass

def extract_information(text):
	"""
	Extract specific information from unstructured text.
	Args:
	text: Unstructured text containing various information
	Returns:
	dict: Extracted information:
	- 'prices': List of prices (formats: $X.XX, $X,XXX.XX)
	- 'percentages': List of percentages (X% or X.X%)
	- 'years': List of 4-digit years (1900-2099)
	- 'sentences': List of complete sentences (end with . ! or ?)
	- 'questions': List of questions (sentences ending with ?)
	- 'quoted_text': List of text in double quotes
	Example:
	>>> text = 'The price is $19.99 (20% off). "Great deal!" she said.'
	>>> result = extract_information(text)
	>>> result['prices']
	['$19.99']
	>>> result['percentages']
	['20%']
	>>> result['quoted_text']
	['Great deal!']
	"""
	# Your code here
	pass

def clean_text_pipeline(text, operations):
	"""
	Apply a series of cleaning operations using both string methods and regex.
	Args:
	text: Input text to clean
	operations: List of operation names to apply in order
	Operations:
	- 'trim': Remove leading/trailing whitespace
	- 'lowercase': Convert to lowercase
	- 'remove_punctuation': Remove all punctuation
	- 'remove_digits': Remove all digits
	- 'remove_extra_spaces': Replace multiple spaces with single space
	- 'remove_urls': Remove URLs (http/https)
	- 'remove_emails': Remove email addresses
	- 'capitalize_sentences': Capitalize first letter of sentences
	Returns:
	dict: {
	'original': Original text,
	'cleaned': Final cleaned text,
	'steps': List of text after each operation
	}
	Example:
	>>> text = " Hello WORLD! Visit https://example.com "
	>>> ops = ['trim', 'lowercase', 'remove_urls', 'remove_extra_spaces']
	>>> result = clean_text_pipeline(text, ops)
	>>> result['cleaned']
	'hello world! visit'
	"""
	# Your code here
	pass

def smart_replace(text, replacements):
	"""
	Perform intelligent text replacements using patterns.
	Args:
	text: Input text
	replacements: Dict of replacement rules
	Replacement types:
	- 'censor_phone': Replace phone numbers with XXX-XXX-XXXX
	- 'censor_email': Replace email with [EMAIL]
	- 'fix_spacing': Fix spacing around punctuation
	- 'expand_contractions': Expand contractions (don't -> do not)
	- 'number_to_word': Convert single digits to words (1 -> one)
	Returns:
	str: Text with replacements applied
	Example:
	>>> text = "Call me at 555-123-4567. I'm busy."
	>>> rules = {'censor_phone': True, 'expand_contractions': True}
	>>> smart_replace(text, rules)
	'Call me at XXX-XXX-XXXX. I am busy.'
	"""
	# Define contractions dictionary
	contractions = {
	"don't": "do not",
	"won't": "will not",
	"can't": "cannot",
	"I'm": "I am",
	"you're": "you are",
	"it's": "it is",
	"he's": "he is",
	"she's": "she is",
	"we're": "we are",
	"they're": "they are",
	"I've": "I have",
	"you've": "you have",
	"we've": "we have",
	"they've": "they have"
	}
	# Your code here
	pass

def analyze_log_file(log_text):
	"""
	Analyze a simplified log file format using string methods and regex.
	Log format: [YYYY-MM-DD HH:MM:SS] LEVEL: Message
	Example: [2024-01-15 10:30:45] ERROR: Database connection failed
	Args:
	log_text: Multi-line string of log entries
	Returns:
	dict: Analysis results:
	- 'total_entries': Total number of log entries
	- 'error_count': Number of ERROR entries
	- 'warning_count': Number of WARNING entries
	- 'info_count': Number of INFO entries
	- 'dates': List of unique dates (YYYY-MM-DD)
	- 'error_messages': List of ERROR messages only
	- 'time_range': Tuple of (earliest_time, latest_time)
	- 'most_active_hour': Hour with most log entries (0-23)
	Example:
	>>> log = '''[2024-01-15 10:30:45] ERROR: Connection failed
	... [2024-01-15 10:31:00] INFO: Retry attempt 1
	... [2024-01-15 11:00:00] WARNING: High memory usage'''
	>>> result = analyze_log_file(log)
	>>> result['error_count']
	1
	>>> result['dates']
	['2024-01-15']
	"""
	# Your code here
	pass

def run_tests():
	"""Test all functions with sample data."""
	print("="*50)
	print("Testing Part 1: String Methods")
	print("="*50)
	# Test 1.1: Receipt formatting
	items = ["Coffee", "Sandwich"]
	prices = [3.50, 8.99]
	quantities = [2, 1]
	receipt = format_receipt(items, prices, quantities)
	print("Receipt Test:")
	print(receipt)
	# Test 1.2: User data processing
	test_data = {
	'name': ' john DOE ',
	'email': ' JOHN@EXAMPLE.COM ',
	'phone': '(555) 123-4567',
	'address': '123 main street'
	}
	cleaned = process_user_data(test_data)
	print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
	print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
	print("\n" + "="*50)
	print("Testing Part 2: Regular Expressions")
	print("="*50)
	# Test 2.1: Pattern finding
	test_text = "I have 25 apples and 3.14 pies"
	patterns = find_patterns(test_text)
	print(f"Found integers: {patterns.get('integers', [])}")
	print(f"Found decimals: {patterns.get('decimals', [])}")
	# Test 2.2: Format validation
	phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
	print(f"\nPhone validation: {phone_valid}")
	if phone_parts:
		print(f"Extracted parts: {phone_parts}")
	# Test 2.3: Information extraction
	info_text = 'The price is $19.99 (20% off).'
	info = extract_information(info_text)
	print(f"\nPrices found: {info.get('prices', [])}")
	print(f"Percentages found: {info.get('percentages', [])}")
	print("\n" + "="*50)
	print("Testing Part 3: Combined Operations")
	print("="*50)
	# Test 3.1: Cleaning pipeline
	dirty_text = " Hello WORLD! "
	operations = ['trim', 'lowercase', 'remove_extra_spaces']
	cleaned_result = clean_text_pipeline(dirty_text, operations)
	print(f"Original: '{cleaned_result.get('original', '')}'")
	print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
	print("\n" + "="*50)
	print("Testing Part 4: Log Analysis")
	print("="*50)
	# Test 4.1: Log analysis
	sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
	[2024-01-15 10:31:00] INFO: Retry attempt
	[2024-01-15 10:32:00] WARNING: Timeout warning"""
	log_analysis = analyze_log_file(sample_log)
	print(f"Total entries: {log_analysis.get('total_entries', 0)}")
	print(f"Error count: {log_analysis.get('error_count', 0)}")
	print(f"Unique dates: {log_analysis.get('dates', [])}")
	print("\n" + "="*50)
	print("All tests completed!")
	print("="*50)

if __name__ == "__main__":
	run_tests()