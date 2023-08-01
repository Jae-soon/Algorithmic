from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    term = {}
    today = datetime.strptime(today, '%Y.%m.%d')
    
    for t in terms:
        term[t.split(" ")[0]] = int(t.split(" ")[1])
    
    idx = 1
    for p in privacies:
        privacyDate = datetime.strptime(p.split(" ")[0], '%Y.%m.%d') + relativedelta(months=term[p[-1]]) - timedelta(days=1)
        
        if privacyDate < today:
            answer.append(idx)
        idx += 1

            
    return answer