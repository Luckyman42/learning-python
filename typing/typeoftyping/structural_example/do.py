from cat import Cat
from speak import speak_loud

c = Cat()
print(speak_loud(c)) 
# Ok but Cat not explicit "inherit" from speakable
# in fact, Cat doesn't even know about Speakable protocol

