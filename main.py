import flet as ft
import time
import threading
import os


def main(page: ft.Page):
    page.title = "Системное обновление"
    page.window.full_screen = True
    page.padding = 0
    page.bgcolor = ft.Colors.BLACK

    # Виджеты для экрана обновления
    status = ft.Text(
        "Установка критического обновления безопасности...",
        color=ft.Colors.WHITE,
        size=18,
        text_align=ft.TextAlign.CENTER,
    )

    progress = ft.ProgressBar(
        width=300,
        color=ft.Colors.GREEN,
        bgcolor=ft.Colors.GREY_800,
        value=0
    )

    percent = ft.Text("0%", color=ft.Colors.WHITE, size=20)

    warning = ft.Text(
        "ВНИМАНИЕ!\nНе выключайте и не отключайте от питания.\n"
        "Прерывание приведёт к УДАЛЕНИЮ СИСТЕМЫ.",
        color=ft.Colors.RED,
        size=16,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD
    )

    # Собираем всё на экране
    page.add(
        ft.Column(
            [
                ft.Container(height=100),
                status,
                ft.Container(height=20),
                ft.Row([progress], alignment=ft.MainAxisAlignment.CENTER),
                percent,
                ft.Container(height=150),
                warning,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()

    # Медленно двигаем прогресс-бар (около часа)
    def update_progress():
        total_seconds = 3600  # 1 час = 3600 секунд
        update_interval = 36  # секунд между обновлениями (100 шагов * 36 = 3600)

        for i in range(101):
            time.sleep(update_interval)
            progress.value = i / 100
            percent.value = f"{i}%"

            if i < 20:
                status.value = "Распаковка системных компонентов..."
            elif i < 40:
                status.value = "Проверка целостности файлов..."
            elif i < 60:
                status.value = "Применение исправлений безопасности..."
            elif i < 80:
                status.value = "Оптимизация приложений (1/3)..."
            elif i < 95:
                status.value = "Оптимизация приложений (2/3)..."
            else:
                status.value = "Завершение установки..."

            page.update()

        # ФИНАЛ: Успешное завершение
        status.value = "Обновление успешно установлено!"
        status.color = ft.Colors.GREEN
        warning.value = "Устройство будет перезагружено через 3 секунды..."
        warning.color = ft.Colors.WHITE
        percent.value = "100%"
        progress.value = 1.0
        page.update()

        # Ждём 3 секунды и закрываем приложение
        time.sleep(3)
        os._exit(0)  # Принудительно закрываем приложение

    threading.Thread(target=update_progress, daemon=True).start()


ft.app(target=main)