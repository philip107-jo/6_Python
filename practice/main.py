from models import Song, Podcast
from playlist import Playlist, SongNotFoundError, DuplicateSongError

pl = Playlist()         

while True:
    print("1.등록 2.검색 3.수정 4.삭제 5.총 재생시간 6.재생 0.종료")
    menu = input("번호입력: ")

    try:
        match menu:
            case "1":
                kind=input("1.노래, 2.팟캐스트: ")
                title= input("제목: ")
                artist=input("아티스트: ")
                time=(int(input("재생시간(초): ")))
                if kind=="1":
                    lyrics=input("가사: ")
                    song=Song(title,artist,time,lyrics)
                else:
                    episode_no=input("에피소드 번호: ")
                    host_name=input("호스트 이름: ")
                    song=Podcast(title,artist,time,episode_no,host_name)
                pl.add_song(song)
                print(f"등록완료")
            case "2":
                artist=str(input("찾을 곡의 가수명:"))
                result=pl.search_by_artist(artist)
                if not result:
                    print("검색 결과 없음")
                else:
                    for s in result:
                        print(s.id,s.title,s.time)
                
            case "3":
                id =int(input("수정할 곡 번호 입력:"))
                title =input("수정할 곡 제목 입력:")
                time =int(input("수정할 곡 재생시간 입력:"))

                pl.edit_song(id,title,time)
            case "4":
                song_id = int(input("삭제할 ID: "))
                pl.delete_song(song_id)
                print("삭제 완료")
            case "5":
                print(pl.total_time())
            case "6":
                id=int(input("재생할 ID: "))
                song=pl.find_by_id(id)
                song.play()
            case "0":
                print("프로그램 종료")
                break
            case _:
                print("메뉴에 있는 번호를 입력해주세요")

    except SongNotFoundError as e:
        print(f"실패: {e}")
    except DuplicateSongError as e:
        print(f"실패: {e}")
    except ValueError:
        print("숫자를 입력해야 하는 곳에 문자가 들어왔어요")