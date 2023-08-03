from django.test import TestCase

from blog.models import User, Post


class UserTest(TestCase):
    """ Test module for User model """
    def setUp(self):
        User.objects.create(
            name='Сергей', email='kruser@yandex.ru')

    def test_user_str(self):
        new_user = User.objects.get(email='kruser@yandex.ru')
        self.assertEqual(new_user.__str__(), "kruser@yandex.ru")


class PostTest(TestCase):
    """ Test module for User model """
    def setUp(self):
        user = User.objects.create(
            name='Сергей', email='kruser@yandex.ru')
        Post.objects.create(
            title='Первый пост',
            body='Lorem lorem',
            user=user
        )

    def test_post_create(self):
        user = User.objects.get(email='kruser@yandex.ru')
        post = Post.objects.get(user=user)
        self.assertEqual(post.__str__(), "Первый пост")
        self.assertEqual(post.user, user)
