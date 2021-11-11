import requests
print("Welcome to Triemaker!")
print(
    '''In every subsequent line, you will be able to enter a command when prompted. Enter \"display\" if you want to visualize your trie. You may enter \"add [keyword]\" or \"delete [keyword]\" to add or delete keywords to your trie. To check whether a keyword exists in a trie, you can input \"check [keyword]\". Finally, you can also type \"suggest [prefix]\" to enter a string prefix and obtain a list of suggestions based on this prefix.\n''')
s = input("<User> ")
commands = ["add", "suggest", "remove", "suggestions", "display", "check"]
host = "https://triemaker.herokuapp.com"
while s != "exit":
    s = s.split()
    if not s:
        print(f"Please enter a command...")
    elif s[0] not in commands:
        s[0] = s[0].lower()
        print(f"Error: Command \"{s[0]}\" not recognized...")
    elif s[0].lower() == "display":
        out = requests.get(host+"/display")
        print(out.json()["status"])
    elif len(s) < 2:
        s[0] = s[0].lower()
        print(
            f"Error: Command \"{s[0]}\" needs an argument [keyword].\nOperation failed...")
    elif len(s) > 2:
        print(f"Error: Too many arguments passed to function at once.\nOperation failed...")
    else:
        s[0] = s[0].lower()
        s[1] = s[1].lower()
        out = requests.get(host+f"/{s[0]}/{s[1]}")
        print(out.json()["status"])
    s = input("<User> ")
