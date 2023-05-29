from enc_dec import encode, decode, alphabet

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

choose = ""
en_de = ""
message = []
s_number = ""

print(logo)
while choose != "no" and choose != "N" and choose != "NO" and choose != "n":
    en_de = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n")
    s_number = int(input("Type the shift number:\n"))

    if en_de == "encode":
        msg = encode(message, s_number)
        print(msg)

    elif en_de == "decode":
        print(decode(message, s_number))

    choose = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
