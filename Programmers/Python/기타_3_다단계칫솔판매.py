def solution(enroll, referral, seller, amount):
    name_money = {name : 0 for name in enroll}
    name_parent = dict(zip(enroll, referral))

    for name, num in zip(seller, amount) :
        next = name
        profit = num*100
        pay = profit//10
        while 1:
            name_money[next] += profit - pay
            if name_parent[next] == '-' or pay == 0:
                break
            else:
                profit = pay
                pay = profit//10
                next = name_parent[next]

    return list(name_money.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))