import telebot

API_TOKEN = '8605879800:AAGnTz_vVdRTy6584AQDl8TtOSdvGvxKrg8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Jika website sedang loading, Anda bisa pesan manual di sini. 😊")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    text = message.text.upper()
    
    # Deteksi Pesanan dari Website
    if "PESANAN BARU WEBSITE" in text:
        bot.reply_to(message, "✅ *PESANAN DITERIMA!* \n\nAdmin kami sedang menuju lokasi Anda. Jika Anda memilih QRIS, silahkan scan kode QR yang dikirim admin sebentar lagi.", parse_mode="Markdown")
        print(f"Log: Pesanan masuk dari website!")
        
    elif "HALO" in text:
        bot.reply_to(message, "Halo! Ketik 'PESAN' untuk mulai atau gunakan website kami agar lebih cepat.")

print("Sistem Ayo Laundry Online...")
bot.polling(none_stop=True, skip_pending=True)