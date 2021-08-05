from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils.http import urlencode

from frame.custdb import CustDB
from frame.error import ErrorCode


def home(request):
    return render(request, 'home.html');

def custlist(request):
    clist = CustDB().select();
    context = {
        'cl': clist
    };
    return render(request, 'custlist.html',context);

def custadd(request):
    return render(request, 'custadd.html');
def custaddimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    try:
        CustDB().insert(id, pwd, name);
        return redirect('custlist');
    except:
        context = {
            'error': ErrorCode.e0001
        };
        return render(request, 'custadd.html', context);
def itemlist(request):
    return render(request, 'itemlist.html');
def itemadd(request):
    return render(request, 'itemadd.html');
def custdetail(request):
    id  = request.GET['id'];
    cust = CustDB().selectone(id);
    context = {'c': cust};
    return render(request, 'custdetail.html',context);

def custdelete(request):
    id  = request.GET['id'];
    CustDB().delete(id);
    return redirect('custlist');

def custupdate(request):
    id  = request.GET['id'];
    cust = CustDB().selectone(id);
    context = {'c': cust};
    return render(request, 'custupdate.html',context);

def custupdateimpl(request):
    id  = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    CustDB().update(id,pwd,name);
    qstr = urlencode({'id': id})
    return HttpResponseRedirect('%s?%s' % ('custdetail', qstr))
