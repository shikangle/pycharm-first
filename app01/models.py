from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateField(auto_now_add=True,null=True)
    uptime = models.DateField(auto_now_add=True,null=True)

class UserInfo(models.Model):
    #id,列，自增，主键
    #用户名类，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=60,null=True)
    test = models.EmailField(max_length= 19 , null=True,error_messages={'invalid':'请输入密码'})
    user_group = models.ForeignKey("UserGroup",to_field='uid',default=1,on_delete=models.CASCADE)

    user_type_choices =(
        (1,'超级用户'),
        (2,'普通用户'),
        (1,'普通普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)