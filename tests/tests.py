import os
import sys
import unittest
import string
import random
# path to this directory
thisDirect = os.path.dirname(os.path.realpath(__file__))
# get the parent directory as that's where app is
parentDirect = os.path.dirname(thisDirect)
#  reference modules in this directory
sys.path.append(parentDirect)
# only import after
from app import app  # nopep8 (from https://stackoverflow.com/a/57067521)


# get random words for testing values. From: https://stackoverflow.com/a/2030081
def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class TestCoronaApp(unittest.TestCase):
    # ================================================================
    # The following tests deal with getting data from the page

    # Test going to landing page
    def test_home_page(self):
        client = app.test_client(self)
        response = client.get(
            '/', content_type="html/text")
        self.assertIn(b'Corona Archive', response.data)

    def test_visitor_register_page(self):
        client = app.test_client(self)
        response = client.get(
            '/reg_visitor', content_type="html/text")
        self.assertIn(b'New user?', response.data)

    def test_register_locale_page(self):
        client = app.test_client(self)
        response = client.get(
            '/reg_place', content_type="html/text")
        self.assertIn(b'Place Owner?', response.data)

    def test_agent_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/agent', content_type="html/text")
        self.assertIn(b'Agent Login', response.data)

    def test_hospital_login_page(self):
        client = app.test_client(self)
        response = client.get(
            '/hospital', content_type="html/text")
        self.assertIn(b'Hospital Login', response.data)

    # ================================================================
    # The following tests deal with posting data

    # Test registration of visitor with dummy info

    def test_register_visitor_post(self):
        client = app.test_client(self)
        response = client.post('/reg_visitor', data=dict(name=randomword(10), address="testAddress",
                               city="testCity", phoneNumber="123456789", email="test@email.com"), follow_redirects=True)
        self.assertIn(b'Visitor', response.data)

    # Test registration of place with dummy info
    def test_register_locale_post(self):
        client = app.test_client(self)
        response = client.post("/reg_place", data=dict(name="test_name", address="Test st. 123",
                               phoneNumber="12345678", email="test@email.com"), follow_redirects=True)
        self.assertIn(b'Place', response.data)

    # Test agent login
    def test_agent_login_post(self):
        client = app.test_client(self)
        response = client.post("/agent", data=dict(username="Sam", password="password123",
                                                   ), follow_redirects=True)
        self.assertIn(b'Welcome as Agent', response.data)

    # test hospital login
    def test_agent_login_post(self):
        client = app.test_client(self)
        response = client.post("/hospital", data=dict(username="GrandVC", password="healthIsCool",
                                                      ), follow_redirects=True)
        self.assertIn(b'Welcome to Hospital dashboard', response.data)


if __name__ == '__main__':
    unittest.main()



