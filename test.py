import database
import unittest

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        database.delete_stories()

    def test_empty(self):
        self.assertEqual(0,len(database.get_stories()))
    def test_add_story(self):
        database.add_story("new story")
        self.assertEqual(1,len(database.get_stories()))
    def test_delete_story(self):
        database.add_story("new story")
        database.delete_story("new story")
        self.assertEqual(0,len(database.get_stories()))
    def test_add_same_story(self):
        database.add_story("new story")
        database.add_story("new story")
        self.assertEqual(1,len(database.get_stories()))
    def test_add_comment(self):
        database.add_story("new story")
        database.add_comment("new story","comment one")
        database.add_comment("new story","comment two")
        self.assertEqual(2,len(database.get_comments("new story")))
    def test_get_comments(self):
        database.add_story("new story")
        database.add_comment("new story","comment one")
        database.add_comment("new story","comment one")
        comments=database.get_comments("new story")
        self.assertEqual(["comment one","comment one"],comments) 

if __name__=='__main__':
    unittest.main()
