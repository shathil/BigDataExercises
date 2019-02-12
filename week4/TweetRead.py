# TweetRead.py
# Modified code obtained from LinkedIn

# pip install tweepy 

'''
Multiple Streaming is not supported by twitter API, so you can use this code and start a local streaming server, then listen to it using your Spark Streaming Code and count the number of words, or hashtags, etc or whatever you are lookign for. 

Note:-
Using famous keywords will overload your receiver, so configure according to your workstaion resources.
'''
import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import threading

# Create your own Twitter API credientials at developer.twitter.com
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''


class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            print(data.split('\n'))
            # print(type(data))
            self.client_socket.send(data.encode())
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['finland', 'suomi']) # you can modify these to any words you like or hashtags or userhandles etc.,

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(1)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
            print("Listening")

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                sendData(client)
            except:
                client.close()
                return False

if __name__ == "__main__":
    ThreadedServer(socket.gethostname() ,9888).listen()