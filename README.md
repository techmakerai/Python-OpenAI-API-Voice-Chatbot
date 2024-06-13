This Python program calls OpenAI's ChatGPT API to obtain responses for requests or questions from a user and then convert the text responses to voice responses. This version has been tested on Windows 10 and Windows 11. 

Following the YouTube video here to learn more about this code: 
https://youtu.be/kE95xA5jVWQ

Before you can run this code on your computer, you will need to install the following packages on your computer to run this code: 

```console
pip install speechrecognition openai pyttsx3 pyaudio pygame
```
If you have Python 3.12 or newer, also install the "setuptools" package,    

```console
pip install setuptools
```

To use the API key from OpenAI, you can add the key to the Python program or set it as a system environment variables in Windows. 

If you want to use your OpenAI API key in the Python program, then add it as,      
```python
client = OpenAI(api_key="this is your API key")
```

If you want to set the API key from OpenAI as a system environment variable. Here are the steps to do so in Windows via GUI. 

Step 1: Follow the video above to open the System Properties window and click on the "Environment Variables" button
 
<img src="https://github.com/techmakerai/Python-OpenAI-API-Voice-Chatbot/blob/main/step1.jpg" width="480"/>
 
Step 2: To add a system-wide environment variable, click the "New…" button.    

<img src="https://github.com/techmakerai/Python-OpenAI-API-Voice-Chatbot/blob/main/step2.jpg" width="480"/>  

Step 3: Enter the variable name as shown and the API key as the value in the New User Variable prompt and click OK.

<img src="https://github.com/techmakerai/Python-OpenAI-API-Voice-Chatbot/blob/main/step3.jpg" width="480"/>  

Step 3: Click OK.

<img src="https://github.com/techmakerai/Python-OpenAI-API-Voice-Chatbot/blob/main/step4.jpg" width="480"/>  

Step 3: Click OK.

<img src="https://github.com/techmakerai/Python-OpenAI-API-Voice-Chatbot/blob/main/step5.jpg" width="480"/>  
