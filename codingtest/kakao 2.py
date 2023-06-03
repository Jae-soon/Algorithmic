def solution(id_list, k):
    answer = 0
    member_list = []
    member_dict = {}

    for id in id_list:
        member_list.append(list(id.split(" ")))
    
    for member in member_list:
        member = set(member)
        for i in member:
            if i in member_dict:
                if member_dict[i] >= k:
                    continue
                
                member_dict[i] += 1
                answer += 1
            else:
                member_dict[i] = 1
                answer += 1
    print(member_dict)

    return answer

id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
print(solution(id_list, 3))