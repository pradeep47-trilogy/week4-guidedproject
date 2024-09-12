from langchain_community.agent_toolkits import FileManagementToolkit

toolkit = FileManagementToolkit()  
# If you don't provide a root_dir, operations will default to the current working directory
toolkit.get_tools()

tools = FileManagementToolkit(
    selected_tools=["read_file", "write_file", "list_directory"],
).get_tools()
print(tools)

read_tool, write_tool, list_tool = tools
write_tool.invoke({"file_path": "example.txt", "text": "Hello World!"})