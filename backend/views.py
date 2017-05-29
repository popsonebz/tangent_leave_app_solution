# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from leave.models import employee

from forms import EmployeeForm
from datetime import date, datetime

# Create your views here.

def newEmployee(request):
    
    if request.method == 'POST':


        form = EmployeeForm(request.POST)

        if form.is_valid():
            #form = form.save(commit=False)
            #form.save()
            username = form['username'].value()
            password = form['password'].value()
            first_name = form['first_name'].value()
            print type(form['employment_date'].value())
            print form['employment_date'].value()
            new_user = User.objects.create_user(username=username,
                                 first_name = first_name,
                                 password=password)
            new_user.save()

            user = User.objects.get(username=username)
            obj = employee()
            obj.user_id = user.id
            obj.employment_date = datetime.strptime(str(request.POST['employment_date']), '%m/%d/%Y').strftime('%Y-%m-%d')
            #obj.employment_date = datetime.strptime(request.POST['employment_date'], '%m/%d/%y').strftime('%Y-%m-%d')
            obj.save()
            return redirect('leave:login')

    else:
    	form = EmployeeForm()
    return render(request, 'backend/add_new_employee.html', {'form':form})
