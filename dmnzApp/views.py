from multiprocessing import context
from unicodedata import category
from winreg import REG_QWORD
from django.shortcuts import render,redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth


from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import os
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Min,Max

# Create your views here.

def home(request):
    new=Product.objects.filter(category=2)
    special=Product.objects.filter(category=1)
    feature=Product.objects.filter(id=2)
    return render(request, 'new_index.html',{'new':new,'fea':feature,'sp':special})

def about(request):
    return render(request, 'new_about.html')

def about_two(request):
    return render(request, 'new_about_two.html')

def checkout(request):
    return render(request, 'new_checkout.html')

def contact(request):
    return render(request, 'new_contact.html')

def contact_two(request):
    return render(request, 'new_contact_two.html')

def model(request):
    all=Product.objects.filter(category_id=1)
    three=Product.objects.filter(format='.3dx')
    return render(request, 'new_models.html',{'all':all,'three':three})

def photoshop(request):
    all=Product.objects.filter(category_id=4)
    price_low=Product.objects.filter(category_id=4).order_by('price')
    price_high=Product.objects.filter(category_id=4).order_by('-price')
    return render(request,'category_photoshop.html',{'all':all,'three':price_low,'high_to':price_high})

def ui_design(request):
    all=Product.objects.filter(category_id=5)
    price_low=Product.objects.filter(category_id=5).order_by('price')
    price_high=Product.objects.filter(category_id=5).order_by('-price')
    return render(request,'category_uidesign.html',{'all':all,'three':price_low,'high_to':price_high})

def house_plans(request):
    all=Product.objects.filter(category_id=6)
    price_low=Product.objects.filter(category_id=6).order_by('price')
    price_high=Product.objects.filter(category_id=6).order_by('-price')
    return render(request,'category_houseplans.html',{'all':all,'three':price_low,'high_to':price_high})

def logo_creation(request):
    all=Product.objects.filter(category_id=7)
    price_low=Product.objects.filter(category_id=7).order_by('price')
    price_high=Product.objects.filter(category_id=7).order_by('-price')
    return render(request,'category_logo.html',{'all':all,'three':price_low,'high_to':price_high})

def drawings(request):
    all=Product.objects.filter(category_id=8)
    price_low=Product.objects.filter(category_id=8).order_by('price')
    price_high=Product.objects.filter(category_id=8).order_by('-price')
    return render(request,'category_drawings.html',{'all':all,'three':price_low,'high_to':price_high})

    
    

    
    

def model_two(request):
    all=Product.objects.all()
    three=Product.objects.filter(format='.3dx')
    return render(request, 'new_models_2.html',{'all':all,})

#.............price low to high .............

def price_low(request):
    price_low=Product.objects.filter(category_id=1).order_by('price')
    return render(request,'cat_price_low.html',{'three':price_low})


def price_high(request):
    price_high=Product.objects.filter(category_id=1).order_by('-price')
    return render(request,'cat_price_high.html',{'three':price_high})
    

#.................category...3dx...................

def three(request):
    three=Product.objects.filter(format='.3dx',category_id=1)
    return render(request, 'cat_three_models.html',{'three':three})

#.................fbx..........................
def fbx(request):
    fbx=Product.objects.filter(format='.fbx',category_id=1)
    return render(request, 'cat_three_models.html',{'three':fbx})

#....................obj......................
def obj(request):
    obj=Product.objects.filter(format='.obj',category_id=1)
    return render(request, 'cat_obj_models.html',{'three':obj})


def product(request):
    return render(request, 'new_product.html')

def profile(request,pk):
    person=Register_freelance.objects.get(id=pk)
    return render(request, 'new_profile.html',{'p':person})

def freelancer(request):
    person=Register_freelance.objects.all()
    return render(request, 'new_freelancer.html',{'person':person})

def admin_log(request):
    return render(request, 'admin_log.html')


def freereg(request):
    if request.method == 'POST':
        #education
        ini=request.POST['insti']
        special=request.POST['speci']
        education=request.POST['educ']
        start=request.POST['start']
        end=request.POST['end']
        #skills
        proffectional=request.POST['proffectional']
        title=request.POST['title']
        skill=request.POST['skill']
        overview=request.POST['overview']
        #expireince
        company=request.POST['compny']
        position=request.POST['postn']
        rate=request.POST['time']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        #protfolio
        project=request.POST['project']
        address=request.POST['url']
        Position2=request.POST['Position2']
        files=request.FILES['files']
        #profile
        fullname=request.POST['fullname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        country=request.POST['country']
        profilepic=request.FILES['profilepic']
        std=Register_freelance(college=ini,
                               special=special,
                               education=education,
                               startdate=start,
                               enddate=end,
                               proffecional_title=proffectional,
                               service=title,
                               skills=skill,
                               over_view=overview,
                               company=company,
                               position=position,
                               Rate=rate,
                               start=start_date,
                               end=end_date,
                               url=address,
                               project_title=project,
                               position2=Position2,
                               file=files,
                               full_name=fullname,
                               email=email,
                               mobile=mobile,
                               country=country,
                               profile_pic=profilepic)
        std.save()
        # messages(request,'success')
        return redirect('freereg')
        
    return render(request,'new_registration.html')

def cartitem(request,pk):
    if 'USID' in request.session:
       k=request.session['USID']  
       prod=Product(id=pk)
       user1=User(id=k)
       std=cart(product=prod,
           User=user1,)
       std.save()
       return redirect('userhome')
    return render('user_logout')

def viewcart(request):
    if 'USID' in request.session:
       pk=request.session['USID']  
       ca=cart.objects.filter(User=pk)
       co=cart.objects.filter(User=pk).count()
       total=0
       for p in ca:
         total+=int(p.product.price)
       return render(request,'cart.html',{'ca':ca,'total':total,'co':co})
    return redirect('user_logout')   

def view_items(request,pk):
    if 'USID' in request.session:
        k=request.session['USID']
        user=User.objects.get(id=k)
        std=Product.objects.get(id=pk)
        new=Product.objects.filter(category=2)
        
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            phone=request.POST['phone']
            description=request.POST['desc']
            status='pending'
            product=std
            user_id=user
            servicee_freelancer=0
            sfm=Service_form(user_name=name,
                             email=email,
                             Address=address,
                             phone_number=phone,
                             description=description,
                             status=status,
                             product=product,
                             user=user_id,
                             servicee_freelancer=servicee_freelancer)
            sfm.save()
        return render(request,'view_item_2.html',{'std':std,'new':new,'u':user})
    return redirect('user_logout')


def view_items_two(request,pk):
    std=Product.objects.get(id=pk)
    new=Product.objects.filter(category=2)
    return render(request,'view_item.html',{'st':std,'new':new})
  
    

def registration(request):
    it = categories.objects.all()
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('admin_log')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                msg_success = "Registration Successfull"
                messages.info(request, 'Registration successfully completed')
                return render(request,'registration.html',{'msg_success':msg_success})
        else:
            messages.info(request, 'password not matching')
            return redirect('registration')
   
    return render(request, 'registration.html',{'it':it})

def admin_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # request.session["uid"] = user.id
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                request.session['admid']=user.id
                return redirect('admin_dashboard')
            else:
                request.session['USID']=user.id
                return redirect('userhome')           
        else:
            print("hi3")
            messages.info(request,'invalid username or password.Try again!')
            return redirect('admin_log')
       # messages.info(request, 'Invalid username or password')
    print("hi4")
    return redirect('admin_log')



def userhome(request):
    if 'USID' in request.session: 
       new=Product.objects.all().order_by('-id')[:3]
       special=Product.objects.all().order_by('id')[:3]
       feature=Product.objects.all().order_by('id')[3:6]
       count_a=Product.objects.filter(category_id=1).count()
       count_b=Product.objects.filter(category_id=4).count()
       count_c=Product.objects.filter(category_id=5).count()
       count_d=Product.objects.filter(category_id=6).count()
       count_e=Product.objects.filter(category_id=7).count()
       count_f=Product.objects.filter(category_id=8).count()
       return render(request, 'new_index2.html',{'new':new,'sp':special,'fea':feature,'count_b':count_b,'count_c':count_c,'count_d':count_d,'count_e':count_e,'count_f':count_f,'count_a':count_a})
    return redirect('user_logout')


def admin_dashboard(request):
    if request.session.has_key('admid'):
        abc= request.session['admid']
        adm=User.objects.filter(id=abc)
        users = User.objects.all().count()
        models = Product.objects.all().count()
        return render(request, 'admin_dashboard.html',{'adm': adm, 'users': users, 'models': models,})
    return redirect('user_logout')


def admin_log(request):
    it = categories.objects.all()
    request.session.flush()
    return render(request, 'admin_log.html',{'it':it})

# def admin_dashboard(request):
#     if 'admid' in request.session:
#         if request.session.has_key('admid'):
#             admid = request.session['admid']
#         else:
#             return redirect('/')
#         adm = Admin_register.objects.filter(reg_id=admid)
#         users = Admin_register.objects.all().count()
#         models = Product.objects.all().count()
#         return render(request, 'admin_dashboard.html', {'adm': adm, 'users': users, 'models': models,})
#     else:
#         return redirect('/')

def user_logout(request):
    request.session.flush()
    return redirect('admin_log')


def buyNow(request, id):
    model = Product.objects.get(id=id)
    it = categories.objects.all()
    SAdm_id = request.session['SAdm_id']
    member = User.objects.get(id=SAdm_id)
    return render(request, 'buynow.html', {'model': model,'it':it, 'member': member,})

def buyNownotloged(request, id):
    model = Product.objects.get(id=id)
    it = categories.objects.all()

    return render(request, 'buynownotloged.html', {'model': model,'it':it,})

def saveform(request):
    if request.method=='POST':
        
        nm=request.POST['name']
        mb=request.POST['mobile']
        el=request.POST['email']
        cg=request.POST['catg']
        im=request.POST['itm']
        pc=request.POST['price']
        mg=request.POST['message']
        
        std=oders(
            name=nm,
            mobile=mb,
            email=el,
            catag=cg,
            item=im,
            price=pc,
            mesg=mg,

                    )
        std.save()
        print("hii")
        return render(request,'submited.html') 


def orderlist(request):
    obj=oders.objects.all()
    context={'msg':obj}
    return render(request,'orderlist.html',context) 

def new_page(request, id):
    
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        member = User.objects.get(id=SAdm_id)
        products = Product.objects.all()
        it = categories.objects.all()
        data = cartData(request)
        cartItems = data['cartItems']
        man1 = Product.objects.filter(category_id=id)
        man = categories.objects.filter(cat_id=id)
        sub = SubCategory.objects.all()
        # return render(request, 'new_page.html', {'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})
        return render(request, 'new_page.html', {'sub':sub,'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1,'member':member})
    # else:
    #         return redirect('/')



def new_page2(request, id):
    # member = User.objects.get(id=SAdm_id)
    products = Product.objects.all()
    it = categories.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    man1 = Product.objects.filter(category_id=id)
    man = categories.objects.filter(cat_id=id)
    sub = SubCategory.objects.all()
        # return render(request, 'new_page.html', {'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})
    return render(request, 'new_page2.html', {'sub':sub,'it':it,'products':products,'cartItems':cartItems,'man': man, 'man1': man1})

def sub(request, id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    member = User.objects.get(id=SAdm_id)
    products = Product.objects.all()
    it = categories.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    man1 = Product.objects.filter(subcategory_id=id)
    man = categories.objects.filter(cat_id=id)
    subcate = SubCategory.objects.filter(id=id)
    sub1 = SubCategory.objects.all()
    return render(request, 'sub.html', {'subcate':subcate,'it':it,'data':data,'cartItems':cartItems,'member':member,'products':products,'sub':sub1,'man': man, 'man1': man1})


def Signup_emailval(request):
    email = request.GET.get('email', None)
 
    data = {
        'is_taken': Admin_register.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Email already exists.'
    return JsonResponse(data)

def registration(request):
    it = categories.objects.all()
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                return redirect('admin_log')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                user.save()
                msg_success = "Registration Successfull"
                messages.info(request, 'Registration successfully completed')
                return render(request,'registration.html',{'msg_success':msg_success})
        else:
            messages.info(request, 'password not matching')
            return redirect('registration')
   
    return render(request, 'registration.html',{'it':it})






def admin_logout(request):
    if 'admid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def admin_settings(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_settings.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_profile(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            abb = Admin_register.objects.get(reg_id=admid)
            abb.fullname = request.POST['fullname']
            abb.email = request.POST['email']
            abb.username = request.POST['username']
            abb.save()
            return redirect("admin_settings")
        return render(request, 'admin_edit_profile.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_picture(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            abb = Admin_register.objects.get(reg_id=admid)
            abb.photo = request.FILES['img']
            abb.save()
            return redirect("admin_settings")
        return render(request, 'admin_edit_picture.html', {'adm': adm})
    else:
        return redirect('/')

def admin_edit_password(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        if request.method == 'POST':
            ac = Admin_register.objects.get(reg_id=admid)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    ac.password = request.POST.get('confirmPassword')
                    ac.save()
                    msg_success = "Password changed successfully"
                    return render(request, 'admin_settings.html', {'msg_success': msg_success})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
        return render(request, 'admin_edit_password.html', {'adm': adm})
    else:
        return redirect('/')



def show_category(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        caty = categories.objects.all()
        return render(request, 'categories.html', {'caty': caty,'adm':adm})
    else:
        return redirect('/')

def Sub_categories(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        cate = categories.objects.all()
        subcate = SubCategory.objects.all()
        return render(request, 'Sub_categories.html', {'subcate':subcate,'caty': cate,'adm':adm})
    else:
        return redirect('/')

def add_category(request):
    try:

        if request.method == 'POST':
            category_name = request.POST['category_name']
            category_logo = request.FILES['category_logo']
            # sub_category1 = request.POST['sub_category1']
            # strippeddata1 = sub_category1.replace(" ", "")
            # sub_category2 = request.POST['sub_category2']
            # strippeddata2 = sub_category2.replace(" ", "")
            # sub_category3 = request.POST['sub_category3']
            # strippeddata3 = sub_category3.replace(" ", "")
            # sub_category4 = request.POST['sub_category4']
            # strippeddata4 = sub_category4.replace(" ", "")
            # sub_category5 = request.POST['sub_category5']
            # strippeddata5 = sub_category5.replace(" ", "")
            cat = categories(category_name=category_name, category_logo=category_logo)
            # cat = categories(category_name=category_name, category_logo=category_logo, sub_category1=strippeddata1,
            #                  sub_category2=strippeddata2, sub_category3=strippeddata3, sub_category4=strippeddata4, sub_category5=strippeddata5)
            cat.save()

            return redirect('category')
        else:
            return redirect('categories')
    except:
        return redirect('categories')

def add_subcategory(request):
        if request.method == 'POST':
            abc = SubCategory()
            abc.category_id  = request.POST['category']
            abc.subcategory = request.POST['subcategory']
            abc.save()
            msg_success = "Added successfull"
            return render(request, 'Sub_categories.html', {'msg_success': msg_success})
        return render(request, 'Sub_categories.html',) 
            

def cat_delete(request, cat_id):

    emp = categories.objects.get(cat_id=cat_id)
    emp.delete()
    return redirect('category')

def subcat_delete(request, id):
    
    emp = SubCategory.objects.get(id=id)
    emp.delete()
    return redirect('Sub_categories')


def admin_models(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_models.html',{'adm':adm})
    else:
        return redirect('/')


def addmodel(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id= abc)
    var = categories.objects.all()
    return render(request, "addmodel.html", {'var': var,'adm':adm})


def createmodel(request):
    if request.method == 'POST':

        modelname = request.POST['modelname']
        description = request.POST['description']
        gib = request.FILES['gib']
        price = request.POST['price']
        types = request.POST['types']
        format = request.POST['format']
        modeltype = request.POST['modeltype']
        category = request.POST['category']
        # fbx = request.FILES['fbx']

        item = Product(modelname=modelname, description=description, gib=gib, price=price, types=types, format=format, modeltype=modeltype, category_id=category)
        item.save()
        return redirect('addmodel')
    else:
        return redirect('createmodel')


def admin_payment_history(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        return render(request, 'admin_payment_history.html',{'adm':adm})
    else:
        return redirect('/')


def payment_table(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        var = payment.objects.all()
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate')
            var = payment.objects.filter(date__range=[fromdate, todate])
        return render(request, 'payment_table.html', {'var': var,'adm':adm})
    else:
        return redirect('/')


def registeredusers(request):
    abc= request.session["admid"]
    adm=User.objects.filter(id=abc)
    
    use = User.objects.filter(is_superuser=0)
    return render(request, 'registeredusers.html', {'use': use,'adm':adm})
    


def delete(request, reg_id):
    admid = request.session['admid']
    use = Admin_register.objects.get(reg_id=reg_id)
    use.delete()
    return redirect('registeredusers')


def adminedit(request, id):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        item = Product.objects.filter(id=id)
        viva = categories.objects.all()
        return render(request, "adminedit.html", {'item': item, 'viva': viva})
    else:
        return redirect('/')

def admin_editmodel(request, id):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        item = Product.objects.filter(id=id)
        viva = categories.objects.all()
        return render(request, "admin_editmodel.html", {'item': item, 'viva': viva})
    else:
        return redirect('/')


def admin_current_models(request):
    if 'admid' in request.session:
        if request.session.has_key('admid'):
            admid = request.session['admid']
        else:
            return redirect('/')
        adm = Admin_register.objects.filter(reg_id=admid)
        category = categories.objects.all()
        item = Product.objects.all()
        return render(request, 'admin_current_models.html', {'category': category, 'item': item,'adm':adm})
    else:
        return redirect('/')


def model_delete(request, id):
    abc = Product.objects.get(id=id)
    abc.delete()
    return redirect('admin_current_models')


def modeledit(request, id):
    if request.session['admid'] == "":
        return redirect('logout')
    else:
        if request.method == "POST":
            item = Product.objects.get(id=id)
            item.modelname = request.POST.get('modelname', item.modelname)
            item.description = request.POST.get('description', item.description)
            item.gib = request.FILES.get('gib', item.gib)
            item.price = request.POST.get('price', item.price)
            item.types = request.POST.get('types', item.types)
            item.format = request.POST.get('format', item.format)
            item.modeltype = request.POST.get('modeltype', item.modeltype)
            item.category_id = request.POST.get('category_name', item.category_id)
            item.fbx = request.FILES.get('fbx', item.fbx)

            item.save()
            return redirect('admin_current_models')






# def login(request):
#     if request.method == 'POST':
#         username  = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username,password=password)
#         if user is not None:
#             request.session['SAdm_id'] = user.id
#             return redirect('store')
        

        # elif Admin_register.objects.filter(username=request.POST['username'], password=request.POST['password'], designation="user").exists():
        #     member = Admin_register.objects.get(
        #         username=request.POST['username'], password=request.POST['password'])
        #     request.session['userid'] = member.reg_id
        #     return redirect('userhome')

#         else:
#             return redirect('login')
#     else:
#          return render(request,'login.html')

# def logout(request):
#     if 'user' in request.session:
#         request.session.flush()
#         return redirect('/')
#     else:
#         return redirect('/')

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart_item(request):
    # if 'SAdm_id' in request.session:
    #     if request.session.has_key('SAdm_id'):
    #         SAdm_id = request.session['SAdm_id']
    #     else:
    #         return redirect('/')
    #     it = categories.objects.all()
    #     member = User.objects.get(id=SAdm_id)
    #     data = cartData(request)
    #     print(data['cartItems'])
    #     cartItems = data['cartItems']
    #     order = data['order']
    #     items = data['items']

    #     context = {'items':items, 'order':order, 'cartItems':cartItems,'member':member,'it':it,}
    return render(request, 'cart.html')

def checkout(request):
	if 'SAdm_id' in request.session:
		if request.session.has_key('SAdm_id'):
			SAdm_id = request.session['SAdm_id']
		else:
			return redirect('/')
		member = User.objects.get(id=SAdm_id)
		data = cartData(request)
		it = categories.objects.all()
		cartItems = data['cartItems']
		order = data['order']
		items = data['items']

		context = {'items':items, 'order':order, 'cartItems':cartItems,'member':member,'it':it}
		return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
    print("name")
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def newcart(request):
    return render(request,'newcart.html')

def request(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        
        member = User.objects.get(id=SAdm_id)
        it = categories.objects.all()
        return render(request, 'request.html',{'it': it, 'member': member})
    

def request_not_logedin(request):
    it = categories.objects.all()
    return render(request,'nologrequest.html',{'it':it})

def reqlist(request):
    re=Request.objects.all()
 
    return render(request,'requestli.html',{'re':re})


def savereq(request):
    if request.method=='POST':
        n=request.POST.get('name')
        nu=request.POST.get('number')
        em=request.POST.get('email')
        at=request.POST.get('about')
        images=request.FILES.get('image')
        req=Request(name=n, mobile=nu, email=em, about=at, image=images)
        req.save()
        return redirect('home')

def deletereq(request,id):
    re=Request.objects.get(id=id)
    re.delete()
    return redirect('reqlist')





