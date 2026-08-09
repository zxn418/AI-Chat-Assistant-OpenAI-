from openai import OpenAI
from setting import config

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=config.get_openai_api_key())

    def query(self, prompt: list[dict]) -> str:
        response = self.client.responses.create(
            model="gpt-5.4-mini",
            input=prompt,
            instructions="You are a helpful assistant for a developer to help fix the code and generate the code.",
        )
        return response.output_text

    def generate_image(self, prompt: str):
        response = self.client.images.generate(
            model="gpt-image-2",
            prompt=prompt
        )
        return response.data[0].b64_json

    def generate_response_from_image(self, image_data_url: str, prompt:str):
        response = self.client.responses.create(
            model="gpt-5.5",
            input=[
                {
                    "role":"user",
                    "content":[
                        {
                            "type": "input_text",
                            "text": prompt,
                        },
                        {
                            "type": "input_image",
                            "image_url": image_data_url,
                        },
                    ],
                }
            ],
        )
        return response.output_text

client = OpenAIClient()