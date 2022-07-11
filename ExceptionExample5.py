try:
    a = 10
    b =0
    res = a / b
    print(res)
except (ValueError, ZeroDivisionError, Exception) as e:
    print("program crashed bcoz of -- ", e)