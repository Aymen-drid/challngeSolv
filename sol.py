import base64

c = "F2GwTSwgoDMdJICwnrz=";

def rot_n(text, shift):
    rotate = []
    for char in text:
        if 'a' <= char <= 'z': 
            rotate.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  
            rotate.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            rotate.append(char) 
    return ''.join(rotate)
# try all the possib then decide the flag by the value ;
for n in range(26):
    rot = rot_n(c, n)

    try:
        b = base64.b64decode(rot).decode('utf-8')
        print( b)
    except Exception as e:
        print("error", e)
