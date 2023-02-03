from django.shortcuts import render,redirect
from django_nextjs.render import render_nextjs_page_sync
import mysql.connector as sql
from django.views.decorators.csrf import csrf_exempt

connection = sql.connect(host="localhost",user="root",passwd="deep2003",database="dbs")
cursor = connection.cursor()
id=''
fn=''
ln=''
village=''
phone=''
vehicle=''
ban='' 
bn=''
ifsc=''
g1=''
quality=''
g2=''
gross=''
tare=''
nett='' 
remark=''

name=''
email=''
password=''

# Create your views here.
def index(request):
    return render_nextjs_page_sync(request)

def about(request):
    return render_nextjs_page_sync(request)

@csrf_exempt
def admin(request):
    global email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value

            if key=="password":
                password=value

        c="select * from user_admin where email='{}' and password='{}'".format(email,password)
        cursor.execute(c)
        
        t=tuple(cursor.fetchall())
        print(t)
        if t==():
            
            return render_nextjs_page_sync(request)
        else:
            
            return redirect(display)
            
    return render_nextjs_page_sync(request)

    

def contact(request):
    return render_nextjs_page_sync(request)

def forgot(request):
    return render_nextjs_page_sync(request)

@csrf_exempt
def owner(request):
    global email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value

            if key=="password":
                password=value

        c="select * from owner_admin where email='{}' and password='{}'".format(email,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render_nextjs_page_sync(request)
        else:
            return redirect(display)
            

    return render_nextjs_page_sync(request)


    
@csrf_exempt
def purchase(request):
    global fn,ln,village,phone,vehicle,ban, bn,ifsc,g1,quality,g2,gross,tare,nett,remark
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
        cursor=m.cursor()
        e=request.POST
        for key,value in e.items():
            if key=='fn':
                fn=value

            if key=='ln':
                ln=value

            if key=='village':
                village=value

            if key=='phone':
                phone=value

            if key=='vehicle':
                vehicle=value

            if key=='ban':
                ban=value

            if key=='bn':
                bn=value

            if key=='ifsc':
                ifsc=value

            if key=='g1':
                g1=value

            if key=='quality':
                quality=value

            if key=='g2':
                g2=value  

            if key=='gross':
                gross=value

            if key=='tare':
                tare=value

            if key=='nett':
                nett=value

            if key=='remark':
                remark=value      

        c="insert into purchase values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,village,phone,vehicle,ban,bn,ifsc,g1,quality,g2,gross,tare,nett,remark)
        cursor.execute(c)
        m.commit()

    return render_nextjs_page_sync(request)  

@csrf_exempt
def sigunp(request):
    global name,email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="name":
                name=value

            if key=="email":
                email=value

            if key=="password":
                password=value

        c="insert into user values('{}','{}','{}')".format(name,email,password)
        cursor.execute(c)
        m.commit()

    return render_nextjs_page_sync(request)   

@csrf_exempt
def staff(request):
    global email,password
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value

            if key=="password":
                password=value

        c="select * from user where email='{}' and password='{}'".format(email,password)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render_nextjs_page_sync(request)
            
        else:
            return redirect(purchase)

    return render_nextjs_page_sync(request)   




def display(request):
    m=sql.connect(host="localhost",user="root",passwd="deep2003",database="minor_project")
    cursor=m.cursor()
    cursor.execute("select * from purchase;")
    data = cursor.fetchall()
    return render(request, 'display.html', {'categories': data})

    




            
            
  

