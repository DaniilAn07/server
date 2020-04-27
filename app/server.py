#
# Серверное приложение для соединений
#
import asyncio
from asyncio import transports

class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    # Initialization of server
    def __init__(self, server: 'Server'):
        self.server = server

    # Logging in to the server
    def data_received(self, data: bytes):
        print(data)

        decoded = data.decode()

        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "")
                self.transport.write(
                    f"Привет, {self.login}!\n".encode()
                )
            else:
                self.transport.write("Неправильный логин\n".encode())

    # Viewing if client connect
    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("Пришел новый клиент")

    # Viewing if client disconnect
    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Клиент вышел")

    # Sending message from client
    def send_message(self, content: str):
        message = f"{self.login}: {content}"

        for user in self.server.clients:
            user.transport.write(message.encode())


class Server:
    clients: list

    # Initialization of clients
    def __init__(self):
        self.clients = []

    # Building protocol
    def build_protocol(self):
        return ServerProtocol(self)

    # Async start of the server
    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()

# Calling the functions
process = Server()
main = process.start
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")