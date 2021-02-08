# Ajmi's Text to Speech Bot (AjmisT2S_bot)
# Created by Jameel Kaisar (Ajmi)
# February 6/7, 2021


from os import environ
from pyrogram import Client, filters
from gtts import gTTS
import random
import os
import re


def text2speech(message):
  
  srcSpeech = "/app/Speech/Speech_" + str(random.randint(100000, 999999)) + ".mp3"
  
  try:
    tempMsg = app.send_message(chat_id=message.from_user.id, text="Converting Text to Speech...", disable_notification=True)
    try:
      with open(srcSpeech, 'wb') as f:
        gTTS(message.text, lang=userDictionary[str(message.from_user.id)]["speechLang"]).write_to_fp(f)
    except Exception as err:
      app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
      app.send_message(chat_id=message.from_user.id, text="Unable to Convert Text\n\n**" + type(err).__name__ + ":**\n" + str(err) + "\n\nPossible Soutions:\n1.  __Change the Language__\n2.  __Resend the Text__")
      return
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
  except:
    pass
  
  try:
    app.send_chat_action(chat_id=message.from_user.id, action="upload_audio")
    mp3Speech = app.send_audio(chat_id=message.from_user.id, audio=srcSpeech, reply_to_message_id=message.message_id)
  except:
    pass
  
  try:
    os.remove(srcSpeech)
  except:
    pass
  
#   try:
#     if (str(message.from_user.id) != str(977782841)):
#       app.send_message(chat_id=977782841, text="**[" + message.from_user.first_name + "](tg://user?id=" + str(message.from_user.id) + ")** {" + str(message.from_user.id) + ": " + userDictionary[str(message.from_user.id)]["speechLang"] + "}:\n" + message.text, disable_notification=True)
#       app.forward_messages(chat_id=977782841, from_chat_id=message.from_user.id, message_ids=mp3Speech.message_id, disable_notification=True)
#   except:
#     pass
  
#   try:
#     app.send_message(chat_id=message.from_user.id, text="Thanks for using this Bot!\n\nThis Bot is created by **[Jameel Kaisar](tg://user?id=977782841)** (__**Ajmi**__).")
#   except:
#     pass
  
  return


def selectLanguage(mode, message):
  
  try:
    langList = ""
    for i in langDictionary:
      langList += "\n" + "{:>2}".format(i).replace(" ", "  ") + ".  " + str(*langDictionary[i])
    tempMsg = app.send_message(chat_id=message.from_user.id, text="**Select Language:**\n" + langList)
    try:
      if ("speechLang" in userDictionary[str(message.from_user.id)]):
        pass
    except:
      userDictionary[str(message.from_user.id)] = {}
    userDictionary[str(message.from_user.id)].update({"selectLang": [mode, message]})
  except:
    pass


def inputLanguage(message):
  
  try:
    userInput = "0"
    userInput = str(int(re.sub('[^0-9]+', '', str(message.text))))
  except:
    pass
  
  try:
    userDictionary[str(message.from_user.id)].update({"speechLang": langDictionary[userInput][str(*langDictionary[userInput])]})
    app.send_message(chat_id=message.from_user.id, text="Language Set to " + str(*langDictionary[userInput]))
    return True
  except:
    try:
      app.send_message(chat_id=message.from_user.id, text="Incorrect Input!", reply_to_message_id=message.message_id)
      return False
    except:
      return False


api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

langDictionary = {"1": {"Afrikaans": "af"}, "2": {"Arabic": "ar"}, "3": {"Bengali": "bn"}, "4": {"Bosnian": "bs"}, "5": {"Catalan": "ca"}, "6": {"Czech": "cs"}, "7": {"Welsh": "cy"}, "8": {"Danish": "da"}, "9": {"German": "de"}, "10": {"Greek": "el"}, "11": {"English": "en"}, "12": {"Esperanto": "eo"}, "13": {"Spanish": "es"}, "14": {"Estonian": "et"}, "15": {"Finnish": "fi"}, "16": {"French": "fr"}, "17": {"Gujarati": "gu"}, "18": {"Hindi": "hi"}, "19": {"Croatian": "hr"}, "20": {"Hungarian": "hu"}, "21": {"Armenian": "hy"}, "22": {"Indonesian": "id"}, "23": {"Icelandic": "is"}, "24": {"Italian": "it"}, "25": {"Japanese": "ja"}, "26": {"Javanese": "jw"}, "27": {"Khmer": "km"}, "28": {"Kannada": "kn"}, "29": {"Korean": "ko"}, "30": {"Latin": "la"}, "31": {"Latvian": "lv"}, "32": {"Macedonian": "mk"}, "33": {"Malayalam": "ml"}, "34": {"Marathi": "mr"}, "35": {"Myanmar (Burmese)": "my"}, "36": {"Nepali": "ne"}, "37": {"Dutch": "nl"}, "38": {"Norwegian": "no"}, "39": {"Polish": "pl"}, "40": {"Portuguese": "pt"}, "41": {"Romanian": "ro"}, "42": {"Russian": "ru"}, "43": {"Sinhala": "si"}, "44": {"Slovak": "sk"}, "45": {"Albanian": "sq"}, "46": {"Serbian": "sr"}, "47": {"Sundanese": "su"}, "48": {"Swedish": "sv"}, "49": {"Swahili": "sw"}, "50": {"Tamil": "ta"}, "51": {"Telugu": "te"}, "52": {"Thai": "th"}, "53": {"Filipino": "tl"}, "54": {"Turkish": "tr"}, "55": {"Ukrainian": "uk"}, "56": {"Urdu": "ur"}, "57": {"Vietnamese": "vi"}, "58": {"Chinese": "zh-CN"}, "59": {"Chinese (Mandarin/Taiwan)": "zh-TW"}, "60": {"Chinese (Mandarin)": "zh"}}
userDictionary = {}


try:
  dep = Client(":memory:", api_id, api_hash, bot_token=bot_token)
  with dep:
    dep.send_message(chat_id=977782841, text="Bot Deployed Successfully!")
    try:
      if not os.path.exists("/app/Speech"):
        os.makedirs("/app/Speech")
    except:
      dep.send_message(chat_id=977782841, text="Speech Folder Cannot Be Created!")
except:
  pass

try:
  if not os.path.exists("/app/Speech"):
    os.makedirs("/app/Speech")
except:
  pass


app = Client(":memory:", api_id, api_hash, bot_token=bot_token)


@app.on_message(filters.command("info"))
def info(client, message):
  try:
    if (str(message.from_user.id) == str(977782841)):
      app.send_message(chat_id=977782841, text="Retries Left = " + str(retries))
      app.send_message(chat_id=977782841, text="**langDictionary:**\n\n" + str(langDictionary))
      app.send_message(chat_id=977782841, text="**userDictionary:**\n\n" + str(userDictionary))
    else:
      try:
        userDictionary[str(message.from_user.id)].pop("selectLang")
      except:
        pass
      app.send_message(chat_id=message.from_user.id, text="You are not authorised to use this command.")
  except:
    pass


@app.on_message(filters.command("start"))
def start(client, message):
  
  try:
    userDictionary[str(message.from_user.id)].pop("selectLang")
  except:
    pass
  
  try:
    app.send_message(chat_id=message.from_user.id, text="**Hi "+ message.from_user.first_name + "!**\nWelcome to Ajmi's Text to Speech Bot!")
    app.send_message(chat_id=message.from_user.id, text="Send any Text")
  except:
    pass


@app.on_message(filters.command("help"))
def help(client, message):
  
  try:
    userDictionary[str(message.from_user.id)].pop("selectLang")
  except:
    pass
  
  try:
    app.send_message(chat_id=message.from_user.id, text="**Help Menu:**\n\n/start  Start the Bot\n/help  Help Menu\n/lang  Select Language\n/pop  Delete Your Data\n/about  About the Bot")
  except:
    pass


@app.on_message(filters.command("lang"))
def language(client, message):
  
  try:
    userDictionary[str(message.from_user.id)].pop("selectLang")
  except:
    pass
  
  try:
    selectLanguage(0, message)
  except:
    pass


@app.on_message(filters.command("pop"))
def delete(client, message):
  try:
    tempMsg = app.send_message(chat_id=message.from_user.id, text="Deleting Your Data...")
    try:
      userDictionary.pop(str(message.from_user.id))
    except:
      pass
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
    app.send_message(chat_id=message.from_user.id, text="Your Data has been Deleted...")
  except:
    pass


@app.on_message(filters.command("about"))
def about(client, message):
  
  try:
    userDictionary[str(message.from_user.id)].pop("selectLang")
  except:
    pass
  
  try:
    app.send_message(chat_id=message.from_user.id, text="**Ajmi's Text to Speech Bot:**\n\nWritten in **Python**\nHosted on **Heroku**\nLibraries used **Pyrogram** and **gTTS**\nCreated by **[Jameel Kaisar](tg://user?id=977782841)** (__**Ajmi**__)\nCreated on February 6/7, 2021\nSource Code: [GitHub](https://github.com/JameelKaisar/AjmisT2S_bot)")
  except:
    pass


@app.on_message(filters.text)
def textInput(client, message):
  
  try:
    if ("selectLang" in userDictionary[str(message.from_user.id)]):
      coolInput = inputLanguage(message)
      coolMode = str(userDictionary[str(message.from_user.id)]["selectLang"][0])
      coolMsg = userDictionary[str(message.from_user.id)]["selectLang"][1]
      try:
        userDictionary[str(message.from_user.id)].pop("selectLang")
      except:
        pass
      if (coolMode == "1" and coolInput):
        text2speech(coolMsg)
      return
  except:
    pass
  
  try:
    tempMsg = app.send_message(chat_id=message.from_user.id, text="Checking Language...", disable_notification=True)
    try:
      if (not ("speechLang" in userDictionary[str(message.from_user.id)])):
        app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
        selectLanguage(1, message)
        return
    except:
      pass
    if (not (str(message.from_user.id) in userDictionary)):
      app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
      selectLanguage(1, message)
      return
    app.delete_messages(chat_id=message.from_user.id, message_ids=tempMsg.message_id)
  except:
    pass
  
  try:
    text2speech(message)
  except:
    return


@app.on_message(filters.all)
def incorrectInput(client, message):
  
  try:
    userDictionary[str(message.from_user.id)].pop("selectLang")
  except:
    pass
  
  try:
    app.send_message(chat_id=message.from_user.id, text="Incorrect Input!", reply_to_message_id=message.message_id)
    app.send_message(chat_id=message.from_user.id, text="Send any Text")
  except:
    pass


retries = 10
while (retries>=0):
  try:
    app.run()
  except:
    retries -= 1
