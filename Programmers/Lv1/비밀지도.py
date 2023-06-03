def binary(n, num):
    bi = []
    while 1:
        a = int(num / 2)
        b = int(num % 2)
        bi.insert(0, b)

        if a != 0:
            num = a
        else:
            if len(bi) != n:
                for _ in range(n - len(bi)):
                    bi.insert(0, 0)
            break
    
    final_bi = "".join(map(str, bi))
    return final_bi

def solution(n, arr1, arr2):
    answer = []
    arr_1 = []
    arr_2 = []
    for i in range(n):
        arr_1_bin = binary(n, arr1[i]).replace("1", "#").replace("0", " ")
        arr_2_bin = binary(n, arr2[i]).replace("1", "#").replace("0", " ")
        arr_1.append(arr_1_bin)
        arr_2.append(arr_2_bin)
    
    print(arr_1)
    print(arr_2)
    for i in range(n):
        new_arr = ""
        for j in range(n):
            if arr_1[i][j] == "#" or arr_2[i][j] == "#":
                new_arr += "#"
            else:
                new_arr += " "
        answer.append(new_arr)
    return answer