def password_candidate(password):
    password_string = str(password)

    if len(password_string) != 6:
        return False

    if not password_string[0] <= password_string[1] <= password_string[2] <= password_string[3] <= password_string[4] <= password_string[5]:
        return False

    if password_string[0] < password_string[1] < password_string[2] < password_string[3] < password_string[4] < password_string[5]:
        return False

    return True

def enhanced_password_candidate(password):
    if not password_candidate(password):
        return False

    password_string = str(password)

    if password_string[0] == password_string[1] < password_string[2] \
        or password_string[0] < password_string[1] == password_string[2] < password_string[3] \
        or password_string[1] < password_string[2] == password_string[3] < password_string[4] \
        or password_string[2] < password_string[3] == password_string[4] < password_string[5] \
        or password_string[3] < password_string[4] == password_string[5]:
        return True

    return False


def test1():
    print("Test 1: ")

    print(sum(1 if password_candidate(x) else 0 for x in range(372037, 905158)))


def test2():
    print("Test 2: ")

    print(sum(1 if enhanced_password_candidate(x) else 0 for x in range(372037, 905158)))


if __name__ == "__main__":
    test1()
    test2()
