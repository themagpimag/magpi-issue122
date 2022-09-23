# Raspberry Radio from The MagPi by Sean McManus
import rr_newsreader, random, pyttsx3, os, sys
from playsound import playsound
from tinytag import TinyTag
import dot3k.lcd as lcd # Remove if not using Display-O-Tron

def output(text):
    print(text)
    voice.say(text)
    voice.runAndWait()

def broadcast_news_and_weather():
    playsound('news_jingle.mp3')
    date = rr_newsreader.get_date()
    output(date)
    news_headlines = rr_newsreader.get_news()
    for line in news_headlines:
        output(line)
    weather_report, temperature = rr_newsreader.get_weather()
    output(weather_report)

def index_directory(path, songs, perform_checks):
    print("Processing directory:", path)
    for entry in os.listdir(path):
        path_plus_entry = os.path.join(path, entry)
        if os.path.isdir(path_plus_entry):
            index_directory(path_plus_entry, songs, perform_checks)
        elif entry.endswith('.mp3'):
            tag = TinyTag.get(path_plus_entry)
            if perform_checks == False or \
                  (tag.title is not None and \
                   tag.genre not in ["Books & Spoken", "Christmas"] and \
                   tag.duration < 6000 and \
                   "live" not in tag.album and \
                   "live" not in tag.title):
                songs.append(path_plus_entry)
                print("Track added:", tag.title, "by", tag.artist, "from", tag.album)
    return songs

def play_songs(number_of_songs):
    for _ in range(number_of_songs):  
        if random.random() > 0.4:
            jingle_to_play = random.choice(jingles)
            playsound(jingle_to_play)
        song_to_play = random.choice(songs)
        tag = TinyTag.get(song_to_play)
        dj_says = random.choice(
            [   f"What were you doing in {tag.year}? Here's what {tag.artist} was up to.",
                f"Here's a {tag.year} track from the album {tag.album}.",
                f"Fancy some {tag.genre} music? Here's {tag.artist}."
            ])
        output(dj_says)
        DAB_display = (tag.artist + ' ' * 16)[:16] \
                      + tag.title[:32]
        lcd.clear()
        lcd.write(DAB_display)
        playsound(song_to_play)

songs = index_directory("music", [], True)  # folder for music
jingles = index_directory("jingles", [], False) # folder for jingles
voice = pyttsx3.init()
voice.setProperty('rate', 170)
while True:
    broadcast_news_and_weather()
    play_songs(8)