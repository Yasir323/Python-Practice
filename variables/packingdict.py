def fun(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print("%s = %s"%(key, kwargs[key]))

fun(name = "Luffy", ID = "101", language = 'Python')
# OR
dic = {'first_name' : 'Monkey D', 'last_name' : 'Luffy'}
fun(**dic)
