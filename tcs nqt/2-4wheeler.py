# totalvehicle=int(input())
# totalwheels=int(input())
# fourwheeler=totalvehicle
# twowheeler=totalvehicle-fourwheeler
# while fourwheeler*4+twowheeler*2!=totalwheels:
#     fourwheeler-=1
#     twowheeler+=1
# print("Four Wheeler:",fourwheeler)
# print("Two Wheeler:",twowheeler)

v=int(input())
w=int(input())
if (w&1)==1 or w<2 or w<=v:
    print("INVALID INPUT")
else:
    x=((4*v) -w)//2
    print("TW={0} FW={1}".format(x,v-x))
