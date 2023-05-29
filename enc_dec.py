alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def encode(msg, shift):
    l_msg = len(msg)
    l_alp = len(alphabet)-1
    en_msg = ""

    for i in range(0, l_msg):
        letter = msg[i].lower()

        if alphabet.count(letter) > 0:
            index = alphabet.index(letter) + shift
            if index < l_alp:
                if msg[i].islower():
                  en_msg = en_msg + alphabet[index]

                else:
                    en_msg = en_msg + alphabet[index].upper()

            elif index >= l_alp:
                index = index - l_alp
                if msg[i].islower():
                    en_msg = en_msg + alphabet[index]

                else:
                    en_msg = en_msg + alphabet[index].upper()

        else:
            en_msg = en_msg + letter
            continue
    return en_msg

def decode(msg, shift):
    l_msg = len(msg)
    l_alp = len(alphabet) -1
    en_msg = ""

    for i in range(0, l_msg):
        letter = msg[i].lower()

        if alphabet.count(letter) > 0:
            index = alphabet.index(letter) - shift
            if index >= 0:
                if msg[i].islower():
                    en_msg = en_msg + alphabet[index]

                else:
                    en_msg = en_msg + alphabet[index].upper()

            elif index < 0:
                index = l_alp + index
                if msg[i].islower():
                    en_msg = en_msg + alphabet[index]

                else:
                    en_msg = en_msg + alphabet[index].upper()

        else:
            en_msg = en_msg + letter
            continue
    return en_msg