import unittest
import requests
import json

class TestAPI(unittest.TestCase):
    URL = "https://teaching-assistant-evaluation.onrender.com/crudop"
    
    data = {
        "id": 3,
        "native_english_speaker": 1,
        "course_instructor": 19,
        "course": 2,
        "semester": 1,
        "class_size": 19,
    }

    expected_result = {
        "id": 1,
        "native_english_speaker": 1,
        "course_instructor": 23,
        "course": 3,
        "semester": 1,
        "class_size": 19,
    }

    update_data = {
        "id": 5,
        "native_english_speaker": 1,
        "course_instructor": 18,
        "course": 1,
        "semester": 1,
        "class_size": 15,
    }
    def test_1_get_all_crudop(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.json()),5)
        print("Test 1 (GET) completed")

    def test_2_post(self):
        resp = requests.post(self.URL + '/3', json=self.data)
        print("Test 2 (POST) completed")

    def test_3_get_specific(self):
        resp = requests.get(self.URL + '/1')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(resp.json(), self.expected_result)
        print("Test 3 (GET-Specific) completed")
    
    def test_4_delete(self):
        resp = requests.delete(self.URL + '/2')
        print("Test 4 (delete) completed")

    def test_5_update(self):
        resp = requests.put(self.URL + '/5', json=self.update_data)
        self.assertEqual(resp.json()['id'], self.update_data['id'])
        self.assertEqual(resp.json()['native_english_speaker'], self.update_data['native_english_speaker'])
        self.assertEqual(resp.json()['course_instructor'], self.update_data['course_instructor'])
        self.assertEqual(resp.json()['course'], self.update_data['course'])
        self.assertEqual(resp.json()['semester'], self.update_data['semester'])
        self.assertEqual(resp.json()['class_size'], self.update_data['class_size'])
        print("Test 5 (update) completed")



if __name__=="__main__":
    tester = TestAPI()
   
    tester.test_1_get_all_crudop()
    tester.test_2_post()
    tester.test_3_get_specific()
    tester.test_4_delete()
    tester.test_5_update()
    
