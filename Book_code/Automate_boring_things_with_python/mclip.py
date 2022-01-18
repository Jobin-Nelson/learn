# multi-clipboard program 
from datetime import date
import sys,pyperclip

TEXT = {
    'ad':"Mammaipuredom CS nagar - 24 vaddy kollam.",
    'age': f"{date.today().year - 1997}",
    'email' : "jobinnelson369@gmail.com",
    'us' : "k3rn3l_p4n1c"
}

if len(sys.argv) < 2:
    print("Usage : mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1] # First command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for {} copied to clipboard.".format(keyphrase))
else:
    print("There is no text for " + keyphrase)