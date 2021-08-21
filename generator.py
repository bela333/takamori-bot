import os
import requests
from requests import api

def generate():
    api_key = os.environ.get("OPENAI_API_KEY")
    data = {
        "prompt": "A story about two girls, Kiara and Calli. They are deeply in love with each other.\ncalli: can i tell you something? don't freak out.\n\nkiara: what makes you think i will freak out?\n\ncalli: i love you.\n\nkiara: im freaking out\n===\nkiara: i thought you wanted to take pics of the scenery? why am i always in it?\n\ncalli: no photograph is beautiful without you in it. now get in the fucking frame.\n===\nkiara: [leans in to kiss calli]\n\ncalli: kiara please, nobody knows we're dating.\n\nina, gura, irys, ame: yes we do.\n===\ncalli: hey kiara, can you do the thing?\n\nkiara: what thing?\n\ncalli: the thing that never fails to make me happy.\n\nkiara: [smiles awkwardly]\n\ncalli: thank you.\n===\n",
        "temperature": 0.69,
        "max_tokens": 128,
        "top_p": 1,
        "frequency_penalty": 0.37,
        "presence_penalty": 0,
        "stop": ["==="]
    }
    headers = {
        'Authorization': "Bearer " + api_key
    }
    r = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        json=data,
        headers=headers
    )
    return r.json()["choices"][0]["text"]