hours=int(input('enter hrs:'))
rate=int(input('enter rate:'))
if hours>40:
    extra_time=float(hours)-40
else:
    extra_time=0
extra_pay=0.5*float(rate)*extra_time
pay=float(hours)*float(rate)+extra_pay
print('ppay:'),
print(pay)
