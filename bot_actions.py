#!/usr/bin/env python
# -*- coding: utf-8 -*-
# made with python 3
# pylint: disable=C1001
"""Methods for the CommandHandler"""
import random
from os import listdir
from os.path import isfile, join
from telegram_tweet import TweetFromTelegram


class BotActions():
    """Makes actions with the bot"""
    @staticmethod
    def start(bot, update):
        """Initialize the bot"""
        update.message.reply_text('Hola, mundo!')

    @staticmethod
    def hola(bot, update):
        """Reply with a cordial salute"""
        update.message.reply_text('Hola, {}!'.format(update.message.from_user.first_name))

    @staticmethod
    def macho(bot, update):
        """Reply if you are altered"""
        chat_id = update.message.chat.id
        bot.send_audio(chat_id=chat_id, audio=open('macho.mp3', 'rb'))

    @staticmethod
    def send_memes(bot, update):
        """Reply with a random meme"""
        chat_id = update.message.chat.id
        file_name = BotActions.random_file_name('/Users/alec/Desktop/Memes')
        bot.send_photo(chat_id=chat_id, photo=open(file_name, 'rb'))

    @staticmethod
    def random_file_name(path):
        """Search a random file inside a path"""
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and f != '.DS_Store']
        lines = len(onlyfiles)
        random_file = int(round(random.random()*lines, 0))
        return path + "/" + onlyfiles[random_file]

    @staticmethod
    def ping(bot, update):
        """Reply with a pong."""
        bot.send_message(chat_id=update.message.chat.id, text="Pong!")

    @staticmethod
    def id(bot, update):
        chat_id = update.message.chat.id
        bot.send_message(chat_id=chat_id, text='`' + str(update.message.from_user.id) + '`', reply_to_message_id=update.message.message_id, parse_mode='Markdown')

    @staticmethod
    def id_chat(bot, update):
        chat_id = update.message.chat.id
        bot.send_message(chat_id=chat_id, text='`' + str(chat_id) + '`', reply_to_message_id=update.message.message_id, parse_mode='Markdown')

    @staticmethod
    def show_error(bot, update, error):
        raise error

    @staticmethod
    def help(bot, update):
        help_text = BotActions.help_commands()
        bot.send_message(chat_id=update.message.from_user.id, text=help_text)

    @staticmethod
    def animals(bot, update):
        """Reply with a random Shiba image"""
        chat_id = update.message.chat.id
        file_name = BotActions.random_file_name('/Users/alec/Desktop/Animals')
        bot.send_photo(chat_id=chat_id, photo=open(file_name, 'rb'))

    @staticmethod
    def help_commands():
        help_text = "/start     Inicializa el bot\n"
        help_text += "/ping     Comprueba si el bot está encendido\n"
        help_text += "/hola     Te saluda cordialmente\n"
        help_text += "/macho    Te manda un audio para que te vayas a la mierda\n"
        help_text += "/nudes    Te manda un meme aleatorio de un repertorio de memes\n"
        help_text += "/animals  Te manda un animal aleatorio de un repertorio de aniamlitos\n"
        help_text += "/id       Manda el ID del usuario que ha ejecutado el comando\n"
        help_text += "/id_c     Manda el ID del chat en el que se ha ejecutado el comando\n"
        return help_text

    @staticmethod
    def tweet(bot, update):
        if update.message.from_user.id == "":
            to_twitter = TweetFromTelegram()
            text_to_tweet = update.message.text_markdown[7:len(update.message.text_markdown)]
            link = to_twitter.new_tweet(text_to_tweet)
            if link == "error":
                bot.send_message(chat_id=update.message.chat.id, text="Intenta no poner carácteres especiales :)", reply_to_message_id=update.message.message_id)
            else:
                mensaje = "Ya he publicado tu tweet: " + link
                bot.send_message(chat_id=update.message.chat.id, text=mensaje, reply_to_message_id=update.message.message_id)
        else:
            bot.send_message(chat_id=update.message.chat.id, text="Creo que no se te permite enviar tweets... :s", reply_to_message_id=update.message.message_id)

    # añadir alguna manera de que si el mensaje de telegram contiene alguna imagen
    # que se descargue la imagen y se publique en twitter.
