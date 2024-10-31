import nonebot
from nonebot.plugin import PluginMetadata
from nonebot import require

from . import handler as handler

# 定义版本号
__version__ = "v0.1.0"

"""
加载saa插件 提供多适配器支持
:::notice 请勿重复加载saa
"""
require("nonebot_plugin_saa")
require("nonebot_plugin_apscheduler")

_driver = nonebot.get_driver()
_command_begin = list(_driver.config.command_start)[0]

from nonebot_plugin_saa import __plugin_meta__ as saa_plugin_meta

__plugin_meta__ = PluginMetadata(
    name="米哈游任务小助手插件",
    description="米哈游游戏辅助工具-每日米游币任务、游戏签到、商品兑换、免抓包登录等",
    usage=
    f"\n📖 {_command_begin}help or {_command_begin}帮助 ➢ 查看帮助信息"
    f"\n🔐 {_command_begin}登录 ➢ 登录绑定米游社账户"
    f"\n📦 {_command_begin}地址 ➢ 设置收货地址ID"
    f"\n🗓️ {_command_begin}签到 ➢ 手动进行游戏签到"
    f"\n📅 {_command_begin}任务 ➢ 手动执行米游币任务"
    f"\n🛒 {_command_begin}兑换 ➢ 米游币商品兑换相关"
    f"\n🎁 {_command_begin}商品 ➢ 查看米游币商品信息(商品ID)"
    f"\n📊 {_command_begin}原神便笺 ➢ 查看原神实时便笺(原神树脂、洞天财瓮等)"
    f"\n📊 {_command_begin}铁道便笺 ➢ 查看星穹铁道实时便笺(开拓力、每日实训等)"
    f"\n👁️‍🗨️ {_command_begin}wb签到 ➢ 手动进行微博超话签到(每日定时:游戏签到后1h)"
    f"\n👁️‍🗨️ {_command_begin}wb兑换 ➢ 查看微博本期超话签到的兑换码(暂支持原神和星穹铁道)"
    f"\n⚙️ {_command_begin}设置 ➢ 设置是否开启通知、每日任务等相关选项"
    f"\n🔑 {_command_begin}账号设置 ➢ 设置设备平台、是否开启每日计划任务、频道任务"
    f"\n🔔 {_command_begin}通知设置 ➢ 设置是否开启每日米游币任务、游戏签到的结果通知"
    f"\n🖨️ {_command_begin}导出Cookies ➢ 导出绑定的米游社账号的Cookies数据"
    f"\n🖇️ {_command_begin}用户绑定 ➢ 绑定关联其他聊天平台或其他账号的用户数据"
    f"\n🔍 {_command_begin}帮助 <功能名> ➢ 查看目标功能详细说明"
    "\n\n⚠️你的数据将经过机器人服务器，请确定你信任服务器所有者再使用。",

    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/scriptsmay/nonebot-plugin-myhoyotool",
    # 发布必填。

    config=None,
    # 插件配置项类，如无需配置可不填写。

    supported_adapters=saa_plugin_meta.supported_adapters,
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
    extra={"version": __version__}
)


# 防止多进程生成图片时反复调用

from .utils import CommandBegin

_driver.on_startup(CommandBegin.set_command_begin)

# 加载命令

from .command import *

# 加载其他代码

from .api import *
from .model import *
from .utils import *