import unittest
from entity.user import User

class TestUserLogin(unittest.TestCase):
    def test_user_login(self):
        user=User(user_id=1,user_name="Sameer",password="Sam@1234")
        self.assertEqual(user.get_user_id(),1)
        self.assertEqual(user.get_user_name(),"Sameer")
        self.assertEqual(user.get_password(),"Sam@1234")
        print("User Logged in successfully!")

if __name__=="__main__":
    unittest.main()