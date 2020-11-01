from dlw.models import *
import time
import re
import datetime,calendar
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from django.db.models import Q

from datetime import date
from django.db import connection
cursor = connection.cursor()


def shed_dashboard(request,type1 = 'default'):
  
    '''    if request.method == 'POST':
        submitvalue = request.POST.get('submit')
        if submitvalue == 'Save_Actual':
            ref_no = request.POST.get('ref_no2')
            date = request.POST.get('date1')
            s=str(date)
            date ='' . join(map(str,s))
            date = date[6:10] + "-" + date[3:5] + "-" + date[0:2]
            remark = request.POST.get('remark')
            result = request.POST.get('select')
            warranty_lodge.objects.filter(ref_no=ref_no).update(status="6",date_verify=date,remark_verify=remark,result_verify=result)
        if submitvalue == 'Save_Actual1':
            ref_no = request.POST.get('refno_upload')
            file11 = request.FILES['file11']
            fs = FileSystemStorage()
            filename = fs.save(file11.name, file11)
            dateupload = request.POST.get('dateupload')
            s=str(dateupload)
            date ='' . join(map(str,s))
            dateupload = date[6:10] + "-" + date[3:5] + "-" + date[0:2]
            remarkupload = request.POST.get('remarkupload')
            warranty_lodge.objects.filter(ref_no=ref_no).update(status="7",file11=file11,date_upload=dateupload,remark_upload=remarkupload)
    if type1 == 'verify':
        obj = warranty_lodge.objects.filter(status="5",zone=zone1,shed=shed1).order_by('compl_date')
    elif type1 == 'pending':
        obj = warranty_lodge.objects.filter((Q(status="1")|Q(status="1")| Q(status="2")|Q(status="3")|Q(status="4")),zone=zone1,shed=shed1).order_by('compl_date')
    elif type1 == 'upload':
        obj = warranty_lodge.objects.filter(status="6",zone=zone1,shed=shed1).order_by('compl_date')
    elif type1 == 'closed_cases':
            obj = warranty_lodge.objects.filter((Q(status="-1")| Q(status="8")),zone=zone1,shed=shed1).order_by('compl_date')
    else:
        obj = warranty_lodge.objects.filter(zone=zone1,shed=shed1).order_by('compl_date')
    for i in obj:
            i.compl_date = i.compl_date.strftime("%d-%m-%Y")
            i.date_fail = i.date_fail.strftime("%d-%m-%Y")
            if i.date_visit:
                i.date_visit = i.date_visit.strftime("%d-%m-%Y")
            if i.date_lr:
                i.date_lr = i.date_lr.strftime("%d-%m-%Y")
    context={
        'obj':obj,
        'username':user1

    }
    '''
    context={}
    return render(request,'shed_dashboard.html',context)


global cust_user
def login_cust(request):
    print("loginpage")
    context={}

    if request.method=='POST':
        print("ander")
        submitvalue=''
        if submitvalue=='':
            idd=request.POST.get('username')
            global cust_user
            
            passw=request.POST.get('pass')
            print("id=",idd,"pass=",passw)
            obj=list(Userall.objects.filter(userid=idd,pwd=passw).values('type_of_user'))
            if obj:
                global cust_user
                cust_user=idd
                
                if(obj[0]['type_of_user']=='Customer' or obj[0]['type_of_user']=='user'):
                    data1=list(Items.objects.all().values('item_id','name','description','pic','rate','quan','color','size'))
                    
                    cust_user=idd
                    tbl=[]
                    for i in range(0,len(data1),2):
                        lst=[]
                        if(i+2<=len(data1)):
                            lst.append(data1[i])
                            lst.append(data1[i+1])
                            tbl.append(lst)
                        else:
                            lst.append(data1[i])
                            tbl.append(lst)
                    print(tbl," is tbl")
                    context={'user':idd,'table_data':tbl,}
                    return render(request,"items.html",context)
                if(obj[0]['type_of_user']=='Supplier'):
                    global username1
                    username1=idd
                    print("Suppp",username1)
                    return redirect('shed_dashboard')
                    #return render(request,"shed_dashboard.html",context)
                if(obj[0]['type_of_user']=='Admin'):
                    data1=list(Items.objects.all().values('item_id','name','description','pic','rate','quan','color','size'))
                    
                    tbl=[]
                    for i in range(0,len(data1),2):
                        lst=[]
                        if(i+2<=len(data1)):
                            lst.append(data1[i])
                            lst.append(data1[i+1])
                            tbl.append(lst)
                        else:
                            lst.append(data1[i])
                            tbl.append(lst)
                    print(tbl," is tbl")
                    context={'user':idd,'table_data':tbl,'type':'Admin'}
                    
                    return render(request,"items_admin.html",context)
                

    return render(request,"index.html",context)



def admin_item(request):
    data1=list(Items.objects.all().values('item_id','name','description','pic','rate','quan','color','size'))
                    
    tbl=[]
    for i in range(0,len(data1),2):
        lst=[]
        if(i+2<=len(data1)):
            lst.append(data1[i])
            lst.append(data1[i+1])
            tbl.append(lst)
        else:
            lst.append(data1[i])
            tbl.append(lst)
            print(tbl," is tbl")
    context={'user':'admin','table_data':tbl,'type':'Admin'}
                    
    return render(request,"items_admin.html",context)
                

def showdetail(request,itemid = '0000',userid=''):
    print(request,"\n REQUEST -----")
    if itemid!='0000':
        print(itemid,'item not zero')
        data1=list(Items.objects.filter(item_id=itemid).values('item_id','name','description','pic','rate','quan','color','size'))
        print(len(data1))
        if data1[0]['item_id']:
            idd=data1[0]['item_id']
        #global cust_user
        print(userid,'is userid')

        if userid==None or userid=='None':
            cust_user=''
        else:
            cust_user=userid
        context={'user':cust_user,
            'data':data1,
            'idd':itemid,
        }
        if cust_user=='':
            print("NO username")
            return render(request,'showitemdetail.html',context)
        

    if itemid=='0000':
        data1=list(Items.objects.all().values('item_id','name','description','pic','rate','quan','color','size'))
        
        tbl=[]
        for i in range(0,len(data1),2):
            lst=[]
            if(i+2<=len(data1)):
                lst.append(data1[i])
                lst.append(data1[i+1])
                tbl.append(lst)
            else:
                lst.append(data1[i])
                tbl.append(lst)
                print(tbl," is tbl")
        context={'user':None,'table_data':tbl,}
        return render(request,"items.html",context)
    submitvalue=request.POST.get('submit')
    print(request.POST,'is post')
    if submitvalue=='Book Now':
        idd=request.POST.get('idd')
        userid=request.POST.get('userid')
        print(idd,itemid," id product idd")
        obj1=list(Userall.objects.filter(userid=userid).values('phone','email','addr','name'))
        obj2=list(Items.objects.filter(item_id=itemid).values('supp_id','rate'))
        if len(obj1) and len(obj2) :
            
            context={'user':userid,
                'data':data1,
                'idd':itemid,
                'suppid':obj2[0]['supp_id'],
                    'phone':obj1[0]['phone'],
                    'email':obj1[0]['email'],
                    'address':obj1[0]['addr'],
                    'rate':obj2[0]['rate'],
                    'name':obj1[0]['name'],

                }
        return render(request,'booking.html',context)
    obj=list(Userall.objects.filter(userid=userid).values('type_of_user'))
    print(obj,"is obj")
    if obj:
        #=='Admin':
        context['type']=obj[0]['type_of_user']
    print(context)
    return render(request,'showitemdetail.html',context)


def rental_register(request):
    context={}
    print("rental register")
    if request.method=="POST":
        if(request.POST.get('submit')=='Register'):
            id=request.POST.get("userid")
            name=request.POST.get("name")
            email=request.POST.get("email")
            passw=request.POST.get("passw")
            phone=request.POST.get("phone")
            tuser=request.POST.get("tuser")
            add=request.POST.get("add")
            Userall.objects.create(userid=id,name=name,email=email,pwd=passw,phone=phone,addr=add,type_of_user=tuser)
            print('Registered...')
            context={'msg':"Successfully Registered"}


    return render(request,'rental_register.html',context)

def booking(request,itemid=''):
    print(request)
    context={'user':'cust_user',
            'idd':itemid,
    }
    
    #print(cc,' is user id -- Booking')
    submitvalue=request.POST.get('submit')
    if submitvalue=='Book Now':
        #idd=request.POST.get('idd')
        #print(idd," id product idd")
        obj2=list(Items.objects.filter(item_id=itemid).values('supp_id','rate'))
        useridd=request.POST.get('userid')
        suppidd=request.POST.get('suppid')
        f_date=request.POST.get('f_date')
        obj1=list(Userall.objects.filter(userid=useridd).values('phone','email','addr'))
        
        t_date=request.POST.get('t_date')
        f_date=f_date.split('-')
        f_date='-'.join(f_date[::-1])
        t_date=t_date.split('-')
        t_date='-'.join(t_date[::-1])
        from datetime import datetime
        from datetime import date

        to_date = date.today()
        Booking.objects.create(supp_id=suppidd,cust_id=useridd,item_id=itemid,status='0',from_date=f_date,to_date=t_date,book_date=to_date)

        ###if(count * from table_name where end_date_entered>=start_date or start_date_entered<=end_date and item_id_entered==item_id)==0 then "ok" else "reject"
        if len(obj1) and len(obj2) :
            
            context={'user':useridd,
                
                'idd':itemid,
                'suppid':obj2[0]['supp_id'],
                    'phone':obj1[0]['phone'],
                    'email':obj1[0]['email'],
                    'address':obj1[0]['addr'],
                    'rate':obj2[0]['rate'],
                'msg':"Successfully Booked",
                }
            return render(request,'booking.html',context)
    return render(request,'booking.html',context)

def check_avail_booking(request):
    if request.method=='GET' and request.is_ajax():
        ###if(count * from table_name where end_date_entered>=start_date or start_date_entered<=end_date and item_id_entered==item_id)==0 then "ok" else "reject"
        
        f=request.GET.get('f_date')
        t=request.GET.get('t_date')
        item=request.GET.get('itemid')
        f=f.split('-')
        f='-'.join(f[::-1])
        t=t.split('-')
        t='-'.join(t[::-1])
        suppid=request.GET.get('suppid')
        obj=list(Booking.objects.filter(item_id=item,supp_id=suppid,status='0').values('from_date','to_date','item_id').distinct())
        obj3=list(Booking.objects.filter(Q(item_id=item)&(Q(from_date__lte=t)&Q(to_date__gte=f))).values('from_date','to_date','item_id'))
        print(obj3,'is obj3')
        obj2=[{'1':'Yes'}]
        for i in obj:
            print(i['item_id'])
            #ss=list(Booking.objects.filter(Q(i['f_date']__ste=t)|Q(to_date__ste)))
            f_date=str(i["from_date"])#.split('-')
            
            t_date=str(i['to_date'])#.split('-')
            
            xx=[t,f_date,f,t_date,item]
            print(xx)
            cursor=connection.cursor()
            ## 
            cursor.execute('''select * from public.dlw_booking where %s >=from_date and %s <=to_date and item_id=%s ''',[t,f,item])
            ll=list(cursor.fetchall())
            connection.close()
            print('ll==',ll)
            if len(ll)>0:
                return JsonResponse([],safe=False)
        print(obj2)
        return JsonResponse(obj2,safe=False)
    return JsonResponse({"success":false},status=400)

def history_cust(request,userid=''):
    context={}
    if userid!='':
        obj1=list(Userall.objects.filter(userid=userid).values('phone','email','addr','name','type_of_user'))
        obj2=list(Booking.objects.filter(cust_id=userid).values('item_id','from_date','to_date','status'))
        data=[]
        for i in obj2:
            ss=list(Items.objects.filter(item_id=i['item_id']).values('name','description','rate'))
            if ss:
                ss[0]['from_date']=i['from_date']
                ss[0]['to_date']=i['to_date']
                ss[0]['status']=i['status']
                data.append(ss[0])
        context={'user':userid,
                'userid':userid,
                'phone':obj1[0]['phone'],
                    'email':obj1[0]['email'],
                    'address':obj1[0]['addr'],
                    'name':obj1[0]['name'],
                    'table_data':data,
                    'type':obj1[0]['type_of_user'],
                            }
    return render(request,'history_cust.html',context)
def view_cust(request):

    context={'user':'admin',}
    return render(request,'view_cust.html',context)

def view_transactions(request):

    context={'user':'admin',}
    return render(request,'view_trans.html',context)


def view_info(request):
    ss=list(Userall.objects.all().distinct())
    ss2=list(Userall.objects.filter(type_of_user='Customer').values('phone'))
    ss3=list(Userall.objects.filter(type_of_user='Supplier').values('phone'))
    ss4=list(Booking.objects.all())
    context={'user':'admin',
        'usersall':len(ss),
        'cust':len(ss2),
        'supp':len(ss3),
        'book':len(ss4),
    }
    return render(request,'view_info.html',context)


def admin_bydate(request):
    if request.is_ajax() and request.method=='GET':
        dt=request.GET.get('book_date')
        print(dt)
        dt=dt.split('-')
        dt='-'.join(dt[::-1])
        print(dt)
        obj=list(Booking.objects.filter(book_date=dt).values('from_date','to_date','supp_id','cust_id','item_id').distinct())
        return JsonResponse(obj,safe=False)
    return JsonResponse({"success":false},status=400)


def admin_byusername(request):
    if request.is_ajax() and request.method=='GET':
        dt=request.GET.get('book_date')
        userid=dt
        obj1=list(Userall.objects.filter(userid=dt).values('phone','email','addr','name','type_of_user'))
        data=[]
        if obj1:
            if obj1[0]['type_of_user']=='Customer' or obj1[0]['type_of_user']=='Supplier' or  obj1[0]['type_of_user']=='User'  :
                obj2=list(Booking.objects.filter(cust_id=dt).values('item_id','from_date','to_date','status'))
                data=[]
                for i in obj2:
                    ss=list(Items.objects.filter(item_id=i['item_id']).values('item_id','name','description','rate'))
                    if ss:
                        ss[0]['from_date']=i['from_date']
                        ss[0]['to_date']=i['to_date']
                        ss[0]['status']=i['status']
                        data.append(ss[0])
            if obj1[0]['type_of_user']=='Supplier':
                data2=[]
                obj2=list(Items.objects.filter(supp_id=dt).values('name','item_id','rate','description'))
            print(userid)
            context={'user':'admin',
                    'userid':'admin',
                    'phone':obj1[0]['phone'],
                        'email':obj1[0]['email'],
                        'address':obj1[0]['addr'],
                        'name':obj1[0]['name'],
                        'table_data':data,
                        'type':obj1[0]['type_of_user'],
                    }
            if context['type']=='Supplier':
                context['table_data2']=obj2
            obj=[context]
        else:
            context={'user':'admin',
                'userid':'admin',
                'type':'Admin',

            }
            obj=[]
        return JsonResponse(obj,safe=False)
    return JsonResponse({"success":false},status=400)

def upcoming(request):
    
    today = date.today()
    print("Today's date:", today)
    now=datetime.datetime.today()
    print('now',now)
    a=1
    obj = list(Booking.objects.filter(status='0').values('cust_id','from_date','to_date','item_id'))
    #obj1 = list(Booking.objects.filter().values('item_id'))
    print('obj',obj)
    obj2=[]

    for i in range(len(obj)):
        obj[i]['sno']=i+1
        obj3=list(Items.objects.filter(item_id=obj[i]['item_id']).values('rate'))
        obj[i]['rate']=obj3[0]['rate']
        #obj.append(obj1[i])
    
    print('obj',obj)
    context={
            'obj':obj,
            'obj2':obj2,
            'a':a,
        }
    return render(request,'upcoming.html',context)


def online_rental(request):
    return render(request, 'online_rental.html')


global username1

def login_page_shed1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        use=list(Userall.objects.filter(userid=username,pwd=password).values('name'))
        print(use)
        global username1
        username1=username
        if len(use)==0:
            messages.success(request, 'Enter Valid Email id and Password')
            return render(request,'index.html')
        else:

            global user1
            user1=use[0]['name']
            
            context={
                'username':user1,

            }
            print("abc")
            
            return redirect('shed_dashboard')
    return render(request,"index.html")


def make_update(request):
    if request.method == "GET" and request.is_ajax():
        item_id=request.GET.get('item_id')
        rate=request.GET.get('rate')
        print('rate',rate)
        Items.objects.filter(item_id=item_id).update(rate=rate)   
        #print('data1',data1)
        obj=[]
        return JsonResponse(obj, safe=False)
    return JsonResponse({"success": False})

def delete_dress1(request):
    if request.method == "GET" and request.is_ajax():
        item_id=request.GET.get('item_id')
        #MRKT_Term_Conditions.objects.filter(id=id1).delete()
            
        Items.objects.filter(item_id=item_id).delete()  
        #print('data1',data1)
        obj=[]
        return JsonResponse(obj, safe=False)
    return JsonResponse({"success": False})

def display(request):
    global username1
    print('username',username1)
    data1=list(Items.objects.filter(supp_id=username1).values('item_id','description','pic','rate','quan','color','size'))
    print('data1',data1)
    context={
            'data':data1,
            'username1':username1,
        }
    if request.method=='POST':
        
        submitvalue=request.POST.get("submit")
        
        if submitvalue=="Proceed": 
            print("a")
            change = request.POST.get('change')

            user= Items.objects.filter(supp_id=username1).update(puchased_category=purchased_category,loco_no=Loco_no)
            context={
            'data':data1,
        }
            

    return render(request,'display.html',context)



global cust_user
def registration(request):
    global username1
    print('username',username1)
    if(request.method=='POST'):
        submitvalue=request.POST.get('submit')
        if(submitvalue=='Submit'):
            item=request.POST.get('item')
            desc=request.POST.get('desc')
            rate=request.POST.get('rate')
            color=request.POST.get('color')
            quan=request.POST.get('quan')
            
            size=request.POST.get('size')
            f=request.FILES['clist']
            cursor=connection.cursor()
            cursor.execute('''select id from public."dlw_items" order by "id" desc;''')
            a=str(cursor.fetchone()[0])
            prcs=list(cursor.fetchall())
            b=int(a)
            b=b+1
            print(a)
            print(b)
            
            Items.objects.create(id=b,supp_id=username1,item_id=item,description=desc,quan=quan,rate=rate,color=color,size=size,pic=f)
            print("Successful")

    return render(request,'registration.html')


def login_page_shed(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        use=list(shed_user.objects.filter(username=username,password=password).values('username','zone','shed','desig'))
        print(use)
        if len(use)==0:
            messages.success(request, 'Enter Valid Email id and Password')
            return render(request,'index.html')
        else:

            global user1,zone1,shed1,desig1
            user1=use[0]['username']
            zone1=use[0]['zone']
            shed1=use[0]['shed']
            desig1=use[0]['desig']
            context={
                'username':user1,
                'zone':zone1,
                'shed':shed1,
                'desig' :desig1

            }
            
            return redirect('shed_dashboard')
    return render(request,"index.html")



def login_page_shed1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        use=list(Userall.objects.filter(userid=username,pwd=password).values('name'))
        print(use)
        global username1
        username1=username
        if len(use)==0:
            messages.success(request, 'Enter Valid Email id and Password')
            return render(request,'index.html')
        else:

            global user1
            user1=use[0]['name']
            
            context={
                'username':user1,

            }
            print("abc")
            
            return redirect('shed_dashboard')
    return render(request,"index.html")

def logout_page_shed(request):
    # try:
    #     del request.session['name']
    # except KeyError:
    #     pass
    return redirect('login_page_shed1')




def login_page_shed(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        use=list(shed_user.objects.filter(username=username,password=password).values('username','zone','shed','desig'))
        print(use)
        if len(use)==0:
            messages.success(request, 'Enter Valid Email id and Password')
            return render(request,'index.html')
        else:

            global user1,zone1,shed1,desig1
            user1=use[0]['username']
            zone1=use[0]['zone']
            shed1=use[0]['shed']
            desig1=use[0]['desig']
            context={
                'username':user1,
                'zone':zone1,
                'shed':shed1,
                'desig' :desig1

            }
            
            return redirect('shed_dashboard')
    return render(request,"index.html")


def feedback(request):

    if request.method=='POST':
        idd=request.POST.get('usernamee')
        feed=request.POST.get('feed')
        Feedback.objects.create(cust_id=idd,feedback=feed)
        context={'msg':"Successfully Saved"}
        return render(request,'feedback.html',context)
    return render(request,'feedback.html')







