# Finds phone numbers and email addresses on the clipboard
import pyperclip,re

# regex for phone number 
phone_regex = re.compile(r'\d{10}')

# regex for email addresses
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+]+  # Username
@                 # @ symbol
[a-zA-Z0-9.-]+    # domain name
(\.[a-zA-Z]{2,4}) # dot something
)''',re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

phone_num = '\n'.join(i for i in phone_regex.findall(text))
email = '\n'.join(i[0] for i in email_regex.findall(text))
matches = phone_num + email 

# copy results to clipboard
if len(matches)>0:
    pyperclip.copy(matches)
    print('Copied to clipboard')
    print(matches)
else:
    print('No phone numbers or email addresses found')

    