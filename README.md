## Build your own GPT Chatbot that runs on Raspberry Pi

ChatGPT has taken the world with by a storm, not denying that. OpenAI's  GPT large language model (LLM) are extremely powerful chatbot that uses natural language processing to create humanlike conversational dialogue. However, having exposed the model to vast text data lake has meant that we can pretty much ask it anything and it will be generative and creative in its response. Hence the term generative pre-trained transformer (GPT). I wanted to give it a go and create an interface for a low-power resource constraint computer and a tiny microcontroller. Let's go.

——————————————————————
## Step 1: Create an #OpenAI account
——————————————————————

You can go to platform.openai.com/signup and create an account. You should get some credit to start with. Note: you need credits to use OpenAI's models, whether you access them via the web or API calls. OpenAI is proprietary, however, there's an open-source alternative, check GPT-J-6B

——————————————————
## Step 2: Generate an API key
——————————————————

This is simple, go to platform.openai.com/account/api-keys, then click the 'Create new secret key' button. Make sure you copy and save the key in a secure location as you won't see this message again.

——————————————————————
## Step 3: Install Python openai library
——————————————————————

`pip install openai`

`[git clone https://](https://github.com/robosinghai/my-chatbot.git)`

Note: You can change the name of the bot in the code and add personality prompts by changing the role and content settings. Finally, you can turn the 'temperature' setting up (range between 0 to 1), that controls the randomness of a response. The higher the number, the more random response you get from the model.
