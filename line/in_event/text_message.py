import line.out_event 

send_text = line.out_event.TextMessage()

class TextMessage(object):
    def __init__(self):
        pass

    def core(self, event):
        text_inp = event.message.text.lower()
        send_text.push(event.source.user_id, text_inp)
        print('in_event')