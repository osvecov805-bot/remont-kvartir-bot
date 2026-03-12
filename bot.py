import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID', '7692089613')

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("❓ Консультация", callback_data="consult"), InlineKeyboardButton("💰 Стоимость", callback_data="price")],
        [InlineKeyboardButton("🔧 Услуги", callback_data="services"), InlineKeyboardButton("📞 Контакты", callback_data="contacts")],
        [InlineKeyboardButton("📝 Этапы работ", callback_data="stages"), InlineKeyboardButton("🌐 На сайт", url="https://remontotdelka159.ru")],
        [InlineKeyboardButton("💬 Telegram для связи", url="https://t.me/VKProtarget1")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("⬅ В меню", callback_data="menu")]])

def back_and_site_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅ В меню", callback_data="menu"), InlineKeyboardButton("🌐 На сайт", url="https://remontotdelka159.ru")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 Добро пожаловать!\n"
        "Я — официальный бот компании \xabРемонт квартир\xbb\n"
        "(ремонт и отделка квартир в Перми).\n\n"
        "Могу оформить заявку, рассказать про услуги, "
        "цены, этапы работ.\n\n"
        "Выберите действие из меню ниже 👇"
    )
    await update.message.reply_text(text, reply_markup=main_menu_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'menu':
        text = "Выберите действие из меню ниже 👇"
        await query.message.reply_text(text, reply_markup=main_menu_keyboard())

    elif data == 'consult':
        text = (
            "❓ <b>Консультация</b>\n\n"
            "Компания \xabРемонт квартир\xbb выполняет все виды "
            "ремонта квартир в Перми под ключ с гарантией 2 года.\n\n"
            "✅ Опыт более 12 лет\n"
            "✅ 500+ сданных объектов\n"
            "✅ Работа по договору\n"
            "✅ Поэтапная оплата без предоплаты\n\n"
            "Сайт: https://remontotdelka159.ru\n"
            "Тел: +7 (952) 330-99-44\n\n"
            "Напишите ваш вопрос:"
        )
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=back_and_site_keyboard())

    elif data == 'price':
        text = (
            "💰 <b>Стоимость услуг</b>\n\n"
            "🔨 Косметический ремонт — от 2 500 руб/м\xb2\n"
            "🏠 Капитальный ремонт — от 5 000 руб/м\xb2\n"
            "✍ Дизайн-проект — от 800 руб/м\xb2\n"
            "🏗 Ремонт в новостройке — от 4 000 руб/м\xb2\n"
            "🚿 Санузел под ключ — от 60 000 руб\n"
            "⚡ Электромонтаж — от 500 руб/точка\n\n"
            "Точную стоимость рассчитаем после бесплатного замера!\n"
            "Нажмите ниже для заявки."
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Оставить заявку", callback_data="order")],
            [InlineKeyboardButton("⬅ В меню", callback_data="menu"), InlineKeyboardButton("🌐 На сайт", url="https://remontotdelka159.ru")]
        ])
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=kb)

    elif data == 'services':
        text = (
            "🔧 <b>Наши услуги</b>\n\n"
            "🔨 <b>Косметический</b> — от 2 500 р/м\xb2\n"
            "🏠 <b>Капитальный</b> — от 5 000 р/м\xb2\n"
            "✍ <b>Дизайн-проект</b> — от 800 р/м\xb2\n"
            "🏗 <b>Новостройка</b> — от 4 000 р/м\xb2\n"
            "🚿 <b>Санузел</b> — от 60 000 р\n"
            "⚡ <b>Электрика</b> — от 500 р/точка"
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📝 Заявка", callback_data="order")],
            [InlineKeyboardButton("⬅ Меню", callback_data="menu")]
        ])
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=kb)

    elif data == 'contacts':
        text = (
            "📞 <b>Контакты</b>\n\n"
            "• Телефон: +7 (952) 330-99-44\n"
            "• Email: remont.perm.159@yandex.ru\n"
            "• Адрес: г. Пермь\n"
            "• Режим: Пн-Пт 9:00-20:00, Сб 10:00-18:00\n\n"
            "Сайт: https://remontotdelka159.ru"
        )
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📞 Позвонить", url="tel:+79523309944")],
            [InlineKeyboardButton("💬 Telegram", url="https://t.me/VKProtarget1"), InlineKeyboardButton("📬 VK", url="https://vk.ru/club236479775")],
            [InlineKeyboardButton("⬅ Меню", callback_data="menu")]
        ])
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=kb)

    elif data == 'stages':
        text = (
            "📝 <b>Этапы работ</b>\n\n"
            "1️⃣ <b>Разговор</b> — обсуждаем пожелания и бюджет\n"
            "2️⃣ <b>Замер</b> — бесплатный выезд мастера\n"
            "3️⃣ <b>Смета</b> — детальный расчет + договор\n"
            "4️⃣ <b>Работа</b> — ежедневные фотоотчеты\n"
            "5️⃣ <b>Приемка</b> — оплата по факту\n"
            "6️⃣ <b>Гарантия</b> — 2 года на все работы"
        )
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=back_and_site_keyboard())

    elif data == 'order':
        context.user_data['awaiting_order'] = True
        text = (
            "📝 <b>Оставить заявку</b>\n\n"
            "Напишите ваше имя, телефон и кратко\n"
            "опишите что нужно сделать.\n\n"
            "Пример:\n"
            "<i>Иван, +7 912 123-45-67, "
            "косметический ремонт 2-комн, 50 м\xb2</i>"
        )
        await query.message.reply_text(text, parse_mode='HTML', reply_markup=back_keyboard())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('awaiting_order'):
        context.user_data['awaiting_order'] = False
        user = update.effective_user
        msg = update.message.text
        admin_text = (
            f"🔔 <b>Новая заявка из бота!</b>\n\n"
            f"👤 {user.full_name}\n"
            f"🆔 @{user.username or 'no username'}\n"
            f"📝 {msg}"
        )
        try:
            await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_text, parse_mode='HTML')
        except Exception as e:
            logger.error(f'Error sending to admin: {e}')
        await update.message.reply_text(
            "✅ Заявка отправлена! Мы свяжемся с вами в ближайшее время.",
            reply_markup=main_menu_keyboard()
        )
    else:
        await update.message.reply_text(
            "Выберите действие из меню 👇",
            reply_markup=main_menu_keyboard()
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print('Bot started!')
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()


