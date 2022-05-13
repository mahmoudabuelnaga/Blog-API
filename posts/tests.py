from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts

# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create(username="mahmoud", password="m1751998")
        testpost1 = Posts.objects.create(author=testuser1, title="Blog Title", body="Blog Content...")
        testuser1.save()
        testpost1.save()
    
    def test_blog_content(self):
        post = Posts.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"

        self.assertEqual(author, "mahmoud")
        self.assertEqual(title, "Blog Title")
        self.assertEqual(body, "Blog Content...")
