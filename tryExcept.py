try:
    a="hello"
    #print(x)
except NameError:
    print("NameError exception occured")
except:
    print("something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("finally block: The 'try-except' is finished")