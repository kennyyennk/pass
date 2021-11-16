
from django.shortcuts import render

def index(request):

        

    return render(request,"multiends/login.html")
def ground(request):

    if  request.method == 'POST':
        color = request.POST.get('color')
        st= request.POST.get('st')

    if st=='出校':
        st1='出校通行证(2分钟内有效)'
        st2='学生出校通行证'
        st3='http://tjxx.lnu.edu.cn/images/pass.png'
    else:
        st1='返校通行证(2分钟内有效)'
        st2='学生返校通行证'
        st3='http://tjxx.lnu.edu.cn/images/pass1.png'
        

    return render(request,"multiends/web.html",{'data':color,'data1':st1,'data2':st2,'data3':st3})
