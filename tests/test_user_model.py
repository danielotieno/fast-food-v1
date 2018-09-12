from app.model import User, db
from .entry import EntryClass


class TestUserModel(EntryClass):
    """ Class for user model test cases """

    def test_can_save_user(self):
        """ Test to save user """
        user = self.user1.save()
        self.assertEqual(1, len(db.users))
        self.assertTrue(isinstance(user, dict))
