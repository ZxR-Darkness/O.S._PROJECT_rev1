#главный файл
import logging
import traceback
from typing import Callable, Dict, Optional

import tkinter as tk

try:
    import pygame
    import progress
except ImportError:
    raise

from dlc import box, texting, radio, baring, crush, testing2, folders
from edes import filesave, textone, texttwo, textfour, textfive

logging.basicConfig(
    level=logging.ERROR,
    filename='os_project.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HELP_TEXT = (
    'команды: me, manto, drag 2, aegis, help me, kill you, ????, '
    'сука, молчи (нинада), hell, UPDATE, darkness, DARK'
)


class CommandRouter:
    def __init__(self, output: tk.Text, output2: tk.Text):
        self.output = output
        self.output2 = output2

        self._simple_responses: Dict[str, str] = {
            "me": "ты? ну ок",
            "update": "VERSION 0.5.0",
            "manto": "manto aio 80 kit",
            "drag 2": "drag 2 ичо дальше?",
            "aegis": "tkaegis boost 2",
            "hell": "мм а ты любишь погоречей",
            "как дела": "нормально а у тебя?",
            "good place": "yeah you know english wow",
            "новый год": "С НОВЫМ ГОДОМ 2024!!!",
            "test": "TEST TEST TEST TEST",
            "darkness": "а может все таки нет? \n версия 0.5.0 все таки выходит похоже",
        }

        self._handlers: Dict[str, Callable[[str], None]] = {
            "help": self._cmd_help,
            "привет": self._cmd_hello,
            "пока": self._cmd_bye,
            "secret": self._cmd_secret,
            "сука": self._cmd_suka,
            "молчи": self._cmd_molchi,
            "help me": self._cmd_help_me,
            "kill you": self._cmd_kill_you,
            "god": self._cmd_god,
            "bot": self._cmd_bot,
            "secrettwo": self._cmd_secret_two,
            "anomaly": self._cmd_anomaly,
            "dark": self._cmd_dark,
            "gids": self._cmd_gids,
            "os dev": self._cmd_os_dev,
            "secure": self._cmd_secure_cmd,
            "memento mori": self._cmd_memento_mori_cmd,
        }

    def run(self, command: str, user_name: str) -> None:
        self._clear_output()

        cmd_key = self._normalize_command(command)
        if not cmd_key:
            self._print("неправильная команда")
            return

        if cmd_key in self._simple_responses:
            self._print(self._simple_responses[cmd_key])
            return

        handler = self._handlers.get(cmd_key)
        if handler is None:
            self._print("неправильная команда")
            return

        handler(user_name)

    def _normalize_command(self, value: str) -> str:
        return (value or "").strip().lower()

    def _print(self, text: str) -> None:
        self.output.insert(tk.END, text)

    def _clear_output(self) -> None:
        self.output.delete(1.0, tk.END)

    def _require_name(self, user_name: str) -> Optional[str]:
        user_name = (user_name or "").strip()
        if user_name:
            return user_name
        self._print("Сначала введи имя")
        return None

    def _cmd_help(self, user_name: str) -> None:
        self._print(HELP_TEXT)

    def _cmd_hello(self, user_name: str) -> None:
        name = self._require_name(user_name)
        if not name:
            return
        self._print(f"{name} привет!")
        texting()

    def _cmd_bye(self, user_name: str) -> None:
        name = self._require_name(user_name)
        if not name:
            return
        self._print(f"{name} возврайщайся!")

    def _cmd_secret(self, user_name: str) -> None:
        self._print('секретный файл разблокирован')
        textone()

    def _cmd_suka(self, user_name: str) -> None:
        name = self._require_name(user_name)
        if not name:
            return
        self._print(f"{name} ты совсем офигел?")

    def _cmd_molchi(self, user_name: str) -> None:
        self._print('окей команда принята пооокааа')
        baring()
        crush()

    def _cmd_help_me(self, user_name: str) -> None:
        baring()
        try:
            with open('projects/secrets/ERROR.txt', 'rt', encoding='utf-8') as f:
                self._print(f.read())
        except FileNotFoundError:
            self._print("Файл ERROR.txt не найден")

    def _cmd_secure_cmd(self, user_name: str) -> None:
        box()

    def _cmd_kill_you(self, user_name: str) -> None:
        name = self._require_name(user_name)
        if not name:
            return
        self._print(f"{name} ты идиот")

    def _cmd_god(self, user_name: str) -> None:
        self._print('пожалуйста подождите...')
        filesave()

    def _cmd_bot(self, user_name: str) -> None:
        self._print("hm bot tg? он хранит много тайн")
        name = self._require_name(user_name)
        if not name:
            return
        self._print(f"\n{name} прими то что ты не можешь принять")

    def _cmd_anomaly(self, user_name: str) -> None:
        self._print("oh god, give me my camer")
        self.output2.insert(tk.END, "EERERERERERE anomale mara shmara erererererer    GIDS")
        print(":3")

    def _cmd_memento_mori_cmd(self, user_name: str) -> None:
        msg = "не надо о ней помнить она сама напомнит о себе..."
        self._print(msg)
        self.output2.insert(tk.END, msg)

    def _cmd_secret_two(self, user_name: str) -> None:
        radio()

    def _cmd_gids(self, user_name: str) -> None:
        self._print("ты что делаешь?")
        texttwo()

    def _cmd_os_dev(self, user_name: str) -> None:
        self._print("хм интересно")
        textfour()

    def _cmd_dark(self, user_name: str) -> None:
        print("в скором времени оно вернется из глубин ада")
        textfive()


def _initialize_system() -> None:
    try:
        folders()
        baring()
    except Exception:
        logging.error(traceback.format_exc())


def main() -> None:
    _initialize_system()

    window = tk.Tk()
    window.configure(background='black')
    window.title('O.S. PROJECT 0.5.0')

    label = tk.Label(window, text="введи что-нибудь:")
    label.configure(background="black", fg='white')
    label.grid_configure(row=10, column=10)

    entry = tk.Entry(window)
    entry.grid_configure(row=20, column=10)

    label2 = tk.Label(window, text="имя:")
    label2.configure(background="black", fg='white')
    label2.grid_configure(row=30, column=10)

    entry2 = tk.Entry(window)
    entry2.grid_configure(row=40, column=10)

    output = tk.Text(window)
    output.configure(background="black", fg='red')
    output.grid_configure(row=60, column=10)

    output2 = tk.Text(window)
    output2.configure(background="black", fg='white')
    output2.grid_configure(row=70, column=10)

    router = CommandRouter(output, output2)
    secret_btn: Optional[tk.Button] = None

    def on_submit() -> None:
        nonlocal secret_btn
        cmd = entry.get()
        name = entry2.get()
        router.run(cmd, name)

        if cmd.strip().lower() == "secrettwo" and secret_btn is None:
            secret_btn = tk.Button(
                window,
                text='не нажимай я прошу тебя открой файл ERROR',
                command=testing2,
            )
            secret_btn.grid_configure(row=80, column=10)

    button = tk.Button(window, text="Ввод", command=on_submit)
    button.configure(background="black", fg='white')
    button.grid_configure(row=50, column=10)

    output.insert(tk.END, "чтобы увидеть все команды напиши help, также сперва впиши имя, предупреждаю что программа может выключать компьютер \n пожалуйста запускайте когда будете готовы \n \n v0.5.0 REALESE")
    window.mainloop()


if __name__ == "__main__":
    main()
