from protector.sock import Socket


class ProtectorClient:
    def __init__(self, addr: str = "127.0.0.1", port: int = 8888):
        self.client = Socket(addr, port)
        self.client.run()

    def password(self, password: str):
        return_msg = self.client.send_message("!PASSWORD " + self.__data_padding(password))
        print(return_msg)

    def close(self):
        self.client.send_message("!CLOSE")

    def __data_padding(self, data: str):
        return "!DATASTART " + data + " !DATAEND"
