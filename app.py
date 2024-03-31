# Import necessary libraries
from g4f.client import Client
import gradio as gr

# Initialize the G4F client
client = Client()

# Function for generating creative writing prompts with advanced options
def generate_writing_prompt(user_input, prompt_style="First Sentence", style="Neutral", tone="Informative", temperature=0.7):
  """
  Generates creative writing prompts based on user input, style, tone, and temperature.

  Args:
      user_input (str): User input like genre, tone, or initial plot point.
      prompt_style (str, optional): Style of the prompt (e.g., First Sentence, Question). Defaults to "First Sentence".
      style (str, optional): Desired style of the prompt (e.g., Formal, Informal, Poetic). Defaults to "Neutral".
      tone (str, optional): Desired tone of the prompt (e.g., Happy, Sad, Mysterious). Defaults to "Informative".
      temperature (float, optional): Controls the randomness of the generated text (0.0 = deterministic, 1.0 = maximum randomness). Defaults to 0.7.

  Returns:
      str: The generated creative writing prompt.
  """
  # Adjust model call based on prompt style
  if prompt_style == "Question":
      message_prefix = f"Write a story in the style of {style} with a tone of {tone} that starts with the question:"
  else:
      message_prefix = f"Write a story in the style of {style} with a tone of {tone} that begins with the sentence:"

  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": message_prefix + user_input}],
      temperature=temperature,
  )
  return response.choices[0].message.content

# Gradio interface with advanced options
interface = gr.Interface(
  fn=generate_writing_prompt,
  inputs=[
      gr.Textbox(lines=3, placeholder="Enter genre, tone, or initial plot point..."),
      gr.Dropdown(choices=["First Sentence", "Question"], value="First Sentence", label="Prompt Style"),
      gr.Radio(choices=["Neutral", "Formal", "Informal", "Poetic"], value="Neutral", label="Style"),
      gr.Radio(choices=["Informative", "Happy", "Sad", "Mysterious"], value="Informative", label="Tone"),
      gr.Slider(minimum=0.0, maximum=1.0, step=0.1, value=0.7, label="Temperature (Randomness)"),
  ],
  outputs="text",
  title="Creative Writing Assistant 📝",
  description="Craft captivating stories with advanced controls! Generate unique prompts with style, tone, and temperature adjustments. Get inspired with plot twists, character ideas, and multiple prompt options.",
  theme="huggingface",
  examples=[
      ["A cyberpunk thriller set in a neon-lit city.", "Question", "Formal", "Mysterious", 0.8],
      ["Compose a humorous limerick about a talking cat.", "First Sentence", "Informal", "Happy", 0.5],
  ],
)

# Launch the interface
if __name__ == "__main__":
  interface.launch()
