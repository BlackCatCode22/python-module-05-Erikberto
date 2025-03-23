#Module 5
#Chapter 9 counting word frequency
#eS 3/22/25
#CIT-95 spring25

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip() #takes white space of right side
    wds = lin.split() #split words in a single lane
    for w in wds:
        #idom: retrieve/create/update counter
        di[w] = di.get(w,0) +1
#print(di)

#now we want to find the most common word
largest = -1
theword = None
for k, v in di.items():
    print(k, v)
    if v > largest:
        largest = v
        theword = k


print(theword,largest)