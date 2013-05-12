open_text_file = open("BEFORE.txt", "r")
List = open_text_file.read().split('\n')
open_text_file.close()

def isForMoxie(word):
    if (7 > len(word) > 1):
        return True
    else:
        return False

temp = filter(isForMoxie, List)

result =[]

for item in temp:
    result.append(item)

with open('AFTER.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(result))



print (len(result))
