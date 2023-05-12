from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email_id=models.EmailField(max_length=254)

class user_information(models.Model):
    # User_id=models.OneToOneField(User,on_delete=models.CASCADE)
    User_id=models.ForeignKey(User,on_delete=models.CASCADE)
    # users=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    def __str__(self):
        return self.User_id.username
    
class treat_cnd_tds_sen(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    cnd=models.BigIntegerField(null=True,blank=True)
    spn=models.BigIntegerField(null=True,blank=True)
    tsp=models.BigIntegerField(null=True,blank=True)
    asp=models.BigIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)

class topics(models.Model):
    Topic_name=models.CharField(max_length=100)    


    def __str__(self):
        return self.Topic_name
    

class disp_atm(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    sts=models.CharField(max_length=50,null=True,blank=True)
    ndv=models.BigIntegerField(null=True,blank=True)
    ntt=models.CharField(max_length=50,null=True,blank=True)
    nta=models.BigIntegerField(null=True,blank=True)
    tmp=models.BigIntegerField(null=True,blank=True)
    ntp=models.BigIntegerField(null=True,blank=True)
    nov=models.BigIntegerField(null=True,blank=True)
    vl1=models.BigIntegerField(null=True,blank=True)
    vl2=models.BigIntegerField(null=True,blank=True)
    vl3=models.BigIntegerField(null=True,blank=True)
    vl4=models.BigIntegerField(null=True,blank=True)
    re1=models.BigIntegerField(null=True,blank=True)
    re2=models.BigIntegerField(null=True,blank=True)
    re3=models.BigIntegerField(null=True,blank=True)
    re4=models.BigIntegerField(null=True,blank=True) 
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class disp_tap1(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    p1=models.BigIntegerField(null=True,blank=True)
    p2=models.BigIntegerField(null=True,blank=True)
    p3=models.BigIntegerField(null=True,blank=True)
    p4=models.BigIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class disp_tap2(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    p1=models.BigIntegerField(null=True,blank=True)
    p2=models.BigIntegerField(null=True,blank=True)
    p3=models.BigIntegerField(null=True,blank=True)
    p4=models.BigIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class disp_tap3(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    p1=models.BigIntegerField(null=True,blank=True)
    p2=models.BigIntegerField(null=True,blank=True)
    p3=models.BigIntegerField(null=True,blank=True)
    p4=models.BigIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class disp_tap4(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    p1=models.BigIntegerField(null=True,blank=True)
    p2=models.BigIntegerField(null=True,blank=True)
    p3=models.BigIntegerField(null=True,blank=True)
    p4=models.BigIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class disp_consen(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    cnd=models.BigIntegerField(null=True,blank=True)
    spn=models.BigIntegerField(null=True,blank=True)
    asp=models.BigIntegerField(null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_ampv1(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    pos=models.CharField(max_length=50,null=True,blank=True)
    rmt=models.BigIntegerField(null=True,blank=True)
    cct=models.BigIntegerField(null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    mot=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    op1=models.CharField(max_length=50,null=True,blank=True)
    op2=models.CharField(max_length=50,null=True,blank=True)
    op3=models.CharField(max_length=50,null=True,blank=True)
    ip1=models.CharField(max_length=50,null=True,blank=True)
    ip2=models.CharField(max_length=50,null=True,blank=True)
    ip3=models.CharField(max_length=50,null=True,blank=True)
    psi=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class treat_ampv2(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    pos=models.CharField(max_length=50,null=True,blank=True)
    rmt=models.BigIntegerField(null=True,blank=True)
    cct=models.BigIntegerField(null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    mot=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    op1=models.CharField(max_length=50,null=True,blank=True)
    op2=models.CharField(max_length=50,null=True,blank=True)
    op3=models.CharField(max_length=50,null=True,blank=True)
    ip1=models.CharField(max_length=50,null=True,blank=True)
    ip2=models.CharField(max_length=50,null=True,blank=True)
    ip3=models.CharField(max_length=50,null=True,blank=True)
    psi=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_ampv3(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    pos=models.CharField(max_length=50,null=True,blank=True)
    rmt=models.BigIntegerField(null=True,blank=True)
    cct=models.BigIntegerField(null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    mot=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    op1=models.CharField(max_length=50,null=True,blank=True)
    op2=models.CharField(max_length=50,null=True,blank=True)
    op3=models.CharField(max_length=50,null=True,blank=True)
    ip1=models.CharField(max_length=50,null=True,blank=True)
    ip2=models.CharField(max_length=50,null=True,blank=True)
    ip3=models.CharField(max_length=50,null=True,blank=True)
    psi=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_ampv4(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    pos=models.CharField(max_length=50,null=True,blank=True)
    rmt=models.BigIntegerField(null=True,blank=True)
    cct=models.BigIntegerField(null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    mot=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    op1=models.CharField(max_length=50,null=True,blank=True)
    op2=models.CharField(max_length=50,null=True,blank=True)
    op3=models.CharField(max_length=50,null=True,blank=True)
    ip1=models.CharField(max_length=50,null=True,blank=True)
    ip2=models.CharField(max_length=50,null=True,blank=True)
    ip3=models.CharField(max_length=50,null=True,blank=True)
    psi=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_ampv5(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    pos=models.CharField(max_length=50,null=True,blank=True)
    rmt=models.BigIntegerField(null=True,blank=True)
    cct=models.BigIntegerField(null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    mot=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    op1=models.CharField(max_length=50,null=True,blank=True)
    op2=models.CharField(max_length=50,null=True,blank=True)
    op3=models.CharField(max_length=50,null=True,blank=True)
    ip1=models.CharField(max_length=50,null=True,blank=True)
    ip2=models.CharField(max_length=50,null=True,blank=True)
    ip3=models.CharField(max_length=50,null=True,blank=True)
    psi=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class treat_rwp(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    sts=models.CharField(max_length=50,null=True,blank=True)
    crt=models.BigIntegerField(null=True,blank=True)
    olc=models.BigIntegerField(null=True,blank=True)
    drc=models.BigIntegerField(null=True,blank=True)
    spn=models.BigIntegerField(null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_hpp(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    sts=models.CharField(max_length=50,null=True,blank=True)
    crt=models.BigIntegerField(null=True,blank=True)
    olc=models.BigIntegerField(null=True,blank=True)
    drc=models.BigIntegerField(null=True,blank=True)
    spn=models.BigIntegerField(null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_panel(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    sts=models.CharField(max_length=50,null=True,blank=True)
    rtl=models.CharField(max_length=50,null=True,blank=True)
    ttl=models.CharField(max_length=50,null=True,blank=True)
    lps=models.CharField(max_length=50,null=True,blank=True)
    hps=models.CharField(max_length=50,null=True,blank=True)
    dgp=models.CharField(max_length=50,null=True,blank=True)
    mod=models.CharField(max_length=50,null=True,blank=True)
    ipv=models.BigIntegerField(null=True,blank=True)
    unv=models.BigIntegerField(null=True,blank=True)
    ovv=models.BigIntegerField(null=True,blank=True)
    spn=models.BigIntegerField(null=True,blank=True)
    nmv=models.BigIntegerField(null=True,blank=True)
    stp=models.CharField(max_length=50,null=True,blank=True)
    srt=models.BigIntegerField(null=True,blank=True)
    bkt=models.BigIntegerField(null=True,blank=True)
    rst=models.BigIntegerField(null=True,blank=True)
    err=models.CharField(max_length=50,null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class treat_flowsen(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    fr1=models.BigIntegerField(null=True,blank=True)
    fr2=models.BigIntegerField(null=True,blank=True)
    ff1=models.BigIntegerField(null=True,blank=True)
    ff2=models.BigIntegerField(null=True,blank=True)
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    day=models.CharField(max_length=50)
    hour=models.CharField(max_length=50)
    minit=models.CharField(max_length=50)
    second=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class repo_latestdata(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    cnd_tds=models.JSONField(null=True,blank=True)
    rwp=models.JSONField(null=True,blank=True)
    hpp=models.JSONField(null=True,blank=True)
    panel=models.JSONField(null=True,blank=True)
    flowsen=models.JSONField(null=True,blank=True)
    ampv1=models.JSONField(null=True,blank=True)
    ampv2=models.JSONField(null=True,blank=True)
    ampv3=models.JSONField(null=True,blank=True)
    ampv4=models.JSONField(null=True,blank=True)
    ampv5=models.JSONField(null=True,blank=True)
    atm=models.JSONField(null=True,blank=True)
    tap1=models.JSONField(null=True,blank=True)
    tap2=models.JSONField(null=True,blank=True)
    tap3=models.JSONField(null=True,blank=True)
    tap4=models.JSONField(null=True,blank=True)
    consen=models.JSONField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.device_id,self.message_type,self.cnd_tds,self.rwp,self.hpp,self.panel,self.flowsen,self.ampv1,self.ampv2,self.ampv3,self.ampv4,self.ampv5,self.atm,self.tap1,self.tap2,self.tap3,self.tap4,self.consen
    
class repo_history(models.Model):
    device_id=models.CharField(max_length=100)
    message_type=models.CharField(max_length=50)
    component_name=models.CharField(max_length=100)
    msg_json=models.JSONField(null=True,blank=True)


class repo_hourly(models.Model):
    device_id=models.CharField(max_length=100)
    service=models.CharField(max_length=100,null=True,blank=True)
    sum=models.BigIntegerField(null=True,blank=True)
    count=models.BigIntegerField(null=True,blank=True)
    avg=models.FloatField(null=True,blank=True)
    # avg=models.f(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    month =  models.CharField(max_length=50)
    year =  models.CharField(max_length=50)
    day =  models.CharField(max_length=50)
    hour =  models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.device_id,self.service,self.sum,self.count,self.avg,self.created_at,self.updated_at
class repo_daily(models.Model):
    device_id=models.CharField(max_length=100)
    service=models.CharField(max_length=100,null=True,blank=True)
    sum=models.BigIntegerField(null=True,blank=True)
    count=models.BigIntegerField(null=True,blank=True)
    avg=models.FloatField(null=True,blank=True)
    month =  models.CharField(max_length=50)
    year =  models.CharField(max_length=50)
    day =  models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self) -> str:
        return self.device_id,self.service,self.sum,self.count,self.avg,self.created_at,self.updated_at
class repo_monthly(models.Model):
    device_id=models.CharField(max_length=100)
    service=models.CharField(max_length=100,null=True,blank=True)
    sum=models.BigIntegerField(null=True,blank=True)
    count=models.BigIntegerField(null=True,blank=True)
    avg=models.FloatField(null=True,blank=True)
    month =  models.CharField(max_length=50)
    year =  models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self) -> str:
        return self.device_id,self.service,self.sum,self.count,self.avg,self.created_at,self.updated_at
class repo_yearly(models.Model):
    device_id=models.CharField(max_length=100)
    service=models.CharField(max_length=100,null=True,blank=True)
    sum=models.BigIntegerField(null=True,blank=True)
    count=models.BigIntegerField(null=True,blank=True)
    avg=models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    month =  models.CharField(max_length=50)
    year =  models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.device_id,self.service,self.sum,self.count,self.avg,self.created_at,self.updated_at
    
class device_info(models.Model):
    Device_id=models.CharField(max_length=100)
    Device_name=models.CharField(max_length=100)
    setting_variable=models.CharField(max_length=100)#nat,
    unit_type=models.CharField(max_length=100)#desp,Treat
    company_name=models.CharField(max_length=100)#
    componant_name=models.CharField(max_length=100)#atm,rwp   
    

    def str(self):
        return self.Device_id,self.Device_name,self.setting_variable,self.unit_type,self.company_name,self.componant_name
    
class key_info(models.Model):
    key_name=models.CharField(max_length=100)
    key_value=models.CharField(max_length=100)
        
    


    def str(self):
        return self.key_name
    
class graph_info(models.Model):
    service_name=models.CharField(max_length=100)
    device_id=models.CharField(max_length=100)    
    


    def str(self):
        return self.service_name
    
class rwp_setting(models.Model):
    olc=models.CharField(max_length=100)
    drc=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100) 
    device_id=models.CharField(max_length=100)   
    

    def str(self):
        return self.olc,self.drc,self.spn,self.unit_type,self.company_name,self.componant_name   
class Rwp_state(models.Model):
    sts=models.CharField(max_length=100) 
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    def str(self):
        return self.sts
    
class hpp_setting(models.Model):
    olc=models.CharField(max_length=100)
    drc=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)    
    

    def str(self):
        return self.olc
class hpp_state(models.Model):
    sts=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.sts
class cnd_setting(models.Model):
    spn=models.CharField(max_length=100)
    tsp=models.CharField(max_length=100)
    asp=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)  

    def str(self):
        return self.spn 
class tds_setting(models.Model):
    spn=models.CharField(max_length=100)
    tsp=models.CharField(max_length=100)
    asp=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)  

    def str(self):
        return self.spn 
    

class F_flowsen_setting(models.Model):
    ff=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.ff
    
class P_flowsen_setting(models.Model):
    ff=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.ff


class panel_setting(models.Model):
    mod=models.CharField(max_length=100)
    unv=models.CharField(max_length=100)
    ovv=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)    
    nmv=models.CharField(max_length=100)    
    stp=models.CharField(max_length=100)    
    srt=models.CharField(max_length=100)    
    bkt=models.CharField(max_length=100)    
    rst=models.CharField(max_length=100)    
    componant_name=models.CharField(max_length=100)    
    unit_type=models.CharField(max_length=100)    
    company_name=models.CharField(max_length=100)    
    
    def str(self):
        return self.mod 

class atm_setting(models.Model):
    ntp=models.CharField(max_length=100)
    nov=models.CharField(max_length=100)
    vl1=models.CharField(max_length=100)
    vl2=models.CharField(max_length=100)    
    vl3=models.CharField(max_length=100)    
    vl4=models.CharField(max_length=100)    
    re1=models.CharField(max_length=100)    
    re2=models.CharField(max_length=100)    
    re3=models.CharField(max_length=100)    
    re4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)    
    

    def str(self):
        return self.ntp 
    
# class consen_setting(models.Model):
#     spn=models.CharField(max_length=100)
#     asp=models.CharField(max_length=100)
#     unit_type=models.CharField(max_length=100)
#     company_name=models.CharField(max_length=100)
#     componant_name=models.CharField(max_length=100)

#     # def str(self):
#     #     return self.spn

class tap1_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap2_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap3_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap4_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class ampv1_setting(models.Model):
    srt=models.CharField(max_length=100)
    bkt=models.CharField(max_length=100)
    rst=models.CharField(max_length=100)
    mot=models.CharField(max_length=100)
    stp=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    ip1=models.CharField(max_length=100)
    ip2=models.CharField(max_length=100)
    ip3=models.CharField(max_length=100)
    psi=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.srt
class ampv2_setting(models.Model):
    srt=models.CharField(max_length=100)
    bkt=models.CharField(max_length=100)
    rst=models.CharField(max_length=100)
    mot=models.CharField(max_length=100)
    stp=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    ip1=models.CharField(max_length=100)
    ip2=models.CharField(max_length=100)
    ip3=models.CharField(max_length=100)
    psi=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.srt

class ampv1_state(models.Model):
    pos=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    
    def str(self):
        return self.pos
class ampv2_state(models.Model):
    pos=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    def str(self):
        return self.pos

    
class rwp_setting(models.Model):
    olc=models.CharField(max_length=100)
    drc=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100) 
    device_id=models.CharField(max_length=100)   
    

    def str(self):
        return self.olc,self.drc,self.spn,self.unit_type,self.company_name,self.componant_name   
class Rwp_state(models.Model):
    sts=models.CharField(max_length=100) 
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    def str(self):
        return self.sts
    
class hpp_setting(models.Model):
    olc=models.CharField(max_length=100)
    drc=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)    
    

    def str(self):
        return self.olc
class hpp_state(models.Model):
    sts=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.sts
class cnd_setting(models.Model):
    spn=models.CharField(max_length=100)
    tsp=models.CharField(max_length=100)
    asp=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)  

    def str(self):
        return self.spn 
class tds_setting(models.Model):
    spn=models.CharField(max_length=100)
    tsp=models.CharField(max_length=100)
    asp=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)  

    def str(self):
        return self.spn 
    

class F_flowsen_setting(models.Model):
    ff=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.ff
    
class P_flowsen_setting(models.Model):
    ff=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.ff


class panel_setting(models.Model):
    mod=models.CharField(max_length=100)
    unv=models.CharField(max_length=100)
    ovv=models.CharField(max_length=100)
    spn=models.CharField(max_length=100)    
    nmv=models.CharField(max_length=100)    
    stp=models.CharField(max_length=100)    
    srt=models.CharField(max_length=100)    
    bkt=models.CharField(max_length=100)    
    rst=models.CharField(max_length=100)    
    componant_name=models.CharField(max_length=100)    
    unit_type=models.CharField(max_length=100)    
    company_name=models.CharField(max_length=100)    
    
    def str(self):
        return self.mod 

class atm_setting(models.Model):
    ntp=models.CharField(max_length=100)
    nov=models.CharField(max_length=100)
    vl1=models.CharField(max_length=100)
    vl2=models.CharField(max_length=100)    
    vl3=models.CharField(max_length=100)    
    vl4=models.CharField(max_length=100)    
    re1=models.CharField(max_length=100)    
    re2=models.CharField(max_length=100)    
    re3=models.CharField(max_length=100)    
    re4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)    
    

    def str(self):
        return self.ntp 
    
class consen_setting(models.Model):
    spn=models.CharField(max_length=100)
    asp=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    # def str(self):
    #     return self.spn

class tap1_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap2_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap3_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class tap4_setting(models.Model):
    p1=models.CharField(max_length=100)
    p2=models.CharField(max_length=100)
    p3=models.CharField(max_length=100)
    p4=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.p1
class ampv1_setting(models.Model):
    srt1=models.CharField(max_length=100)
    srt2=models.CharField(max_length=100)
    bkt=models.CharField(max_length=100)
    rst=models.CharField(max_length=100)
    mot=models.CharField(max_length=100)
    stp=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    ip1=models.CharField(max_length=100)
    ip2=models.CharField(max_length=100)
    ip3=models.CharField(max_length=100)
    psi=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.srt
class ampv2_setting(models.Model):
    srt1=models.CharField(max_length=100)
    srt2=models.CharField(max_length=100)
    bkt=models.CharField(max_length=100)
    rst=models.CharField(max_length=100)
    mot=models.CharField(max_length=100)
    stp=models.CharField(max_length=100)
    op1=models.CharField(max_length=100)
    op2=models.CharField(max_length=100)
    op3=models.CharField(max_length=100)
    ip1=models.CharField(max_length=100)
    ip2=models.CharField(max_length=100)
    ip3=models.CharField(max_length=100)
    psi=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)

    def str(self):
        return self.srt

class ampv1_state(models.Model):
    pos=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    
    def str(self):
        return self.pos
class ampv2_state(models.Model):
    pos=models.CharField(max_length=100)
    unit_type=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    componant_name=models.CharField(max_length=100)
    def str(self):
        return self.pos