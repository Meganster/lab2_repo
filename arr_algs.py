pr = [2, 3, 5, 7, 11, 13]
prim = [1, 0, 15, -7, 51, 13]

def search_min_in_arr(arr):
    min_elem = arr[0]
    for elem in arr:
        if min_elem > elem:
            min_elem = elem
    print(min_elem)
    
def search_avg_in_arr(arr):
    sum = 0
    for elem in arr:
        sum = sum + elem
    avg = sum / len(arr)
    print(avg)


search_min_in_arr(pr)
search_min_in_arr(prim)

search_avg_in_arr(pr)
search_avg_in_arr(prim)
