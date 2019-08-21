'''
# test_pplproper.py - Testing suite
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
            email="tuser@test.com",
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
        print("Testing create person...", end="")
        resp = self.client.post("/people/",
                                headers=self.headers,
                                json=self.sample_person.as_dict())

        data = resp.json["Person"]
        status = resp.json["Status"]
        self.assertEqual(status, "Created")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data["first_name"], "Test")
        self.assertTrue(data["active"])
        self.assertRegex(data["password"], "^pbkdf2:sha256:")
        print("Done")
    # test_create_person

    def test_get_all_people(self):
        print("Testing get all people...", end="")
        self.client.post("/people/",
                         headers=self.headers,
                         json=self.sample_person.as_dict())
        resp = self.client.get("/people/", headers=self.headers)

        data = resp.json["People"]
        status = resp.json["Status"]
        self.assertEqual(status, "OK")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(data), list)
        self.assertEqual(data[0]["first_name"], "Test")

        print("Done")
    # test_get_all_people

    def test_get_one_person(self):
        print("Testing get one person...", end="")
        self.client.post("/people/",
                         headers=self.headers,
                         json=self.sample_person.as_dict())
        resp = self.client.get("/people/1", headers=self.headers)

        data = resp.json["Person"]
        status = resp.json["Status"]
        self.assertEqual(status, "OK")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["first_name"], "Test")

        print("Done")
    # test_get_one_person

    def test_update_person(self):
        print("Testing update person...", end="")
        post_resp = self.client.post("/people/",
                                     headers=self.headers,
                                     json=self.sample_person.as_dict())
        person = post_resp.json["Person"]
        person["first_name"] = "NewName"
        resp = self.client.put("/people/1", headers=self.headers, json=person)

        data = resp.json["Person"]
        status = resp.json["Status"]
        self.assertEqual(status, "Updated")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data["first_name"], "NewName")
        self.assertEqual(data["id"], 1)

        print("Done")
    # test_update_person

    def test_delete_person(self):
        print("Testing delete_person...", end="")
        self.client.post("/people/",
                         headers=self.headers,
                         json=self.sample_person.as_dict())

        resp = self.client.delete("/people/1", headers=self.headers)

        status = resp.json["Status"]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(status, "Deleted")

        print("Done")
    # test_delete_person

    def test_login(self):
        print("Testing login...", end="")

        print("Done")
    # test_login

    def test_refresh_jwt(self):
        print("Testing refresh jwt...", end="")

        print("Done")
    # test_refresh_jwt

    def test_password_reset(self):
        print("Testing password reset...", end="")

        print("Done")
    # test_password_reset

    def tearDown(self):
        db.session.remove()
        db.drop_all()


# PPLProperTestCase
if __name__ == "__main__":
    unittest.main()
