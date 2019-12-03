import string

def isPunc(s):
    if (s in string.punctuation):
        return True
    else:
        return False

def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

target = open("FifaClean5.txt", 'wb')
big_comment = []

with open('Fifa5.txt', 'r') as myfile:

    lines = myfile.readlines()
myfile.close()

for content in lines:
    content = content.split()
    new_list = []
    # remove all the usernames
    for i in content:
        if (":" in i):
            content.pop(content.index(i))
        for j in i:
            if ((not (isEnglish(j))) or (isPunc(j))):
                i = i.replace(j,'')
        
        new_list.append(i)
        target.write((i+' ').encode())
    target.write(('\n').encode())

target.close()

