from pyrogram import Client, filters
from pyrogram.types import Message
from .lib.handler import HandlerResponseJSON
from .lib.objects import CHAT
from google.generativeai.types.generation_types import GenerateContentResponse
from pyrogram import enums

from blind.src.utils.utilities import clearComand
from blind.src.utils.buttons import keymakers

# El controlador del comando
@Client.on_message((filters.command("relu") & filters.text) | (filters.private & filters.text))
async def CUVO(client: Client, message: Message):
    text_user = clearComand(message.text)

    # Si el texto adicional está vacío
    if not text_user or text_user == "":
        botones = keymakers(["🧹 Limpiar memoria"], ["cuvoAction-clear"])
        return await message.reply("ReLU es un asistente desarrollado con el objetivo de ofrecer asistencia a estudiantes y programadores en general.", reply_markup=botones)

    await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)

    # Enviado el mensaje a la IA
    AICUVO = CHAT(message, client)
    RESPONSE:GenerateContentResponse = await AICUVO.talk(text_user)

    if not RESPONSE:
        await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
        return "_"

    # Procesando la respuesta
    HANDLER = HandlerResponseJSON(RESPONSE, message, client)
    await HANDLER.execute()

    client.set_parse_mode(enums.ParseMode.MARKDOWN)
    await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)