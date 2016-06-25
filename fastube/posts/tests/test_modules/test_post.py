from django.test import TestCase
from django.contrib.auth import get_user_model


class TestPost(TestCase):

    def setUp(self):
        self.test_username = "test_user"
        self.test_userpassword = "test_password"

        user = self.user = get_user_model().objects.create_user(
            username=self.test_username,
            password=self.test_userpassword,
        )

        self.assertEqual(
            user.username,
            self.test_username
        )

        # Create Post
        self.post_video_id = "lcmAdIdSA5k"

        self.post = self.user.post_set.create(
            video_id=self.post_video_id,
            title="test_title",
        )

    def test_post_model_should_have_youtube_origin_url(self):
        """
        Post 모델은 가지고 있는 video_id를 이용해서
        youtube 원본영상의 링크를 생성할 수 있어야 한다.
        """
        self.assertEqual(
            self.post.youtube_original_url,
            "https://www.youtube.com/watch?v={post_video_id}".format(
                post_video_id=self.post_video_id,
            )
        )
