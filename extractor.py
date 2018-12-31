#! python3
# extractor.py - an email and phone number extractor

import re, pyperclip

# for extracting emails

text = pyperclip.paste()

emailRegex = re.compile(r'(\S*@\S*\.\S*)', re.I)
emailsFound = emailRegex.findall(text)

formatted_email = '\n'.join(emailsFound)
pyperclip.copy(formatted_email)
if formatted_email:
    print("Emails copied to clipboard")
else:
    print("No emails found")

# for extracting phone numbers (US only)

phoneRegex = re.compile(r'''(
(\+?\d)?        #country code
(\s|\.|-)?      #separator
(\(?\d{3}\)?)  #area code
(\s|\.|-)?      #separator
(\d{3})         #first 3 digits
(\s|\.|-)?      #separator 
(\d{4})         #last 4 digits
(\s*(ext|ext.|x)\s*)? #extension marker
(\d{2,5})?      #extension
)''', re.VERBOSE)

phonesFound = phoneRegex.findall(text)
formatted_phone = []
for each in phonesFound:
    if not each[8]:
        phone_num = '-'.join([each[3], each[5], each[7]])
    else:
        phone_num = '-'.join([each[3], each[5], each[7]]) + " ext. " + each[10]
    formatted_phone.append(phone_num)
pyperclip.copy(formatted_email + '\n' + '\n'.join(formatted_phone))
if formatted_phone:
    print("Phone numbers copied to clipboard")
else:
    print("No phone numbers found")
