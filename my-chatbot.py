# import the OpenAI Python library for calling the OpenAI API
import openai

# Your openAI API key does here:
openai.api_key = "enter your key here"

# the model we'll be using
MODEL = "gpt-3.5-turbo"

# your chatbot's name
botname = "Zeus"

# The initial prompt. Tell the chatbot how you want it to behave.
messages=[
    {"role": "system", "content": "Present yourself as a Greek God. Use colourful language and talk like Zeus."}
]

# we want to run some commands once when we start the program, so we'll use this flag
first_run = True

# our chat routine
while True:

    # Show the user instructions and introduce the chatbot by name.
    if first_run == True:
       print("Type exit to leave the chat. Initialising chatbot: "+str(botname)+".")
       first_run = False

    user_input = input("You: ")
    # exit on command 
    if user_input == 'exit':
        exit()

    prompt = {"role": "user", "content": user_input}
    messages.append(prompt)

    # Example OpenAI Python library request - defines the model we wish to use, and uses the ChatCompletion routine to send a prompt.
    response = openai.ChatCompletion.create(model=MODEL, temperature=0, messages=messages)

    # extract and print the response
    print(str(botname)+': '+str(response['choices'][0]['message']['content'])+'\n')
    messages.append(response['choices'][0]['message'])
            

