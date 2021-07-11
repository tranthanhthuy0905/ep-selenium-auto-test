from Configs.TestData.BaseTestData import BaseTestData
import random
import os


class CustomDomainTestData(BaseTestData):

    INSTANCE_NAME = os.getenv("DEFAULT_AUTOTEST_VM_HOST")
    INSTANCE_IP = os.getenv("DEFAULT_AUTOTEST_VM_IP")
    INSTANCE_INFO = INSTANCE_NAME + " - " + INSTANCE_IP
    PORT = os.getenv("DEFAULT_AUTOTEST_VM_PORT")
    HTTP_PORT = "80"
    HTTPS_PORT = "443"
    HTTP = "http://"
    HTTPS = "https://"
    

    def gen_domain_name():
        return "domain-" + str(random.randint(100000,999999))
    