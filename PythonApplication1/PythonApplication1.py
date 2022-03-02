
from instabot import Bot
bot = Bot()
bot.login(username = "soulful_vampyr", password = "1coconut1")
print('Logged in!!!!')
bot.upload_photo('lone-samurai-sekiro-thumb.jpg', caption = 'Uploaded using python!')
bot.logout()
print('Logged out!!!')