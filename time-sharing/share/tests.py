"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client 
from django.utils import unittest
from models import Share, Category
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ShareTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'test2', password = 'test1')
        # self.up = UserProfile.objects.create(user=self.user)
        self.cat = Category.objects.create(name = 'maskar')
        self.ad = Share.objects.create(title = 'Foo', text = 'foo bar', category = self.cat, image = 'dog.jpg', user = self.user.profile)
    
  
    def test_title_set(self):
        self.assertEqual(unicode(self.ad.title), 'Foo')
    
    def test_status(self):
        self.assertEqual(unicode(self.ad.text), 'foo bar')
    
    def test_category_that_don_t_exist(self):
        self.assertNotEqual(self.ad.category, 'jord')
    

   
    def test_add_ad(self):
        c = Client()
        response = c.post('/ads/add/',
                          {
                            'title': 'Foo',
                            'text': 'foo bar',
                            'category': 'djur', 
                            'image': 'djur.jpg',
                           })
        self.assertEqual(response.status_code, 302) #har redirectat
        data = Share.objects.get(pk=1)
        self.assertEqual(data.title, 'Foo')
        
    def tearDown(self):
        self.user.delete()
        self.cat.delete()
        self.ad.delete()