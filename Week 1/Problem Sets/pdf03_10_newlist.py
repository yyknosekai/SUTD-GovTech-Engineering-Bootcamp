numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]


assert newlist == [34 , 44 , 68, 44 , 12]
