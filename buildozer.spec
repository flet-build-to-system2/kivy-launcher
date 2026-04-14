[app]

title = Kivy Launcher
package.name = launcher
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.exclude_dirs = tests,bin,art

version = 0.1

# 🔥 FIX: requirements
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# 🔥 Android config (FIXED)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

android.archs = armeabi-v7a,arm64-v8a

p4a.branch = master

# 🔥 Permissions minimal (stable)
[app:android.permissions]
INTERNET
READ_EXTERNAL_STORAGE
WRITE_EXTERNAL_STORAGE
