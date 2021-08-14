mylist = []
mylist = [int(item) for item in input("Enter All Bid : ").split()]
mylist.sort(reverse=True)
if len(mylist) == 1:
 print("not enough bidder")
elif mylist[0] == mylist[1]:
    print("error : have more than one highest bid")
else :
    print("winner bid is "+str(mylist[0])+" need to pay "+str(mylist[1]))