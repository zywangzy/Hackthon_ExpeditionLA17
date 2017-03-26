# coding: utf-8
import csv

f=file('/Users/Yu/Downloads/DestByPopPolygon.txt')
f2=file('/Users/Yu/Downloads/CitiesByPopulation.csv')
f=list(f)
f=map(lambda x:x.split(','),f)
f[-1][-1]=f[-1][-1]+'\r\n'
f=f[1:]
f=map(lambda x:[x[0],x[5],float(x[-6]),float(x[-5]),int(x[-1][:-2])],f)
f2=csv.reader(f2)
f2=list(f2)
f2=f2[3:]
for x in f:
    print x

f2=map(lambda x:[x[0].upper(),x[1]],f2)
for x in f:print x
for x in f2:print x
result=[]
count=0
count2=0
f3=file('/Users/Yu/Desktop/test.txt','w')
f3.write('Province_Name, Population, Postal_ID,Postal_XX,Postal_XY\n')
for x in f2:
    popu=0
    for y in f:
        if y[1]==x[0]:
            s = x[0]
            s = s + ', '+x[1]+', '+y[0]+', '+str(y[2])+', '+str(y[3])
            f3.write(s)
            f3.write('\n')
            count2+=1

            if y[-1]>popu:popu=y[-1]
    if s==x[0]:count+=1
print count,count2