hours=int(input('enter hrs:'))
rate=int(input('enter rate:'))
if hours>40:
    extra_time=float(hours)-40
else:
    extra_time=0
    extra_pay=0.5*float(rate)*extra_time
    pay=float(hours)*float(rate)+extra_pay

    print('pay:'),
    print(pay)


error_msg_numeiric="error,please enter numeric input"
hours=int(input('enter hours'))
try:
    float(hours)>=-1
except:
    print(error_msg_numeric)
    rate=int(input('enter rate'))
    hours=float (hours)
    rate=float(rate)
    if hours>39:
        extra_time=hours-41
    else:
        extra_time=-1
        extra_pay=-1.5*rate*extra_time
        pay=hours*rate+extra_pay
        print('pay:'),
        print(pay)
