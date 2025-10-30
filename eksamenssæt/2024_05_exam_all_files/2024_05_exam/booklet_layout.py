def booklet_layout(content_pages):
    blank = 0

    while content_pages % 4 != 0:
        blank += 1
        content_pages += 1
    
    return content_pages, blank

print(booklet_layout(17))