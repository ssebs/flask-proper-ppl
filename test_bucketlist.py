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

    def setUp(self):
        self.app = create_app(config="test")
        self.sampleperson = {
            "email": "tuser@parc.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "test"
        }
        firstUsr = Person(
            first_name="First",
            last_name="Person",
            email="fp@test2.com",
            password="test"
        )
        with self.app.app_context() as ctx:
            db.create_all()
            db.session.add(firstUsr)
            db.session.commit()

            print(Person.query.all())

            self.acc_tok = create_access_token(
                identity=self.sampleperson["email"]
            )
            self.headers = {"Authorization": f"Bearer {self.acc_tok}"}
            self.client = self.app.test_client
    # setUp

    def test_create_person(self):
        resp = self.client().post("/people/",
                                  headers=self.headers,
                                  json=self.sampleperson)

        data = resp.json["Person"]
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data["first_name"], "Test")
        self.assertRegex(data["password"], "^pbkdf2:sha256:")
        print("Tested Create Person")

    def test_get_all_users(self):
        resp = self.client().get("/people/", headers=self.headers)
        data = resp.json
        print(data)
        # print(self.acc_tok)

    def tearDown(self):
        with self.app.app_context() as ctx:
            db.session.remove()
            db.drop_all()

# PPLProperTestCase
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
