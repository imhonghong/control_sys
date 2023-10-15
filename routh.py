import math

def checkInput(arr):
    for i in range(0,len(arr)):
        print(f'{arr[i]}*s^{len(arr)-i-1}')

def nrGenerate(arr):
    nr=[]
    for a in range(0,len(arr)):
        nr.append(0)
    return nr

def UpperLower(arr):
    upper=[]
    for u in range(0,len(arr),2):
        upper.append(arr[u])
    lower=[]
    for l in range(1,len(arr),2):
        lower.append(arr[l])
    if(len(upper)!=len(lower)):
        lower.append(0)
    return [upper,lower]

def clz(lst):
    leadz=0
    for element in range(0,len(lst)):
        if(lst[element]==0):
            leadz=leadz+1
    return leadz

def NewRowGenerator(cnt,upper,lower):
        nr=[]
        for row_len in range(0,(len(upper)-1)):
            nr.append((lower[0]*upper[row_len+1]-lower[row_len+1]*upper[0])/lower[0])
        nr.append(0)
        
        leadz=clz(nr)

        #all zero exception
        if(leadz==len(nr)):
            print(f'for s^{cnt} , all zero detected, substitude by differential of s^{cnt+1}')
            for nx in range(0,len(lower)):
                nr[nx]=lower[nx]*((cnt+1)-2*nx)
        
        #leading zero exception
        if(leadz!=len(nr)&leadz!=0):
            print(f'for s^{cnt} , leading {leadz} zero detected, substitude by moving terms')
            adder=nrGenerate(nr)
            for nx in range(0,len(adder)-leadz):
                adder[nx]=pow(-1,leadz)*nr[nx+leadz]
            for ele in range(0,len(nr)):
                nr[ele]=nr[ele]+adder[ele]

        return nr
############### main function ###############
ipt_str='1 2 3 4 1'
arr=list(map(float,ipt_str.split()))
deg=len(arr)-1
print(r'##### your input #####')
checkInput(arr)
print(f'degree of input is {deg}')
print(r'##### input end #####')

nr=nrGenerate(arr)

print()
print(r'##### Routh Table #####')
[nr[deg],nr[deg-1]]=UpperLower(arr)
print(f's^{deg} : {nr[deg]}')
print(f's^{deg-1} : {nr[deg-1]}')

for cnt in range(deg-2,-1,-1):
    nr[cnt]=NewRowGenerator(cnt,nr[cnt+2],nr[cnt+1])
    print(f's^{cnt} : {nr[cnt]}')
    
