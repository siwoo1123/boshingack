from gtts import gTTS
import pygame
import time
pygame.mixer.init()
pygame.init()

allha = time.strftime('%Y', time.localtime(time.time()))
text = f"{str(int(allha) + 1)}년 새해가 밝았습니다."
filename = "helloKO.mp3"

tts = gTTS(text=text, lang='ko')
tts.save(filename)
while True:
    print(time.strftime('%Z %Y %m %d %p %I %M %S', time.localtime(time.time())))
    time.sleep(1)
    if time.strftime('%Z %Y %m %d %p %I %M %S', time.localtime(time.time())) == f"KST {allha} 12 31 PM 11 59 55" or time.strftime("%Z %Y %m %d %p %I %M %S", time.localtime(time.time())) == f"대한민국 표준시 {allha} 12 31 PM 11 59 55":
        for i in range(1, 34):
            pygame.mixer.music.load("보신각 종소리.mp3")
            pygame.mixer.music.play(loops=0, start=0.0)
            time.sleep(10)
            pygame.mixer.music.set_volume(10)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=0, start=0.0)
        time.sleep(10)
        pygame.mixer.music.set_volume(10)
        break
exit()
