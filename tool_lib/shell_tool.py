from langchain_community.tools import ShellTool

shell_tool = ShellTool()

print(shell_tool.run({"commands": ["echo 'Hello World!'", "time"]}))