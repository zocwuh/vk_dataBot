# vk_dataBot
Run main.py file, all required libs are in **venv** <br>  
Bot saved one data container from user and can send it where user send to bot "!get"
Connected to [VK](https://vk.com/) community(group) by api token, the dafault token's place is envinronment variable "VKKEY"<br>
Bot takes commands:
1. **!r** - to register new user
2. **!put** - to add new data
3. **!get** - to get user data
4. **!d** - to stop escort user <br><br>

***Errors***
1. **"vk_api.exceptions.ApiError: [5] User authorization failed: invalid access_token (4)"**
It means you don't have api token or api token is invalid. If environment variable "VKKEY" doesn't exists programm will attempt to get it from **token.txt** file.
In rest case - you have invalid api token. Api token will be taken from **Manage>API usage>Access tokens**
2. **vk_api.exceptions.ApiError: [15] Access denied: group messages are disabled**
It means your community doesn't allow to use messages. To fix it **Manage>Messages>Community messages** and turn it up Enable
