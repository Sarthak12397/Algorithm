import unittest
import User

class test(unittest.TestCase):
    def test_uname(self):
        self.assertEqual(User.add_btn("asfa"),"asfa")

    def userinfo(self):
        self.assertEqual(User.userinfo("username"),"userID")

if __name__ == '__main__':
    unittest.main()