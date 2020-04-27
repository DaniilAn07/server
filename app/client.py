# Client's chat
import asyncio
from asyncio import transports
from PySide2.QtWidgets import QMainWindow, QApplication
from asyncqt import QEventLoop
from app.interface import Ui_MainWindow

# Main Window
class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'MainWindow'

    # Initialization of main Window
    def __init__(self, chat_window: 'MainWindow'):
        self.window = chat_window

    # Main Window receiving data
    def data_received(self, data: bytes):
        decoded = data.decode()
        self.window.append_text(decoded)

    # Input sending message
    def send_data(self, message: str):
        encoded = message.encode()
        self.transport.write(encoded)

    # Connecting to the server
    def connection_made(self, transport: transports.Transport):
        self.window.append_text("Подключено")
        self.transport = transport

    # Disconnecting from the server
    def connection_lost(self, exception):
        self.window.append_text("Отключено")


# Logic of user interface
class MainWindow(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    # Initialization of button click
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.message_button.clicked.connect(self.button_handler)

    # Sending text by protocol
    def button_handler(self):
        message_text = self.message_input.text()
        self.message_input.clear()
        self.protocol.send_data(message_text)

    # Viewing text on main message box
    def append_text(self, content: str):
        self.message_box.appendPlainText(content)

    # Building protocol
    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    # Async start of the server
    async def start(self):
        self.show()

        event_loop = asyncio.get_running_loop()

        coroutine = event_loop.create_connection(
            self.build_protocol,
            "127.0.0.1",
            8888
        )

        await asyncio.wait_for(coroutine, 1000)

# Calling functions
app = QApplication()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

window = MainWindow()

loop.create_task(window.start())
loop.run_forever()