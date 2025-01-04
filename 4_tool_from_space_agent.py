from smolagents import Tool, CodeAgent, HfApiModel
from gradio_client import Client

class ImageGenerationTool(Tool):
    name = "image_generator"
    description = "Generate an image from a text prompt using FLUX.1-schnell model"
    inputs = {
        "prompt": {
            "type": "string",
            "description": "The text prompt to generate the image from"
        }
    }
    output_type = "image"

    def __init__(self):
        super().__init__()
        self.client = Client("black-forest-labs/FLUX.1-schnell")
    
    def forward(self, prompt: str):
        result, seed = self.client.predict(
            prompt,              # prompt
            0,                  # seed
            True,               # randomize_seed
            1024,              # width
            1024,              # height
            4,                 # num_inference_steps
            api_name="/infer"
        )
        return result

# Create an instance of our custom tool
image_generation_tool = ImageGenerationTool()

# Create the agent and run
model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
agent = CodeAgent(tools=[image_generation_tool], model=model)

# Pass the prompt as part of the instruction
agent.run(
    "Improve this prompt and generate an image of it: 'A rabbit wearing a space suit'"
)