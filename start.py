import csv
import fileinput
import time
import sys
# time at the start of program is noted
import csv
import math
word=[]
french=[]
nonword=[]

st = time.process_time()


f = open("find_words.txt")
findword=csv.reader(f,delimiter=',')

d= open("french_dictionary.csv")
file=csv.reader(d,delimiter=',')
#--------------------------result csv and whole dictionary making -------------------------
def create_Result():
    result= open('result_new.csv', 'w+',newline='')
    writer = csv.writer(result)

    whole_dict={}

    for word in findword:
            #print(word)
            re = []
            for i in file:
                #print(i)
                if (str(word[0])==str(i[0])):
                   re.append(str(word[0]))
                   re.append(str(i[1]))
                   whole_dict[word[0]]=str(i[1])
                   writer.writerow(re)
                   break
    return  whole_dict

#print(whole_dict)


#---------------copyin a file to new directory-----------------------------------

def replace(line):
    whole =""
    for i in line.split():
        c = open("result_new.csv")
        change = csv.reader(c, delimiter=',')
        for character in change:
            if i == str(character[0]):
                french.append(character[1])
                word.append(character[0])
                whole=whole+str(character[1])+" "
                c.close()
                break
        else:
           whole= whole+str(i)+" "
    #print(whole)
    return whole


whole_dict=create_Result()

with open('t8.shakespeare.txt', mode='rt') as f:
    with open('t8.shakespeare.translated.txt', mode="wt") as g:
        for line in f:
            a=replace(line)
            g.write(str(a)+"\n")



#-------------------------------------count no.of occurences--------------------------------------

counts=dict()
for wo in word:
    if wo in counts:
            counts[wo] += 1
    else:
            counts[wo] = 1

#print(counts)
sums=0
for k in counts.values():
    sums=k+sums
#print(sums)




with open("frequency.csv",'w+') as per:
   writer=csv.writer(per)
   per.write("English word,French word,Frequency\n\n")
   for (k,j) in counts.items():
      a= k,whole_dict[k],j
      writer.writerow(a)


#--------------------time calculating-----------------------
et = time.process_time()
res = et-st
res_min=res/60
frac, whole = math.modf(res_min)
minu=int(whole)
sec=int(frac*60)

timetoprocess="Time to process: "+ str(minu)+" minutes "+str(sec)+" seconds\n"

import os, psutil
process = psutil.Process(os.getpid())
byte= process.memory_info().rss # in bytes
#print(process.memory_info().rss)
mb=byte/(1.024*(10**6))
#print(mb)
memused="Memory used: "+str(mb)+" MB"


#print(type(timetoprocess))
#print(type(memused))
with open("performance.txt",'w+') as t:
    t.write(timetoprocess)
    t.write(memused)
