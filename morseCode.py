MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-','':''}
print("Morse Code Encryptor and decryptor")
print("1.Morse Code - Plain Text(Decryption)")
print("2.Plain Text - Morse Code(Encryption)")
print("Make your choice")
ch = int(input())
if ch == 1:
    morse_code = input("Enter the morse Code: ")
    morse_code += ' '
    plain_text = ''
    stext = ''
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    for i in morse_code:
        if i != " ":
            s =0 
            stext += i
        else:
            s +=1
            if s == 2:
                plain_text += ' '
            else: 
                plain_text +=  key_list[val_list.index(stext)]
                stext = ''
    print(plain_text)
if ch == 2:
    text = input("Enter the Text:")
    ciperText = ''
    for i in text:
        i = i.upper()
        if i != " ":
            ciperText += MORSE_CODE_DICT[i] + " "
        else:
            ciperText += "  "
    print(ciperText)



        

            


