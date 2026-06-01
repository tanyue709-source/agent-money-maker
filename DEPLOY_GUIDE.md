# 🚀 一键部署指南：小苹果 Agent (Render/Railway)

## 📋 前置准备
1. **GitHub 账号**：已登录。
2. **Base 链钱包**：MetaMask 或 Coinbase Wallet，已切换至 **Base 主网** 或 **Base 测试网**。
3. **USDC**：准备少量 USDC (主网需真钱，测试网可领测试币)。

---

## 🛠️ 第一步：推送到 GitHub (只需一次)

在终端运行：
```bash
cd /home/mac/.openclaw/workspace/agent-money-maker
./deploy.sh
```
按提示输入您的 GitHub 仓库地址 (如 `git@github.com:yourname/agent-money-maker.git`)。

**如果不想运行脚本，手动操作如下：**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:yourname/agent-money-maker.git
git push -u origin main
```

---

## ☁️ 第二步：部署到 Render (推荐，免费)

1. **登录 Render**：[https://render.com](https://render.com)
2. **新建服务**：点击 `New +` -> `Web Service`
3. **连接仓库**：选择刚才推送的 GitHub 仓库。
4. **配置参数**：
   - **Name**: `agent-money-maker`
   - **Environment**: `Python 3.11` (自动识别)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Instance Type**: `Free` (免费层)

5. **设置环境变量** (点击 "Advanced" 或 "Environment Variables")：
   | Key | Value |
   |---|---|
   | `WALLET_ADDRESS` | 您的真实 Base 钱包地址 (如 `0x123...`) |
   | `X402_SECRET_KEY` | 一个随机安全字符串 (如 `my-super-secret-key-123`) |
   | `PORT` | `5000` |
   | `FLASK_ENV` | `production` (可选) |

6. **点击 "Create Web Service"**。

---

## 🎉 第三步：上线与测试

1. **等待部署**：Render 会自动构建并启动，约 2-5 分钟。
2. **获取 URL**：部署成功后，地址栏会显示您的公网地址，如：
   `https://agent-money-maker-abc123.onrender.com`
3. **测试服务**：
   ```bash
   curl http://localhost:5000/health
   # 替换为实际 URL
   curl https://your-agent.onrender.com/health
   ```
4. **测试收款**：
   使用 `real_payment_test.py`，将 `SERVICE_URL` 改为您的公网地址：
   ```bash
   export SERVICE_URL="https://your-agent.onrender.com"
   python3 real_payment_test.py
   ```

---

## 📊 第四步：监控收入

- **访问监控面板**：`https://your-agent.onrender.com/metrics`
- **查看实时收入**：返回 JSON 包含 `total_revenue_usdc`。
- **Webhook 通知** (可选)：在 Render 设置中配置 Webhook，每次调用后发送通知到您。

---

## 🔐 安全提示

- **私钥保护**：切勿将私钥提交到代码库，仅通过环境变量注入。
- **生产验证**：当前代码使用**模拟验证**。上线前建议接入真实 x402 SDK (见 `app.py` 注释)。
- **速率限制**：Render 免费层有限制，如需高并发，请升级实例。

---

## 🌐 第五步：上架 x402 目录 (可选)

让您的 API 被其他 Agent 自动发现：
1. 访问 [x402 开发者目录](https://x402.org) (或类似平台)。
2. 提交您的 API 信息：
   - **Name**: 小苹果情绪分析
   - **URL**: `https://your-agent.onrender.com/api/v1/sentiment`
   - **Price**: 0.1 USDC
   - **Description**: 实时链上情绪分析，基于 LLM。

---

**恭喜！您现在拥有一个 24/7 自动收钱的 AI 智能体！** 🍎
如有问题，查看 `server.log` 或访问 Render 日志面板。
