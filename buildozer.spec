[app]

# Название приложения на экране телефона
title = followed nonroot

# Имя пакета
package.name = followed
package.domain = org.app

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 1.0

# Зависимости
requirements = python3,kivy

# Иконка приложения (положи картинку icon.png в эту же папку)
icon.filename = %(source.dir)s/icon.png

# Настройки экрана
orientation = portrait
fullscreen = 1

# Разрешения и Android API
android.permissions = INTERNET
android.api = 33
android.minapi = 21

# Архитектуры для большинства Android устройств
android.archs = arm64-v8a, armeabi-v7a

# Поддержка AndroidX
android.enable_androidx = True

[buildozer]

# Уровень логов для отладки
log_level = 2
warn_on_root = 1