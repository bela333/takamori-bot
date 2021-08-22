import renderer
import generator


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

text = generator.generate()
image = renderer.render(text)

image.save("image.png")