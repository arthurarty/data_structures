def convert_money(money:str) -> int:
    if not isinstance(money, str):
        return money
    money = money.strip('$')
    money = money.lower()
    for char in money:
        if char == 'm':
            money = money.strip('m')
            money = float(money) * 1000000
    return int(money)


print(convert_money('$14.2M'))
