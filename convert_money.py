def convert_money(money:str) -> int:
    if not isinstance(money, str):
        return money
    money = money.strip('$')
    money = money.lower()
    multiplier = 1
    for char in money:
        if char == 'm':
            money = money.strip('m')
            multiplier = 1000000
        if char == 'k':
            money = money.strip('k')
            multiplier = 1000
    try:
        money = float(money) * multiplier
    except ValueError:
        return


print(convert_money('$14.2M'))
