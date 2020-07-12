# Add @profile above the function whose memory profile you need to check
@profile
def func():
    lst=[]
    for i in range(5000):
        lst.append(i)
    lst

# func2() was added only to show that not all function's memory profile is displayed.
def func2():
    temp = []
    for i in range(5000):
        temp.append(i)
    temp
func()
func2()