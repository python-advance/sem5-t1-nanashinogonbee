import json

class Guestbook:
    def __init__(self, fn):
        try:
            self.handler = open(fn, 'r+')
        except FileNotFoundError:
            open(fn, 'w')
            self.handler = open(fn, 'r+')
        finally:
            self.json = json.loads(self.handler.read() or '{}')

    def register(self, uid, name, time):
        if uid in self.json.keys():
            print('you are already registered')
        else:
            self.json.update({'id': uid, 'name': name, 'time': time})

    def update(self, uid, name, time):
        self.json.update({'id': uid, 'name': name, 'time': time})

    def read(self):
        print('\n'.join('{}: {}'.format(k, v) for k, v in self.json.items()))


book = Guestbook('book')
book.register(uid=123, name='qwe', time='12:34')
book.read()
book.update(uid=123, name='asdf', time='11:11')
book.read()

