lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Text=str(input("Enter text for decryption:"))
Text=Text.lower()
for z in range(26):
    Textcoded=''
    for x in range(len(Text)):
        if Text[x] in lowercase:
            Textcoded=Textcoded+(lowercase[(lowercase.index(Text[x]))+26-z])
        if Text[x]==' ':
            Textcoded=Textcoded+' '
    print(Textcoded)
