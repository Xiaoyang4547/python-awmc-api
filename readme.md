# Python AWMC API

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

这是一个用于与 [**AWMC**](https://api.wmc.pub/) 公共 API 交互的非官方 Python 客户端库。它封装了认证、用户数据查询、充值等核心接口，方便开发者通过 Python 脚本管理街机游戏数据。

## ✨ 功能

*   **服务健康检查**：验证 API 服务状态和 Token 有效性。
*   **用户数据查询**：获取玩家的详细资料，包括 ID、Rating、段位、收藏品、游玩统计等。
*   **充值倍率票**：为玩家添加 2倍、3倍 或 5倍 经验/货币票。
*   **数据更新接口**：提供了 `update-lx` 等后端数据同步功能的封装（具体用途需结合服务端）。

## 🚀 快速开始

### 1. 初始化与健康检查

所有函数都需要一个有效的 `token`（Bearer 令牌）。首先检查服务状态：

```python
import awmc

# 替换为你的有效令牌
YOUR_TOKEN = "your_api_token_here"

# 检查服务健康状态
awmc.health(YOUR_TOKEN)
# 输出示例: ok
```

### 2. 查询用户数据

使用二维码（或用户标识）查询玩家的完整数据：

```python
# 查询用户信息
qrcode = "user_qrcode_or_id"
awmc.userdata(YOUR_TOKEN, qrcode)
```

该函数会打印出结构化的用户信息，包括：
- **基本信息**：用户ID、名称、封禁状态
- **Rating数据**：总Rating、B35 Rating、B15 Rating
- **段位与收藏**：段位等级、头像、姓名框、背景、称号、搭档
- **旅行伙伴**：全部5个伙伴的ID
- **游玩统计**：总游玩次数、DX分数
- **版本与日期**：首次/最后游玩版本、登录/游玩时间等

### 3. 添加倍率票

为指定用户添加经验/货币倍率票：

```python
# chargeId: 2=2倍票, 3=3倍票, 5=5倍票
awmc.ticket(YOUR_TOKEN, qrcode, chargeId=3)
```

### 4. 数据更新接口 (高级)

以下函数用于后端数据同步或特定更新，参数 `key` 或 `token` 的含义需参考服务端文档：

```python
# 更新 LX 数据
awmc.updatelx(YOUR_TOKEN, qrcode, key="some_key")

# 更新 Maiu 数据 (实际调用的是 update-lx 接口)
awmc.maiulx(YOUR_TOKEN, qrcode, key="some_key")

# 更新 Fish 数据 (使用 token 参数)
awmc.updatefish(YOUR_TOKEN, qrcode, key="some_token")

# 更新 Maiu 数据 (使用 token 参数)
awmc.maiu(YOUR_TOKEN, qrcode, key="some_token")
```

> **注意**：`updatelx` 和 `maiulx` 函数体内均调用 `/v1/update-lx` 接口，`updatefish` 和 `maiu` 函数体内均调用 `/v1/update-lx` 接口，但参数名（`key` 或 `token`）不同，请根据实际场景选用。

## 📚 API 参考

| 函数 | 参数 | 描述 |
| :--- | :--- | :--- |
| `health(token)` | `token`: 认证令牌 | 检查 API 服务状态。 |
| `userdata(token, qrcode)` | `qrcode`: 用户二维码字符 | 获取并打印用户完整数据。 |
| `ticket(token, qrcode, chargeId)` | `chargeId`: 2, 3, 或 5 | 为玩家添加倍率票。 |
| `updatelx(token, qrcode, key)` | `key`: 落雪个人 API 密钥 | 调用 `/v1/update-lx` 接口。 |
| `maiulx(token, qrcode, key)` | `key`: 落雪个人 API 密钥 | 同 `updatelx`。 |
| `updatefish(token, qrcode, key)` | `key`: 水鱼Token | 调用 `/v1/update-lx` 接口，参数名不同。 |
| `maiu(token, qrcode, key)` | `key`: 水鱼Token | 同 `updatefish`。 |

## ⚠️ 注意事项

*   本库为**非官方**实现，请遵守 AWMC 服务的使用条款。
*   所有 API 请求需要有效的 Bearer Token，请妥善保管。
*   函数中 `userdata` 的封禁状态（`banState`）值 `1` 和 `2` 的含义是基于代码猜测的，可能与实际服务定义有出入。
*   部分接口（如 `update-lx`）的具体业务逻辑需结合服务端理解。
*   更多API用法请参考[AWMC API文档](https://wiki.awmc.team/dev/awmc-api)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request。请确保您的代码与现有风格一致，并清晰描述改动目的。

## 📄 许可证

本项目使用 **GNU General Public License v3.0** 授权。详情请见 [LICENSE](LICENSE) 文件。
