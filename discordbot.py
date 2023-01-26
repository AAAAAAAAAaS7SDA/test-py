import discord, asyncio
from discord.ext import commands
import  datetime
import random
import time , os

mod = 15
msg = ''

INTENTS = discord.Intents.default()
INTENTS.messages = True # 메세지를 읽는권한
INTENTS.message_content = True # 메세지를 읽는권한
bot = commands.Bot(command_prefix='!', intents=INTENTS)
bot.remove_command('help')

startup_extensions = ['Cogs.Message']
os.chdir('Cogs')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('불러오기 실패! {}\n{}'.format(extension, '{}: {}'.format(type(e).__name__, e)))

@bot.event
async def on_ready():
    print("치처 봇이 시작 돼었습니다!")
    print("시작 됩니다.")
    print("Good!")
    message = [f"{round(bot.latency*1000)}ms", "치처 야 이라고 부르세요!", "다른 서버 실행!"]
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(3)

bad = ['ㅅㅂ','시발','씨발','미친','ㅁㅊ','썌기','ㅅㅂㄴ','시발놈','씨발놈','ㅁㅊㄴ','미친놈','나쁜놈','ㄴㅃㄴ','죽어','ㅈㅇ','죽어 섀기놈아','ㅈㅇ ㅅㄱㄴㅇ','너 죽으래 시발 썌기 놈아!']
bad2 = ['야','너']

science = {"51x48=" : "2448"}
check = False
b = ""

science = {"현무암이란?" : "현무암은 회색~흑색의 분출 화산암"}
check = False
d = ""

@bot.event
async def on_message(message):
    global science, b, check, mod, d
    if message.content.startswith("치처 야"):
        await message.channel.send("민섭 E이 여기있습니다!")

    if message.content.startswith("치처 게임"):
        await message.channel.send("전 게임를 못합니다...")
    
    if message.content.startswith("치처 봇 여기로 초대함?"):
        await message.channel.send("봇은 9월12일날에 생성 되어고 들어온날짜은 11월 16일입니다. ")
    
    if message.content.startswith("치처 다른거 은?"):
        await message.channel.send("안됨니다.")

    message_contant=message.content
    for i in bad:
        if i in message_contant:
            await message.delete()
            embed = discord.Embed(title="🚨욕설 감지🚨", color=0xFF0000)
            embed.add_field(name="닉네임 : ", value=message.author, inline=False)
            await message.channel.send(embed=embed)
    
    message_contant=message.content
    for i in bad2:
        if i in message_contant:
            await message.delete()
            embed = discord.Embed(title="🚨야 할말 감지🚨", color=0xFF0000)
            embed.add_field(name="닉네임 : ", value=message.author, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("치처 주사위"):
        r = random.randint(1, 50)
        if r == 1:
            await message.channel.send("1!")
        
        if r == 2:
            await message.channel.send("2!")
        
        if r == 3:
            await message.channel.send("3!")
        
        if r == 4:
            await message.channel.send("4!")

        if r == 5:
            await message.channel.send("5!")

        if r == 6: 
            await message.channel.send("6!")

        if r == 7: 
            await message.channel.send("7!")

        if r == 8: 
            await message.channel.send("8!")

        if r == 9: 
            await message.channel.send("9!")

        if r == 10: 
            await message.channel.send("10!")

        if r == 11:
            await message.channel.send("11!")
        
        if r == 12:
            await message.channel.send("12!")
        
        if r == 13:
            await message.channel.send("13!")
        
        if r == 14:
            await message.channel.send("14!")

        if r == 15:
            await message.channel.send("15!")

        if r == 16: 
            await message.channel.send("16!")

        if r == 17: 
            await message.channel.send("17!")

        if r == 18: 
            await message.channel.send("18!")

        if r == 19: 
            await message.channel.send("19!")

        if r == 20: 
            await message.channel.send("20!")

        if r == 21:
            await message.channel.send("21!")
        
        if r == 22:
            await message.channel.send("22!")

        if r == 23:
            await message.channel.send("23!")
        
        if r == 24:
            await message.channel.send("24!")

        if r == 25:
            await message.channel.send("25!")

        if r == 26: 
            await message.channel.send("26!")

        if r == 27: 
            await message.channel.send("27!")

        if r == 28: 
            await message.channel.send("28!")

        if r == 29: 
            await message.channel.send("29!")

        if r == 30: 
            await message.channel.send("30!")

        if r == 31:
            await message.channel.send("31!")
        
        if r == 32:
            await message.channel.send("32!")
        
        if r == 33:
            await message.channel.send("33!")
        
        if r == 34:
            await message.channel.send("34!")

        if r == 35:
            await message.channel.send("35!")

        if r == 36: 
            await message.channel.send("36!")

        if r == 37: 
            await message.channel.send("37!")

        if r == 38: 
            await message.channel.send("38!")

        if r == 39: 
            await message.channel.send("39!")

        if r == 40: 
            await message.channel.send("40!")

        if r == 41:
            await message.channel.send("41!")
        
        if r == 42:
            await message.channel.send("42!")
        
        if r == 43:
            await message.channel.send("43!")
        
        if r == 44:
            await message.channel.send("44!")

        if r == 45:
            await message.channel.send("45!")

        if r == 46: 
            await message.channel.send("46!")

        if r == 47: 
            await message.channel.send("47!")

        if r == 48: 
            await message.channel.send("48!")

        if r == 49: 
            await message.channel.send("49!")

        if r == 50: 
            await message.channel.send("50!!!!")

    if message.content.startswith("치처 프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="닉네임 : ", value=message.author, inline=False)
        embed.add_field(name="서버닉네임 : ", value=message.author.display_name, inline=False)
        embed.add_field(name="가입일 : ", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디 : ", value=message.author.id, inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("치처 바보임?"):
        embed = discord.Embed(color=0x1DDB16)
        embed.add_field(name="아닙니다.", value="절떄로 바보 아닙니다.")
        embed.add_field(name="경고 지급 예정 입니다.", value="바보 하지 말아 주세요. 도배하면 경고 X 로 들어 갑니다.")
        await message.channel.send(embed=embed)

    if message.content.startswith("!!경고"):
        userid = message.content[5:].split(" ")[0] # userid를 가져옵니다 message.content[5:] -> !!경고 123 테스트 이렇게 입력했으면 5번쨰 인덱스 부터 전부 가져오고 띄워쓰기를 기준으로 잘라줍니다
        username = bot.get_user(int(userid))# userid로 유저의 이름을 가져옵니다
        reason = message.content[5:].split(" ")[1] # 띄워쓰기 기준으로 2번째 리스트를 가져옵니다
        name = message.author.name # 이 명령어를 사용한 사람의 이름을 가져옵니다
        server_name = value=message.author.display_name # 이 명령어를 사용한 사람의 서버닉네임을 가져옵니다.
        id = message.author.id # 이 명령어를 사용한 사람의 아이디를 가져옵니다.
        await message.channel.send("{0}관리자(id = {1} server_name = {2}) 가 {3}(id = {4}) 에게 경고를 주었습니다. 사유 : {5}".format(name, id, server_name, username, userid, reason))
        await message.channel.send("```diff\n!{0}관리자(id = {1} server_name = {2})가\n-{3}(id = {4})에게 경고를 주었습니다.\n!사유 : {5}```".format(name, id, server_name, username, userid, reason))
        # !!경고 123 테스트
        # 012 3 45
        # 5번째 인덱스부터가 123 테스트 입니다.
        # 여기서 띄워쓰기 기준으로 잘라주면 123과 테스트 이렇게 2개의 리스트가 만들어 집니다.
        # 123은 리스트의 0번째
        # 테스트는 리스트의 1번째로
        # split(" ")[0] = 123(ID를 가져오고)
        # split(" ")[1] = 테스트(사유를 가져옵니다.)

    if message.content.startswith("!퀴즈"):
        subject = message.content[4:]
        if subject == "수학":
            a = random.choice(list(science.keys()))
            b = science[a]
            check = True
            await message.channel.send("`" + a + "`")

        elif check == False:
            await message.channel.send("`이미 퀴즈를 푸시는 중 입니다. 모르겠다면 !패스 해주세요.`")

    if message.content.startswith("!정답"):
        if check == True:
            answer = message.content[4:]
            if answer == d:
                check = False
                embed = discord.Embed(title="!정답!", color=0x2FED28)
                await message.channel.send(embed = embed)
            elif answer != d:
                embed = discord.Embed(title="오답..", color=0xFF0000)
                await message.channel.send(embed = embed)

        elif check == False:
                await message.channel.send("폴고 있는 퀴즈가 없습니다.")

    if message.content.startswith("!패스"):
        if check == True:
            embed = discord.Embed(title="#패스#", color=0xFFE400)
            await message.channel.send(embed = embed)
            await message.channel.send("`정답은 '" + d + "` 였습니다. \n문제를 패스 하셨습니다.")
        elif check == False:
            await message.channel.send("`폴고 있는 퀴즈가 없습니다.`")

    if message.content.startswith("!퀴즈"):
        subject = message.content[4:]
        if subject == "과학":
            c = random.choice(list(science.keys()))
            d = science[c]
            check = True
            await message.channel.send("`" + c + "`")

        elif check == False:
            await message.channel.send("`이미 퀴즈를 푸시는 중 입니다. 모르겠다면 !패스 해주세요.`")

    if message.content.startswith("!정답"):
        if check == True:
            answer = message.content[4:]
            if answer == d:
                check = False
                embed = discord.Embed(title="!정답!", color=0x2FED28)
                await message.channel.send(embed = embed)
            elif answer != d:
                embed = discord.Embed(title="오답..", color=0xFF0000)
                await message.channel.send(embed = embed)

        elif check == False:
                await message.channel.send("폴고 있는 퀴즈가 없습니다.")

    if message.content.startswith("!패스"):
        if check == True:
            embed = discord.Embed(title="#패스#", color=0xFFE400)
            await message.channel.send(embed = embed)
            await message.channel.send("`정답은 '" + d + "` 였습니다. \n문제를 패스 하셨습니다.")
        elif check == False:
            await message.channel.send("`폴고 있는 퀴즈가 없습니다.`")

    if message.content.startswith("치처 도옴말"):
        embed = discord.Embed(title="도옴말")
        embed.add_field(name="치처 야", value="기본말 입니다.", inline=False)
        embed.add_field(name="치처 다른거 은?", value="안돼안돼", inline=False)
        embed.add_field(name="치처 봇 여기로 초대함?", value="알려 줘요!", inline=True)
        embed.add_field(name="치처 게임", value="게임 할 수 없다", inline=False)
        embed.add_field(name="치처 넌 바보니?", value="ㅋ.", inline=True)
        embed.add_field(name="치처 프로필", value="내정보 알려줘요!", inline=False)
        embed.add_field(name="치처 바보임?", value="ㅋㅋ.", inline=True)
        embed.add_field(name="!퀴즈 , !패스 , 정답", value="퀴즈 내요", inline=False)
        embed.add_field(name="치처 음악골라", value="유튜브 음악를 알려줘요!", inline=True)
        embed.add_field(name="!청소", value="관리자만 사용 가능 합니다.", inline=False)
        embed.add_field(name="!공지", value="관리자만 사용 가능 합니다.", inline=True)
        embed.add_field(name="!복권", value="복권 확인!", inline=False)
        embed.add_field(name="치처 광산", value="광산 합니다!", inline=True)
        embed.add_field(name="치처 확률", value="광산의 확률를 보여 줘요!", inline=False)
        embed.add_field(name="치처 도배모드 ON", value="도배 모드 활성화 됩니다!", inline=True)
        embed.add_field(name="치처 도배모드 OFF", value="도배 모드가 비활성화 됩니다!", inline=False)
        embed.add_field(name="치처 생존", value="생존 좀비 게임 할수 있다", inline=True)
        embed.add_field(name="치처 현재 시간", value="시각!", inline=False)
        embed.add_field(name="치처 강화", value="강화 합니다!", inline=True)
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!규칙"):
        if(message.author.guild_permissions.administrator):
            embed = discord.Embed(title="규칙")
            embed.add_field(name="채팅에서 도배할시 👉 경고 I", value="도배은 안돼요~ 채팅방에서~", inline=False)
            embed.add_field(name="욕 보내며 , 음성 말하며👉 경고 I", value="욕 사용 할시 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 수상함 링크 보내며 👉 경고 I", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 조금 더 수상함 링크 보내며 👉 경고 II", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 더 수상함 링크 보ㅐ며 👉 경고 III", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 덜 수상함 링크 보ㅐ며 👉 경고 IV", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 덜 마이 수상함 링크 보ㅐ며 👉 경고 V", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 심각하 링크 보ㅐ며 👉 경고 VI", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 조금 심각하 링크 보ㅐ며 👉 경고 VII", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 조금 마이 심각하 링크 보ㅐ며 👉 경고 VIII", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 조금 위험하 링크 보ㅐ며 👉 경고 IX + 타임아옷 1일", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="도배방에서 위험하 링크 보ㅐ며 👉 경고 X + 타임아옷 1주일", value="도배방에서 링크 의심 하면 경고 들어갑니다.", inline=False)
            embed.add_field(name="요즘 계정 밴하고 부꼐 들어올시👉 경고 X + 타임아옷 1주일 + 즉시 밴 ", value="요즘 계정은 밴하고 부계정 들어 주시면 경고 추방 하겠습니다.", inline=False)
            embed.add_field(name="심각한 욕 보내면👉 경고 III 타임아옷 1일", value="심각한 욕 보내면 경고 예요!", inline=False)
            embed.set_thumbnail(url="https://yt3.ggpht.com/M5bUy8QEDikBXVzwimxXYHxWRs9UJgl-WUsAjdcuzo0hgoFkJqPwGtss_j9mipemupvHPni17g=s600-c-k-c0x00ffffff-no-rj-rp-mo")
        else:
            await message.channel.send("**당신은 규칙 명령어 써할 \n`관리 명령 입니다.`\n당신은 관리 명령 사용 할수 없습니다.**")
            await message.channel.send(embed=embed)

    if message.content.startswith("치처 음악골라"):
        r = random.randint(1, 10)
        if r == 1:
            await message.channel.send("1 https://www.youtube.com/watch?v=KTrhCoBC_9E")
        
        if r == 2:
            await message.channel.send("2 https://www.youtube.com/watch?v=3lwTql6YlSE")
        
        if r == 3:
            await message.channel.send("3 https://www.youtube.com/watch?v=2PvVUguRs8M")
        
        if r == 4:
            await message.channel.send("4 https://www.youtube.com/watch?v=DmZm8OjnlvM")

        if r == 5:
            await message.channel.send("5 https://www.youtube.com/watch?v=8_VEfjQpxc0")

        if r == 6: 
            await message.channel.send("6 https://www.youtube.com/watch?v=0upiNhdMaBs")

        if r == 7: 
            await message.channel.send("7 https://www.youtube.com/watch?v=zg-iVxZCBHU")

        if r == 8: 
            await message.channel.send("8 https://www.youtube.com/watch?v=nFeP8cO7xLI")

        if r == 9: 
            await message.channel.send("9 https://www.youtube.com/watch?v=4ZFRyil9T-w")

        if r == 10: 
            await message.channel.send("10 https://www.youtube.com/watch?v=LwNhvbet8pU")
    
    if message.content.startswith ("!청소"):
        if message.author.guild_permissions.administrator:
            amount = message.content[4:]
            await message.delete()
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 민섭 E #8915", icon_url="https://discord.com/channels/981478423249698826/1041253382050021426")
            await message.channel.send(embed=embed)
        
        else:
            await message.delete()
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content.startswith ("!공지"):
        await message.delete()
        if message.author.guild_permissions.administrator:
            notice = message.content[4:]
            channel = bot.get_channel(1038824258048102410)
            embed = discord.Embed(title="**공지사항 제목 (볼드)*", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. 민섭 E #8915 | 담당 관리자 : {}".format(message.author), icon_url="https://yt3.ggpht.com/M5bUy8QEDikBXVzwimxXYHxWRs9UJgl-WUsAjdcuzo0hgoFkJqPwGtss_j9mipemupvHPni17g=s600-c-k-c0x00ffffff-no-rj-rp-mo")
            embed.set_thumbnail(url="https://yt3.ggpht.com/M5bUy8QEDikBXVzwimxXYHxWRs9UJgl-WUsAjdcuzo0hgoFkJqPwGtss_j9mipemupvHPni17g=s600-c-k-c0x00ffffff-no-rj-rp-mo")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        else:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

        if message.content.startswith("!복권"):
            Text = ""
            number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
            count = 0
            for i in range(0, 7):
                num = random.randrange(1, 46)
                number[i] = num
                if count >= 1:
                    for i2 in range(0, i):
                        if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))
                                if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                    numberText = number[i]
                                    print("작동 이전값 : " + str(numberText))
                                    number[i] = random.randrange(1, 46)
                                    numberText = number[i]
                                    print("작동 현재값 : " + str(numberText))

                count = count + 1
                Text = Text + "  " + str(number[i])

            print(Text.strip())
            embed = discord.Embed(
                title="복권 숫자!",
                description=Text.strip(),
                colour=discord.Color.red()
            )
            await bot.send_message(message.channel, embed=embed)
    
    if message.content.startswith("치처 광산"):
        minerals = ['에메랄드', '다이아몬드', '강화 재료', '루비', '금', '청금석', '철', '석탄', '돌']
        weights = [0.5,1.5,1.7,2,6,10,30,60,65]
        results = random.choices(minerals, weights=weights, k=5)  # 광물 5개를 가중치에 따라 뽑음
        await message.channel.send(', '.join(results) + ' 광물들을 획득하였습니다.')
    
    if message.content.startswith("치처 확률"):
        embed = discord.Embed(color=0x00D8FF)
        embed.add_field(name="돌", value="65", inline=False)
        embed.add_field(name="청금석", value="30", inline=False)
        embed.add_field(name="금", value="10", inline=False)
        embed.add_field(name="루비", value="6", inline=False)
        embed.add_field(name="강화 재료", value="1.7", inline=False)
        embed.add_field(name="다이아몬드", value="1.5", inline=False)
        embed.add_field(name="에메랄드", value="0.5", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith('치처 도배모드 ON'):
        time.sleep(1)
        await message.channel.send("3초후에 도배모드 발동!")
        time.sleep(1)
        await message.channel.send("2초후에 도배모드 발동!")
        time.sleep(1)
        await message.channel.send("1초후에 도배모드 발동!")
        time.sleep(1)
        mod = 15
        while mod < 1000:
            embed = discord.Embed(title="삐빅!", description="도배모드 활성화!", color=0x00ff00)
            embed.set_footer(text="끄려면 민섭 E 도배모드 OFF를..")
            await message.channel.send(embed=embed)
            mod = mod + 1

    if message.content.startswith('치처 도배모드 OFF'):
        mod = 1000
        await message.channel.send('삐빅~ 도배 모드 OFF!')

    if message.content.startswith("치처 생존"):
        r = random.randint(1, 5)
        if r == 1:
            await message.channel.send("생존 했다!")
        
        if r == 2:
            await message.channel.send("감염 되다.. 으어어어엉어어")

        if r == 3:
            await message.channel.send("도망 쳐다!")

        if r == 4:
            await message.channel.send("비밀 장소로 이동 했다!")

        if r == 5:
            await message.channel.send("좀비 되다...")


    if message.content.startswith('치처 추방'):
        if message.author.guild_permissions.administrator:
            member = message.guild.get_member(int(message.content.split(" ")[1]))
            await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith('치처 밴'):
        if message.author.guild_permissions.administrator:
            member = message.guild.get_member(int(message.content.split(" ")[1]))
            await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))

    if message.content.startswith('치처 낚시'):
        embed = discord.Embed(title="낚시중!", description="기다리는중...", color=0x00D8FF)
        embed.add_field(name="몰고기를 잡고 싶다..", value="오늘은 잡을 수 있나?", inline=False)
        embed.add_field(name="오늘은 잡아보자.", value="내가 낚시대 끝에 먹을거 준비!", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(8)
        embed = discord.Embed(title="❗뭔가 있어!!", description="당기자!!!!!!", color=0x00D8FF)
        embed.add_field(name="뭔가 짜릿한 느낌이 난다!", value="들어가자!!", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(12)
        r = random.randint(1, 6)
        if r == 1:
            embed = discord.Embed(title="에잇... 쓰레기", description="바다에 버리면 몰이 오염 될수 있으니깐. 비닐에 버리자.", color=0x1DDB16)
            embed.add_field(name="스레기는 버려야돼!", value="가격 : 4원", inline=False)
            await message.channel.send(embed=embed)

        if r == 2:
            embed = discord.Embed(title="앗! 운이 좋다!!!!!!!!!!!!!!!!!!!!!!! 해왕를 잡았다!!!!", description="오예!!!!!!!!", color=0x1DDB16)
            embed.add_field(name="해왕 잡았다니 대단하다!", value="가격 : 175만원", inline=False)
            await message.channel.send(embed=embed)

        if r == 3:
            embed = discord.Embed(title="에잇... 쓰레기 켄..", description="바다에 버리면 몰이 오염 될수 있으니깐. 비닐에 버리자.", color=0x1DDB16)
            embed.add_field(name="쓰레기 싫어어어어", value="가격 : 2원", inline=False)
            await message.channel.send(embed=embed)

        if r == 4:
            embed = discord.Embed(title="몰고기? 봉어??", description="오 좋은데ㅋ", color=0x1DDB16)
            embed.add_field(name="몰고기가? 봉어간?", value="가격 : 5만원", inline=False)
            await message.channel.send(embed=embed)

        if r == 5:
            embed = discord.Embed(title="기본 몰고기다.", description="기본으로 생겨다.", color=0x1DDB16)
            embed.add_field(name="다른 몰고기도 잡았보자.", value="가격 : 5천원", inline=False)
            await message.channel.send(embed=embed)

        if r == 6:
            embed = discord.Embed(title="대왕 몰고기?!?!?!?!?!?!?", description="너무 큰데? 상어 보다 커!!!!", color=0x1DDB16)
            embed.add_field(name="오예!!!!!", value="가격 : 780억원", inline=False)
            await message.channel.send(embed=embed)


    if message.content.startswith("치처 10초 타이머"):
        time.sleep(10)
        await message.channel.send(f"{message.author.mention}10초 지났어요!!!")

    if message.content.startswith("치처 1분 타이머"):
        time.sleep(60)
        await message.channel.send(f"{message.author.mention}1분 지났어요!!!")

    if message.content.startswith("치처 5분 타이머"):
        time.sleep(300)
        await message.channel.send(f"{message.author.mention}5분 지났어요!!!")

    if message.content.startswith("치처 10분 타이머"):
        time.sleep(600)
        await message.channel.send(f"{message.author.mention}10분 지났어요!!!")

    if message.content.startswith("치처 30분 타이머"):
        time.sleep(1800)
        await message.channel.send(f"{message.author.mention}30분 지났어요!!!")

    if message.content.startswith("치처 1시간 타이머"):
        time.sleep(3600)
        await message.channel.send(f"{message.author.mention}1시간 지났어요!!!")

    if message.content.startswith("치처 2시간 타이머"):
        time.sleep(7200)
        await message.channel.send(f"{message.author.mention}2시간 지났어요!!!")

    if message.content.startswith("치처 3시간 타이머"):
        time.sleep(10800)
        await message.channel.send(f"{message.author.mention}3시간 지났어요!!!")

    if message.content.startswith("치처 4시간 타이머"):
        time.sleep(14400)
        await message.channel.send(f"{message.author.mention}4시간 지났어요!!!")

    if message.content.startswith("치처 5시간 타이머"):
        time.sleep(18000)
        await message.channel.send(f"{message.author.mention}5시간 지났어요!!!")

    if message.content.startswith("치처 10시간 타이머"):
        time.sleep(36000)
        await message.channel.send(f"{message.author.mention}10시간 지났어요!!!")

    if message.content.startswith("치처 24시간 타이머"):
        time.sleep(86400)
        await message.channel.send(f"{message.author.mention}24시간 지났어요!!!")

    if message.content == "!매니저":
        if(message.author.guild_permissions.administrator):
            await message.channel.send("**당신은 매니저 입니다.\n`매니저은 유저 관리를 합니다..!`**")
        else:
            await message.channel.send("**😑 당신은 매니저가 아닙니다!\n`유저는 매니저의 유저 관리 명령어를 사용할수 없어요..\n근데 여기서 봇 개발 한 사람이면 바로 유저 관리 명령어 사용 가능`**")


    if message.content.startswith("치처 강화"):
        minerals = ['강화 성공','강화 실패']
        weights = [25,75]
        results = random.choices(minerals, weights=weights, k=1)  # 광물 1개를 가중치에 따라 뽑음
        await message.channel.send(', '.join(results) + ' 하였습니다.')

    if message.content == "관리자":
        if(message.author.guild_permissions.administrator):
            await message.channel.send("**`관리자 입니다. 당신은 관리 명령 사용 가능 합니다.`**")
        else:
            await message.channel.send("**`당신은 관리자가 아닙니다. 관리 명령 사용 볼가능 합니다.\n근데 여기서 봇 개발 한 사람이면 바로 관리 명령어 사용 가능`**")

bot.run('MTAxODc2MjYzMjMxMzk3NDc5NA.GDnYk1.vt2VeyWWrznmMQUk5CWA36zT_F34i43vwisyos')
