'''
# test_bucketlist.py - Testing suite
'''
import unittest
import os
import json

from flask_jwt_extended import create_access_token

from pplproper import create_app, db
from pplproper.models import Person


class PPLProperTestCase(unittest.TestCase):

    def create_app(self):
        return create_app(config="test")

    def setUp(self):
        self.app = self.create_app()
        self.sample_person = Person(
            first_name="Test",
            last_name="User",
            email="tuser@parc.com",
            password="test"
        )
        with self.app.test_request_context() as ctx:
            db.create_all()

            self.acc_tok = create_access_token(
                identity=self.sample_person.email
            )
            self.headers = {"Authorization": f"Bearer {self.acc_tok}"}
            self.client = self.app.test_client()
    # setUp

    def test_create_person(self):
        print("Testing Create Person...", end="")
        resp = self.client.post("/people/",
                                headers=self.headers,
                                json=self.sample_person.as_dict())
        data = resp.json["Person"]

        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data["first_name"], "Test")
        self.assertTrue(data["active"])
        self.assertRegex(data["password"], "^pbkdf2:sha256:")
        print("Done")

    def test_get_all_users(self):
        print("Testing Get all People...", end="")
        self.client.post("/people/",
                         headers=self.headers,
                         json=self.sample_person.as_dict())
        resp = self.client.get("/people/", headers=self.headers)
        data = resp.json["People"]

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(data), list)
        self.assertEqual(data[0]["first_name"], "Test")

        print("Done")

    def tearDown(self):
        db.session.remove()
        db.drop_all()


# PPLProperTestCase
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
