from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class APIRootTests(TestCase):
	def setUp(self):
		self.client = APIClient()

	def test_api_root(self):
		response = self.client.get(reverse('api-root'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('users', response.data)
		self.assertIn('teams', response.data)
		self.assertIn('activities', response.data)
		self.assertIn('leaderboard', response.data)
		self.assertIn('workouts', response.data)
