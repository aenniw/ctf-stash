#!/usr/bin/env python3

import sys
import hashlib
import binascii
from Crypto.PublicKey import RSA

class User(object):
    
    def __init__(self, username, server):
        self.username = username

        self.inbox = []
        self.outbox = []

        self.server = server

class Server(object):
    
    def __init__(self):
        
        key = open("./key.pem", "rb")
        
        self.key = RSA.import_key(key.read())
        key.close()
        
        flag = open("./flag.txt").read()
        flag = binascii.hexlify(flag.encode('utf-8'))
        flag = int(b"0x%s" % flag, 16)

        c = self.key._encrypt(flag)
        m = hashlib.sha256()
        m.update(str(c).encode('utf-8'))

        self.seen_hashes = [m.hexdigest()]
         
        print("Ciphertext: %s" % c)

        self.users = {}

    def send_message(self, msg, user):

        if user not in self.users.keys():
            return False

        msg = binascii.hexlify(msg.encode('utf-8'))
        msg = int(b"0x%s" % msg, 16)

        try:
            ctx = self.key._encrypt(msg)
        except:
            print("Invalid plaintext")
            return False

        self.users[user].inbox.append(ctx)

        print(ctx)
        sys.stdout.flush()

        return True

    def recv_message(self, msg):

        msg = str(int(msg))

        m = hashlib.sha256()
        m.update(msg.encode('utf-8'))
        h = m.hexdigest()

        if h in self.seen_hashes:
            return False

        self.seen_hashes.append(h)
        
        try:
            p = self.key._decrypt(int(msg))
        except:
            print("Invalid Ciphertext")
            return False

        print(p)
        sys.stdout.flush()

        return True

    def handle_send_message(self, msg):
        msg = msg.split(':')
        _, smsg, user = msg
        
        if not self.send_message(smsg, user):
            print("FAILED TO SEND MESSAGE") 
            sys.stdout.flush()
            return

    def handle_recv_message(self, msg):
        msg = msg.split(':')
        _, rmsg = msg

        if not self.recv_message(rmsg):
            print("FAILED TO RECEIVE MESSAGE")
            sys.stdout.flush()
            return

    def handle_key_message(self):
        n = self.key._n
        e = self.key._e

        print("N:%s\nE:%s\n" % (n, e))
        sys.stdout.flush()

    def serve(self):
        while 1:
            msg = input()

            if msg.startswith("SEND:"):
                self.handle_send_message(msg)
            elif msg.startswith("RECV:"):
                self.handle_recv_message(msg)
            elif msg.startswith("KEY:"):
                self.handle_key_message()
            else:
                print("BAD API COMMAND")
                continue


if __name__ == "__main__":
    s = Server()

    Alice = User("Alice", s)
    Bob = User("Bob", s)

    s.users["Alice"] = Alice
    s.users["Bob"] = Bob

    s.serve()
