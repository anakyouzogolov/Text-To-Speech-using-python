import pyttsx3

#create pyttsc3 object
engine = pyttsx3.init() 


# Rate 
rate = engine.getProperty("rate")


#change the default rate 
engine.setProperty("rate",150)

#Volume
#setting up volume level between 0 and 1 (min:0, max:1)
volume = engine.getProperty("volume")
print("volume is {0}".format(volume))

#change the default volume
engine.setProperty("volume", 1)


#Voices
voices = engine.getProperty("voices")

# male voice of index 0 and female of index 1
print("Male Voice : {0}".format(voices[0].id))
print("Female Voice : {0}".format(voices[1].id))

#setting up voice
engine.setProperty("voice", voices[0].id)


engine.say("hello in magic code youtube channel your welcome")
print("Engine Is Runing...")

engine.runAndWait()
engine.stop()