import json

f=open("country.csv","r",encoding="gbk") #
b=[]
for line in f:
        line = line.replace("\n", "")
        a=line.split(",")
        s={}
        s["name"]=a[0]
        s["value"]=float(a[10])
        b.append(s)
f.close()
fw=open("OOSR_Upper_Secondary_Age_Female.js","w",encoding='utf-8')
#for i in range(1,len(ls)):
    #ls[i]=dict(zip(ls[0],ls[i]))
print(b)
b = json.dumps(b,ensure_ascii=False)
fw.write(b)
fw.close()
print("finished!")
