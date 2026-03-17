# PhishingDay
A phishing email Analyzer  {WIP} 

#### ** This is by no means meant to be used as a service, it is proof of concept and a fun project that I wanted to do.**
#### ** It will not protect you from phishing attempts. **

# Requirements:
```pip install mail-parser beautifulsoup4```

# How does it function?
- By converting a list of known suspicious domains (emails) and links into a dictionary, we are able to convert it into a dictionary
- We then are able to extract the html of an email and the sender domain using mail-parser.py | ```pip install mail-parser```
- Then we parse through the HTML of the email to extract links using bs4 | ```pip install beautifulsoup4```
- We then take the list of links and the sender email/ID and check if they are present in the list of known suspicious links or domains
- We then output if the email is Safe or Unsafe depending on if the program detects

# Credit: 
## The list of known suspicious links and domains was taken from [Phishing-Database](https://github.com/Phishing-Database/Phishing.Database)
### Here is their License: 
MIT License

Copyright (c) 2018-2025 Mitchell Krog - @mitchellkrogza

Copyright (c) 2018-2025 Nissar Chababy - @funilrys

Copyright (c) 2018-2025 Phishing.Database Contributors - @Phishing-Database

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
