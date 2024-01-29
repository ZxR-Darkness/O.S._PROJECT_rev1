try:
    import pygame
    import progress
except ImportError:
    # Если модуль не найден, выполняется данный код
    import subprocess
    subprocess.check_call(["pip", "install", "pygame"])  # Установка модуля через pip
    subprocess.check_call(["pip", "install", "progress"])  # Установка модуля через pip
    import pygame  # Попытка импорта модуля снова
    import progress  # Попытка импорта модуля снова