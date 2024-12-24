from  itertools import product
import string
minlen=3
maxlen=3
counter=0
charater=string.digits

file_open=open("wordlist.txt",'w')
for i in range(minlen,maxlen+1):
    for j in product(charater,repeat=i):
        
            word="".join(j)
            file_open.write(word)
            file_open.write('\n')
            counter+=1
print("wordlist of {} password created".format(counter))