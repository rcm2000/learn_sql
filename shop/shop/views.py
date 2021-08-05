import logging
import os

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.http import urlencode

from config.settings import BASE_DIR, UPLOAD_DIR
from frame import itemdb
from frame.error import ErrorCode
from frame.itemdb import ItemDb
from frame.userdb import UserDb
logger = logging.getLogger('users');

def userlist(request):
    #logger.debug('GET access User List....')
    rsuserlist = UserDb().select();
    context = {
        'section':'shop2/userlist.html',
        'rsusers':rsuserlist
    };
    return render(request, 'shop2/shop2.html',context)
def userdetail(request):
    id  = request.GET['id'];
    #logger.debug('user id:'+id)
    rsuser = UserDb().selectone(id);
    context = {
        'section': 'shop2/userdetail.html',
        'rsuser': rsuser
    };
    return render(request, 'shop2/shop2.html',context)

def useradd(request):
    context = {
        'section': 'shop2/useradd.html'
    };
    return render(request, 'shop2/shop2.html',context)

def userupdate(request):
    id = request.GET['id'];
    user = UserDb().selectone(id);
    context = {
        'section': 'shop2/userupdate.html',
        'uuser':user,
    };
    return render(request, 'shop2/shop2.html',context)

def userdelete(request):
    id = request.GET['id'];

    try:
        UserDb().delete(id);
    except:
        context = {
            'section': 'shop2/error.html',
            'error': ErrorCode.e0002
        };
        return render(request,'shop2/shop2.html',context);
    return redirect('userlist');

def userupdateimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    try:
        UserDb().update(id,pwd,name);
    except:
        context = {
            'section': 'shop2/error.html',
            'error': ErrorCode.e0001
        };
        return render(request,'shop2/shop2.html',context);
    qstr = urlencode({'id': id})
    return HttpResponseRedirect('%s?%s' % ('userdetail', qstr))

def useraddimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    try:
        UserDb().insert(id,pwd,name);
    except:
        context = {
            'section': 'shop2/error.html',
            'error': ErrorCode.e0001
        };
        return render(request,'shop2/shop2.html',context);
    return redirect('userlist');

class ItemView:
    def itemaddimpl(request):
        name = request.POST['name'];
        price = request.POST['price'];
        imgname = '';
        if 'img' in request.FILES:
            img = request.FILES['img']
            imgname = img._name

            fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
            for chunk in img.chunks():
                fp.write(chunk);
                fp.close();

        ItemDb().insert(name,int(price),imgname);
        return redirect('itemlist');


    def itemlist(request):
        items = ItemDb().select();
        context = {
            'section': 'shop2/itemlist.html',
            'itemlist':items,
        };
        return render(request, 'shop2/shop2.html',context)
    def itemadd(request):
        context = {
            'section': 'shop2/itemadd.html'
        };
        return render(request, 'shop2/shop2.html',context)

    def itemdetail(request):
        id = request.GET['id'];
        item = ItemDb().selectone(int(id));
        context = {
            'section': 'shop2/itemdetail.html',
            'item':item,
        };
        return render(request, 'shop2/shop2.html', context)

    def itemupdate(request):
        id = request.GET['id'];
        item = ItemDb().selectone(int(id));
        context = {
            'section': 'shop2/itemupdate.html',
            'item':item,
        };
        return render(request, 'shop2/shop2.html', context)

    def itemupdateimpl(request):
        id = request.POST['id'];
        name = request.POST['name'];
        price = request.POST['price'];
        img = request.POST['img'];

        imgname = '';
        if 'newimg' in request.FILES:
            newimg = request.FILES['newimg']
            imgname = newimg._name

            fp = open('%s/%s' % (UPLOAD_DIR, imgname), 'wb')
            for chunk in newimg.chunks():
                fp.write(chunk);
                fp.close();
        else:
            imgname = img;

        ItemDb().update(int(id),name,int(price),imgname);
        qstr = urlencode({'id': id})
        return HttpResponseRedirect('%s?%s' % ('itemdetail', qstr))

class MainView:
    def login(request):
        context = {
            'section': 'shop2/login.html'
        };
        return render(request, 'shop2/shop2.html', context)

    def logout(request):
        if request.session['suser'] != None:
            del request.session['suser'];
        return render(request, 'shop2/shop2.html')

    def loginimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        try:
            user = UserDb().selectone(id);
            if pwd == user.pwd:
                request.session['suser'] = id;
                context = {
                    'section': 'shop2/loginok.html',
                    'loginuser': user
                };
            else:
                raise Exception;
        except:
            context = {
                'section': 'shop2/error.html',
                'error': ErrorCode.e0003
            };

        return render(request, 'shop2/shop2.html', context);













