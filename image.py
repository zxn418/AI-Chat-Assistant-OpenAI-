import base64
from ai import client

def generate_and_save(prompt: str, filename: str = "output.png"):
    b64_data = client.generate_image(prompt)
    image_bytes = base64.b64decode(b64_data)
    with open(filename, "wb") as f:
        f.write(image_bytes)
    return filename