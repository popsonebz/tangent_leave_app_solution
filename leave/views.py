# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from leave.forms import LeaveForm
from datetime import date, datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import employee, leave
from django.core.urlresolvers import reverse

# Create your views here.

def main_page(request):
    return render_to_response('home.html', RequestContext(request))

@login_required(login_url='/leave/login/')
def leave(request):

    
    if request.method == 'POST':

    	user = request.user

        try:
            obj = User.objects.select_related().get(username=str(user))
        except employee.DoesNotExist:
            obj = None
            return redirect('leave:login')


        form = LeaveForm(request.POST, user=request.user)

        if form.is_valid():
            form = form.save(commit=False)
            if obj.employee:
                form.employee = obj.employee
            form.save()
            return redirect('leave:leave')

    else:
    	form = LeaveForm()
    return render(request, 'leave/leaveApplication.html', {'form':form})

def employee(request):
    return render_to_response('leave/leaveApplication.html')