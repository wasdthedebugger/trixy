import sys
import openai
import re
import os
import json

# Ask user for OpenAI API key and system/shell choice and secure mode preference on first run
if not os.path.isfile('settings.json'):
    print("Trixy will help you with command line tasks. She needs some information to get started with.")
    systemname = input(
        "Enter your system/shell name (e.g. bash, zsh, powershell): ")
    isSecure = input(
        "Do you want to run in secure mode? (y/n): ").lower() == "y"
    openai_api_key = input("Enter your OpenAI API key: ")
    with open('settings.json', 'w') as f:
        json.dump({'openai_api_key': openai_api_key,
                  'systemname': systemname, 'isSecure': isSecure}, f)
    print("Trixy is ready to help you. You can now get her help by typing 'trixy' followed by your instruction.")
    print("Example: trixy create a new file named 'test.txt' in the current directory")
    sys.exit()
else:
    # Load saved settings from file
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        openai_api_key = settings['openai_api_key']
        systemname = settings['systemname']
        isSecure = settings['isSecure']

openai.api_key = openai_api_key


def parse_command(user_input):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Generate a {systemname} command equivalent command to carry out the task mentioned: {user_input}. If you don't get enough context and are not sure about it then just say 'confused' and nothing else.\n"),
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    parsed_command = response.choices[0].text.strip()
    return parsed_command


def execute_command(command):
    os.system(command)


def handle_user_input(user_input):
    parsed_command = parse_command(user_input)
    # if lowercase confused is found in the command then we assume that GPT is confused and we ask the user to try again
    if "confused" in parsed_command.lower():
        print("Trixy is confused. Please try again with a different instruction.")

    elif isSecure:
        # if secure we ask for confirmation before executing the command
        print("The command generated is: " + parsed_command)
        confirmation = input(
            "Are you sure you want to execute this command? (y/n): ")
        if confirmation == "y":
            execute_command(parsed_command)
        else:
            print("Command not executed.")
    else:
        execute_command(parsed_command)


if len(sys.argv) > 1:
    user_input = ' '.join(sys.argv[1:])
    handle_user_input(user_input)
else:
    print("Trixy. Version 1.0. Developed by Nikas Ghimire.")
