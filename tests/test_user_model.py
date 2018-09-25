from app.model import User, DB
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

    def test_get_unavailable_user(self):
        """ Test to get un-available user """
        user = User.get(id=4)
        self.assertEqual('User does not exist.', user['message'])

    def test_save_user(self):
        """ Test to save user """
        user = self.user1.save()
        self.assertEqual(1, len(DB.users))
        self.assertTrue(isinstance(user, dict))

    def test_update_user_details(self):
        """ Test for updating user details """
        data = {
            'username': 'updatename',
            'email': 'updatename@email.com'}
        self.user1.save()
        user = User.get(id=1)
        user = user.update(data=data)
        self.assertEqual(data['username'], user['username'])
        self.assertEqual(data['email'], user['email'])

    def test_delete_user(self):
        """ Test for deleting an user """
        self.user1.save()
        self.assertEqual(1, len(DB.users))
        user = User.get(id=1)
        user.delete()
        self.assertEqual(0, len(DB.users))
