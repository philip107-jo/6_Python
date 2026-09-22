class SongNotFoundError(KeyError):
    def __init__(self,id):
        self.id=id
        super().__init__(f"존재하지 않는 아이디입니다.")

class DuplicateSongError(Exception):
    def __init__(self,title,artist):
        self.title=title
        self.artist=artist
        super().__init__(f"이미 등록되어 있는 곡입니다.")

class Playlist:
    def __init__(self):
        self.songs=[]
        self.next_id=1


    def add_song(self,song):
        """ 곡을 등록하는 메서드"""
        for s in self.songs:
            if s.title==song.title and s.artist==song.artist:
                raise DuplicateSongError(s.title,s.artist)

        song.id=self.next_id
        self.songs.append(song)
        self.next_id+=1
            
    def find_by_id(self,id):
        """곡을 조회하는 메서드"""
        for song in self.songs:
            if song.id==id:
                return song
        raise SongNotFoundError(id)
        

    def edit_song(self,id,title,time):
        """곡을 수정하는 메서드"""
        song=self.find_by_id(id)
        song.title=title
        song.time=time

    def delete_song(self,id):
        """곡을 삭제하는 메서드"""
        song=self.find_by_id(id)
        self.songs.remove(song)

    def search_by_artist(self,artist):
        """아티스트 기준으로 곡을 검색하는 메서드"""
        result=[]
        for s in self.songs:
            if s.artist==artist:
               result.append(s) 
        return result    

    def total_time(self):   
        """등록된 곡의 총 재생시간을 조회하는 메서드"""
        total=0
        for s in self.songs:
            total+=s.time
        return total
        