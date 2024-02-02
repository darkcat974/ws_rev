import sys

def change_hex(c):
    if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
        match c:
            case 'a':
                return 0x80;
            case 'A':
                return 0x80;
            case 'b':
                return 0x81;
            case 'B':
                return 0x81;
            case 'c':
                return 0x82;
            case 'C':
                return 0x82;
            case 'd':
                return 0x83;
            case 'D':
                return 0x83;
            case 'e':
                return 0x84;
            case 'E':
                return 0x84;
            case 'f':
                return 0x85;
            case 'F':
                return 0x85;
            case 'g':
                return 0x86;
            case 'G':
                return 0x86;
            case 'h':
                return 0x87;
            case 'H':
                return 0x87;
            case 'i':
                return 0x88;
            case 'I':
                return 0x88;
            case 'j':
                return 0x89;
            case 'J':
                return 0x89;
            case 'k':
                return 0x8A;
            case 'K':
                return 0x8A;
            case 'l':
                return 0x8B;
            case 'L':
                return 0x8B;
            case 'm':
                return 0x8C;
            case 'M':
                return 0x8C;
            case 'n':
                return 0x8D;
            case 'N':
                return 0x8D;
            case 'o':
                return 0x8E;
            case 'O':
                return 0x8E;
            case 'p':
                return 0x8F;
            case 'P':
                return 0x8F;
            case 'q':
                return 0x90;
            case 'Q':
                return 0x90;
            case 'r':
                return 0x91;
            case 'R':
                return 0x91;
            case 's':
                return 0x92;
            case 'S':
                return 0x92;
            case 't':
                return 0x93;
            case 'T':
                return 0x93;
            case 'u':
                return 0x94;
            case 'U':
                return 0x94;
            case 'v':
                return 0x95;
            case 'V':
                return 0x95;
            case 'w':
                return 0x96;
            case 'W':
                return 0x96;
            case 'x':
                return 0x97;
            case 'X':
                return 0x97;
            case 'y':
                return 0x98;
            case 'Y':
                return 0x98;
            case 'z':
                return 0x99;
            case 'Z':
                return 0x99;

if __name__ == "__main__":
    name = sys.argv[2]
    if name.__len__() > 7:
        print("name to long !")
        exit(84)
    with open(sys.argv[1], "rb+") as f:
        sav = bytearray(f.read()) # This variable is an array containing each bytes of your save file. If you want to modify the byte at address 0x42DE to the value 0x83 for example you can simply use sav[0x42DE] = 0x83 (just like a normal array :-))
        # Write some code here
        if sav[0x2590]:
            for i in name:
                match name.__len__():
                    case 1:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = 0x00
                        sav[0x259A] = 0x00
                        sav[0x259B] = 0x00
                        sav[0x259C] = 0x00
                        sav[0x259D] = 0x00
                        sav[0x259E] = 0x00
                        sav[0x259F] = 0x00
                    case 2:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = 0x00
                        sav[0x259B] = 0x00
                        sav[0x259C] = 0x00
                        sav[0x259D] = 0x00
                        sav[0x259E] = 0x00
                        sav[0x259F] = 0x00
                    case 3:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = change_hex(name[2])
                        sav[0x259B] = 0x00
                        sav[0x259C] = 0x00
                        sav[0x259D] = 0x00
                        sav[0x259E] = 0x00
                    case 4:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = change_hex(name[2])
                        sav[0x259B] = change_hex(name[3])
                        sav[0x259C] = 0x00
                        sav[0x259D] = 0x00
                        sav[0x259E] = 0x00
                    case 5:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = change_hex(name[2])
                        sav[0x259B] = change_hex(name[3])
                        sav[0x259C] = change_hex(name[4])
                        sav[0x259D] = 0x00
                        sav[0x259E] = 0x00
                    case 6:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = change_hex(name[2])
                        sav[0x259B] = change_hex(name[3])
                        sav[0x259C] = change_hex(name[4])
                        sav[0x259D] = change_hex(name[5])
                        sav[0x259E] = 0x00
                    case 7:
                        sav[0x2598] = change_hex(name[0])
                        sav[0x2599] = change_hex(name[1])
                        sav[0x259A] = change_hex(name[2])
                        sav[0x259B] = change_hex(name[3])
                        sav[0x259C] = change_hex(name[4])
                        sav[0x259D] = change_hex(name[5])
                        sav[0x259E] = change_hex(name[6])
        checksum = 0xff
        for i in sav[0x2598:0x3523]:
            checksum -= i
        sav[0x3523] = checksum & 0xff
        f.seek(0, 0)
        f.write(sav)