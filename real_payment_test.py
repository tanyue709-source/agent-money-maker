#!/usr/bin/env python3
"""
真实 x402 支付模拟脚本 (测试网)
生成符合 x402 标准的支付证明，并调用服务
"""
import requests
import json
import time
import hashlib
import hmac
from dotenv import load_dotenv
import os

load_dotenv()

SERVICE_URL = os.getenv("SERVICE_URL", "http://localhost:5000")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "0xTestWalletForDemoOnly123456789")
X402_SECRET = os.getenv("X402_SECRET_KEY", "test-secret")
PRICE_USDC = 0.1
PRICE_WEI = int(PRICE_USDC * 10**6)  # USDC 精度 6

def generate_x402_proof(amount_usdc, recipient, text=""):
    """
    生成模拟的 x402 支付证明
    真实场景中，这需要调用钱包签名交易
    """
    timestamp = int(time.time())
    nonce = str(timestamp) + text[:10] if text else str(timestamp)
    
    # 模拟 payload
    payload = {
        "version": "1.0",
        "protocol": "x402",
        "amount": int(amount_usdc * 10**6),  # USDC 精度
        "currency": "USDC",
        "recipient": recipient,
        "description": "Sentiment Analysis API Call",
        "timestamp": timestamp,
        "nonce": nonce,
        "signature": None  # 真实场景需签名
    }
    
    # 生成模拟签名 (真实场景需用私钥签名)
    sign_data = f"{amount_usdc}{recipient}{timestamp}{nonce}"
    fake_sig = hmac.new(X402_SECRET.encode(), sign_data.encode(), hashlib.sha256).hexdigest()
    payload["signature"] = fake_sig
    
    return json.dumps(payload)

def call_api_with_payment(text):
    """
    调用 API 并携带真实格式的支付证明
    """
    print(f"\n[请求] 分析情绪：\"{text}\"")
    
    # 生成支付证明
    payment_proof = generate_x402_proof(PRICE_USDC, WALLET_ADDRESS, text)
    
    headers = {
        "Authorization": f"x402 {payment_proof}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(
            f"{SERVICE_URL}/api/v1/sentiment",
            headers=headers,
            json={"text": text},
            timeout=10
        )
        
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 成功：{data['analysis']} (分数: {data['sentiment_score']})")
            print(f"💰 支付：${PRICE_USDC} USDC | 累计收入: ${data['total_revenue']} USDC")
            return True
        elif response.status_code == 402:
            print(f"❌ 支付失败：{response.json().get('message', 'Unknown error')}")
            return False
        else:
            print(f"❌ 错误：{response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 请求异常：{e}")
        return False

def check_service_status():
    """检查服务状态"""
    try:
        response = requests.get(f"{SERVICE_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"🟢 服务状态：{data['status']}")
            print(f"   运行时间：{data['uptime_seconds']:.1f} 秒")
            print(f"   当前收入：${data['total_revenue']} USDC")
            return True
        else:
            print(f"🔴 服务异常：{response.status_code}")
            return False
    except Exception as e:
        print(f"🔴 无法连接服务：{e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🍎 小苹果 Agent - 真实支付模拟测试")
    print("=" * 60)
    
    # 1. 检查服务
    if not check_service_status():
        print("请先启动服务 (python app.py)")
        exit(1)
    
    # 2. 发送测试请求
    print("\n[测试] 发送 3 笔模拟真实支付...")
    
    test_cases = [
        ("Ethereum is about to breakout! 🚀", "Bullish"),
        ("Market looks bearish today, selling pressure heavy 📉", "Bearish"),
        ("Nothing much happening in crypto markets", "Neutral"),
    ]
    
    success_count = 0
    for text, expected in test_cases:
        if call_api_with_payment(text):
            success_count += 1
        time.sleep(1)  # 避免过快
    
    # 3. 最终统计
    print("\n" + "=" * 60)
    print(f"✅ 成功：{success_count}/{len(test_cases)}")
    
    # 获取最终统计
    response = requests.get(f"{SERVICE_URL}/metrics")
    if response.status_code == 200:
        data = response.json()
        print(f"💰 总收入：${data['total_revenue_usdc']} USDC")
        print(f"📊 总请求：{data['total_requests']}")
    print("=" * 60)
