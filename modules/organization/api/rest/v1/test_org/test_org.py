from django.urls import reverse

from rest_framework.test import APITestCase

from modules.common.factory import UserFactory


class TestOrg(APITestCase):

    def setUp(self):
        self.phone = '09135350686'
        self.user = UserFactory(username='09121111111', is_active=True, is_verified=True)
        self.client.force_authenticate(self.user)

    def test_add_org(self):
        res = self.client.post(
            path=reverse("org-list"),
            data={"name": "test org", "language": "fa"},
            format="json"
        )
        self.assertEqual(res.status_code, 201)
