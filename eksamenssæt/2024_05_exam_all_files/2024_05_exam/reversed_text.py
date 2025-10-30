def reversed_text(text, option):
    if option == "letters":
        new_string = ""
        for i in text.split():
            new_string += i[::-1] + " "
        return new_string[:-1]
    else:
        return " ".join(text.split()[::-1])
    
print(reversed_text('Hello world we are going to do some programming', 'words'))
