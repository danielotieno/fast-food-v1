from app.model import User, db
from .entry import EntryClass


class TestUserModel(EntryClass):
    """ Class for user model test cases """

    def test_get_user(self):
        """ Test to get an user  """
        self.user1.save()
        user = User.get(id=1)
        self.assertIsInstance(user, User)
        keys = sorted(list(user.view().keys()))
        self.assertListEqual(keys, sorted(['username', 'email', 'id']))

    def test_can_save_user(self):
        """ Test to save user """
        user = self.user1.save()
        self.assertEqual(1, len(db.users))
        self.assertTrue(isinstance(user, dict))
