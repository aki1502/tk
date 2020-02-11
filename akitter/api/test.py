from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase



class AkeetListCreateAPITestCase(APITestCase):
    """AkeetListCreateAPIViewのテスト"""
    path = "/akitter/api/akeets/"
    rpath = "/akitter/api/register/"
    tpath = "/akitter/api/auth/token/"

    def setUp(self):
        User.objects.create(username="alice", password="arisugawa")
        User.objects.create(username="bob", password="dylan")
        self.alice = User.objects.get(username="alice")
        self.bob = User.objects.get(username="bob")

    def test_get_akeet_list(self):
        Token.objects.create(user=self.alice)
        token = Token.objects.get(user=self.alice)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = self.client.get(self.path, None, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token.delete()

    def test_akeet_new_akeet(self):
        response = self.client.post(
            self.rpath,
            {
                "username": "charlie",
                "password": "chocolate",
                "re_password": "chocolate"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            self.tpath+"login/",
            {
                "username": "charlie",
                "password": "chocolate"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data["auth_token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")
        response = self.client.post(
            self.path,
            {
                "text": "こんにちは、世界！",
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(
            self.path,
            None,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.post(
            self.tpath+"logout/",
            None,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.post(
            self.path,
            {
                "text": "Hello, World!"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
