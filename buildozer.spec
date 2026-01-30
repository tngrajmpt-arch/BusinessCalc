[app]
title = Business Calc
package.name = businesscalc
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
p4a.branch = master
android.entrypoint = org.kivy.android.PythonActivity
