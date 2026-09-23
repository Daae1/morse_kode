# Dictionary til oversættelse fra bogstaver til morsekode
# Vi har valgt at linjeskift efter hver bogstav, for at gøre det mere overskueligt
# Her skriver man først bogstavet så : og hvad den skal oversættes til
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
# Her har vi gjort det samme som overnover, bare i reverse
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
# Her translater den et bogstav fra dictionary om til koden hvis den ikke er der returner den ?
def translate(letter, code):
    letter = letter.lower()
    # det gøre så alle bogstaver er i lowercase
    if letter in code:
        return code[letter]
    else:
        return '?'
print(translate('*', morseCode))

# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):



# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    pass



