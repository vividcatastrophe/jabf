import subprocess
import shlex
import os
from targets.target import FileContainerTarget


class LuksTarget(FileContainerTarget):
    name = 'luks'

    def check_data(self, data):
        luks_cmd = shlex.split(
            'cryptsetup luksOpen {container} lukstmp --test-passphrase -'
            .format(container=self.container_path)
        )
        echo_cmd = shlex.split('echo -n "{data}"'.format(data=data))
        try:
            echo_ps = subprocess.Popen(echo_cmd, stdout=subprocess.PIPE)
            with open(os.devnull, 'wb') as shutup:
                subprocess.check_call(luks_cmd, stdin=echo_ps.stdout,
                                      stdout=shutup, stderr=shutup)
            echo_ps.wait()
        except subprocess.CalledProcessError:
            return False
        return True
