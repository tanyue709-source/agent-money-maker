# 🍎 小苹果 Agent 变现系统 (v1.0)

**基于 x402 协议的自动收款情绪分析 API**

---

## 🚀 功能亮点

- **自动收款**：集成 x402 协议，外部 Agent 调用需先支付 USDC。
- **情绪分析**：自动分析文本情绪（Bullish/Bearish/Neutral）。
- **零代码部署**：Docker 一键运行，支持 Render/Railway 等云平台。
- **模拟测试**：内置测试脚本，验证收款逻辑。

---

## 🛠️ 快速启动 (本地)

### 1. 安装依赖
```bash
cd agent-money-maker
pip install -r requirements.txt
```

### 2. 配置环境变量
编辑 `.env` 文件（或使用 `.env.example` 复制）：
```bash
WALLET_ADDRESS=0xYourRealWalletAddress
X402_SECRET_KEY=your-secret-key
PORT=5000
```

### 3. 启动服务
```bash
python app.py
```
服务将运行在 `http://localhost:5000`

### 4. 测试收款
```bash
python test_client.py
```
您将看到模拟的支付请求和收入统计。

---

## 🌐 部署到云端 (Render/Railway)

### 方案 A: Render (推荐)
1. 将代码推送到 GitHub 仓库。
2. 登录 [render.com](https://render.com)，创建 **Web Service**。
3. 连接您的 GitHub 仓库。
4. 设置环境变量：
   - `WALLET_ADDRESS`
   - `X402_SECRET_KEY`
   - `PORT=5000`
5. 点击 **Create Web Service**。
6. 部署成功后，您将获得一个 `https://your-app.onrender.com` 地址。

### 方案 B: Railway
1. 连接 GitHub 仓库。
2. 添加环境变量。
3. 一键部署。

---

## 📡 API 文档

### 1. 情绪分析 (需支付)
**POST** `/api/v1/sentiment`

**Headers**:
- `Authorization: x402 paid_amount_0.1_usdc...` (模拟支付头)

**Body**:
```json
{
  "text": "Bitcoin is going to the moon!"
}
```

**响应 (200 OK)**:
```json
{
  "status": "success",
  "sentiment_score": 85,
  "analysis": "Bullish 🚀",
  "price_paid": 0.1,
  "total_revenue": 1.5,
  "request_count": 15
}
```

**响应 (402 Payment Required)**:
```json
{
  "error": "Payment Required",
  "message": "Payment not found or invalid",
  "payment_instruction": {
    "protocol": "x402",
    "amount": 100000,
    "recipient": "0xYourWallet",
    "currency": "USDC",
    "description": "1x Sentiment Analysis Request"
  }
}
```

### 2. 健康检查 (免费)
**GET** `/health`

### 3. 查看统计 (免费)
**GET** `/metrics`

---

## 🔐 安全提示

- **生产环境**：请替换 `.env` 中的真实钱包地址和密钥。
- **x402 验证**：当前为**模拟模式**（仅检查 `paid` 关键字）。生产环境请接入真实的 x402 SDK 验证链上支付状态。
- **私钥管理**：切勿将私钥提交到 GitHub，使用 `.env` 或云平台环境变量。

---

## 📈 下一步计划

1. **接入真实 x402 SDK**：验证链上支付状态。
2. **接入真实 LLM**：用 Ollama 或 HuggingFace 替代关键词匹配。
3. **上架 x402 目录**：让您的 API 被其他 Agent 自动发现。
4. **多语言支持**：扩展支持中文、日文等。

---

**作者**: 小苹果 (🍎)  
**版本**: 1.0.0  
**日期**: 2026-06-01
