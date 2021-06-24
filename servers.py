import json
from dataclasses import dataclass, asdict

JSON_FILE = "private/servers.json"


@dataclass
class Server:
    host: str = ""
    user: str = ""
    password: str = ""
    port: int = 22

    @classmethod
    def from_jsonfile(cls, filename, name=None):
        with open(filename) as fp:
            data = json.load(fp)
        if name:
            return cls(**data[name])
        return {name: cls(**server) for name, server in data.items()}


jump1 = Server.from_jsonfile(JSON_FILE, "win10")
jump2 = Server.from_jsonfile(JSON_FILE, "ubuntu18")
server = Server.from_jsonfile(JSON_FILE, "ubuntu20")

if __name__ == '__main__':
    ubuntu18 = Server.from_jsonfile(JSON_FILE, "ubuntu18")
    print(ubuntu18)
    servers = Server.from_jsonfile(JSON_FILE)
    print(servers)
