def punctuation_ratio(text):
    text = text.split(' ')
    ratio_comma = 0
    ratio_no_comma = 0
    for i in range(len(text)):
        if text[i] == "and":
            if text[i - 1][-1] == ",":
                ratio_comma += 1
            else:
                ratio_no_comma += 1
    
    return ratio_comma / ratio_no_comma


text = ("Sara and Emma like to travel, bike, and hike, and when they are " +
"traveling they always take their bikes, hiking shoes, and sleeping bags. " +
"Last year, Sarah and Emma traveled to Italy, France, and Spain. And that " +
"was fun, and, according to Sara and Emma, very expensive!")
print(punctuation_ratio(text))
1.3333333333333333