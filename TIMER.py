import time
import os
import random
import msvcrt as m
one=[]
two=[]
three=[]
four=[]
five=[]
six=[]
seven=[]
eight=[]
nine=[]
def strm(x):
    return str(int(x))+str(x-int(x))[1:4]
def prnt():
    for i in one:
        print(i,end='')
    print('')
    for i in two:
        print(i,end='')
    print('')
    for i in three:
        print(i,end='')
    print('')
    for i in four:
        print(i,end='')
    print('')
    for i in five:
        print(i,end='')
    print('')
    for i in six:
        print(i,end='')
    print('')
    for i in seven:
        print(i,end='')
    print('')
    for i in eight:
        print(i,end='')
    print('')
    for i in nine:
        print(i,end='')
    print('')
def display(i,n):
    if n=='1':
        one[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
        two[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        three[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        four[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
    elif n=='2':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        three[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        four[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        seven[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        eight[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='3':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        three[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        four[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='4':
        one[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        three[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        four[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
    elif n=='0':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        three[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        four[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
        six[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='5':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        three[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        four[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        five[i:i+7]=[' ','_','_','_','_','_','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='6':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        three[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        four[i:i+7]=['|',' ',' ',' ',' ',' ','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='7':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        three[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        four[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ',' ',' ',' ',' ',' ','  ']
    elif n=='8':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        three[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        four[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='9':
        one[i:i+7]=[' ','_','_','_','_',' ','  ']
        two[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        three[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        four[i:i+7]=['|',' ',' ',' ',' ','|','  ']
        five[i:i+7]=[' ','_','_','_','_',' ','  ']
        six[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        seven[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        eight[i:i+7]=[' ',' ',' ',' ',' ','|','  ']
        nine[i:i+7]=[' ','_','_','_','_',' ','  ']
    elif n=='.':
        one[i:i+3]=[' ',' ',' ']
        two[i:i+3]=[' ',' ',' ']
        three[i:i+3]=[' ',' ',' ']
        four[i:i+3]=[' ',' ',' ']
        five[i:i+3]=[' ',' ',' ']
        six[i:i+3]=[' ',' ',' ']
        seven[i:i+3]=[' ',' ',' ']
        eight[i:i+3]=[' ',' ',' ']
        nine[i:i+3]=['.',' ',' ']
    
        
def scramble():
    moves=["F","F'","F2","R","R'","R2","U","U'","U2","B","B'","B2","D","D'","D2","L","L'","L2",]
    print('SCRAMBLE SEQUENCE:\n')
    seq=[]
    seq.append(moves[random.randint(0,17)])
    print(seq[0],end=' ')
    for i in range(1,20):
        x=random.randint(0,17)
        while ((seq[i-1]==moves[x]) or (x%3==0 and (seq[i-1]==moves[x+1] or seq[i-1]==moves[x+2])) or ((x-1)%3==0 and (seq[i-1]==moves[x+1] or seq[i-1]==moves[x-1]) ) or ((x-2)%3==0 and (seq[i-1]==moves[x-1] or seq[i-1]==moves[x-2]) )):
            x=random.randint(0,17)
        seq.append(moves[x])
        print(seq[i],end=' ')
z=0
i=1
tm=[]
while True:
    scramble()
    print("\nPress Any Key to start the TIMER\n[Press Q to delete a record]")
    if m.getwche()=='q' :
        try:
            if tm:
                tm.__delitem__(int(input('\nEnter the record index\n')))
                i=i-2
                os.system('cls')
                if i<0:
                    #print('Index Out of range')
                    i=0
            else :
                os.system('cls')
                print('No record to delete')
                i=0
        except :
            os.system('cls')
            #print('Index out of range')
            #if i==1:
             #   i=0
    else:
        x=time.time()
        os.system('cls')
        m.getwch()
        y=time.time()
        h=strm(y-x)
        c=0
        cc=0
        for nn in range(0,len(h)):
            display(cc,h[c])
            if h[c]=='.':
                cc=cc+3
            else:
                cc=cc+7
            c=c+1
        print('Your Current TIME is')
        prnt()
        hhh=input('Accept?')
        if hhh and i>0:
            i=i-1
        else :
            z=z+y-x
            tm.append(h)
    if i:
        z=0
        for gobi in tm:
           z=z+float(gobi) 
        print('\nCurrent Average of '+str(i)+ ' solves is:\n'+strm(z/i))
    else :
        print('\nCurrent Average of '+str(i)+ ' solves is:\n0.0')
    print('\nALL TIMES')
    print('[',end='')
    if tm:
        for n in tm:
            print(n+'   ',end='')
    print(']',end='')
    print('\n\n')
    i=i+1
    
