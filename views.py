from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def WatchData(request):
    return HttpResponse('<h1>Prasad Django practice</h1>')


def FetchData(request):
    context={}
    if request.method=='POST':
       eno = int(request.POST['empno'])
       cur = connection.cursor()
       cur.execute('select *from emp_7am where empno=%s',(eno,))
       data = cur.fetchall()
       print(data)
       context['empinfo'] = data
       return render(request,'fetchdata.html',context) 
    return render(request,'fetchdata.html')
