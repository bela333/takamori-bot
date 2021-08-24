import renderer
import generator
import io
import base64
import json

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

text = generator.generate()
image = renderer.render(text)

image.save("image.png")
mem = io.BytesIO()
image.save(mem, format = "PNG")
mem.seek(0)

with open("text.txt", "w") as f:
    f.write(text)

ret = {
    "image": base64.b64encode(mem.read()).decode("ASCII"),
    "text": text
}
print(json.dumps(ret))