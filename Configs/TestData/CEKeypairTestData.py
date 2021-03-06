from Configs.TestData.BaseTestData import BaseTestData
import random
import time

class CEKeypairTestData(BaseTestData):
    KEYPAIR_NAME = "autotest-keypair-" + str(random.randint(100000,999999))
    PUBLIC_KEY = "autotest-keypair-" + str(random.randint(100000,999999))

    VALID_PUBLIC_KEY_1 = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDIapSCBZe6ax3jWRHs5FPNFvUpN6bq13JouxBslMXehNruUZHeYQaEdCpH/LMM2GrLPp21Q0uFqVsTSADyK+RP4FNnXtm8Qjm2dh16vy/rmkI3E35ozJI3Zmq+oUpbiAnvmq74lVfP5qv7o0wvYgGtz4nTFr+CMJhzFedbLRGkOzW/GeSWI/xYs8WKBS4O4mBgb2FPaSRVTg61dhjcCeGjP56EOU3APLqhhLuMhO5hqGTMB7ozlqGk32IjJHZmpNPvOMiXDQYAjZe7WC6uXbpfpweidAYZQ32FKPnK12SaEeakYQNhvg8ZLydraL01qSZLwzjHaoflEo72dsFTfQX3/dm3LL1hzgl8V8pNdO5+QrSjM/ylxcdA8ObiaUnUHRlIiYC9S2G7ppQLLQz43CNwG5+KfUeUQhXHrlZd4VZzNVdWKU6hRnR3KWkMSNFe9P5e8/kXDi2klZdk84HxLKqZgJKpUb6AmNMbhbpKoKhRF4rtzEkybRQwYiuCjG/lamquanhoang+cesKTm4v0S5ZIxnORjDR4vCF9OILopjZH/4tMEzASO96uCpslwx0DNxPnbuTBz+7uymnuaxiubUQU65iKwPatn7e0HLptVd0OEFOjSp7UAg9CDtaFuJJv/I/skoep+Ft/WOFBz1B3i0KsKV4dMWttZzBMXUTqHSiQ== quanlh5@vng.com.vn"
    INVALID_PUBLIC_KEY_01 = "abdquandeptraief"

    @staticmethod
    def gen_new_keypair_name():
        return "autotest-keypair-" + str(random.randint(100000,999999))
