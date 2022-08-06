# Import required libraries
import json 
import re 

# Define function to classify email type: "Human" and "Non-Human"
def email_type(email):
    emailSplit = email.split('@')
    if len(emailSplit[0].split('.'))>1 and len(emailSplit[0])>8:
       EmailType="Human"
    else:
        EmailType="Non-Human"
    return EmailType

#  Define function to find all emails from txt file and save it in the Nested JSON.
def outputjson(file):
    textfile = file.read().decode('utf-8') # read the input txt file
    requiredEmails= re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",textfile) #find all matching emails using regex.
    out_dict = {}  # initialize dictionary 
    for email in requiredEmails:
        out_dict[email]={}
        out_dict[email]['Ocuurance']= requiredEmails.count(email)
        out_dict[email]['EmailType'] = email_type(email)

# Convert above the python dictionary into a JSON   
    with open('result.json', 'w') as jsonFile:
        json.dump(out_dict,jsonFile,indent=4)
    return out_dict

# main
if __name__ == "__main__":
    input = 'websiteData.txt' # Input txt file
    file = open(input,'rb')
    outputjson(file)