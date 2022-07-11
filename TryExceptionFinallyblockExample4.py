try:
    try:
        file = open("myfile", "r")
        print(file.read())
    except Exception as e:
        print("program crashed bcoz of EX -- ", e)
    a = 10
    b =0
    res = a / b
    print(res)

except ValueError as ve:
    print("program crashed bcoz of VE-- ", ve)
except ZeroDivisionError as ze:
    print("program crashed bcoz of ZE -- ",ze)
except Exception as e:
    print("program crashed bcoz of EX -- ", e)

else:
    print("no exception")
finally:
    print("this is my finally block")

print("end of the program")