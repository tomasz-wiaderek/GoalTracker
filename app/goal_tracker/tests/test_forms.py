from django.test import TestCase
from ..forms import UserRegisterForm, UserUpdateForm


class UserRegisterFormTest(TestCase):

    def setUp(self):

        self.data = {
            'username': 'TestUser',
            'email': 'testuser@mail.com',
            'password1': 'testing321',
            'password2': 'testing321'}

    def test_UserRegisterForm_is_valid(self):

        form = UserRegisterForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_UserRegisterForm_missing_username(self):

        self.data['username'] = None
        form = UserRegisterForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_UserRegisterForm_missing_email(self):

        self.data['email'] = None
        form = UserRegisterForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_UserRegisterForm_missing_password1(self):

        self.data['password1'] = None
        form = UserRegisterForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_UserRegisterForm_missing_password2(self):

        self.data['password2'] = None
        form = UserRegisterForm(data=self.data)

        self.assertFalse(form.is_valid())


class UserUpdateFormTest(TestCase):

    def setUp(self):

        self.data = {
            'username': 'UpdatedUser',
            'email': 'updatedmail@mail.com'}

    def test_UserUpdateForm_is_valid(self):

        form = UserUpdateForm(data=self.data)

        self.assertTrue(form.is_valid())

    def test_UserUpdateForm_missing_username(self):

        self.data['username'] = None
        form = UserUpdateForm(data=self.data)

        self.assertFalse(form.is_valid())

    def test_UserUpdateForm_missing_email(self):

        self.data['email'] = None
        form = UserUpdateForm(data=self.data)

        self.assertFalse(form.is_valid())
