import tweet
#import json
#import base64
#from urllib.parse import quote
from PIL import Image

#link_data = {
#    "text":text,
#    "width":"250",
#    "v":"20",
#    "h":"100",
#    "side":"left"
#}
#link_data = json.dumps(link_data)
#link_data = base64.b64encode(link_data.encode("UTF-8"))
#link_data = quote(link_data)
#link = "https://rescrabs.github.io/takamori_comic/#"+link_data
image = Image.open("image.png")
tweet.upload(image)