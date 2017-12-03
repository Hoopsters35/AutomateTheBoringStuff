import re

#See Python-Workspace/SoloLearnLessons/Regular\ Expressions for more in-depth review

#subl method (word_to_replace, string_to_search) on a compiled regex object

#VERBOSE argument at end of the compile constructor of a regex object allows to compile multi-line regex without counting extra spacing
#requites triple quotes at start and end of regex
#to get phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
#other ending arguments include re.DOTALL which will go past any new line characeters when compiling
#without re.DOTALL, the regex will only search up until the first \n
#
#re.IGNORECASE will ignore case throughout the regex - much more convenient than including both styles
#
#to get emails
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+       # username
	@                       # @ symbol
	[a-zA-Z0-9.-]+          # domain name
	(\.[a-zA-Z]{2,4})       # dot-something
	)''', re.VERBOSE)