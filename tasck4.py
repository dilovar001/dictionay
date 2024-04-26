employees=['Kelly','Emma']
defaults={"designation":'Developer',"salary":8000}
a={}
for i in employees:
    a[i]=defaults.copy()
print(a)