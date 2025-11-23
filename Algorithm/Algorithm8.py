text = input()

result = ""

for i in text:
    
    if 'a' <= i <= 'z':
        result = result + chr(ord(i) - 32)
        
    elif 'A' <= i <= 'Z':
        result = result + chr(ord(i) + 32)
        

print(result)