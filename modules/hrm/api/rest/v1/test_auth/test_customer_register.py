from rest_framework.test import APITestCase
from django.urls import reverse


class TestCustomerAuth(APITestCase):
    header = {
        "Content-Type": "application/json",
    }

    def test_login_get_token(self):
        res = self.client.post(
            path=reverse("auth-customer-login"),
            data={"username": "09358588181"},
            headers=self.header,
            format="json"
        )
        self.assertEqual(res.status_code, 200)
        self.client.post(
            path=reverse("auth-customer-get-token"),
            data={"username": "09358588181", "code": res.json()["data"]["code"]},
            format="json",
            headers=self.header,
        )
        self.assertEqual(res.status_code, 200)
