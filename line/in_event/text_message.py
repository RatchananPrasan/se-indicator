import line.out_event
from .crypto_bot import CryptoBot

send_text = line.out_event.TextMessage()

class TextMessage(object):
    def __init__(self):
        self.currencies = ["BTC", "ETH", "DAS", "OMG", "XRP"]
        self.cryptoBot = CryptoBot(self.currencies)

    def core(self, event):
        #nput = event.message.text
        #self.cryptoBot.command(input)
        pass