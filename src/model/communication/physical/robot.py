class Robot:
    def __init__(self, name: str, ip: str) -> None:
        self.name = name
        self.ip = ip

    def get_name(self) -> str:
        return self.name

    def get_ip(self) -> str:
        return self.ip
