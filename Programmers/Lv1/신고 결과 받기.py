def solution(id_list, report, k):
    answer = []
    report_dic = {name : 0 for name in id_list}
    mailing_dic = {name : 0 for name in id_list}
    report_id = []
    report = set(report)

    for r in report:
        report_dic[r.split(" ")[1]] += 1        
    
    for key, val in report_dic.items():
        if val >= k:
            report_id.append(key)
    
    for r in report:
        if r.split(" ")[1] in report_id:
            mailing_dic[r.split(" ")[0]] += 1

    answer = list(mailing_dic.values())
    return answer