from django.shortcuts import render, render_to_response
from django.template import RequestContext
from loanapp.models import AuthUsers, LoanEntries,LoanEligibility
#from passlib.hash import md5_crypt
import hashlib
# Create your views here.
# Create your views here.
def index(request):
    return render_to_response("index.html", {'mess': '','index': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance = RequestContext(request))

def register(request):
    return render_to_response("register.html", {'mess': '','reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance=RequestContext(request))

def loginpage(request):
    return render_to_response("login.html", {'mess': ''}, context_instance=RequestContext(request))

def reguser(request):
    if request.method == "POST":
        fname = request.POST['fullname']
        uname = request.POST['username']
        pword = request.POST['password']
        eid = request.POST['emailid']

        if AuthUsers.objects.filter(emailid=eid).exists():
            return render_to_response("register.html", {'mess': 'Email already  Exit.','reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'},
                                      context_instance=RequestContext(request))
        # Create object for the model
        authusers = AuthUsers(
            fullname= fname,
            username = uname,
            #password = md5_crypt.encrypt(pword),
            #password = hashlib.md5(pword),
            #password = hashlib.new(pword).hexdigest(),
            password = pword,
            emailid = eid
        )

        # REcord inserted
        authusers.save()
    	return render_to_response("login.html", {'mess': 'Registration Successful','reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance=RequestContext(request))
    return render_to_response("login.html", {'reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance=RequestContext(request))

def signin(request):
    if request.method == 'POST':
        check_count = AuthUsers.objects.count()
        if check_count > 0:
            username = request.POST['username']
            password = request.POST['passwd']
            checkuser = AuthUsers.objects.filter(emailid = username).exists()
            cust_count = LoanEntries.objects.filter(check_email = username).count()
    	    data = LoanEntries.objects.filter(cust_name = username)
            if checkuser == True:
            	checkuser = AuthUsers.objects.get(emailid = username)
            	if  username == checkuser.emailid.strip() and password == checkuser.password:
        		request.session['usersname'] = username
                	#request.session["usersname"] = emailid
                	#request.session["usersname"] = checkuser.emailid
                	#loan_limit = request.session['loan_limit']
                	#return render_to_response("loanform.html", {'mess': 'Welcome to loan page','cust_count':str(cust_count)}, context_instance=RequestContext(request))
                	return render_to_response("history.html", {'mess': 'Welcome to loan page','cust_count':str(cust_count),'data':data}, context_instance=RequestContext(request))
            	else:
                	return render_to_response("login.html", {'mess': 'Invalid Userid or Password'},
                                      context_instance=RequestContext(request))
            else:
                return render_to_response("login.html", {'mess': 'Invalid Username'},context_instance=RequestContext(request))
        else:
            return render_to_response("register.html", {'mess': 'First Registeruser'},
                                      context_instance=RequestContext(request))

def loanapply(request):
    cust_count = ''
    check_count = AuthUsers.objects.count()
    if check_count > 0:
        email = request.session["usersname"] 
        cust_count = LoanEntries.objects.filter(check_email = email).count()
    if request.method == 'POST':
        fname = request.POST['fname']
        loan_amount = request.POST['lamount']
        earn_amount = request.POST['eamount']
        #loan_amount_limit =request.POST['l_limit']
        loan_limit = int(earn_amount) * 3
        year = request.POST['year']
	if check_count > 0:
            email = request.session["usersname"] 
            cust_count = LoanEntries.objects.filter(check_email = email).count()
	else:
	    return render_to_response("loanform.html", {'reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance=RequestContext(request))
       
        if int(loan_amount) > loan_limit:
            return render_to_response("loanform.html", {'mess': 'Your Loan amount should not be greater than loanlimit.','reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children','cust_count':str(cust_count)}, context_instance=RequestContext(request))
        loantable = LoanEntries(
            cust_name=fname,
            loan_amount = loan_amount,
            earn_amount = earn_amount,
            loan_limit = loan_limit,
	    check_email = email,
            year = year

        )

        loantable.save()

        # send all data to session
        request.session['fname'] = fname
        request.session['lamt'] = loan_amount
        request.session['eamt'] = earn_amount
        request.session['loan_limit'] = loan_limit
        request.session['year'] = year

    	return render_to_response("loanview.html", {'mess': 'a','reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children','cust_count':str(cust_count)}, context_instance=RequestContext(request))
    return render_to_response("loanform.html", {'reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children','cust_count':str(cust_count)}, context_instance=RequestContext(request))

def get_data(request):
    return render_to_response("loanview.html", {'mess': ''}, context_instance=RequestContext(request))

def history(request):
    check_count = AuthUsers.objects.count()
    if check_count > 0 :
        username = request.session["usersname"]
        data = LoanEntries.objects.filter(cust_name = username)
	return render_to_response("history.html", {'data': data}, context_instance=RequestContext(request))
    else:
        return render_to_response("history.html", context_instance=RequestContext(request))

def checklimit(request):
    if request.method == 'POST':
        username = request.POST['username']
        companyname = request.POST['c_name']
        loan_amount = request.POST['l_amount']
        earn_amount = request.POST['e_amount']
        loan_limit = int(earn_amount) * 3
        email = request.POST['email']
        year = request.POST['year']
        if LoanEligibility.objects.filter(email=email).exists():
	    get_data = LoanEligibility.objects.get(email=email)
	    data = get_data.loan_limit
            return render_to_response("eligibility.html", {'mess': 'Your email already exist your loan eligibility is '+str(data)}, context_instance=RequestContext(request))
        #if loan_amount
	
        loanelig = LoanEligibility(
            customername=username,
            company=companyname,
            loan_amount = loan_amount,
            earn_amount = earn_amount,
            loan_limit = loan_limit,
            email=email,
            year = year
        )
        request.session['username'] = username
        request.session['l_amt'] = loan_amount
        request.session['e_amt'] = earn_amount
        request.session['loan_limit'] = loan_limit
        request.session['email'] = email
        request.session['year'] = year
        loanelig.save()
        return render_to_response("eligibility.html", {'mess': 'Your loan eligibility is '+str(loan_limit)}, context_instance=RequestContext(request))
    return render_to_response("eligibility.html", {'reguser': 'class=active-trail first odd sf-item-1 sf-depth-1 sf-no-children'}, context_instance=RequestContext(request))


def apply_loan(request):
    return render_to_response("loanform.html", context_instance=RequestContext(request))

def newuser(request):
    return render_to_response("register.html", context_instance=RequestContext(request))
