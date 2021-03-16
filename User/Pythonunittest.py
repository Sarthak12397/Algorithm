import unittest
import Model.model
class TestInventory_m(unittest.TestCase):
    def setUp(self):
        """
            creating a new instance for class Inventory_m
        """
        self.a = Model.model.user()

    def test_set_userid(self):
        #Assume
        uid = "saugat"
        #Action
        result = self.a.set_userId(uid)
        #Assert
        self.assertEqual("saugat", self.a.get_userId())
    def test_username(self):
        #Assume
        shar = "nikita"
        #Action
        result = self.a.set_username(shar)
        #Assert
        self.assertEqual("nikita", self.a.get_username())
    def test_age(self):
        #Assume
        agg= "11"
        #Action
        result = self.a.set_address(agg)
        #Assert
        self.assertEqual("11", self.a.get_address())
    def test_email(self):
        #Assume
        gen = "sujan@gmail.com"
        #Action
        result = self.a.set_email(gen)
        #Assert
        self.assertEqual("sujan@gmail.com", self.a.get_email())
    def test_password(self):
        #Assume
        fname = "snli"
        #Action
        result = self.a.set_password(fname)
        #Assert
        self.assertEqual("snli", self.a.get_password())



    def tearDown(self):
        """
                function to tear down the object
        """
        del self.a

if __name__ == '__main__':
    unittest.main()