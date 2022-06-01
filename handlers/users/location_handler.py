from aiogram.types import Message, ReplyKeyboardRemove

from masjid_aniqlash.masofa_aniqlash import choose_shortes
from loader import dp

from keyboards.default.menuKeyboard import menu

@dp.message_handler(content_types='location')
async def get_contact(msg: Message):
    location = msg.location
    latitude = location.latitude
    longitude = location.longitude
    closest_masjid = choose_shortes(location)

    text ="\n\n".join([f"<a href='{url}'>'Masjidlar'</a>\n Uzoqlik: {distance:.1f} km"
                       for distance, url, masjid_location in closest_masjid])

    await msg.answer(f"Rahmat.\n"
                     f"Latitude = {latitude}\n"
                     f"Longitude ={longitude}\n\n"
                     f"{text}", disable_web_page_preview=True, reply_markup=menu)
    for distance, url, masjid_location in closest_masjid:
        await msg.answer_location(latitude=masjid_location["lat"],
                                  longitude=masjid_location["lon"])
