from ics import Calendar
import requests

url = "https://outlook.office365.com/owa/calendar/d7749e57c7964bc1ae8406ac11ff6f10@edu.devinci.fr/8c71d34af3f849e0b1a6dfc66c17d87714175672858623324700/calendar.ics"
c = Calendar(requests.get(url).text)
event=str(c.events)
disallowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZéàè': ’+'`-?_&{.<[]>"
for character in disallowed_characters:
	event = event.replace(character, "")

#event=filter(str.isalpha,c.events)
L=event.split(",")
j=0
save=""
for element in L:
    i=0
    val=False
    while not val:
        if element[i:i+2]=="20":
            val=True
            L[j]=element[i:i+12]
        else:
            i+=1
    j+=1

L.sort()
N=[int(L[1])]
for i in range(1,len(L)):
    if (L[i][5:8]!=L[i-1][5:8]):
        N=N+[int(L[i])]
print(N)