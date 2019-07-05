from django.test import TestCase

# Create your tests here.

#All 

class HomePageTesting(TestCase):
    
    def test_home_page_status_code(self):
        response=self.client.get('/home/')
        self.assertEquals(response.status_code,200)
    
    def test_homepage_html(self):
        response=self.client.get('/home/')
        self.assertContains(response,'Search')
        
    def test_for_incorrect_html(self):
        response=self.client.get('/home/')
        self.assertNotContains(response,'I SHOULDNT BE HERE!')
    
    def test_template_correctness(self):
        response=self.client.get('/home/')
        self.assertTemplateUsed(response,'home_page.html')
        