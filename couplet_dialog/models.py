from django.db import models

# https://docs.djangoproject.com/en/3.1/ref/models/fields/

class Couplet_warehouse(models.Model):
    couplet_id = models.AutoField(primary_key=True)
    couplet_left = models.CharField(max_length = 20)
    couplet_right = models.CharField(max_length = 20)
    
    def __str__(self):
        return [self.couplet_left, self.couplet_right]

class User_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length = 320)  # local part 255@domain part 64
    user_nickname = models.CharField(max_length = 32) # Limit Chinese characters to 16, as WeChat
    user_head_portrait = models.ImageField(max_length = 200)
    user_password = models.CharField(max_length=200)
    user_vip_level = models.IntegerField()
    user_vip_endtime = models.DateField()    # need a transformer to timestamp
    
    def __str__(self):
        return self.user_nickname
        
    def save(self, *args, **kwargs):
        self.password = make_password(self.password, None, 'pbkdf2_sha256')
        super(User_info, self).save(*args, **kwargs)
    '''
    前端验证密码
    from django.contrib.auth.hashers import check_password
    
    user_password = request.POST.get("user_password", None)
    if check_password(user_password, item.password):
        return HttpResponseRedirect('/automation/')
    return HttpResponse('用户名密码错误')
    '''

class Dialog_api(models.Model):
    dialog_id = models.AutoField(primary_key=True)
    dialog_core = models.CharField(max_length = 32)
    dialog_url = models.URLField(max_length = 200)   # 如果url不接受ip:port，就换成GenericIPAddressField
    def __str__(self):
        return self.dialog_url
    

# 评价表，不在sqlite里，移到redis了
 
# 管理员信息表(django有自己的管理员机制，就不需要这个了吧)
 '''
class Administrator_info(models.Model):
    Administrator_id = models.AutoField(primary_key=True)
    Administrator_nickname = models.CharField(max_length = 32)
    Administrator_password = models      # 加密密码，需要encode和decode处理
'''