class credential:
    def __init__(self, servername, mysecret, myport):
        self.servername = servername
        self.mysecret = mysecret
        self.myport = myport
        
sys_local = credential("127.0.0.1", "MySecretKey", 25575)
