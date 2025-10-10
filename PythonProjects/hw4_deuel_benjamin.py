import re
import time

def problem1():
	dates_text = "Important dates: - Project due: 2024-03-15 - Meeting on: 12/25/2024 - Holiday: July 4, 2025"
	pattern_iso = r"(\d{4})-(\d{2})-(\d{2})"
	iso_dates = re.findall(pattern_iso, dates_text)
	
	emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
	pattern_email = r"(?P<user>[\w\d._ ]+)\@(?P<domain>[\w\d._]+\.[\w\d._]+)\b" # Use (?P<name>...) syntax
	email_parts = [{"user": x.group("user"), "domain": x.group("domain")} for x in re.finditer(pattern_email, emails_text)]
	
	phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
	pattern_phone = r"\(?(\d{3})\)?[ -]?(\d{3}[ -]?\d{4})"
	phone_numbers = [(x.group(1), x.group(2)) for x in re.finditer(pattern_phone, phones_text)]
	
	repeated_text = "The the quick brown fox jumped over the the lazy dog"
	pattern_repeated = r"(\w+) *(?:\1 *)+"
	repeated_words = [x for x in re.findall(pattern_repeated, repeated_text)] # List of repeated words (just the word, not the duplicate)
	
	return { 'iso_dates': iso_dates, 'email_parts': email_parts, 'phone_numbers': phone_numbers, 'repeated_words': repeated_words }

def problem2():
	files_text = "Documents: report.pdf, notes.txt, presentation.pptx\nImages: photo.jpg, diagram.png, icon.gif, picture.jpeg\nCode: script.py, program.java, style.css"
	pattern_images = r"\b([\w_]+)\.(jpg|jpeg|png|gif)[\n\b, ]"
	image_files = [(x.group(1), x.group(2)) for x in re.finditer(pattern_images, files_text)]
	
	mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
	pattern_dates = r"(?:\d{4}-\d{2}-\d{2})|(?:\d{2}/\d{2}/\d{4})|(?:(?:[Jj]an(?:uary)?|[Ff]eb(?:uary)?|[Mm]ar(?:ch)?|[Aa]pr(?:il)?|[Mm]ay|[Jj]une?|[Jj]uly?|[Aa]ug(?:ust)?|[Ss]ep(?:tember)?|[Oo]ct(?:ober)?|[Nn]ov(?:ember)?|[Dd]ec(?:ember)?) \d{2},? \d{4})" # Match ISO, US, and text formats
	all_dates = [x for x in re.findall(pattern_dates, mixed_dates)]
	
	prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
	pattern_prices = r"(?:[$€£]|USD )\d+(?:.\d+)?|\d+(?:.\d+)?(?: dollars)?"
	prices = [x for x in re.findall(pattern_prices, prices_text)]
	
	code_text = "We use Python for data science, Java for enterprise apps,\nJavaScript or JS for web development, and C++ or CPP for systems."
	pattern_langs = r"[Pp]ython|[Jj]ava(?:[Ss]cript)?|[Jj][Ss]|[Cc](?:\+|[Pp]){1,2}"
	languages = [x for x in re.findall(pattern_langs, code_text)]
	
	return { 'image_files': image_files, 'all_dates': all_dates, 'prices': prices, 'languages': languages }

def problem3():
	"""
	Practice with findall() and finditer() methods.
	"""
	log_text = """
	[2024-03-15 10:30:45] INFO: Server started on port 8080
	[2024-03-15 10:31:02] ERROR: Connection failed to database
	[2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
	[2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
	[2024-03-15 10:32:30] ERROR: File not found: config.yml
	"""
	# a) Use findall() to extract all timestamps
	# TODO: Pattern for timestamp [YYYY-MM-DD HH:MM:SS]
	pattern_timestamp = r""
	# TODO: Extract all timestamps
	timestamps = [] # Using findall()
	# b) Use findall() with groups to extract log levels and messages
	# TODO: Pattern with groups for log level and message
	pattern_log = r"" # Capture level and message separately
	# TODO: Extract tuples of (level, message)
	log_entries = [] # List of tuples using findall()
	# c) Use finditer() to get positions of all IP addresses
	# TODO: Pattern for IP addresses
	pattern_ip = r"" # Match IPv4 addresses
	# TODO: Find all IP addresses with their positions
	ip_addresses = [] # List of dicts with 'ip', 'start', 'end' keys
	# d) Use finditer() to create a highlighted version of errors
	# TODO: Replace ERROR entries with **ERROR** (highlighted)
	highlighted_log = log_text # Modified version with highlighted errors
	# TODO: Create function to highlight all ERROR entries
	def highlight_errors(text):
		"""
		Surround all ERROR log entries with ** markers.
		Return modified text.
		"""
		# Your implementation here
		pass
	highlighted_log = highlight_errors(log_text)
	return { 'timestamps': timestamps, 'log_entries': log_entries, 'ip_addresses': ip_addresses, 'highlighted_log': highlighted_log }

try:
	input(problem2())
except Exception as e:
	input(e)

def problem4():
	"""
	Practice text transformation using re.sub().
	"""
	# a) Clean and format phone numbers
	messy_phones = """
	Contact list:
	- John: 555.123.4567
	- Jane: (555) 234-5678
	- Bob: 555 345 6789
	- Alice: 5554567890
	"""
	
	# TODO: Standardize all phone numbers to format: (555) 123-4567
	def standardize_phones(text):
		"""
		Convert all phone number formats to (XXX) XXX-XXXX.
		week6-homework.md 2025-09-22
		6 / 12
		"""
		# Your pattern and substitution here
		pattern = r""
		replacement = r""
		return re.sub(pattern, replacement, text)
	
	cleaned_phones = standardize_phones(messy_phones)
	# b) Redact sensitive information
	sensitive_text = """
	Customer: John Doe
	SSN: 123-45-6789
	Credit Card: 4532-1234-5678-9012
	Email: john.doe@email.com
	Phone: (555) 123-4567
	"""
	
	# TODO: Redact SSN and Credit Card numbers
	def redact_sensitive(text):
		"""
		Replace SSN with XXX-XX-XXXX and
		Credit Card with XXXX-XXXX-XXXX-XXXX.
		"""
		# Your implementation here
		return text # Modified text
	
	redacted_text = redact_sensitive(sensitive_text)
	# c) Convert markdown links to HTML
	markdown_text = """
	Check out [Google](https://google.com) for search.
	Visit [GitHub](https://github.com) for code.
	Read documentation at [Python Docs](https://docs.python.org).
	"""
	
	# TODO: Convert [text](url) to <a href="url">text</a>
	def markdown_to_html(text):
		"""
		Convert markdown links to HTML anchor tags.
		"""
		# Your pattern and substitution here
		return text # Modified text
	
	html_text = markdown_to_html(markdown_text)
	# d) Implement a simple template system
	template = """
	Dear {name},
	Your order #{order_id} for {product} has been shipped.
	Tracking number: {tracking}
	"""
	values = {
	'name': 'John Smith',
	'order_id': '12345',
	'product': 'Python Book',
	'tracking': 'TRK789XYZ'
	}
	
	# TODO: Replace {key} with corresponding values
	def fill_template(template, values):
		"""
		Replace all {key} placeholders with values from dictionary.
		"""
		# Your implementation here
		return template # Filled template
	
	filled_template = fill_template(template, values)
	return { 'cleaned_phones': cleaned_phones, 'redacted_text': redacted_text, 'html_text': html_text, 'filled_template': filled_template }

def problem5():
	"""
	Use compiled patterns for efficiency and clarity.
	"""
	
	# Create a class to hold compiled patterns
	class PatternLibrary:
		"""
		Library of compiled regex patterns for common use cases.
		"""
		# TODO: Compile these patterns
		# Use re.IGNORECASE, re.MULTILINE, re.VERBOSE as appropriate
		# a) Email validation pattern (case insensitive)
		EMAIL = None # re.compile(...)
		# b) URL pattern (with optional protocol)
		URL = None # re.compile(...)
		# c) US ZIP code (5 digits or 5+4 format)
		ZIP_CODE = None # re.compile(...)
		# d) Strong password (verbose pattern with comments)
		# Requirements: 8+ chars, uppercase, lowercase, digit, special char
		PASSWORD = None # re.compile(..., re.VERBOSE)
		# e) Credit card number (with spaces or dashes optional)
		CREDIT_CARD = None # re.compile(...)
	
	# Test your patterns
	test_data = {
	'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
	'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
	'zips': ['12345', '12345-6789', '1234', '123456'],
	'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
	'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456',
	'1234567890123456']
	}
	# TODO: Validate each item using your compiled patterns
	validation_results = {
	'emails': [], # List of booleans
	'urls': [], # List of booleans
	'zips': [], # List of booleans
	'passwords': [], # List of booleans
	'cards': [] # List of booleans
	}
	# TODO: Implement validation logic
	# For each category, check if pattern matches
	return validation_results

def problem6():
	"""
	Create a log file analyzer using regex.
	"""
	# Sample web server log (Apache/Nginx format)
	log_data = """
	192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200
	5234
	192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401
	234
	192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1"
	304 0
	192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1"
	403 0
	192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200
	week6-homework.md 2025-09-22
	9 / 12
	1234
	192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200
	15234
	192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
	"""
	# TODO: Parse log entries to extract:
	# - IP address
	# - Timestamp
	# - HTTP method (GET, POST, etc.)
	# - URL path
	# - Status code
	# - Response size
	# a) Create pattern to parse log lines
	log_pattern = r"" # Your comprehensive pattern here
	# b) Extract all log entries as structured data
	parsed_logs = [] # List of dictionaries
	# c) Analyze the logs
	analysis = {
	'total_requests': 0,
	'unique_ips': [],
	'error_count': 0, # 4xx and 5xx status codes
	'total_bytes': 0,
	'most_requested_path': '',
	'methods_used': [] # Unique HTTP methods
	}
	# TODO: Implement log parsing and analysis
	return {
	'parsed_logs': parsed_logs,
	'analysis': analysis
	}

# Add this at the bottom of your file to test all problems
if __name__ == "__main__":
	print("Problem 1 Results:")
	print(problem1())
	print("\nProblem 2 Results:")
	print(problem2())
	print("\nProblem 3 Results:")
	print(problem3())
	print("\nProblem 4 Results:")
	print(problem4())
	print("\nProblem 5 Results:")
	print(problem5())
	print("\nProblem 6 Results:")
	print(problem6())
	print("\nProblem 7 Results:")
	print(problem7())
	# Uncomment if attempting bonus
	# print("\nBonus Challenge Results:")
	# print(bonus_challenge())