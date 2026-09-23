# Dictionary til oversættelse fra bogstaver til morsekode
morseCode = {'a':'.-'
    ,'b':'-...'
    ,'c':'-.-.'
    ,'d':'-..'
    ,'e':'.'
    ,'f':'..-.'
    ,'g':'--.'
    ,'h':'....'
    ,'i':'..'
    ,'j':'.---'
    ,'k':'-.-'
    ,'l':'.-..'
    ,'m':'--'
    ,'n':'-.'
    ,'o':'---'
    ,'p':'.--.'
    ,'q':'--.-'
    ,'r':'.-.'
    ,'s':'...'
    ,'t':'-'
    ,'u':'..-'
    ,'v':'...-'
    ,'w':'.--'
    ,'x':'-..-'
    ,'y':'-.--'
    ,'z':'--..'
    ,'æ':'.-.-'
    ,'ø':'---.'
    ,'å':'.--.-'}

# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCodeReverse = {'.-':'a',
    '-...':'b',
    '-.-.':'c',
    '-..':'d',
    '.':'e',
    '..-.':'f',
    '--.':'g',
    '....':'h',
    '..':'i',
    '.---':'j',
    '-.-':'k',
    '.-..':'l'
    ,'--':'m',
    '-.':'n',
    '---':'o',
    '.--.':'p',
    '--.-':'q',
    '.-.':'r',
    '...':'s',
    '-':'t',
    '..-':'u',
    '...-':'v',
    '.--':'w',
    '-..-':'x',
    '-.--':'y',
    '--..':'z',
    '.-.-':'æ',
    '---.':'ø',
    '.--.-':'å',}

# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    if letter in code:
        return code[letter]
print(translate('a', morseCode))

# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    pass

# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    pass