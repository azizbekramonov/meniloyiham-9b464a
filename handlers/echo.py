from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message):
    # Foydalanuvchi yuborgan har qanday matnni qaytarib yuboradi (echo)
    await message.answer(f"Siz yozdingiz: <i>{message.text}</i>", parse_mode="HTML")