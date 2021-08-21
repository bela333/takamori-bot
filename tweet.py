import tweepy
import os
from PIL import Image
import io

def upload(image, reply_message):
    auth = tweepy.OAuthHandler(os.environ.get("TWITTER_KEY"), os.environ.get("TWITTER_SECRET"))
    auth.set_access_token(os.environ.get("TWITTER_TOKEN"), os.environ.get("TWITTER_TOKEN_SECRET"))
    api = tweepy.API(auth)

    b = io.BytesIO()
    image.save(b, "png")
    b.seek(0)

    media = api.media_upload("image.png", file=b)
    status = api.update_status(media_ids=[media.media_id])
    api.update_status(status=reply_message, in_reply_to_status_id=status.id)