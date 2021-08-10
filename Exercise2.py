def sp_checker(sp):
    # sp is short form of speed
    sp = float(sp)
    if sp <= 70:
        return 'OK'
    elif sp > 130:
        return 'License suspended'
    else:
        dpoint = int((sp - 70) / 5)
        return dpoint


speed = input("> ")
print(sp_checker(speed))
