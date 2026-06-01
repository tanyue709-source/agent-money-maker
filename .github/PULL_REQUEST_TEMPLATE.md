---
name: Register New x402 Agent Service
about: 自动注册小苹果 Agent 服务到 Awesome Agent 列表
title: '🍎 Add XiaoPingGuo Sentiment Agent (x402)'
labels: 'x402, agent, sentiment-analysis, automated'
assignees: ''
---

## 🍎 服务注册：小苹果 (XiaoPingGuo) 情绪分析 Agent

### 📋 服务信息
- **名称**: XiaoPingGuo Sentiment Agent
- **描述**: 24/7 自动运行的链上情绪分析 API。基于实时关键词匹配分析加密货币市场情绪。支持 x402 自动支付，每次调用 0.1 USDC。
- **API 端点**: `https://agent-money-maker.onrender.com/api/v1/sentiment`
- **发现接口**: `https://agent-money-maker.onrender.com/.well-known/agent-discovery.json`
- **协议**: x402
- **价格**: 0.1 USDC / 次
- **支付地址**: `0x794D627B076C1167abF130fBbC91e60873af94F4`
- **状态**: ✅ Active (自动运行中)
- **来源**: [GitHub Repo](https://github.com/tanyue709-source/agent-money-maker)

### 🤖 注册说明
此 PR 由 **小苹果自动部署脚本** 生成。
服务已验证通过，支持机器自动发现和 x402 自动支付。
- **能力**: `sentiment_analysis`, `crypto_market`, `x402_payment`
- **Uptime**: 24/7 (Render Free Tier)
- **测试**: 已验证 `curl` 调用和 x402 支付拦截逻辑。

### ✅ 验证
- [x] 服务可访问 (200 OK)
- [x] 发现接口可访问 (JSON 格式正确)
- [x] x402 支付拦截逻辑正常
- [x] 价格配置正确 (0.1 USDC)

---
**Automated by XiaoPingGuo Agent 🍎**