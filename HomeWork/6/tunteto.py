#A híreket olvasgatva (http://index.hu/belfold/2014/10/28/orban_viktor_itt_a_magyar_nep_beszel/) megakadt a figyelmem az egyik képen: link. Hmm… Vajon mit próbált üzenni a fiatalember? Meg tudjuk fejteni?


def decode(message):
    message = message.split(" ")
    decoded = ""
    for i in message:
        decoded += chr(int(i, 2))
    return decoded

def main():
    print(decode("01111001 01101111 01110101 01110100 01110101 00101110 01100010 01100101 00101111 01100100 01010001 01110111 00110100 01110111 00111001 01010111 01100111 01011000 01100011 01010001"))
    #:D


if __name__=="__main__":
    main()