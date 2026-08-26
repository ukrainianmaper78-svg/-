[app]
# Название и имя пакета
title = Followed
package.name = followed
package.domain = org.test

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Версия приложения
version = 0.1

# Зависимости
requirements = python3,kivy

# Иконка (если есть)
icon.filename = %(source.dir)s/icon.png

# Ориентация экрана
orientation = portrait

# --- НАСТРОЙКИ ANDROID (от Android 7.0 до 16) ---
fullscreen = 0

# Поддержка от Android 7.0 (API 24)
android.minapi = 24

# Целевая версия (Target API level)
android.api = 35

# Версия инструментов сборки NDK / SDK
android.sdk_build_tools_version = 34.0.0
android.ndk_api = 24

# Разрешать лицензии автоматически
android.accept_sdk_licence = True

# Архитектуры процессоров (поддержка большинства смартфонов)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# Уровень логирования
log_level = 2
warn_on_root = 1
