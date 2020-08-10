def print_book_info(title, author=None, year=None):
    if author is not None and year is not None:
        print('"{}" was written by {} in {}'.format(title, author, year))
    elif author is None and year is not None:
        print('"{}" was written in {}'.format(title, year))
    elif author is not None and year is None:
        print('"{}" was written by {}'.format(title, author))
    else:
        print('"{}"'.format(title))
