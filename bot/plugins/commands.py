#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@MG_MEDIA"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("??五 Sorry Dude, You are B A N N E D ??不??不??不")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>Join Our Movie Channel ??五   鉥?鉥擒捶鉥耜曾鉞? 鉥兒曾鉥?鉞?鉥?鉞? 鉥?鉥?鉞?鉥?鉞? 鉥?鉥?鉞?鉥?鉥賴善 鉥桌晷鉥戈??鉥啤揹鉞? 鉥? 鉥眇??鉥?鉞?鉥?鉞? 鉥菽斐鉥? 鉥兒曾鉥?鉞?鉥?鉞擒??鉞?鉥?鉞? 鉥詮曾鉥兒曾鉥? 鉥?鉥賴??鉞?鉥?鉞?鉥?鉥能??鉥喪斑鉞?.鉥?鉥戈??鉥?鉞?鉥?鉞?鉥?鉞? 鉥?鉥擒捶鉞?鉥耜曾鉞? 鉥?鉞?鉥能曾鉞? 鉥?鉥菽??鉥?...????????</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ???衷OIN OUR CHANNEL???? ", url=f"https://t.me/MG_MEDIA")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '???儭?JOIN CHANNEL???儭?', url="https://t.me/joinchat/nppwyzxMr8NhN2M9"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '???儭?JOIN CHANNEL???儭?', url="https://t.me/joinchat/nppwyzxMr8NhN2M9"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '???儭?JOIN CHANNEL???儭?', url="https://t.me/joinchat/nppwyzxMr8NhN2M9"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('???ｚHANNEL', url='https://t.me/joinchat/nppwyzxMr8NhN2M9'),
        InlineKeyboardButton('GROUP????', url ='http://t.me/MGmoviegram')
    ],[
        InlineKeyboardButton('OWNER???', url='https://t.me/Wafikh')
    ],[
        InlineKeyboardButton('Help ???', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ???', callback_data='start'),
        InlineKeyboardButton('About ????', callback_data='about')
    ],[
        InlineKeyboardButton('Close ????', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ???', callback_data='start'),
        InlineKeyboardButton('Close ????', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
