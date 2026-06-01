#!/usr/bin/env python3
"""
模拟外部 Agent 调用并支付 USDC (x402 模拟)
运行此脚本测试您的服务是否正常工作
"""
import requests
import json
import time

SERVICE_URL = "http://localhost:5000"

def test_no_payment():
    """测试：未支付应返回 402"""
    print("\n[测试 1] 未支付请求 (应返回 402)...")
    response = requests.post(f"{SERVICE_URL}/api/v1/sentiment", json={"text": "Bitcoin is going to the moon!"})
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
    assert response.status_code == 402, "应该返回 402"
    print("✅ 通过：正确拦截未支付请求\n")

def test_paid_request():
    """测试：模拟支付后请求 (应返回 200)"""
    print("[测试 2] 模拟支付请求 (应返回 200)...")
    
    # 模拟 x402 支付头 (包含 "paid" 关键字)
    headers = {
        "Authorization": "x402 paid_amount_0.1_usdc_recipient_0xTestWallet",
        "Content-Type": "application/json"
    }
    
    # 测试不同情绪
    test_cases = [
        ("Bitcoin is pumping hard! 🚀", "Bullish"),
        ("This coin is a scam, dumping hard 📉", "Bearish"),
        ("Just another day, nothing special", "Neutral")
    ]
    
    for text, expected_label in test_cases:
        response = requests.post(
            f"{SERVICE_URL}/api/v1/sentiment",
            headers=headers,
            json={"text": text}
        )
        print(f"输入: {text}")
        print(f"状态码: {response.status_code}")
        data = response.json()
        print(f"结果: {data['analysis']} (分数: {data['sentiment_score']})")
        print(f"当前总收入: ${data['total_revenue']} USDC")
        print("-" * 30)
        assert response.status_code == 200, f"应该返回 200，但返回了 {response.status_code}"
        assert data['status'] == 'success', "状态应为 success"
    
    print("✅ 通过：所有付费请求处理成功\n")

def check_metrics():
    """检查服务统计"""
    print("[测试 3] 检查服务统计...")
    response = requests.get(f"{SERVICE_URL}/metrics")
    data = response.json()
    print(f"总请求数: {data['total_requests']}")
    print(f"总收入: ${data['total_revenue_usdc']} USDC")
    print(f"最近日志: {data['recent_logs']}")
    print("✅ 通过：统计正常\n")

def check_health():
    """检查服务健康状态"""
    print("[测试 4] 检查服务健康状态...")
    response = requests.get(f"{SERVICE_URL}/health")
    data = response.json()
    print(f"状态: {data['status']}")
    print(f"运行时间: {data['uptime_seconds']} 秒")
    print(f"总收入: ${data['total_revenue']} USDC")
    print("✅ 通过：服务健康\n")

if __name__ == "__main__":
    print("=" * 60)
    print("🍎 小苹果 Agent 收款测试套件启动")
    print("=" * 60)
    
    try:
        # 1. 检查服务是否运行
        print("\n[准备] 检查服务是否运行...")
        try:
            requests.get(f"{SERVICE_URL}/health", timeout=2)
        except requests.exceptions.ConnectionError:
            print("❌ 错误：服务未运行！请先运行 'python app.py'")
            exit(1)
        print("✅ 服务已运行\n")
        
        # 2. 执行测试
        test_no_payment()
        test_paid_request()
        check_metrics()
        check_health()
        
        print("=" * 60)
        print("🎉 所有测试通过！您的 Agent 已准备好收款！")
        print("💰 当前已收到模拟收入: $", end="")
        response = requests.get(f"{SERVICE_URL}/metrics")
        print(f"{response.json()['total_revenue_usdc']} USDC")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        exit(1)
