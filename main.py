import renderer
import generator
import tweet
import json
import base64
from urllib.parse import quote

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

text = generator.generate()
#text = "kiara: hey calli, are you ready for your audition?\n\ncalli: im nervous, but i think i'll be fine.\n\nkiara: you'll do great.\n\ncalli: how do you know?\n\nkiara: because you're amazing. and also, i believe in you."
link_data = {
    "text":text,
    "width":"250",
    "v":"20",
    "h":"100",
    "side":"left"
}
link_data = json.dumps(link_data)
link_data = base64.b64encode(link_data.encode("UTF-8"))
link_data = quote(link_data)
link = "https://rescrabs.github.io/takamori_comic/#"+link_data
image = renderer.render(text)
tweet.upload(image, "You can edit this comic at {}".format(link))