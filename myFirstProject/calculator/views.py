from django.shortcuts import render
from .models import calculator


# Create your views here.
def default(request):
    return render(request, 'calculator/default.html')


def create_cal(request, x, d, y):
    cal1 = calculator(x)
    cal2 = calculator(y)
    if d == '+':
        result = cal1 + cal2
    if d == '-':
        result = cal1 - cal2
    if d == '*':
        result = cal1 * cal2
    if d == 'div':
        result = cal1 / cal2
    print(x)
    print(d)
    print(y)
    print(cal1 + cal2)
    return render(request, 'calculator/calculator.html', {'x': x, 'd': d, 'y': y, 'result': result})

def wrong(request, x, d, y):
    return render(request, 'calculator/error.html')
