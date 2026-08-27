[app]
# Название и пакет
title = Followed
package.name = followed
package.domain = org.test

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия
version = 0.1

# Требования
# Версии python3 и hostpython3 зафиксированы и совпадают явно: без этого
# p4a по умолчанию берёт для hostpython3 ещё нестабильный Python 3.14,
# чей встроенный pip ломается при создании служебного venv
# (ImportError в pip._internal). python3 и hostpython3 обязаны совпадать.
requirements = python3==3.11.9,hostpython3==3.11.9,kivy

# Экран
orientation = portrait
fullscreen = 0

# Версии Android (Поддержка от Android 7.0 до Android 16)
android.minapi = 24
android.api = 34
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b

# Авто-принятие лицензий
android.accept_sdk_licence = True

# Архитектуры
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
