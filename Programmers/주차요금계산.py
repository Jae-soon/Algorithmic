import datetime
import math

def dateToMinute(date):
    h, m = map(int, date.split(":"))
    return h * 60 + m

def solution(fees, records):
    answer = []
    car_dic = {}

    bt, bf, at, af = fees

    # 차의 입/출차 car_dic에 기록 {5961 : [["05:34", "IN"]]} 
    for i in records:
        time, number, history = i.split()
        number = int(number)
        
        if number in car_dic:
            car_dic[number].append([dateToMinute(time), history])
        else:
            car_dic[number] = [[dateToMinute(time), history]]

    rList = list(car_dic.items())
    rList.sort(key = lambda x : x[0])
    
    for r in rList:
        t = 0

        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]
        
        if r[1][-1][1] == "IN":
            t += dateToMinute("23:59")
        
        if t <= bt:
            answer.append(bf)
        else:
            answer.append(bf + math.ceil((t - bt) / at) * af)    

    return answer

fee = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

print(solution(fee, records))

