# Lime_auto_test_python
данный репозитори хранит код UI автотестов на python/selenium на фреймворке систематизации тестов pytest

при запуске тестов принимаются параметры:
1) указатель на каком браузере запустить автотесты, на текущий момент проект поддерживает два браузера google chrome и firefox. Если не указывать значение применяется дефолтное 'chrome'
--browser_name=chrome 
--browser_name=firefox
2) указатель на каком языке открыть браузер, для проверки адаптивности переводов страниц. Если не указывать значение применяется дефолтное 'ru'
--language=ru
--language=en
и т.д.
3) указатель на каком сервере запускать тесты. Если не указывать значение применяется дефолтное 'dev'
--server=dev
--server=stage
--server=prod