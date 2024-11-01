
from nonebot import on_command
from nonebot.internal.params import ArgStr
from nonebot.matcher import Matcher
# from nonebot.params import CommandArg
from nonebot_plugin_saa import Image, Text, MessageFactory, SaaTarget

from ..command.common import CommandRegistry
from ..model import plugin_config, CommandUsage
from ..utils.common import PLUGIN, COMMAND_BEGIN, logger, get_last_command_sep

__all__ = ["helper"]

helper = on_command(
    f"{plugin_config.preference.command_start}帮助",
    priority=1,
    aliases={f"{plugin_config.preference.command_start}help"},
    block=True
)

CommandRegistry.set_usage(
    helper,
    CommandUsage(
        name="帮助",
        description="🍺欢迎使用米游社小助手帮助系统！\n"
                    "{HEAD}帮助 ➢ 查看米游社小助手使用说明\n"
                    "{HEAD}帮助 <功能名> ➢ 查看目标功能详细说明"
    )
)


@helper.handle()
async def handle_helper(matcher: Matcher):
    """
    主命令触发
    """
    try:
        # 创建消息工厂
        reply = MessageFactory(
            Text(
                f"{PLUGIN.metadata.name}"
                f"{PLUGIN.metadata.description}\n"
                "具体用法：\n"
                f"{PLUGIN.metadata.usage.format(HEAD=COMMAND_BEGIN)}"
            ))
        await reply.send(reply=True)
        await helper.finish()
        # await matcher.finish(
        #     f"{PLUGIN.metadata.name}"
        #     f"{PLUGIN.metadata.description}\n"
        #     "具体用法：\n"
        #     f"{PLUGIN.metadata.usage.format(HEAD=COMMAND_BEGIN)}"
        # )
    except Exception as e:
        logger.exception(f"错误：{e}")


@helper.got('content')
async def _(content=ArgStr()):
    """
    二级命令触发。功能详细说明查询
    """
    # 相似词
    if content == '登陆':
        content = '登录'

    matchers = PLUGIN.matcher
    for matcher in matchers:
        try:
            command_usage = CommandRegistry.get_usage(matcher)
            if command_usage and content.lower() == command_usage.name:
                description_text = command_usage.description or ""
                usage_text = f"\n\n{command_usage.usage}" if command_usage.usage else ""
                finish_text = f"『{COMMAND_BEGIN}{command_usage.name}』- 使用说明\n{description_text}{usage_text}"
                await helper.finish(
                    finish_text.format(
                        HEAD=COMMAND_BEGIN,
                        SEP=get_last_command_sep()
                    )
                )
        except AttributeError:
            continue
    await helper.finish("⚠️未查询到相关功能，请重新尝试")
