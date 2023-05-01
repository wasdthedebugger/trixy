# Trixy 

Trixy is an AI assistant that can help you with running commands, creating files, and more. Trixy is still in development, so there may be alot of bugs. If you find any bugs, please report them in the issues tab.

## How to use
To use Trixy, you can clone this repo and run the `trixy.py` file, or you can download the `trixy.exe` file from the releases tab if you are on Windows. On the first run of Trixy, she will ask you for an API key from Open AI. You can get one [here](https://beta.openai.com/). After you get your API key, paste it into the terminal and press enter. Trixy will then save your API key to a file called `settings.json` so you don't have to enter it again.

## Security

Since Trixy is still in development, she cannot always be trusted to run commands. There is a secure mode that you can enable while setting up Trixy. This will make Trixy ask you if you want to run a command before running it. To enable secure mode, type `secure` when Trixy asks you for a command. 

If you want to run secure mode on a specific command, type `secure` before the command. For example, if you want to run `mkdir test` in secure mode, type `secure mkdir test`.

## Examples

### Create a file
```
trixy create a file called test.txt
```

### Create a folder
```
trixy create a folder called test
```

### initialize a git repo in current directory
```
trixy init a git repo
```

The general idea is to just make a command that you would normally run in the terminal, but in plain english. Trixy will then run the command for you. Trixy is useful for people who are new to the terminal or feel more comfortable using plain english instead of commands.
