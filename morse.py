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
    ,'å':'.--.-'
    ,' ':''}

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
    '.--.-':'å',
    ' ':'',
    '':' '}
# i denne funktion har vi brugt (letter, code) til at gøre alle bogstaver der bliver sat ind til et lille
# bogstav så vorse dic kan aflæse det siden den kun indholder små bogstaver og kan derfor kun aflæse dem.
# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
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
    oversat = ''
    for letter in message:
        oversat += translate(letter, code)+'/'
    return oversat

print (encodeMessage('viktors finger er længere end os', morseCode))

# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    oversat = ''
    message=message.split('/')
    for letter in message:
        oversat += translate(letter, code)
    return oversat


print(decodeMessage('...-/../-.-/-/---/.-./...//..-./../-./--././.-.//./.-.//.-../.-.-/-./--././.-././/./-./-..//---/.../', morseCodeReverse))




