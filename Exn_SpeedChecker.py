def sp_checker(speed): # sp => speed
    speed = float(speed)
    if speed <= 70:
        return 'OK'
    elif speed > 130:
        return 'License suspended'
    else:
        dpoint = int((speed - 70) / 5)
        return dpoint


speed = input("> ")
check_result = sp_checker(speed)
