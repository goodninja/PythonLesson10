# Создать телеграм бота для cкачивания видео из YouTube по ссылке (и дальнейшая его отправка пользователю)

from pytube import YouTube 
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, ContextTypes, CommandHandler

yt = YouTube('ВСТАВЬТЕ ССЫЛКУ НА ВИДЕО С YouTube')
Youtube_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

updater = Updater(token = "ВСТАВЬТЕ СВОЙ ТОКЕН")

dispatcher = updater.dispatcher

def initial_stage(update:Update, context:ContextTypes):
    context.bot.send_message(chat_id = update.effective_chat.id,text = 'Чтобы открыть видео введите: PLAY')

def play_video(update:Update,context:ContextTypes):
    global Youtube_video
    msg = update.message.text.upper()
    if msg == 'PLAY':
        context.bot.send_video(chat_id = update.effective_chat.id,video = open(Youtube_video, 'rb'))
        context.bot.send_message(chat_id = update.effective_chat.id,text = 'Ваше видео')
    else:
        context.bot.send_message(chat_id = update.effective_chat.id,text = "Ошибка ввода, попробуйте снова")
    return

dispatcher.add_handler(CommandHandler("start", initial_stage))
dispatcher.add_handler(MessageHandler(Filters.text,play_video))

updater.start_polling()

updater.idle()