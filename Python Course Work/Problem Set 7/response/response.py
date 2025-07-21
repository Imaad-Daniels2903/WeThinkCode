from validator_collection import validators, errors

def main():
    print(validate(input("What's your email address? ")))


def validate(e):
    try:
        is_valid = validators.email(e)

    except errors.InvalidEmailError:
        return "Invalid"

    else:
        return "Valid"

if __name__ == "__main__":
    main()
