import unittest
from protector.client import ProtectorClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        client = ProtectorClient("127.0.0.1", 8888)
        return_msg = client.password("123456789")
        print(return_msg)
        # self.assertIsNotNone(return_msg)

        client.close()

        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
