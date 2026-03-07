import mailparser
import sys
from bs4 import BeautifulSoup

# Make the list of urls into a dictionary so that we can later get a boolean true or false if the Links in the email are malicious
with open('.\links\phishingLinks.txt', 'r', encoding='utf-16') as file: 
    phishLinks = {line.strip() for line in file}

# Make the list of domains into a dictionary ' ' '
with open('.\domains\phishingDomains.txt', 'r', encoding='utf-16') as file:
    phishDomains = {line.strip() for line in file}
    
    
print('Enter your stupid email:\n')
test = sys.stdin.read() # test input for multiple lines


def mail_parser(raw):
    mail = mailparser.parse_from_string(s=raw)
    plain = ""

    # Extracting Sender email ID:
    sender_email = mail.headers.get('From', 'Unknown')
    SenderAddress = sender_email[0][1] # Extract the email part

    plain = " ".join(mail.text_html) if mail.text_html else ""
    return htmlparser(plain, SenderAddress)  # Send to HTML parser


def htmlparser(plain, sender_email):
        soup = BeautifulSoup(plain, "html.parser") # makes the html we extracted from email into a bs4 object
        
        links = [a['href'] for a in soup.find_all('a', href=True)] # extracts all the html links from the bs4 object
        return links, sender_email


def maliciousDetector(listOfLinks:list, senderID:str):
    maliciousCount = 0
    
    # Find if the link in emails are in the known list of malicious links
    if listOfLinks: # check if the list is not empty
        for Link in listOfLinks:
            if Link in phishLinks:
                maliciousCount +=1
    else:
        return 'ERROR - No Links detected' 
    
    if len(senderID) > 0: # check if the string is not empty
        # Extract the domain of the sender email
        if '@' in senderID:
            domain = senderID.split('@')[1]
        else:
            domain = None
            
        # Determine if the domain is malicious by comparing them with a dictionary of malicious domains
        if domain in phishDomains:
            maliciousCount +=1
    else:
        return 'ERROR - NO Sender email detected'
    
    
    if maliciousCount > 0:
        return 'Unsafe'
    else:
        return 'Safe but always proceed with caution'
    

Links, sender_email = mail_parser(test)

print(f'Links: \n{Links} \n\n\n\n\n\n\n\n \n Sender: \n{sender_email}')

print('\n' + maliciousDetector(Links,sender_email))