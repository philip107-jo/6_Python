
class Track:
    def __init__(self,title,artist,time):
        self.id=None
        self.title=title
        self.artist=artist
        self.time=time

    def play(self):
        print(f"{self.title} 재생")

    def __str__(self):
        return f"[{self.id},{self.title}-{self.artist},({self.time}초)]"



class Song(Track):
    def __init__(self,title,artist,time,lyrics):
        super().__init__(title,artist,time)
        self.lyrics=lyrics

    def play(self):
        print(f"{self.lyrics}와 함께 음악 재생")

    def __str__(self):
        return f"{super().__str__()} | 가사:{self.lyrics}"
class Podcast(Track):
    def __init__(self,title,artist,time,episode_no,host_name):
        super().__init__(title,artist,time)
        self.episode_no=episode_no
        self.host_name=host_name

    def play(self):
        print(f"{self.host_name}의 토크방송 재생")
    def __str__(self):
        return f"{super().__str__()} | 호스트: {self.host_name}"