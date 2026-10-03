from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Salom, <b>{message.from_user.full_name}</b>!\n\n"
        "Men Render serverida test rejimida ishlayotgan namuna botman.\n"
        "Menga biror matn yuboring yoki /help buyrug'ini bosing!",
        parse_mode="HTML"
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "🛠 <b>Bot buyruqlari:</b>\n\n"
        "/start - Botni qayta ishga tushirish\n"
        "/help - Yordam oynasini ko'rsatish\n"
        "/info - Server haqida ma'lumot",
        parse_mode="HTML"
    )

@router.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer("🚀 Ushbu bot Python 3.11+ va aiogram 3.x kutubxonasida yaratilgan.")