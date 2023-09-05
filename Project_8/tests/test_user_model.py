import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def test_password_setter(self):
        u = User()#применяет сеттер
        u.password = "power"
        self.assertFalse(u.password is None)

    def test_no_password_getter(self):
        u = User()  # применяет сеттер
        u.password = "power"
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User()
        u.password = "power"
        u.verify_password("pop")
        self.assertFalse(u.verify_password("pop"))
        self.assertFalse(u.verify_password("true"))