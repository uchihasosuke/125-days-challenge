#Day4
#Implement a program to find the intersection of two lists.

def find_intersection(list1, list2):
   
    intersection_set = set(list1) & set(list2)
    
    intersection_list = list(intersection_set)
    
    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection_result = find_intersection(list1, list2)


print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Intersection: {intersection_result}")
