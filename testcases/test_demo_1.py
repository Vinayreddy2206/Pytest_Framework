import pytest
from common.SSH import *
from library.const import *

class TestDemo:
    def test_case_1(self):
        self.ssh_obj = SSHConnectivity()
        print(self.ssh_obj.execute_remote_command(HOST,PORT_NO,USERNAME,USER_PASSWORD,COMMAND))