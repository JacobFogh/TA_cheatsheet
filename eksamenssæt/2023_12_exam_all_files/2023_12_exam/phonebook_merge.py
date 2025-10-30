def phonebook_merge(book1, book2):

    for i in book2:
        if i not in book1:
            book1[i] = book2[i]
        else:
            for number in book2[i]:
                if number not in book1[i]:
                    book1[i].append(number)
    