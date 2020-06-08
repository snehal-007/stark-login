from django.shortcuts import render ,HttpResponse
from django.contrib import messages
from home.models import Signin

# login and Home Page
def index(request):

    if request.method == 'POST':
        loginemail = request.POST['login_email']
        loginpassword = request.POST['login_password']

        # Fetch data from Database
        login = Signin.objects.filter(email = loginemail,password = loginpassword)

        update = []

        try:
            for item in login:
                update.append({'Email':item.email,"Username":item.u_name,'Password':item.password,"Full_Name":item.f_name,"Address_1":item.address_1,"Address_2":item.address_2,"City":item.city,"Date":item.date,"Image":item.image})


            profile_values = update[0]
            print("update",update)
            print("profile_values:",profile_values)

            if len(update) == 0:

                print("Login failed")
                messages.error(request,"Login error...")
                return render(request,"index.html") 

            else:
                print("Login sucess") 
                messages.success(request,"Login success...")

                params = profile_values
                return render(request,"welcome.html",params)  

        except Exception as e:
            print("Login failed")
            messages.error(request,"Login error...")
            return render(request,"index.html")


    # messages.error(request,"Login error...")
    return render(request,"index.html")
    # return HttpResponse("Thats home")

def about(request):
    return HttpResponse("About Page")
    # return render(request,"about.html")

def contact(request):
    return HttpResponse("Thats Contact")
    # return render(request,"contact.html")  


# signup
def signup(request):
    # to get info by Post Requests 
    if request.method == "POST":
        name = request.POST.get('uname','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        password = request.POST.get('pass','')
        conf_password = request.POST.get('confpass','')
        address_1 = request.POST.get('address1','')
        address_2 = request.POST.get('address2','')
        city = request.POST.get('city','')
        img = request.FILES['filename']
        
        check = request.POST.get('gridCheck','')

        # For Debugging
        print("name",name)
        print("fname",fname)
        print("lname",lname)
        print("email",email)
        print("password",password)
        print("conferm_password",conf_password)
        print("address 1",address_1)
        print("address 2",address_2)
        print("City",city)
        print("image",img)
        print("Check",check)

        # siginup validation checking
        login = Signin.objects.filter(email = email)

        sign_update = []

        for item in login:

            sign_update.append(item.email)

            print("sign_update",sign_update)

        if email in sign_update:
            messages.error(request,"Your Email is Already Used Please Try a New Email")
            return render(request,"signup.html")

            

        if len(name) < 10:
            messages.error(request,"Your username under 10 charecters please use more charecters")
            return render(request,"signup.html")

        if not name.isalnum():
            messages.error(request,"username should be letters and numbers")
            return render(request,"signup.html")

        if password != conf_password:
            messages.error(request,"Your password is not match please check again")
            return render(request,"signup.html")

        if len(password) < 5:

            messages.error(request,"Your password is too short")
            return render(request,"signup.html")


        if check == "1":

            singin = Signin(u_name=name,f_name=fname,l_name=lname,email=email,password=password,address_1=address_1,address_2=address_2,city=city,image=img)

            singin.save()
            print("success")
            messages.success(request,"You are Successfully Sign up please login ...")  

            return render(request,"signup.html")

        
        messages.error(request,"Please check on Accept me")
        return render(request,"signup.html")


        # else:
        #     print("Not submited")
        #     messages.error(request,"Your password is not match please check again")  

        #     return render(request,"signup.html")  

    return render(request,"signup.html")           