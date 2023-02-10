special_words = ["-", "_", ".", "1", "2", "3", "4", "5", "6", "7", "8" ,"9", "0"]
accept_words = ["a", "b", "c", "d", "e", "f", "g", "h", "i" "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def solution(new_id):
    answer = ''


def step1(new_id):
    return step2(new_id.lower())

def step2(new_id):
    new = ""
    for i in new_id:
        if i == "i":
            new += i
        if i == "j":
            new += i
        if i in special_words or i in accept_words:
            new += i
    new_id = new
    step3(new_id)


def step3(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    
    step3(new_id)

def step4(new_id):
    if new_id[0] == "." or new_id[-1] == ".":
        new_id_list = list(new_id)
        if new_id[0] == ".":
            new_id_list[0] = ""
        elif new_id[-1] == ".":
            new_id_list[-1] = ""
        new_id = "".join(new_id_list)
    print("4 : " + new_id)

    if len(new_id) == 0:
        new_id += "a"
    print("5 : " + new_id)
            
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == ".":
            new_id = new_id.replace(".", "")
    print("6 : " + new_id)

    if len(new_id) <= 2:
        while 1:
            if len(new_id) == 3:
                break
            new_id += new_id[-1]
    print("7 : " + new_id)

    return new_id