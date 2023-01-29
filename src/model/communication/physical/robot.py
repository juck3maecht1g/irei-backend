class Robot:
    def __init__(self, ip: str, name: str) -> None:
        self.ip = ip
        self.name = name


    def get_ip(self) -> str:
        return self.ip

    def get_name(self) -> str:
        return self.name