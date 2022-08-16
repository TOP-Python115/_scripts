def test():
    try:
        raise TypeError
    except TypeError:
        print('except clause')
        return False
    finally:
        print('finally clause')
        return True

