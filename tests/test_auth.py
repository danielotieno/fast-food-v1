import json

from .entry import EntryClass

SIGNUP_URL = '/api/v1/auth/signup'
LOGIN_URL = '/api/v1/auth/login'


class TestAuth(EntryClass):
    """ Add tests for Auth """

    def test_registration(self):
        """ Test user registration works correcty """
        response = self.client.post(SIGNUP_URL,
                                    data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"],
                         "registration successful, now login")

    def test_wrong_registration(self):
        """Test wrong registration when user doesn't fill fields"""
        response = self.client.post(SIGNUP_URL,
                                    data=json.dumps(
                                        {'username': 'danny', 'email': 'short@gmail.com', 'password': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "All fields are required")

    def test_cannot_register_twice(self):
        """ Test User cannot register twice """
        self.client.post(SIGNUP_URL,
                         data=json.dumps(self.user_data), content_type='application/json')
        response2 = self.client.post(SIGNUP_URL,
                                     data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response2.status_code, 203)
        result = json.loads(response2.data.decode())
        self.assertEqual(result["message"], "User already exists")
