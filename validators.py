def checkpass(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return False
    return True

def lengthcheck(content):
    if len(content)<25:
        return False
    return True


def is_valid_data(data):
    if not data.strip():
        return False
    return True

def is_int(data):
    if not isinstance(data,int):
        return False
    return True

def check_weekdays(day):
    weekdays=["monday","tuesday","wednesday","friday","thursday"]
    if day.lower() in weekdays:
        return False
    return True 
