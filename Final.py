#WAP to a accept a list from the user and from binary search 
def binarysearch(l): #defining funciton for binary search 
    x = sorted(l)
    repeat = 'yes'
    while repeat == "yes":
        end = 0
        beg = (len(x)-1)
        found = int(input("\n Enter the element which needs to be found: "))
        flag = 0
        while end <= beg:
            mid = (end+beg)//2
            if x[mid] == found:
                print("\n The element ", found," was found at position ", l.index(found)+1)
                flag = 1
                break
            elif x[mid] > found:
                beg = mid-1
            elif x[mid] < found:
                end = mid+1
        if flag == 0:
            print("\n The element ", found, " is not present in the list ")
        print("\n __________________________________________")
        repeat = input("\n do you want to use it again....? yes/no:  ")

#main 
l = []
n = int(input("Enter the number of elements you want in the list : "))
print("\n Enter the elements: ")
for i in range(n):
    elements = int(input())
    l.append(elements)
print(l)
binarysearch(l)
