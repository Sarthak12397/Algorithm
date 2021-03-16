import unittest
import backend.Dbconnection


class TestDBconnect(unittest.TestCase):
    def setUp(self):
        """
            creating an object for class DBconnect
        """
        self.obj = backend.Dbconnection.DBConnect()


    def test_delete(self):
        query = "insert into user_detail values (%s,%s,%s,%s,%s)"
        values = ('n', 'n', 'n', 'n', 'n')
        self.obj.insert(query, values)

        query = "delete from user_detail where userid=%s"
        value = ('n',)
        result = self.obj.delete(query, value)
        self.assertEquals(None, result)

    def test_update(self):
        query = "insert into user_detail values (%s,%s,%s,%s,%s)"
        values = ('n', 'n', 'n', 'n', 'n')
        self.obj.insert(query, values)
        query = "Update user_detail set username=%s,password=%s,email=%s,address=%s where userid=%s"
        values = ('n', 'e', 'r', 't', 'y')
        self.obj.update(query, values)

    def test_insert(self):
        query = "insert into user_detail values (%s,%s,%s,%s,%s)"
        values = ('n', 'n', 'n', 'n', 'n')
        self.obj.insert(query, values)
        result = self.obj.insert(query, values)
        self.assertEquals(None, result)

    def test_read(self):
        query = "insert into user_detail values (%s,%s,%s,%s,%s)"
        values = ('n', 'n', 'n', 'n', 'n')
        self.obj.read(query, values)
        result = self.obj.read(query, values)
        self.assertEquals(None, result)



    def tearDown(self):
        """
                function to tear down the object
        """
        del self.obj

if __name__ == '__main__':
    unittest.main()