import requests
import random

facts = [
    'The door bell makes different sounds, depending on if someone rings downstairs or upstairs',
    'You can controll what I say. Just visit pegasus.noise:5000 and enter a text',
    'You can display text, images and videos on Flaschentaschen. Just visit pegasus.noise:9000 and enter a text or upload an image or video',
    'We have a library with all kinds of awesome books!',
    'Hackerspaces exist all over the world. And the movement actually started in Germany. See a map of all hackerspaces on hackerspaces.org',
    'Everyone can organize events at Noisebridge. In fact its a great way to introduce more people to Noisebridge',
    'Every Tuesday evening we have our weekly General Meeting. Where we talk about Noisebridge, announcements and more. In case you want to organize an event at Noisebridge, this is also a great chance to announce your event.'
]


def speak(text):
    # make marry speak
    parts = text.split('. ')
    requests.get('http://pegasus.noise:5000?text=Did you know?')
    for part in parts:
        requests.get('http://pegasus.noise:5000?text=' +
                     part.replace('.', ' dot ').replace(':', ' colon '))


def interestingFacts():
    entry_num = random.randint(0, len(facts)-1)
    speak(facts[entry_num])
