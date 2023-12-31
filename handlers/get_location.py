from aiogram import F, Router
from aiogram.types import Message

from servises import FOREST_LOCATION, MOUNTAIN_LOCATION, WATER_LOCATION, get_stiker

location_router = Router()


@location_router.message(F.text == "Лесная")
async def forest(message: Message) -> None:
    await message.answer_sticker(get_stiker(FOREST_LOCATION))


@location_router.message(F.text == "Горная")
async def mountain(message: Message) -> None:
    await message.answer_sticker(get_stiker(MOUNTAIN_LOCATION))


@location_router.message(F.text == "Водная")
async def watter(message: Message) -> None:
    await message.answer_sticker(get_stiker(WATER_LOCATION))
