from django.shortcuts import render
import random
# Create your views here.
#写业务逻辑代码
from django.shortcuts import render,redirect,HttpResponse


def login(request):
    return HttpResponse("App02.login")
# def home(request):
#     return HttpResponse('<h1>hello</h1>')

# def login(request):
#     #包含用户提价的所有信息
#     #获取用户提交方式
#     error_msg = ""
#     if request.method == "POST":
#         #获取用户提交的数据
#         user = request.POST.get('user',None)
#         pwd = request.POST.get('pwd',None)
#         # user = request.POST['user']
#         # pwd = request.POST['pwd']
#         if user == 'root' and pwd == '123':
#             return redirect('/home')
#         else:
#             #用户名密码不匹配
#             error_msg = '用户名或密码错误'
#     return render(request, 'login.html', {'error_msg': error_msg})
#
# USER_LIST=[
#     {'username':'alex','email':'asdasdasd',"gender":'男'},
#     {'username': 'alex', 'email': 'asdasdasd', "gender": '男'},
#     {'username': 'alex', 'email': 'asdasdasd', "gender": '男'},
# ]
# # for index in range(20):
# #     temp = {'username':'alex'+str(index),'gender':'男','email':'alex@189.cm'}
# #     USER_LIST.append(temp)
#
# def home(request):
#     if request.method =="POST":
#         #获取用户提交的数据
#         u= request.POST.get('username')
#         e = request.POST.get('email')
#         g = request.POST.get('gender')
#         temp = {'username': u, 'gender': g, 'email': e}
#         USER_LIST.append(temp)
#     return render(request,'home.html',{'user_list':USER_LIST})
#
#         # print(user,pwd)
#     # string = '''
#     #     <form>
#     #         <input type= 'text'/>
#     #     </form>
#     # '''
#     # f = open('templates/login.html','r',encoding='utf8')
#
#     # data = f.read()
#     # return HttpResponse(data)
