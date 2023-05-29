# tyoma_tg_bot

# Создание конфигурации для запуска и перезапуска телеграм бота 
# -----------------

# Создайте systemd службу для бота
sudo nano /lib/systemd/system/tyoma_tg_bot.service


# С конфигурацией
[Unit]
Description=Tyoma_tg - Telegram Bot
After=syslog.target
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/tyoma_tg_bot/
ExecStart=/usr/bin/python3 /root/tyoma_tg_bot/main.py
RestartSec=60
Restart=always

[Install]
WantedBy=multi-user.target

# Нажмите CTRL+S и CTRL+X что бы сохранить и выйти

# Выполните эти две команды что бы запустить службу
sudo systemctl enable tyoma_tg_bot
sudo systemctl start tyoma_tg_bot

# Ваш бот будет всегда запускаться при старте системы, и перезапускается при возникновении ошибки. Для примера вы можете специально вызвать исключения в одной из функций обернутой обработчиком, и отследить ее в журнале командой:
# sudo journalctl -u tyoma_tg_bot.service