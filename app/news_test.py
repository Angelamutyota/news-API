import unittest
from models import Source
News = Source

class TestSource(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source('apple','apple launch', 'angela','apple launches a new iphone to the market', 'https://1734811051.rsc.cdn77.org/data/images/full/386795/apples-new-electric-car.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News))


if __name__ == '__main__':
    unittest.main()