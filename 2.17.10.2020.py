pervoechislo=25
vtoroechislo=25.5
tretiechislo=24.8
stroka=1
print(pervoechislo,vtoroechislo,tretiechislo)
for i in range(1,999):
    pervoechislo+=1
    vtoroechislo+=1
    tretiechislo+=1
    print(pervoechislo,vtoroechislo,tretiechislo)
    if pervoechislo==35:
        break
