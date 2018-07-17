from django.shortcuts import render
# Create your views here.
#写业务逻辑代码
from django.shortcuts import HttpResponse,redirect


# def login(request):
#     return HttpResponse("<h1>hello</h1>")
# # def home(request):
# #     return HttpResponse('<h1>hello</h1>')

def login(request):
    #包含用户提价的所有信息
    #获取用户提交方式
    if request.method == "GET":
        #获取用户提交的数据
        return render(request,'login.html')
    elif request.method == "POST":
        #数据库中查询 select * from user where username = '' and pwd = ''
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request,'login.html')

        return render(request,'login.html')
    else:
        return redirect('/index/')

def index(request):
    return render(request,'index.html')

from app01 import models
def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        user_group = models.UserGroup.objects.all()
        #print(user_list.query)
        #QuerySet[obj(id,username,email,user_group_id(uid,capition)),obj]
        return render(request,'user_info.html',{'user_list':user_list,'user_group':user_group})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        t = request.POST.get('group_id')

        models.UserInfo.objects.create(username=u,password=p,user_group_id=t)
        return redirect('/cmdb/user_info/')
        # user_list = models.UserInfo.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})

def user_detail(request,nid):
    t = models.UserInfo.objects.filter(id = nid).values('user_group__caption')#取一条数据
    obj = models.UserInfo.objects.filter(id = nid).first()#取一条数据
    print(obj,t)


    return render(request,'user_detail.html',{'obj':obj,'t' :t})

def user_del(request,nid):
    models.UserInfo.objects.filter(id = nid).delete()#取一条数据
    return redirect('/cmdb/user_info/')

def user_edit(request,nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info/')


#一对多
def orm(request):
    #1创建
    #models.UserInfo.objects.create(username='root',password='123',)
    #2  obj = models.UserInfo.objects.create(username='hubaocheng',password='345',)
    # obj.save()
    # dic = {'username':'alex','password':'666'}
    # models.UserInfo.objects.create(**dic)
    #查
    #result = models.UserInfo.objects.all()
    #resullt = models.UserInfo.objects.filter(username='hubaocheng',)
    #删除
    #models.UserInfo.objects.filter(id=3).delete()
    # for row in resullt:
    #     print(row.id,row.username,row.password)
    #更新
   # models.UserInfo.objects.filter(id =2).update(password = 123456789)
   #  models.UserInfo.objects.create(
   #      username='root1',
   #      password='123',
   #      email='asdasdas',
   #      test='fdssdgdsgs',
   #      user_group=models.UserGroup.objects.filter(id =1).first()
   #  )

    models.UserInfo.objects.create(
        username='root1',
        password='123',
        email='asdasdas',
        test='fdssdgdsgs',
        user_group_id=1
    )
    return HttpResponse('username')




# # def home(request):
# #     return HttpResponse('home')
# from django.views import View
# class Home(View):
#    def get(self,request):
#        pass
#    def post(self,request):
#        pass


