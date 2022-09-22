"""Scoping"""
a = 100

def func():
    global a  # global nicht verwenden
    sum_ = 0
    a = 10
    print('locals', locals())
    print('globals', globals())
    print('in', a)
    print(sum_)

print('vorher', a)
func()
print('nachher', a)