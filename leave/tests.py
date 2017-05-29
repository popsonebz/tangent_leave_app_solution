# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from django.test.client import Client
from selenium import webdriver
from django.core.urlresolvers import reverse
import time



class LeaveApplication(TestCase):
    c = Client()
    def test_0_call_view_denies_anonymous(self):
        response = self.client.get('http://localhost:8010/leave/apply', follow=True)
        self.assertRedirects(response, '/leave/login/?next=/leave/apply/', status_code=301)

    def test_login_page(self):
    	response = self.c.get('http://localhost:8010/leave/login', follow=True)
    	self.assertEqual(response.status_code, 200)
        response = self.c.post('/leave/login/', {'username': 'john', 'password': 'john'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Username')
        self.assertContains(response, 'Password')




        
        


    

