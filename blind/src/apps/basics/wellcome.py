# Importando los modulos
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message

# Controlando el mensaje con las siguientes características
@Client.on_message(filters.command(["start", "iniciar", "inicio", "play", "empezar"], prefixes=["!", "/", ".", "\\" ]) & filters.text)
async def start(client:Client, message:message.Message, **kwargs):
    await message.reply_text("""
        Hola! Soy ReLU, un bot de Telegram creado por @TechAtlasDev.
    """
    )