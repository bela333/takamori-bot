import renderer
import generator
import io
import base64

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

text = generator.generate()
image = renderer.render(text)

image.save("image.png")
mem = io.BytesIO()
image.save(mem, format = "PNG")
mem.seek(0)
print(base64.b64encode(mem.read()))