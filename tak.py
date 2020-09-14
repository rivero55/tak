
print("HITUNG TAK MU")
print("")
cekin=int(input("berapa jumlah cek in mu?"))
hitung=0
if cekin<15 :
    hitung="Kosong"
elif 14<cekin<30:
    hitung=cekin*0.10
elif 30<cekin<45:
    hitung=cekin*0.15
elif 44<cekin<60:
    hitung=cekin*0.20
elif 60<=cekin<70:
    hitung=cekin*0.25
elif cekin>=70 :
    print("null")
else:
    print("null")

print("TAK YANG KAMU DAPAT ADALAH ",hitung)
print(type(hitung))
    

