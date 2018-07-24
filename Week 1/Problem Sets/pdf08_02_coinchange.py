def coin_change(num):
    if num in [10, 20, 50, 100]:
        return {num: 1}
    elif num > 100:
        a = {100:num // 100}
        a.update(coin_change(num % 100))
        return a
    elif num > 50:
        a = {50:num // 50}
        a.update(coin_change(num % 50))
        return a
    elif num > 20:
        a = {20:num // 20}
        a.update(coin_change(num % 20))
        return a
    elif num > 10:
        a = {10:num // 10}
        a.update(coin_change(num % 10))
        return a
    else:
        return {}

assert coin_change (50) == {50:1}
assert coin_change(80) == {50:1, 20:1, 10:1}
assert coin_change (120) == {100:1 , 20:1}
assert coin_change(90) == {50:1, 20:2}
