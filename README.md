# Crypto Fear & Greed Telegram Alert

Bot mengambil Crypto Fear & Greed Index dari Alternative.me dan mengirim ringkasan ke Telegram setiap hari sekitar pukul 08.00 WIB.

## Setup singkat

1. Buat repository GitHub baru, misalnya `crypto-telegram-alert`.
2. Upload `main.py` ke folder utama repository.
3. Upload file workflow ke `.github/workflows/daily-alert.yml`.
4. Buka **Settings → Secrets and variables → Actions → New repository secret**.
5. Tambahkan dua secret berikut:
   - `TELEGRAM_BOT_TOKEN` = token dari BotFather (jangan pernah masukkan ke kode atau chat publik).
   - `TELEGRAM_CHAT_ID` = `328816344`.
6. Buka tab **Actions**, pilih workflow **Daily Crypto Fear and Greed Telegram Alert**, lalu tekan **Run workflow** untuk tes pertama.
7. Jika berhasil, laporan berikutnya dijadwalkan setiap hari sekitar pukul 08.00 WIB.

Catatan:
- GitHub Actions memakai UTC; `01:00 UTC` sama dengan `08:00 WIB`.
- Jadwal GitHub Actions dapat terlambat beberapa menit saat antrean sibuk.
- Jika workflow tidak terlihat, pastikan file berada tepat di `.github/workflows/daily-alert.yml` pada branch default.
