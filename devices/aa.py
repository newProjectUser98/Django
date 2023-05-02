from django.shortcuts import render
from .models import *
from django.utils import timezone
from dateutil.relativedelta import relativedelta
import datetime
import pytz
import json
import ast
from rest_framework import viewsets
from tzlocal import get_localzone # $ pip install tzlocal
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
from channels.generic.websocket import WebsocketConsumer
import json

from django.http import HttpResponse
from datetime import datetime

# get local timezone    
local_tz = get_localzone()

from .serializers import *

from django.http import JsonResponse
from .mqttconn import client as mqtt_client
# from waterinn import mqttconn.mqttconn
# from mqttconn.mqtt import client as mqtt_client
# from mqttconn import mqtt
# Create your views here.
# from pymongo import MongoClient
# # connection_string = mongodb+srv://<username>:<password>@<atlas cluster>
# # /<myFirstDatabase>?retryWrites=true&w=majority
# client = pymongo.MongoClient('connection_string')
# db = client['db_name']


# makemyrx_db = client['sample_medicines']
# #collection object
# medicines_collection = makemyrx_db['medicinedetails']
def dateandtime():
    year=datetime.today().strftime('%Y')
    month=datetime.today().strftime('%m')
    day=datetime.today().strftime('%d')
    hour=datetime.now().strftime('%H')
    minit=datetime.now().strftime('%M')
    second=datetime.now().strftime('%S')
    return year,month,day,hour,minit,second
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': "message"
        }))
chatvar = ChatConsumer()


# # import mongoengine
# # mongoengine.connect(db=waterinn, host=localhost:27017, username=username, password=pwd)
class TopicViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = topics.objects.all()

	# specify serializer to be used
	serializer_class = TopicSerializer
        
graphdata = graph_info.objects.last()
print("graph data is:",graphdata.service_name,graphdata.device_id)

servi=graphdata.service_name
ds_id=graphdata.device_id
class YearlyViewset(viewsets.ModelViewSet):
	# define queryset
    # global servi,ds_id
	queryset = repo_yearly.objects.filter(service=servi,device_id=ds_id)
    # graphdata = graph_info.objects.last()
    # print("graph data is:",graphdata.service_name,graphdata.device_id)
    

	# specify serializer to be used
	serializer_class = YearlySerializer
        
class DeviceViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = device_info.objects.all()

	# specify serializer to be used
	serializer_class = DeviceSerializer
        
class keyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = key_info.objects.all()

	# specify serializer to be used
	serializer_class = KeySerializer
        
class HourlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = repo_hourly.objects.all()

	# specify serializer to be used
	serializer_class = HourlySerializer
        
class MonthlyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = repo_monthly.objects.all()

	# specify serializer to be used
	serializer_class = MonthlySerializer
        
class DailyViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = repo_daily.objects.all()

	# specify serializer to be used
	serializer_class = DailySerializer
        
class GraphViewset(viewsets.ModelViewSet):
	# define queryset
	queryset = graph_info.objects.all()

	# specify serializer to be used
	serializer_class = GraphSerializer
class TopicViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = topics.objects.all()

	# specify serializer to be used
	serializer_class = TopicSerializer

def Treat_cnd(request):
    print("hello")
    return render(request,'test.html')

# def publish_message(request):
#     # request_data = json.loads(request.body)
#     # testlist=['test/topic/1','test/topic/2']
#     # msg=input("Enter message:")
#     testlist={'test/topic/1':input("Enter message:"),'test/topic/2':input("Enter message:")}

#     for k,v in testlist.items():
#         rc, mid = mqtt_client.publish(k,v)
#         # data=subscribers.objects.create(Topic=k,msg=v)
#         # data.save()
#     return JsonResponse({'code': rc})

# cnd=0
# spn=0
# tsp=0
# asp=0
# sts=''
# crt=0
# olc=0
# drc=0
# rtl=''
# ttl=''
# lps=''
# hps=''
# dgp=''
# mod=''
# ipv=0
# unv=0
# ovv=0
# nmv=0
# stp=0
# srt=0
# bkt=0
# rst=0
# err=''
# fr1=0
# fr2=0
# ff1=0
# ff2=0
# pos=''
# rmt=0
# cct=0
# srt=0
# bkt=0
# mot=0
# stp=''
# op1=''
# op2=''
# op3=''
# ip1=''
# ip2=''
# ip3=''
# psi=''
# ndv=0
# ntt=''
# nta=0
# tmp=0
# ntp=0
# nov=0
# vl1=0
# vl2=0
# vl3=0
# vl4=0
# re1=0
# re2=0
# re3=0
# re4=0
# p1=0
# p2=0
# p3=0
# p4=0
# cnd=0
# spn=0
# asp=0


def testo(request):
    def on_connect(mqtt_client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            mqtt_client.subscribe('wc/#')
            # topicdata=topics.objects.all()
            # for top in topicdata:
            #     print("topic is:",top)
            # print("Topic data is:",topicdata)
            # topicdata=dict(topicdata)
            # for k, v in topicdata.items():
            #     if k=='Topic_name':
            # mqtt_client.subscribe('django/mqtt')
        else:
            print('Bad connection. Code:', rc)


    def on_message(mqtt_client, userdata, msg):
        # global cnd,spn,tsp,asp,sts,crt,olc,drc,rtl,ttl,lps,hps,dgp,mod,ipv,unv,ovv,nmv,stp,srt,bkt,rst,err,fr1,fr2,ff1,ff2,pos,rmt,cct,srt,bkt,mot,stp,op1,op2,op3,ip1,ip2,ip3,psi,ndv,ntt,nta,tmp,ntp,nov,vl1,vl2,vl3,vl4,re1,re2,re3,re4,p1,p2,p3,p4,cnd,spn,asp

        print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
        jstring=msg.payload
        print("vikaso:",jstring)
        # mydata1=0
        dict_str = jstring.decode("UTF-8")
        print("decoded:",dict_str,type(dict_str))
        rep1=dict_str.replace("}",'')
        rep2=rep1.replace("{",'')
        print('rep1',rep2)
        array_dat = rep2.split(',')
        mydata ={}

        cnd=0
        spn=0
        tsp=0
        asp=0
        sts=''
        crt=0
        olc=0
        drc=0
        rtl=''
        ttl=''
        lps=''
        hps=''
        dgp=''
        mod=''
        ipv=0
        unv=0
        ovv=0
        nmv=0
        stp=0
        srt=0
        bkt=0
        rst=0
        err=''
        fr1=0
        fr2=0
        ff1=0
        ff2=0
        pos=''
        rmt=0
        cct=0
        srt=0
        bkt=0
        mot=0
        stp=''
        op1=''
        op2=''
        op3=''
        ip1=''
        ip2=''
        ip3=''
        psi=''
        ndv=0
        ntt=''
        nta=0
        tmp=0
        ntp=0
        nov=0
        vl1=0
        vl2=0
        vl3=0
        vl4=0
        re1=0
        re2=0
        re3=0
        re4=0
        p1=0
        p2=0
        p3=0
        p4=0

        for loop_data in array_dat:
            print("array_dat",loop_data)
            removed_col = loop_data.split(':')
            print("removed_col",removed_col)
            mydata[removed_col[0]] =removed_col[1]


           

            
            if removed_col[0]=='cnd':
                cnd=removed_col[1]
            elif removed_col[0]=='spn':
                spn=removed_col[1]
            elif removed_col[0]=='tsp':
                tsp=removed_col[1]
            elif removed_col[0]=='asp':
                asp=removed_col[1]
            elif removed_col[0]=='sts':
                sts=removed_col[1]
            elif removed_col[0]=='crt':
                crt=removed_col[1]
            elif removed_col[0]=='olc':
                olc=removed_col[1]
            elif removed_col[0]=='drc':
                drc=removed_col[1]
            elif removed_col[0]=='rtl':
                rtl=removed_col[1]
            elif removed_col[0]=='ttl':
                ttl=removed_col[1]
            elif removed_col[0]=='lps':
                lps=removed_col[1]
            elif removed_col[0]=='hps':
                hps=removed_col[1]
            elif removed_col[0]=='dgp':
                dgp=removed_col[1]
            elif removed_col[0]=='mod':
                mod=removed_col[1]
            elif removed_col[0]=='ipv':
                ipv=removed_col[1]
            elif removed_col[0]=='unv':
                unv=removed_col[1]
            elif removed_col[0]=='ovv':
                ovv=removed_col[1]
            elif removed_col[0]=='nmv':
                nmv=removed_col[1]
            elif removed_col[0]=='stp':
                stp=removed_col[1]
            elif removed_col[0]=='srt':
                srt=removed_col[1]
            elif removed_col[0]=='bkt':
                bkt=removed_col[1]
            elif removed_col[0]=='rst':
                rst=removed_col[1]
            elif removed_col[0]=='err':
                err=removed_col[1]
            elif removed_col[0]=='fr1':
                fr1=removed_col[1]
            elif removed_col[0]=='fr2':
                fr2=removed_col[1]
            elif removed_col[0]=='ff1':
                ff1=removed_col[1]
            elif removed_col[0]=='ff2':
                ff2=removed_col[1]
            elif removed_col[0]=='pos':
                pos=removed_col[1]
            elif removed_col[0]=='rmt':
                rmt=removed_col[1]
            elif removed_col[0]=='cct':
                cct=removed_col[1]
            elif removed_col[0]=='srt':
                srt=removed_col[1]
            elif removed_col[0]=='bkt':
                bkt=removed_col[1]
            elif removed_col[0]=='mot':
                mot=removed_col[1]
            elif removed_col[0]=='stp':
                stp=removed_col[1]
            elif removed_col[0]=='op1':
                op1=removed_col[1]
            elif removed_col[0]=='op2':
                op2=removed_col[1]
            elif removed_col[0]=='op3':
                op3=removed_col[1]
            elif removed_col[0]=='ip1':
                ip1=removed_col[1]
            elif removed_col[0]=='ip2':
                ip2=removed_col[1]
            elif removed_col[0]=='ip3':
                ip3=removed_col[1]
            elif removed_col[0]=='psi':
                psi=removed_col[1]
            elif removed_col[0]=='ndv':
                ndv=removed_col[1]
            elif removed_col[0]=='ntt':
                ntt=removed_col[1]
            elif removed_col[0]=='nta':
                nta=removed_col[1]
            elif removed_col[0]=='tmp':
                tmp=removed_col[1]
            elif removed_col[0]=='ntp':
                ntp=removed_col[1]
            elif removed_col[0]=='nov':
                nov=removed_col[1]
            elif removed_col[0]=='vl1':
                vl1=removed_col[1]
            elif removed_col[0]=='vl2':
                vl2=removed_col[1]
            elif removed_col[0]=='vl3':
                vl3=removed_col[1]
            elif removed_col[0]=='vl4':
                vl4=removed_col[1]
            elif removed_col[0]=='re1':
                re1=removed_col[1]
            elif removed_col[0]=='re2':
                re2=removed_col[1]
            elif removed_col[0]=='re3':
                re3=removed_col[1]
            elif removed_col[0]=='re4':
                re4=removed_col[1]
            elif removed_col[0]=='p1':
                p1=removed_col[1]
            elif removed_col[0]=='p2':
                p2=removed_col[1]
            elif removed_col[0]=='p3':
                p3=removed_col[1]
            elif removed_col[0]=='p4':
                p4=removed_col[1]
          
           
           
           
        print("sts", sts)

        print("mydata before dump:",mydata,type(mydata))  
        mydata1=mydata      
        mydata = json.dumps(mydata, indent = 4) 
        # mydata = ast.literal_eval(mydata)
        # mydata = ast.literal_eval(dict_str)
        print("final data:",mydata,type(mydata))
        mydatadict=json.loads(mydata)
        print(mydatadict,type(mydatadict))
        hmq=msg.topic
        hmqm_split=hmq.split('/')
        print(hmqm_split)
        device_id=hmqm_split[1]
        msg_type=hmqm_split[2]
        components=hmqm_split[3]
        print("*"*10,mydata)
        od=mydata.strip()
        print("#"*10,od)
        repo_histobj=repo_history.objects.create(device_id=device_id,message_type=msg_type,component_name=components,msg_json=mydata1)
        repo_histobj.save()
        get_device_id=repo_latestdata.objects.all()
        # print(get_device_id.)
        device_idlist=[]
        tds1={}
        rwp={}
        hpp={}
        panel={}
        flowsen={}
        ampv1={}
        ampv2={}
        ampv3={}
        ampv4={}
        ampv5={}
        atm={}
        tap1={}
        tap2={}
        tap3={}
        tap4={}
        consen={}

        monthset=set()
        print("device id is:",device_id,type(device_id))
        for did in get_device_id:
             s=str(did.device_id)
             if device_id == s:
                print("latest data is:",did.device_id)
                print("latest data is:",did.message_type)
                tds=did.cnd_tds
                tds1=tds
                # tdsstr=(str(tds))
                print("tdso data is:",tds,type(tds))
                print("latest data is:",did.cnd_tds,type(did.cnd_tds))
                rwp=did.rwp
                print("latest data is:",did.rwp)
                hpp=did.hpp
                print("latest data is:",did.hpp)
                panel=did.panel
                print("latest data is:",did.panel)
                flowsen=did.flowsen
                print("latest data is:",did.flowsen)
                ampv1=did.ampv1
                print("latest data is:",did.ampv1)
                ampv2=did.ampv2
                print("latest data is:",did.ampv2)
                ampv3=did.ampv3
                print("latest data is:",did.ampv3)
                ampv4=did.ampv4
                print("latest data is:",did.ampv4)
                ampv5=did.ampv5
                print("latest data is:",did.ampv5)
                atm=did.atm
                print("latest data is:",did.atm)
                tap1=did.tap1
                print("latest data is:",did.tap1)
                tap2=did.tap2
                print("latest data is:",did.tap2)
                tap3=did.tap3
                print("latest data is:",did.tap3)
                tap4=did.tap4
                print("latest data is:",did.tap4)
                consen=did.consen
                print("latest data is:",did.consen)
             device_idlist.append(s)
             print(device_idlist)
        print("component is:",components)
        service_list=[]
        repoyearly=repo_yearly.objects.all()
        for ry in repoyearly:
                ser=ry.service
                service_list.append(ser)
                print("service is:",ser)
        print("out of for loop")
        olddata={}
        hourset=set()
        if 'cnd_tds'== components:
                # com=cl
                print("in cndtds")
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,cnd_tds=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, cnd_tds=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            print("latest data is:",did.device_id)
                            print("latest data is:",did.message_type)
                            tds=did.cnd_tds
                            tds1=tds
                            # tdsstr=(str(tds))
                            print("tdso data is:",tds,type(tds))
                            print("latest data is:",did.cnd_tds,type(did.cnd_tds))

                    klist = list(tds1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tds1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, cnd_tds=olddata)
                
                dd=dateandtime()  
                print("$$$$$$$dd is:",dd,type(dd)) 
                print(dd[0])
                ds=treat_cnd_tds_sen.objects.create(device_id=device_id,message_type=msg_type,cnd=cnd,spn=spn,tsp=tsp,asp=asp,year=dd[0],month=dd[1],day=dd[2],hour=dd[3],minit=dd[4],second=dd[5])
                ds.save()
                #yearly data
                # end_date = timezone.localtime(timezone.now()).replace(tzinfo=pytz.timezone('America/Guatemala')) 
                # end_date = local_tz.localize(datetime.datetime.now())
                # print("first end date is:",end_date)
                # end_date = end_date.replace(tzinfo=local_tz)

                # print("replaced date :",end_date)
                # # start_date = end_date + relativedelta(hours=-8760)
                # start_date = end_date + relativedelta(years=-1)
                # print("staredate is:",start_date)
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            print("cnds is:",cnds)
                            sums=sums+cnds
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                else:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    yr_data.save()
                               


                #month
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            print("cnds is:",cnds)
                            sums=sums+cnds
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                if hr:
                    yr_data=repo_monthly.objects.filter(year=dd[0],month=dd[1],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                else:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    yr_data.save()
                
                
                # day
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            print("cnds is:",cnds)
                            sums=sums+cnds
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                if hr:
                    yr_data=repo_daily.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                
                
                # Hour
                yrdata=treat_cnd_tds_sen.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            cnds=yr.cnd
                            print("cnds is:",cnds)
                            sums=sums+cnds
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                if hr:
                    yr_data=repo_hourly.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id).update(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='cnd_tds_cnd',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                  
        try:    
            if 'rwp'==components:
                    if device_id not in device_idlist:
                        repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,rwp=mydata1)
                    else:
                        repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, rwp=mydata1)

                        get_device_id=repo_latestdata.objects.all()
                        for did in get_device_id:
                            s=str(did.device_id)
                            if device_id == s:
                                rwp=did.rwp
                                # rwp=rwp
                        klist = list(rwp.keys())
                        print("klist is:",klist)
                        mydatakey = list(mydata1.keys())
                        print("mydatakey:",mydatakey)
                        for k,v in rwp.items():
                            if k not in mydatakey:
                                olddata.update({k:v})
                                
                        mydata5=olddata.update(mydata1)    
                        print("old data is:",olddata) # add/update keys in mydata1 to olddata
                        repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, rwp=olddata)

                    # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,rwp=mydata1)
                    ds=treat_rwp.objects.create(device_id=device_id,message_type=msg_type,sts=sts,crt=crt,olc=olc,drc=drc,spn=spn)
                    ds.save()
                    end_date = local_tz.localize(datetime.datetime.now())
                    print("first end date is:",end_date)
                    end_date = end_date.replace(tzinfo=local_tz)
                    print("replaced date :",end_date)
                    # start_date = end_date + relativedelta(hours=-8760)
                    start_date = end_date + relativedelta(years=-1)
                    print("staredate is:",start_date)
                    yrdata=treat_rwp.objects.filter(year=dd[0],device_id=device_id)
                    count=0
                    sums=0
                    avgs = 0
                    if yrdata:
                        for yr in yrdata:
                            yr_d_id=yr.device_id
                            if yr_d_id == device_id:
                                crt=yr.crt
                                print("crt is:",crt)
                                sums=sums+crt
                                count=count+1
                                print("sums is:",sums)
                                print("count is:",count)
                        avgs=sums/count
                        print('avg is:',avgs)
                    hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                    if hr:
                        yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    else:
                        yr_data=repo_yearly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                        yr_data.save()
                                

                    # yrdata=treat_rwp.objects.filter(created_at__range=(start_date, end_date))
                    # count=0
                    # sums=0
                    # for yr in yrdata:
                    #     yr_d_id=yr.device_id
                    #     if yr_d_id == device_id:
                    #         crt=yr.crt
                    #         print("crt is:",crt)
                    #         sums=sums+crt
                    #         count=count+1
                    #         print("sums is:",sums)
                    #         print("count is:",count)
                    # avgs=sums/count
                    # print('avg is:',avgs)
                    # if device_id not in device_idlist and 'rwp_crt'  not in service_list :
                    #     yr_data=repo_yearly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    #     yr_data.save()
                    # else:
                    #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    

                    # month
                    yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                    count=0
                    sums=0
                    avgs = 0
                    if yrdata:
                        for yr in yrdata:
                            yr_d_id=yr.device_id
                            if yr_d_id == device_id:
                                crt=yr.crt
                                print("crt is:",crt)
                                sums=sums+crt
                                count=count+1
                                print("sums is:",sums)
                                print("count is:",count)
                        avgs=sums/count
                    hr=repo_monthly.objects.filter(year=dd[0],device_id=device_id)
                    if hr:
                        yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    else:
                        yr_data=repo_monthly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                        yr_data.save()
                    
                    # end_date = local_tz.localize(datetime.datetime.now())
                    # print("first end date is:",end_date)
                    # end_date = end_date.replace(tzinfo=local_tz)
                    # print("replaced date :",end_date)
                    # # start_date = end_date + relativedelta(hours=-8760)
                    # start_date = end_date + relativedelta(month=-1)
                    # print("staredate is:",start_date)
                    # yrdata=treat_rwp.objects.filter(created_at__range=(start_date, end_date))
                    # count=0
                    # sums=0
                    # for yr in yrdata:
                    #     yr_d_id=yr.device_id
                    #     if yr_d_id == device_id:
                    #         crt=yr.crt
                    #         print("crt is:",crt)
                    #         sums=sums+crt
                    #         count=count+1
                    #         print("sums is:",sums)
                    #         print("count is:",count)
                    # avgs=sums/count
                    # print('avg is:',avgs)
                    # if device_id not in device_idlist:
                    #     yr_data=repo_monthly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    #     yr_data.save()
                    # else:
                    #     yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    
                    # day
                    yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                    count=0
                    sums=0
                    avgs = 0
                    if yrdata:
                        for yr in yrdata:
                            yr_d_id=yr.device_id
                            if yr_d_id == device_id:
                                crt=yr.crt
                                print("crt is:",crt)
                                sums=sums+crt
                                count=count+1
                                print("sums is:",sums)
                                print("count is:",count)
                        avgs=sums/count
                    hr=repo_daily.objects.filter(year=dd[0],device_id=device_id)
                    if hr:
                        yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                    else:
                        yr_data=repo_daily.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                        yr_data.save()
                    
                    # end_date = local_tz.localize(datetime.datetime.now())
                    # print("first end date is:",end_date)
                    # end_date = end_date.replace(tzinfo=local_tz)
                    # print("replaced date :",end_date)
                    # # start_date = end_date + relativedelta(hours=-8760)
                    # start_date = end_date + relativedelta(days=-1)
                    # print("staredate is:",start_date)
                    # yrdata=treat_rwp.objects.filter(created_at__range=(start_date, end_date))
                    # count=0
                    # sums=0
                    # for yr in yrdata:
                    #     yr_d_id=yr.device_id
                    #     if yr_d_id == device_id:
                    #         crt=yr.crt
                    #         print("crt is:",crt)
                    #         sums=sums+crt
                    #         count=count+1
                    #         print("sums is:",sums)
                    #         print("count is:",count)
                    # avgs=sums/count
                    # print('avg is:',avgs)
                    # if device_id not in device_idlist and 'rwp_crt'  not in service_list :
                    #     yr_data=repo_daily.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    #     yr_data.save()
                    # else:
                    #     yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    
                    # hour
                    yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],hour=dd[3],device_id=device_id)
                    count=0
                    sums=0
                    avgs = 0
                    if yrdata:
                        for yr in yrdata:
                            yr_d_id=yr.device_id
                            if yr_d_id == device_id:
                                crt=yr.crt
                                print("crt is:",crt)
                                sums=sums+crt
                                count=count+1
                                print("sums is:",sums)
                                print("count is:",count)
                        avgs=sums/count
                    
                    hr=repo_hourly.objects.filter(year=dd[0],device_id=device_id)
                    if hr:
                        yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                    else:
                        yr_data=repo_hourly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,hour=dd[3],month=dd[1],year=dd[0],day=dd[2])
                        yr_data.save()
                    
                    # end_date = local_tz.localize(datetime.datetime.now())
                    # print("first end date is:",end_date)
                    # end_date = end_date.replace(tzinfo=local_tz)
                    # print("replaced date :",end_date)
                    # # start_date = end_date + relativedelta(hours=-8760)
                    # start_date = end_date + relativedelta(hours=-1)
                    # print("staredate is:",start_date)
                    # yrdata=treat_rwp.objects.filter(created_at__range=(start_date, end_date))
                    # count=0
                    # sums=0
                    # for yr in yrdata:
                    #     yr_d_id=yr.device_id
                    #     if yr_d_id == device_id:
                    #         crt=yr.crt
                    #         print("crt is:",crt)
                    #         sums=sums+crt
                    #         count=count+1
                    #         print("sums is:",sums)
                    #         print("count is:",count)
                    # avgs=sums/count
                    # print('avg is:',avgs)
                    # if device_id not in device_idlist and 'rwp_crt'  not in service_list :
                    #     yr_data=repo_hourly.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
                    #     yr_data.save()
                    # else:
                    #     yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs)
        except Exception as e:
                # await self.send(text_data=json.dumps({
                #     'message': e
                # }))
                # asyncio.run(chatvar.receive(e))
                print("error ==>", e)
                # return e            
        if 'hpp'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,hpp=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, hpp=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            hpp=did.hpp
                    klist = list(hpp.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in hpp.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, hpp=olddata)

                
                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,hpp=mydata1)
                # repo_latestobj.save()

                yrdata=treat_hpp.objects.filter(year=dd[0],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            crt=yr.crt
                            print("crt is:",crt)
                            sums=sums+crt
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                    print('avg is:',avgs)
                hr=repo_yearly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                else:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    yr_data.save()
                            

                # ds=treat_hpp.objects.create(device_id=device_id,message_type=msg_type,sts=sts,crt=crt,olc=olc,drc=drc,spn=spn)
                # ds.save()
                # end_date = local_tz.localize(datetime.datetime.now())
                # print("first end date is:",end_date)
                # end_date = end_date.replace(tzinfo=local_tz)
                # print("replaced date :",end_date)
                # # start_date = end_date + relativedelta(hours=-8760)
                # start_date = end_date + relativedelta(years=-1)
                # print("staredate is:",start_date)
                # yrdata=treat_hpp.objects.filter(created_at__range=(start_date, end_date))
                # count=0
                # sums=0
                # for yr in yrdata:
                #     yr_d_id=yr.device_id
                #     if yr_d_id == device_id:
                #         crt=yr.crt
                #         print("crt is:",crt)
                #         sums=sums+crt
                #         count=count+1
                #         print("sums is:",sums)
                #         print("count is:",count)
                # avgs=sums/count
                # print('avg is:',avgs)
                # if device_id not in device_idlist:
                #     yr_data=repo_yearly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                #     yr_data.save()
                # else:
                #     yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                
                # month
                yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            crt=yr.crt
                            print("crt is:",crt)
                            sums=sums+crt
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_monthly.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                else:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0])
                    yr_data.save()
                
                # end_date = local_tz.localize(datetime.datetime.now())
                # print("first end date is:",end_date)
                # end_date = end_date.replace(tzinfo=local_tz)
                # print("replaced date :",end_date)
                # # start_date = end_date + relativedelta(hours=-8760)
                # start_date = end_date + relativedelta(month=-1)
                # print("staredate is:",start_date)
                # yrdata=treat_hpp.objects.filter(created_at__range=(start_date, end_date))
                # count=0
                # sums=0
                # for yr in yrdata:
                #     yr_d_id=yr.device_id
                #     if yr_d_id == device_id:
                #         crt=yr.crt
                #         print("crt is:",crt)
                #         sums=sums+crt
                #         count=count+1
                #         print("sums is:",sums)
                #         print("count is:",count)
                # avgs=sums/count
                # print('avg is:',avgs)
                # if device_id not in device_idlist:
                #     yr_data=repo_monthly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                #     yr_data.save()
                # else:
                #     yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                
                # day
                yrdata=treat_rwp.objects.filter(year=dd[0],month=dd[1],day=dd[2],device_id=device_id)
                count=0
                sums=0
                avgs = 0
                if yrdata:
                    for yr in yrdata:
                        yr_d_id=yr.device_id
                        if yr_d_id == device_id:
                            crt=yr.crt
                            print("crt is:",crt)
                            sums=sums+crt
                            count=count+1
                            print("sums is:",sums)
                            print("count is:",count)
                    avgs=sums/count
                hr=repo_daily.objects.filter(year=dd[0],device_id=device_id)
                if hr:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                else:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='rwp_crt',sum=sums,count=count,avg=avgs,month=dd[1],year=dd[0],day=dd[2])
                    yr_data.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_hpp.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        crt=yr.crt
                        print("crt is:",crt)
                        sums=sums+crt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_hpp.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        crt=yr.crt
                        print("crt is:",crt)
                        sums=sums+crt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='hpp_crt',sum=sums,count=count,avg=avgs)
                
        if 'panel'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,panel=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, panel=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            panel=did.panel
                    klist = list(panel.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in panel.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, panel=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,panel=mydata1)
                # repo_latestobj.save()
                ds=treat_panel.objects.create(device_id=device_id,message_type=msg_type,sts=sts,rtl=rtl,ttl=ttl,lps=lps,hps=hps,dgp=dgp,mod=mod,ipv=ipv,unv=unv,ovv=ovv,spn=spn,nmv=nmv,stp=stp,srt=srt,bkt=bkt,rst=rst,err=err)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_panel.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ipv=yr.ipv
                        print("ipv is:",ipv)
                        sums=sums+ipv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_panel.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ipv=yr.ipv
                        print("ipv is:",ipv)
                        sums=sums+ipv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_panel.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ipv=yr.ipv
                        print("ipv is:",ipv)
                        sums=sums+ipv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_panel.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ipv=yr.ipv
                        print("ipv is:",ipv)
                        sums=sums+ipv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='panel_ipv',sum=sums,count=count,avg=avgs)
                
        if 'flowsen'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,flowsen=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            flowsen=did.flowsen

                    klist = list(flowsen.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in flowsen.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,flowsen=mydata1)
                # repo_latestobj.save() 
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr1=yr.fr1
                        print("fr1 is:",fr1)
                        sums=sums+fr1
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr2=yr.fr2
                        print("fr2 is:",fr2)
                        sums=sums+fr2
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                 
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr1=yr.fr1
                        print("fr1 is:",fr1)
                        sums=sums+fr1
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr2=yr.fr2
                        print("fr2 is:",fr2)
                        sums=sums+fr2
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr1=yr.fr1
                        print("fr1 is:",fr1)
                        sums=sums+fr1
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr2=yr.fr2
                        print("fr2 is:",fr2)
                        sums=sums+fr2
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr1=yr.fr1
                        print("fr1 is:",fr1)
                        sums=sums+fr1
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr1',sum=sums,count=count,avg=avgs)
                ds=treat_flowsen.objects.create(device_id=device_id,message_type=msg_type,fr1=fr1,fr2=fr2,ff1=ff1,ff2=ff2)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_flowsen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        fr2=yr.fr2
                        print("fr2 is:",fr2)
                        sums=sums+fr2
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='flowsen_fr2',sum=sums,count=count,avg=avgs)
                

        if 'ampv1'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv1=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv1=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv1=did.ampv1
                    klist = list(ampv1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv1=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv1=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv1.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv1.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv1_cct',sum=sums,count=count,avg=avgs)
                
        if 'ampv2'==components:
                # com=cl

                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv2=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv2=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv2=did.ampv2
                    klist = list(ampv2.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv2.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv2=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv2=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv2.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv2.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv2_cct',sum=sums,count=count,avg=avgs)
                
        if 'ampv3'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv3=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv3=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv3=did.ampv3
                    klist = list(ampv3.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv3.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv3=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv3=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv3.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv3.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv3_cct',sum=sums,count=count,avg=avgs)
                
        if 'ampv4'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv4=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv4=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv4=did.ampv4
                    klist = list(ampv4.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv4.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv4=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv4=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv4.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
            #    month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv4.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv4_cct',sum=sums,count=count,avg=avgs)
               
        if 'ampv5'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,ampv5=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv5=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            ampv5=did.ampv5
                    klist = list(ampv5.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in ampv5.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, ampv5=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,ampv5=mydata1)
                # repo_latestobj.save()
                ds=treat_ampv5.objects.create(device_id=device_id,message_type=msg_type,pos=pos,rmt=rmt,cct=cct,srt=srt,bkt=bkt,rst=rst,mot=mot,stp=stp,op1=op1,op2=op2,op3=op3,ip1=ip1,ip2=ip2,ip3=ip3,psi=psi)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        rmt=yr.rmt
                        print("rmt is:",rmt)
                        sums=sums+rmt
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_rmt',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=treat_ampv5.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cct=yr.cct
                        print("cct is:",cct)
                        sums=sums+cct
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='ampv5_cct',sum=sums,count=count,avg=avgs)
               
        if 'atm'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,atm=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, atm=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            atm=did.atm
                    klist = list(atm.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in atm.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, atm=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,atm=mydata1)
                # repo_latestobj.save() 
                ds=disp_atm.objects.create(device_id=device_id,message_type=msg_type,sts=sts,ndv=ndv,ntt=ntt,nta=nta,tmp=tmp,ntp=ntp,nov=nov,vl1=vl1,vl2=vl2,vl3=vl3,vl4=vl4,re1=re1,re2=re2,re3=re3,re4=re4)
                ds.save()
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ndv=yr.ndv
                        print("ndv is:",ndv)
                        sums=sums+ndv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        nta=yr.nta
                        print("nta is:",nta)
                        sums=sums+nta
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        tmp=yr.tmp
                        print("tmp is:",tmp)
                        sums=sums+tmp
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
            #    month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ndv=yr.ndv
                        print("ndv is:",ndv)
                        sums=sums+ndv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        nta=yr.nta
                        print("nta is:",nta)
                        sums=sums+nta
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        tmp=yr.tmp
                        print("tmp is:",tmp)
                        sums=sums+tmp
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                
                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ndv=yr.ndv
                        print("ndv is:",ndv)
                        sums=sums+ndv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        nta=yr.nta
                        print("nta is:",nta)
                        sums=sums+nta
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        tmp=yr.tmp
                        print("tmp is:",tmp)
                        sums=sums+tmp
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        ndv=yr.ndv
                        print("ndv is:",ndv)
                        sums=sums+ndv
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_ndv',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        nta=yr.nta
                        print("nta is:",nta)
                        sums=sums+nta
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_nta',sum=sums,count=count,avg=avgs)
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=disp_atm.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        tmp=yr.tmp
                        print("tmp is:",tmp)
                        sums=sums+tmp
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='atm_tmp',sum=sums,count=count,avg=avgs)
               
        if 'tap1'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap1=mydata1)
                else:

                    # repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, flowsen=mydata1)
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap1=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap1=did.tap1
                    klist = list(tap1.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap1.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap1=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap1=mydata1)
                # repo_latestobj.save()  
                ds=disp_tap1.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4)
                ds.save()
        if 'tap2'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap2=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap2=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap2=did.tap2
                    klist = list(tap2.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap2.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap2=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap2=mydata1)
                # repo_latestobj.save()
                ds=disp_tap2.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4)
                ds.save()
        if 'tap3'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap3=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap3=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap3=did.tap3
                    
                    klist = list(tap3.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap3.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap3=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap3=mydata1)
                # repo_latestobj.save()   
                ds=disp_tap3.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4)
                ds.save()
        if 'tap4'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,tap4=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap4=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            tap4=did.tap4
                    klist = list(tap4.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in tap4.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, tap4=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,tap4=mydata1)
                # repo_latestobj.save()
                ds=disp_tap4.objects.create(device_id=device_id,message_type=msg_type,p1=p1,p2=p2,p3=p3,p4=p4)
                ds.save()
        if 'consen'==components:
                # com=cl
                if device_id not in device_idlist:
                     repo_latestdata.objects.create(device_id=device_id,message_type=msg_type,consen=mydata1)
                else:
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, consen=mydata1)

                    get_device_id=repo_latestdata.objects.all()
                    for did in get_device_id:
                        s=str(did.device_id)
                        if device_id == s:
                            consen=did.consen
                    klist = list(consen.keys())
                    print("klist is:",klist)
                    mydatakey = list(mydata1.keys())
                    print("mydatakey:",mydatakey)
                    for k,v in consen.items():
                         if k not in mydatakey:
                              olddata.update({k:v})
                              
                    mydata5=olddata.update(mydata1)    
                    print("old data is:",olddata) # add/update keys in mydata1 to olddata
                    repo_latestobj = repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id, message_type=msg_type, consen=olddata)

                # repo_latestobj=repo_latestdata.objects.filter(device_id=device_id).update(device_id=device_id,message_type=msg_type,consen=mydata1)
                # repo_latestobj.save()
                ds=disp_consen.objects.create(device_id=device_id,message_type=msg_type,cnd=cnd,spn=spn,asp=asp)
                ds.save()  
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(years=-1)
                print("staredate is:",start_date)
                yrdata=disp_consen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cnd=yr.cnd
                        print("cnd is:",cnd)
                        sums=sums+cnd
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_yearly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)

                # month
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(month=-1)
                print("staredate is:",start_date)
                yrdata=disp_consen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cnd=yr.cnd
                        print("cnd is:",cnd)
                        sums=sums+cnd
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_monthly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_monthly.objects.filter(device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)

                # day
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(days=-1)
                print("staredate is:",start_date)
                yrdata=disp_consen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cnd=yr.cnd
                        print("cnd is:",cnd)
                        sums=sums+cnd
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_daily.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_daily.objects.filter(device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)

                # hour
                end_date = local_tz.localize(datetime.datetime.now())
                print("first end date is:",end_date)
                end_date = end_date.replace(tzinfo=local_tz)
                print("replaced date :",end_date)
                # start_date = end_date + relativedelta(hours=-8760)
                start_date = end_date + relativedelta(hours=-1)
                print("staredate is:",start_date)
                yrdata=disp_consen.objects.filter(created_at__range=(start_date, end_date))
                count=0
                sums=0
                for yr in yrdata:
                    yr_d_id=yr.device_id
                    if yr_d_id == device_id:
                        cnd=yr.cnd
                        print("cnd is:",cnd)
                        sums=sums+cnd
                        count=count+1
                        print("sums is:",sums)
                        print("count is:",count)
                avgs=sums/count
                print('avg is:',avgs)
                if device_id not in device_idlist:
                    yr_data=repo_hourly.objects.create(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)
                    yr_data.save()
                else:
                    yr_data=repo_hourly.objects.filter(device_id=device_id).update(device_id=device_id,service='consen_cnd',sum=sums,count=count,avg=avgs)
                  
        
    # end_date = timezone.localtime(timezone.now())
    # end_date = local_tz.localize(datetime.datetime(2023, 4, 20, 0, 0, 0, 0))
    # end_date = local_tz.localize(datetime.datetime.now())
    # print("first end date is:",end_date)
    # end_date = end_date.replace(tzinfo=local_tz)
    # print("replaced date :",end_date)
    # # start_date = end_date + relativedelta(hours=-8760)
    # start_date = end_date + relativedelta(years=-1)
    # print("staredate is:",start_date)
    # yrdata=treat_cnd_tds_sen.objects.filter(created_at__range=(start_date, end_date),device_id='127')
    # # print("yr data is:",yrdata,type(yrdata))

    # count=0
    # sums=0
    # for yr in yrdata:
    #     device_id=yr.device_id
    #     if device_id == '127':
    #         print("device is is:",device_id)
    #         cnds=yr.cnd
    #         print("cnds is:",cnds)
    #         sums=sums+cnds
    #         count=count+1
    # avgs=sums/count
    # print('avg is:',avgs)
    # yr_data=repo_yearly.objects.filter(device_id=device_id).update(device_id=device_id,service='cnd',sum=sums,count=count,avg=avgs)
                     
    # yr_data=repo_yearly.objects.create(device_id='127',service='cnd',sum=sums,count=count,avg=avgs)
    # yr_data.save()



    # client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    # client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
    # client.connect(
    #     host=settings.MQTT_SERVER,
    #     port=settings.MQTT_PORT,
    #     keepalive=settings.MQTT_KEEPALIVE
    # )
    # mqtt_client.connect('broker.example.com', 1883)

    # Start the client loop
    mqtt_client.loop_forever()

