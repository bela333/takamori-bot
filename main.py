import renderer
import generator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#text = generator.generate()
text = "kiara: hey calli, are you ready for your audition?\n\ncalli: im nervous, but i think i'll be fine.\n\nkiara: you'll do great.\n\ncalli: how do you know?\n\nkiara: because you're amazing. and also, i believe in you."
image = renderer.render(text)
image.show()