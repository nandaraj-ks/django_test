from django.test import LiveServerTestCase
from django.utils.unittest import skipIf
from django.conf import settings
 
from pyvirtualdisplay import Display
from selenium import webdriver
 
 
 
class ExampleTestCase(LiveServerTestCase):
	def setUp(self):
		# start display
		self.vdisplay = Display(visible=0, size=(1024, 768))
		self.vdisplay.start()
 
		# start browser
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		super(ExampleTestCase, self).setUp()
 
	def tearDown(self):
		# stop browser
		self.selenium.quit()
		super(ExampleTestCase, self).tearDown()
 
		# stop display
		self.vdisplay.stop()
 
	def test_example(self):
		# run tests
                print self.live_server_url
		self.selenium.get(
			'%s%s' % (self.live_server_url,'/add')
		)
		test = self.selenium.find_element_by_id('test')
		self.assertEqual(test.text,"Hello World!")
