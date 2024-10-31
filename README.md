# nonebot-plugin-myhoyotool

_✨ 米哈游任务小助手 - NoneBot 插件  ✨_

一个基于nonebot2的米哈游工具，支持米哈游游戏签到、账号管理等工具。

> [!NOTE]
> 模板库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

<details>
<summary>配置发布工作流</summary>

1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，打开 [Actions secrets and variables](./settings/secrets/actions) 页面。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

</details>

> [!IMPORTANT]
> 这个发布工作流需要 pyproject.toml 文件, 并且只支持 [PEP 621](https://peps.python.org/pep-0621/) 标准的 pyproject.toml 文件

<details>
<summary>触发发布工作流</summary>
从本地推送任意 tag 即可触发。

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

</details>

## 📖 介绍

一个基于nonebot2的 签到工具，专门为了兼容tg bot而重写的插件。

参考源码：
- [nonebot-plugin-mystool](https://github.com/Ljzd-PRO/nonebot-plugin-mystool)
- [nonebot-plugin-batarot](https://github.com/Perseus037/nonebot_plugin_batarot)


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-myhoyotool

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-myhoyotool
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-myhoyotool
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-myhoyotool
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-myhoyotool
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| HOST  | 否 | `127.0.0.1` | nonebot配置的host，和本插件无瓜，可以改成 `0.0.0.0` |
| PORT  | 否 | `8080` | nonebot配置的port，和本插件无瓜 |
| [适配器参数]  | 否 | 无 | 根据适配器文档说明去配置 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| /help | 所有人 | 否 | 私聊 | 帮助说明 |

### 效果图

[TODO]

插件商店： https://nonebot.dev/store/plugins

