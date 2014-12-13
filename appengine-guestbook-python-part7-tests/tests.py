import random
import unittest
import webtest
import webapp2

class HelloWorldHandler(webapp2.RequestHandler):
   def get(self):
       # Create the handler's response "Hello World!" in plain text.
       self.response.headers['Content-Type'] = 'text/plain'
       self.response.out.write('Hello, Universe!')

class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass
    def test(self):
        self.assertTrue(True)
        self.assertFalse(True)

class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGI application.
        app = webapp2.WSGIApplication([('/', HelloWorldHandler)])
        # Wrap the app with WebTest's TestApp.
        self.testapp = webtest.TestApp(app)

    # Test the handler.
    def testHandler(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.normal_body, 'Hello, Universe!')
        self.assertEqual(response.content_type, 'text/plain')

if __name__ == '__main__':
    unittest.main()
