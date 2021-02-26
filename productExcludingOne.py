def find_product(lst):
    # Write your code here
    result = []
    # result = [0] * len(lst)
    # print(result)
    prod = 1
    if 0 in lst:
        index = lst.index(0)
        #b = [x for i,x in enumerate(a) if i!=3]

        result = [x for i, x in enumerate(lst) if i!=index]
        print(result) 

    for element in lst:
        if element != 0:
            prod *= element

    for element in lst:
        if element != 0:
            prod /= element
            result.insert(lst.index(element), prod)
            prod *= element
    return result