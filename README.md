# tyoma_tg_bot

# Создание конфигурации для запуска и перезапуска телеграм бота 
# -----------------

# Создайте systemd службу для бота
vi tyoma_tg_bot.service


# С конфигурацией
[Unit]
Description=Telegram bot 'Town Wars'
After=syslog.target
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/usr/local/bin/bot
ExecStart=/usr/bin/python3 /usr/local/bin/bot/bot.py
RestartSec=10
Restart=always
 
[Install]
WantedBy=multi-user.target

# Нажмите CTRL+S и CTRL+X что бы сохранить и выйти

# Выполните эти две команды что бы запустить службу
systemctl enable tyoma_tg_bot.service
systemctl start tyoma_tg_bot.service

# Ваш бот будет всегда запускаться при старте системы, и перезапускается при возникновении ошибки. Для примера вы можете специально вызвать исключения в одной из функций обернутой обработчиком, и отследить ее в журнале командой:
# sudo journalctl -u tyoma_tg_bot.service