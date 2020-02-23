# -*- coding: utf-8 -*-
import vk_api1 as vk_api
from audio import VkAudio

login = "89150028318"
password = "python123sql"


def resize_photo(name, n=1, save_name="ans"):

    image2 = Image.open(name)

    print(type(image2))

    width2 = image2.size[0]
    height2 = image2.size[1]
    width = width2//n
    height = height2//n
    image = Image.new("RGB", (width,height), (0,0,0))
    draw = ImageDraw.Draw(image)
    pix = image2.load()

    def grouping_of_pixels_in_1():

        for i in range(width):
            for j in range(height):
                a=0
                b=0
                c=0
                for t in range(n):
                    for l in range(n):
                        #print(a)
                        #print(pix[n*i+t, n*j+l][0])
                        a += pix[n*i+t, n*j+l][0]
                        b += pix[n*i+t, n*j+l][1]
                        c += pix[n*i+t, n*j+l][2]

                draw.point((i, j), (a//(n**2), b//(n**2), c//(n**2)))

    grouping_of_pixels_in_1()

    if type(image2) == "<class 'PIL.PngImagePlugin.PngImageFile'>":
        save_name+= ".png"
        image.save(save_name,"PNG")
    else:
        save_name+= ".jpg"
        image.save(save_name, "JPEG")
    del draw
def song_download(url):
    song = re.urlopen(url).read()
    f = open("ans.mp3", "wb")  # ans.jpg
    f.write(song)
    f.close()
    # img = cv2.imread('ans.jpg', 0)
    # cv2.imshow('image', img)
    # k = cv2.waitKey(0)
    os.startfile("ans.mp3")
def photo_download(url):

    logo = re.urlopen(url).read()
    f = open("ans.jpg", "wb")
    f.write(logo)
    f.close()



class my_vk:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.vk_session = vk_api.VkApi(login, password)

        try:
            self.vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return

        self.vk = self.vk_session.get_api()
        self.my_info = self.vk.users.get()[0]
        self.my_id = self.my_info["id"]
        self.my_name = self.my_info["first_name"]
        self.my_last_name = self.my_info["last_name"]
        self.vkaudio = VkAudio(self.vk_session)

    def searchSong(self, name, count = 1):
        music_list = [0] * count
        songList = self.vkaudio.search(name,count)
        return songList
    def info(self, id=None, parss=None):

        if not id:
            info = self.my_info
        else:
            info = self.vk.users.get(user_ids = id)[0]

        return str(info["id"]) + " " + info["first_name"] + " " + info["last_name"]
    def music_download(self,name,count = 1, info = False):
        music_list = [0]*count
        vkaudio = VkAudio(self.vk_session)
        #print(vkaudio.get_albums())
        #print(vkaudio.get_audio_by_id(owner_id=371745455,audio_id=456288015))
        num =0
        s =  vkaudio.search(name, count)
        #print(s)
        for j in s:
            print(j)
            num+=1
        bets_url = music_list
        #song_download(music_list[0][0])
        if info:

                print(bets_url)

    def muss(self,name="as",count = 1, info = False):
        music_list = [0] * count
        vkaudio = VkAudio(self.vk_session).get()
        for j in vkaudio[:count]:
            print(j["artist"],j["title"], j["url"])
    def music_of_user(self, id=None, count = 5, info = False):
        vkaudio = VkAudio(self.vk_session)
        num = 0
        if not id:
            id = self.my_id
        else:
            id = self.vk.users.get(user_ids = id)[0]["id"]
        music_list = []
        for j in vkaudio.search("lose yourself",1):
            print(j)
        for j in vkaudio.get_iter(id):
            num += 1
            if num > count:
                break
            music_list.append([j["artist"] , j["title"],j["url"]])
        if info:
            for j in music_list:
                print(j[0] + " " + j[1])
        return music_list
    def wow(self):
        vkaudio = VkAudio(self.vk_session)
        return vkaudio.get()

        # attachment = 49587996
        # url = 'https://m.vk.com/audios{}'.format(49587996)
        # response = vkaudio.http.get(
        #     url,
        #     allow_redirects=False
        # )
        # # response = self.vk.http.get(
        # #     'https://m.vk.com/{}'.format(attachment),
        # #     allow_redirects=False)
        # return response
    def friends(self, id=None, count=None,info = False):
        if not id:
            id = self.my_id
        friend_list = self.vk.friends.get(user_id = id,count = count)
        cou_friends = len(friend_list["items"])
        friend_list = friend_list["items"]
        if info:
            print(cou_friends)
            for j in friend_list:
                print(a.info(j))
        return friend_list


def codeSample(some):
    return some[::-1]

#resize_photo("lulia.jpg",n=3)
user = my_vk(login, password)
print(user.info())
#print(a.info(id=371745455))
#print(a.music_of_user(info=True))
#a.music_download(name="lose yourself", count= 5, info=True)
# songs = (a.searchSong("eminem",5))
# for j in songs:
#     print(j)
#for j in a.vk.photos.getAll( owner_id = int(a.info(id = "maxinator57").split()[0]), count=2)["items"]:
#    photo = j["sizes"][0]["url"], j["sizes"][0]["width"],j["sizes"][0]["height"]
#print(photo[0])

#tkinter_work(photo[0])
#pyga()
print(user.music_download("eminem",5))

#print(a)

#print(a.wow())
#music = (a.music(count = 3, id = "id96485735", info=False))
#print(music[0][2])
#a.friends(info = True,count=5)
#https://m.vk.com/mp3/audio_api_unava
# ilable.mp3?extra=mfvMndHlDgHfuLnKwwrL
# EJrZyuiTAJfOms9sztO3uMHNzgyZuxfnDM1HmtLHCNnlnZrKv29WzK9r
# lKXODLbXl1vbyLjAyvK1As9iAOyOBM9pyw1Joe5VoNnJqwrAzsOZqwnKudCZlLPowMuUtOXQx29c
# qNbpC3H5BgH2EhvOmJz0mMuOtJz1mJj0zgDvvOLjDM1NuMu1EvznufyOqwK3utL5Buj1uxvAnM9JnN
# rhww15stb1A3jZqO9LngXHnuzcp1zNBgzey2Tkzxjym3b2l3r4EG#AqS3nty