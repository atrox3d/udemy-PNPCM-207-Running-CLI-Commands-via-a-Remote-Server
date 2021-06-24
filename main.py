################################################################################
# https://jumpssh.readthedocs.io/en/latest/
# https://buildmedia.readthedocs.org/media/pdf/jumpssh/1.1.0/jumpssh.pdf
################################################################################
from jumpssh import SSHSession
import servers

jump1 = SSHSession(
                    host=servers.jump1.host,
                    port=servers.jump1.port,
                    username=servers.jump1.user,
                    password=servers.jump1.password
                ).open()

jump2 = jump1.get_remote_session(
                    host=servers.jump2.host,
                    port=servers.jump2.port,
                    username=servers.jump2.user,
                    password=servers.jump2.password
                )

remote = jump2.get_remote_session(
                    host=servers.server.host,
                    port=servers.server.port,
                    username=servers.server.user,
                    password=servers.server.password
                )


print(remote.get_cmd_output('hostname'))
print(remote.get_cmd_output('cat /HOSTNAME'))
print(remote.get_cmd_output('hostname -I'))
print(remote.get_cmd_output('python3 -V'))
# print(remote.get_cmd_output('top -n 1'))

jump1.close()