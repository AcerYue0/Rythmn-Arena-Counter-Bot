import discord
from discord.ext import commands

# 設置意圖 (Intents)
intents = discord.Intents.default()
intents.message_content = True

# 創建 Bot 實例並設置命令前綴
bot = commands.Bot(command_prefix="!", intents=intents)

# 判斷質數的函數
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 反應邏輯的配置
reactions = {
    "is_prime": {
        "check": is_prime,
        "emoji": "<:Prime:1284068466457837568>"
    },
    "is_palindromes": {
        "check": lambda n: str(n) == str(n)[::-1],
        "emoji": "<:ReviveR:1284070970125979720>"
    },
    "multiple_of_573": {
        "check": lambda n: n % 573 == 0,
        "emoji": "<:Konami:1284067440296198144>"
    },
    "multiple_of_666": {
        "check": lambda n: n % 666 == 0,
        "emoji": "<:SAtAN:1284070140669071402>"
    },
    "ends_with_69": {
        "check": lambda n: str(n).endswith("69"),
        "emoji": "♋"
    },
    "ends_with_666": {
        "check": lambda n: str(n).endswith("666"),
        "emoji": "<:666:1284069330509893662>"
    },
    "ends_with_777": {
        "check": lambda n: str(n).endswith("777"),
        "emoji": "🎰"
    }
}

# 當收到訊息時觸發事件
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 檢查訊息是否為數字
    if message.content.isdigit():
        number = int(message.content)
        
        # 檢查每個反應邏輯並添加反應
        for reaction in reactions.values():
            if reaction["check"](number):
                await message.add_reaction(reaction["emoji"])

    await bot.process_commands(message)

# 你的 Discord Bot Token (請替換為你的實際 Token)
bot.run('ap-LuLF7Bf9tqkHOziyhMexbY2SIvoi_')