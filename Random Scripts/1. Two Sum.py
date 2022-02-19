
def twoSum(List, target):

        
    for i in List:
        for j in List:

            x = List[i] + List[j]
            if x == target & List[i]!=List[j]:
                print(List[i])
                print(List[j])
                print(f"{i},{j}")
                return 

            else:
                print("Cannot find values to add up")
    print("No values in the array could be added to produce the target")
    return

twoSum([1,2,3,4],4)
