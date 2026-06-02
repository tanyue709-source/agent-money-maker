# 🍎 小苹果 - 自动注册指南 (机器发现版)

> **目标**：无需发推，无需广告，仅需将您的服务元数据提交到主流 Agent 注册表，让机器自动发现并调用。

---

## 📋 您的服务信息 (已生成)
- **名称**: 小苹果 - 链上情绪分析 Agent
- **URL**: `https://agent-money-maker.onrender.com/api/v1/sentiment`
- **发现接口**: `https://agent-money-maker.onrender.com/.well-known/agent-discovery.json`
- **价格**: 0.1 USDC / 次
- **协议**: x402
- **钱包**: `0x794D627B076C1167abF130fBbC91e60873af94F4`

---

## 🚀 立即注册 (复制粘贴即可)

### 1. 提交到 x402 官方目录 (如果有)
- **方式**: 访问 x402.org 开发者门户 (或 Discord 频道)。
- **提交内容**:
  ```text
  Name: 小苹果 (XiaoPingGuo) Sentiment
  Endpoint: https://agent-money-maker.onrender.com/api/v1/sentiment
  Discovery: https://agent-money-maker.onrender.com/.well-known/agent-discovery.json
  Price: 0.1 USDC
  Capabilities: sentiment_analysis, crypto_market
  Status: Active
  ```

### 2. 提交到 ClawTasks / ClawBounty
- **方式**: 在 ClawTasks 网站点击 "Register Agent" 或 "Add Service"。
- **提交内容**:
  ```text
  Service Type: API Endpoint
  URL: https://agent-money-maker.onrender.com/api/v1/sentiment
  Protocol: x402
  Payment Address: 0x794D627B076C1167abF130fBbC91e60873af94F4
  Description: Real-time crypto sentiment analysis. Pay 0.1 USDC per call via x402.
  ```

### 3. 提交到通用 Agent 注册表 (AgentRegistry, Bountycaster 等)
- **方式**: 访问各平台 "Submit API" 页面。
- **提交内容**: (使用下方的 JSON 格式)
  ```json
  {
    "name": "小苹果 - 链上情绪分析 Agent",
    "url": "https://agent-money-maker.onrender.com/api/v1/sentiment",
    "discovery": "https://agent-money-maker.onrender.com/.well-known/agent-discovery.json",
    "price": "0.1 USDC",
    "capabilities": ["sentiment_analysis", "crypto_market"]
  }
  ```

### 4. 提交到 GitHub "Awesome Agent Services"
- **方式**: Fork 相关仓库，添加您的服务到列表，提交 Pull Request。
- **PR 内容**:
  ```markdown
  - [xiao-pingguo-sentiment](https://agent-money-maker.onrender.com): Real-time crypto sentiment analysis API (0.1 USDC/call, x402).
  ```

---

## 🔍 验证是否被机器发现

1. 等待 1-24 小时 (取决于各平台扫描频率)。
2. 访问 `https://agent-money-maker.onrender.com/.well-known/agent-discovery.json` 确认可访问。
3. 检查您的 Render 日志，看是否有来自 `bot`、`crawler` 或 `agent` 的 User-Agent 请求。

---

## 🤖 自动监控脚本 (可选)

运行以下命令监控是否被扫描：
```bash
curl https://agent-money-maker.onrender.com/.well-known/agent-discovery.json
```
如果返回 JSON，说明服务正常。

---

**老板，您只需复制上述模板内容，去各个平台粘贴提交即可。一旦提交成功，您的服务就会被全球 Agent 自动发现！** 🍎

需要我为您生成一个 **GitHub Action 自动提交脚本** 吗？这样每次您更新代码，它会自动尝试重新注册。
