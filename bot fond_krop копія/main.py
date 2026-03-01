import os
import time
import telebot
from telebot import types

# ===================== CONFIG =====================
# ⚠️ Рекомендовано: зберігай токен в змінній середовища BOT_TOKEN
# TOKEN = os.getenv("BOT_TOKEN")
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def p(name: str) -> str:
    """Absolute path helper (file next to bot.py)."""
    return os.path.join(BASE_DIR, name)

# Адмін (куди приходять заявки/реєстрації)
ADMIN_ID = int(os.getenv("ADMIN_ID", "773277013"))

PROJECT_NAME = os.getenv("PROJECT_NAME", "fund.khorobrogo")

# --- Посилання (прямі перекази + соцмережі + звіти) ---
LINKS = {
    "mono_direct": "https://send.monobank.ua/jar/6jZ7BD5ZU3",
    "privat_direct": "https://next.privat24.ua/payments/form/%7B%22token%22%3A%22a05142a4-23dd-44be-9ec4-59640055e62a%22%7D",

    "instagram": "https://www.instagram.com/fund.khorobrogo/",
    "facebook": "https://www.facebook.com/fund.khorobrogo",
    "telegram": "https://t.me/fund_khorobrogo",
    "tiktok": "https://www.tiktok.com/@fund.khorobrogo",

    # ✅ Звіти (заміниш на свої посилання)
    "report_2024": "https://fundkhorobrogo.com.ua/zvit-2024",
    "report_2025": "https://fundkhorobrogo.com.ua/zvit-2025",
}

# --- Контакти ---
CONTACTS = {
    "phone": "+380 66 255 92 90",
    "email": "FUND.KHOROBROGO@GMAIL.COM",
    "address": "Простір хоробрих, вул. Віктора Чміленка, 53/35",
}

# --- FAQ тексти ---
FAQ = {
    "faq_money": (
        "💬 <b>Звідки фонд бере гроші?</b>\n\n"
        "<b>Фонд Полк Святослава Хороброго</b> заснований на пожертвах приватних осіб та компаній.\n\n"
        "Ми постійно працюємо над залученням нових джерел фінансування та не забираємо жодного відсотку з благодійних внесків на допомогу армії.\n\n"
        "Ми маємо можливість покривати заробітні плати команди та інші операційні потреби завдяки окремим партнерствам з компаніями, які роблять прямі внески "
        "на інтитуційну підтримку фонду та прямим благодійним внескам на рахунок операційної діяльності фонду."
    ),
    "faq_help": (
        "💬 <b>Як отримати допомогу?</b>\n\n"
        "Щоб отримати допомогу, необхідно надати контактні дані заявника, скан/фото запиту від командування підрозділу та прописати додаткові деталі "
        "про ваш запит/підрозділ на пошту fund.khorobrogo@gmail.com."
    ),
    "faq_partner": (
        "💬 <b>Як стати партнером фонду?</b>\n\n"
        "Для того, щоб стати партнером фонду, напишіть на електронну пошту fund.khorobrogo@gmail.com або зателефонуйте +380 66 255 92 90\n\n"
        "Ми з радістю розглянемо ваші пропозиції для допомоги в конкретному зборі, організації спільних акцій або підтримки організаційної діяльності фонду "
        "на постійній основі."
    ),
    "faq_zapit": (
        "💬 <b>Чи можна надати допомогу не фінансову?</b>\n\n"
        "Так. Ви можете закупити обладнання та передати фонду на подальший розподіл.\n\n"
        "Напишіть нам fund.khorobrogo@gmail.com або зателефонуйте 097 197 13 23"
    ),
}

# --- Донат: ВСЕ ТЕКСТ, окрім прямих переказів mono/privat (вони ЛІНКИ) ---
DONATE_TEXTS = {
    "info": (
        "💳 <b>Збір / Донат</b>\n\n"
        "Оберіть спосіб підтримки 👇"
    ),
    "uah": (
        "💳 <b>Донат UAH</b>\n\n"
        "<b>𝗨𝗔𝟳𝟭𝟯𝟬𝟱𝟮𝟵𝟵𝟬𝟬𝟬𝟬𝟬𝟮𝟲𝟬𝟬𝟲𝟬𝟬𝟱𝟭𝟬𝟱𝟬𝟵𝟯</b>\n"
        "AБО БЛАГОДІЙНИЙ ФОНД ПОЛК СВЯТОСЛАВА ХОРОБРОГО\n"
        "ЄДРПОУ 44698121\n"
        "Призначення платежу «Благодійна допомога»"
    ),
    "usd": (
        "💳 <b>Донат USD</b>\n\n"
        "<b>𝗨𝗔𝟱𝟬𝟯𝟬𝟱𝟮𝟵𝟵𝟬𝟬𝟬𝟬𝟬𝟮𝟲𝟬𝟬𝟱𝟬𝟰𝟱𝟭𝟬𝟯𝟮𝟲𝟭</b>\n"
        "𝗖𝗼𝗺𝗽𝗮𝗻𝘆 𝗻𝗮𝗺𝗲: CO SVIATOSLAVA KHOROBROHO REGIMENT\n"
        "𝗦𝗪𝗜𝗙𝗧 𝗰𝗼𝗱𝗲: <b>PBANUA2X</b>\n"
        "𝗡𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗯𝗮𝗻𝗸: JSC CB PRIVATBANK, 1D HRUSHEVSKOGO STR., KYIV, 01001, UKRAINE"
    ),
    "eur": (
        "💳 <b>Донат EUR</b>\n\n"
        "<b>𝗨𝗔𝟯𝟳𝟯𝟬𝟱𝟮𝟵𝟵𝟬𝟬𝟬𝟬𝟬𝟮𝟲𝟬𝟬𝟱𝟬𝟮𝟱𝟭𝟬𝟲𝟮𝟲𝟲</b>\n"
        "𝗖𝗼𝗺𝗽𝗮𝗻𝘆 𝗻𝗮𝗺𝗲: CO SVIATOSLAVA KHOROBROHO REGIMENT\n"
        "𝗦𝗪𝗜𝗙𝗧 𝗰𝗼𝗱𝗲: <b>PBANUA2X</b>\n"
        "𝗡𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗯𝗮𝗻𝗸: JSC CB PRIVATBANK, 1D HRUSHEVSKOGO STR., KYIV, 01001, UKRAINE"
    ),
    "pln": (
        "💳 <b>Донат PLN</b>\n\n"
        "<b>𝗨𝗔𝟰𝟴𝟯𝟬𝟱𝟮𝟵𝟵𝟬𝟬𝟬𝟬𝟬𝟮𝟲𝟬𝟬𝟯𝟬𝟮𝟱𝟭𝟬𝟰𝟬𝟵𝟵</b>\n"
        "𝗖𝗼𝗺𝗽𝗮𝗻𝘆 𝗻𝗮𝗺𝗲: CO SVIATOSLAVA KHOROBROHO REGIMENT\n"
        "𝗦𝗪𝗜𝗙𝗧 𝗰𝗼𝗱𝗲: <b>PBANUA2X</b>\n"
        "𝗡𝗮𝗺𝗲 𝗼𝗳 𝘁𝗵𝗲 𝗯𝗮𝗻𝗸: JSC CB PRIVATBANK, 1D HRUSHEVSKOGO STR., KYIV, 01001, UKRAINE"
    ),
    "paypal": (
        "💳 <b>PayPal</b>\n\n"
        "<b>𝗳𝘂𝗻𝗱.𝟰𝟱𝟬@𝗴𝗺𝗮𝗶𝗹.𝗰𝗼𝗺</b>"
    ),
    "support": (
        "🤝 <b>Підтримати діяльність фонду</b>\n\n"
        "<b>𝗨𝗔473052990000026009005111534</b>\n"
        "БО БЛАГОДІЙНИЙ ФОНД ПОЛК СВЯТОСЛАВА ХОРОБРОГО\n"
        "ЄДРПОУ 44698121\n"
        "Призначення платежу «Благодійна допомога»"
    ),
}

# ===================== BOT INIT =====================
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ===================== SIMPLE STATE =====================
STATE = {}  # chat_id -> dict

def set_state(chat_id: int, mode: str, data=None):
    STATE[chat_id] = {"mode": mode, "data": data or {}, "ts": int(time.time())}

def get_state(chat_id: int):
    return STATE.get(chat_id, {}).get("mode")

def get_data(chat_id: int):
    return STATE.get(chat_id, {}).get("data", {})

def clear_state(chat_id: int):
    STATE.pop(chat_id, None)

def safe_username(user) -> str:
    return f"@{user.username}" if user.username else "без_юзернейму"

def send_admin(text: str):
    if ADMIN_ID and ADMIN_ID != 0:
        try:
            bot.send_message(ADMIN_ID, text)
        except Exception:
            pass

# ===================== KEYBOARDS =====================
def kb_main():
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("💳 Збір / Донат", callback_data="donate"),
        types.InlineKeyboardButton("🆘 Звернутися по допомогу", callback_data="help_form"),
    )
    kb.add(
        types.InlineKeyboardButton("📱 Наші соцмережі", callback_data="social"),
        types.InlineKeyboardButton("📞 Контакти", callback_data="contacts"),
    )
    kb.add(
        types.InlineKeyboardButton("❓ Часті питання", callback_data="faq"),
        types.InlineKeyboardButton("📝 Реєстрація", callback_data="register"),
    )
    return kb

def kb_back_home():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("⬅️ Назад в меню", callback_data="home"))
    return kb

def kb_social():
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("Instagram", url=LINKS["instagram"]),
        types.InlineKeyboardButton("Facebook", url=LINKS["facebook"]),
    )
    kb.add(
        types.InlineKeyboardButton("Telegram", url=LINKS["telegram"]),
        types.InlineKeyboardButton("TikTok", url=LINKS["tiktok"]),
    )
    kb.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="home"))
    return kb

def kb_donate_main():
    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.add(
        types.InlineKeyboardButton("UAH", callback_data="don:UAH"),
        types.InlineKeyboardButton("USD", callback_data="don:USD"),
    )
    kb.add(
        types.InlineKeyboardButton("EUR", callback_data="don:EUR"),
        types.InlineKeyboardButton("PLN", callback_data="don:PLN"),
    )
    kb.add(
        types.InlineKeyboardButton("PayPal", callback_data="don:PAYPAL"),
        types.InlineKeyboardButton("Підтримати діяльність фонду", callback_data="don:SUPPORT"),
    )

    kb.add(
        types.InlineKeyboardButton("Прямий переказ mono 🔗", url=LINKS["mono_direct"]),
        types.InlineKeyboardButton("Прямий переказ Privat 🔗", url=LINKS["privat_direct"]),
    )

    kb.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="home"))
    return kb

def kb_faq():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("Звідки фонд бере гроші?", callback_data="faq:money"),
        types.InlineKeyboardButton("Як отримати допомогу?", callback_data="faq:help"),
        types.InlineKeyboardButton("Як стати партнером фонду?", callback_data="faq:partner"),
        types.InlineKeyboardButton("Чи можна надати допомогу не фінансову?", callback_data="faq:zapit"),
        types.InlineKeyboardButton("📊 Звіти", callback_data="faq:reports"),  # ✅ НОВА КНОПКА
    )
    kb.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="home"))
    return kb

def kb_reports():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton("Звіт 2024", url=LINKS["report_2024"]),
        types.InlineKeyboardButton("Звіт 2025", url=LINKS["report_2025"]),
    )
    kb.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="faq"))
    return kb

# ===================== START / MENU =====================
@bot.message_handler(commands=["start", "menu"])
def cmd_start(message):
    clear_state(message.chat.id)
    bot.send_message(
        message.chat.id,
        f"👋 Вітаю! Це бот проєкту <b>{PROJECT_NAME}</b>.\n\nОбери розділ 👇",
        reply_markup=kb_main()
    )

@bot.message_handler(commands=["help"])
def cmd_help(message):
    bot.send_message(
        message.chat.id,
        "Команди:\n"
        "/start — відкрити меню\n"
        "/menu — відкрити меню\n",
        reply_markup=kb_main()
    )

# ===================== CALLBACKS =====================
@bot.callback_query_handler(func=lambda c: True)
def on_cb(call):
    chat_id = call.message.chat.id
    data = call.data

    # HOME
    if data == "home":
        clear_state(chat_id)
        bot.edit_message_text(
            f"🏠 Меню <b>{PROJECT_NAME}</b> 👇",
            chat_id, call.message.message_id,
            reply_markup=kb_main()
        )
        return

    # DONATE
    if data == "donate":
        clear_state(chat_id)
        bot.edit_message_text(
            DONATE_TEXTS["info"],
            chat_id, call.message.message_id,
            reply_markup=kb_donate_main()
        )
        return

    if data.startswith("don:"):
        cur = data.split(":", 1)[1]
        if cur == "UAH":
            txt = DONATE_TEXTS["uah"]
        elif cur == "USD":
            txt = DONATE_TEXTS["usd"]
        elif cur == "EUR":
            txt = DONATE_TEXTS["eur"]
        elif cur == "PLN":
            txt = DONATE_TEXTS["pln"]
        elif cur == "PAYPAL":
            txt = DONATE_TEXTS["paypal"]
        elif cur == "SUPPORT":
            txt = DONATE_TEXTS["support"]
        else:
            txt = "💳 Донат\n\nТут буде твій текст."

        bot.edit_message_text(txt, chat_id, call.message.message_id, reply_markup=kb_back_home())
        return

    # SOCIAL
    if data == "social":
        clear_state(chat_id)
        bot.edit_message_text(
            "📱 <b>Наші соцмережі</b>\n\nПереходь за посиланнями 👇",
            chat_id, call.message.message_id,
            reply_markup=kb_social()
        )
        return

    # CONTACTS
    if data == "contacts":
        clear_state(chat_id)
        text = (
            "📞 <b>Контакти</b>\n\n"
            f"📱 Телефон: <b>{CONTACTS['phone']}</b>\n"
            f"✉️ Email: <b>{CONTACTS['email']}</b>\n"
            f"📍 Адреса: <b>{CONTACTS['address']}</b>\n\n"
            "Якщо хочеш — напиши нам прямо тут."
        )
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("📝 Написати нам", callback_data="msg_form"))
        kb.add(types.InlineKeyboardButton("⬅️ Назад", callback_data="home"))
        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=kb)
        return

    # FAQ
    if data == "faq":
        clear_state(chat_id)
        bot.edit_message_text(
            "❓ <b>Часті питання</b>\n\nОберіть питання 👇",
            chat_id, call.message.message_id,
            reply_markup=kb_faq()
        )
        return

    # ✅ Звіти (підменю)
    if data == "faq:reports":
        bot.edit_message_text(
            "📊 <b>Звіти</b>\n\nОберіть звіт 👇",
            chat_id, call.message.message_id,
            reply_markup=kb_reports()
        )
        return

    if data.startswith("faq:"):
        key = data.split(":", 1)[1]
        if key == "money":
            text = FAQ["faq_money"]
        elif key == "help":
            text = FAQ["faq_help"]
        elif key == "partner":
            text = FAQ["faq_partner"]
        elif key == "zapit":
            text = FAQ["faq_zapit"]
        else:
            text = "❓ Невідоме питання."

        bot.edit_message_text(text, chat_id, call.message.message_id, reply_markup=kb_back_home())
        return

    # REGISTRATION
    if data == "register":
        set_state(chat_id, "reg_pib", {})
        bot.edit_message_text(
            "📝 <b>Реєстрація</b>\n\n"
            "1/3 Введіть ваше <b>ПІБ</b>:",
            chat_id, call.message.message_id,
            reply_markup=kb_back_home()
        )
        return

    # MESSAGE TO ADMIN
    if data == "msg_form":
        set_state(chat_id, "message_text", {})
        bot.edit_message_text(
            "📝 <b>Написати нам</b>\n\n"
            "Напишіть повідомлення одним текстом.\n"
            "Після відправки воно піде адміну ✅",
            chat_id, call.message.message_id,
            reply_markup=kb_back_home()
        )
        return

    # HELP FORM
    if data == "help_form":
        set_state(chat_id, "help_name", {})
        bot.edit_message_text(
            "🆘 <b>Звернутися по допомогу</b>\n\n"
            "1/4 Вкажіть, будь ласка, <b>Ім’я</b>:",
            chat_id, call.message.message_id,
            reply_markup=kb_back_home()
        )
        return

# ===================== TEXT HANDLER (форми) =====================
@bot.message_handler(content_types=["text"])
def on_text(message):
    chat_id = message.chat.id
    mode = get_state(chat_id)
    text = message.text.strip()

    if not mode:
        bot.send_message(chat_id, "Відкрий меню: /start", reply_markup=kb_main())
        return

    # --- форма "написати нам" ---
    if mode == "message_text":
        clear_state(chat_id)
        bot.send_message(chat_id, "✅ Дякую! Повідомлення відправлено.", reply_markup=kb_main())

        admin_text = (
            "📩 <b>Нове повідомлення</b>\n"
            f"👤 @{message.from_user.username if message.from_user.username else 'без_юзернейму'} | "
            f"ID: <code>{message.from_user.id}</code>\n"
            f"🗨️ {text}"
        )
        send_admin(admin_text)
        return

    data = get_data(chat_id)

    # --- РЕЄСТРАЦІЯ (3 кроки) ---
    if mode == "reg_pib":
        data["pib"] = text
        set_state(chat_id, "reg_phone", data)
        bot.send_message(chat_id, "2/3 Введіть <b>номер телефону</b>:", reply_markup=kb_back_home())
        return

    if mode == "reg_phone":
        data["phone"] = text
        set_state(chat_id, "reg_event", data)
        bot.send_message(chat_id, "3/3 Введіть <b>назву заходу</b>:", reply_markup=kb_back_home())
        return

    if mode == "reg_event":
        data["event"] = text
        clear_state(chat_id)

        bot.send_message(
            chat_id,
            "✅ <b>Реєстрацію прийнято!</b>\n\nДякуємо за участь.",
            reply_markup=kb_main()
        )

        admin_text = (
            "📝 <b>Нова реєстрація</b>\n\n"
            f"👤 ПІБ: <b>{data.get('pib','-')}</b>\n"
            f"📱 Телефон: <b>{data.get('phone','-')}</b>\n"
            f"🎯 Захід: <b>{data.get('event','-')}</b>\n\n"
            f"ID користувача: <code>{message.from_user.id}</code>"
        )
        send_admin(admin_text)
        return

    # --- форма "звернутися по допомогу" (4 кроки) ---
    if mode == "help_name":
        data["name"] = text
        set_state(chat_id, "help_phone", data)
        bot.send_message(chat_id, "2/4 Вкажіть <b>номер телефону</b>:", reply_markup=kb_back_home())
        return

    if mode == "help_phone":
        data["phone"] = text
        set_state(chat_id, "help_email", data)
        bot.send_message(chat_id, "3/4 Вкажіть <b>Email</b>:", reply_markup=kb_back_home())
        return

    if mode == "help_email":
        data["email"] = text
        set_state(chat_id, "help_problem", data)
        bot.send_message(chat_id, "4/4 Опишіть <b>суть звернення</b>:", reply_markup=kb_back_home())
        return

    if mode == "help_problem":
        data["problem"] = text
        clear_state(chat_id)

        bot.send_message(
            chat_id,
            "✅ Дякую! Заявку прийнято.\nМи зв’яжемось з вами найближчим часом.",
            reply_markup=kb_main()
        )

        admin_text = (
            "🆘 <b>Нова заявка на допомогу</b>\n"
            f"👤 @{message.from_user.username if message.from_user.username else 'без_юзернейму'} | "
            f"ID: <code>{message.from_user.id}</code>\n\n"
            f"👤 Ім’я: <b>{data.get('name','-')}</b>\n"
            f"📱 Телефон: <b>{data.get('phone','-')}</b>\n"
            f"✉️ Email: <b>{data.get('email','-')}</b>\n\n"
            f"🗨️ Опис: {data.get('problem','-')}"
        )
        send_admin(admin_text)
        return

    # fallback
    clear_state(chat_id)
    bot.send_message(chat_id, "Відкрий меню: /start", reply_markup=kb_main())

# ===================== RUN =====================
if __name__ == "__main__":
    print("✅ Bot is running...")
    bot.infinity_polling(timeout=60, long_polling_timeout=60)
