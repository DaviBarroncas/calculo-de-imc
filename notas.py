temp= []
princ= []
mai=men=0
while True:
    temp.append(input("nome:"))
    temp.append(float(input("peso: " )))
    if len(princ)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp=input("quer continuar? [S/N]")
    if resp in "Nn":
        break
print("-="*30)
print(f"{princ}")
print(f"{len(princ)}")
print(f"maior: {mai}")
print(f"menor: {men}")