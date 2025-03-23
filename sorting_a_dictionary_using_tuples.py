#Module 5
#Chapter 10 sorting a dictionary using tuples
#eS 3/22/25
#CIT-95 spring25

fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'

fhand = open(fname)

many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) +1

#FIND THE TOP 5 WORD BY FREQUENCY
tmp = dict()
newlist = list()
for k, v in many.items():
    tup = (v, k)
    newlist.append(tup)
cool = sorted(newlist, reverse=True)

for v, k in cool[:5] :
    print(k, v)