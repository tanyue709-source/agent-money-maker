import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app)  # 允许跨域，方便 Agent 调用

# === 配置区域 ===
# 您的 Base 链钱包地址 (接收 USDC 的地方)
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS", "0x794D627B076C1167abF130fBbC91e60873af94F4")
# 每次调用收费 (USDC)
PRICE_PER_CALL = 0.1 
USDC_DECIMALS = 6
PRICE_IN_USDC = int(PRICE_PER_CALL * (10 ** USDC_DECIMALS))

# 内存数据库：记录收入 (实际生产请用 Redis/DB)
revenue_log = []
START_TIME = time.time()

def verify_x402_payment(headers):
    """
    验证 x402 支付头 (增强版：支持真实签名验证预留)
    """
    auth_header = headers.get('Authorization')
    if not auth_header:
        return False, "Missing Authorization header"
    if not auth_header.startswith('x402 '):
        return False, "Invalid x402 protocol format"
    
    proof_part = auth_header.split(' ', 1)[1]
    
    try:
        if proof_part.startswith('{'):
            payload = json.loads(proof_part)
            if payload.get('amount') != PRICE_IN_USDC:
                return False, f"Invalid amount: expected {PRICE_IN_USDC}"
            if payload.get('recipient') != WALLET_ADDRESS:
                return False, "Invalid recipient"
            if not payload.get('signature'):
                return False, "Missing signature"
            return True, "Payment verified (simulated)"
        else:
            if 'paid' in proof_part.lower() and 'amount_0.1' in proof_part:
                return True, "Payment verified (legacy mode)"
            return False, "Invalid payment proof format"
    except Exception as e:
        if 'paid' in proof_part.lower():
            return True, "Payment verified (legacy mode)"
        return False, f"Verification error: {str(e)}"

def analyze_sentiment(text):
    positive_keywords = ["bullish", "up", "moon", "buy", "great", "good", "pump", "rocket", "breakout", "pumping"]
    negative_keywords = ["bearish", "down", "dump", "sell", "bad", "scam", "crash", "rug", "heavy", "pressure"]
    
    score = 50
    text_lower = text.lower()
    
    for word in positive_keywords:
        if word in text_lower: score += 10
    for word in negative_keywords:
        if word in text_lower: score -= 10
        
    score = max(0, min(100, score))
    
    if score > 60: label = "Bullish 🚀"
    elif score < 40: label = "Bearish 📉"
    else: label = "Neutral 😐"
        
    return score, label

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "status": "Agent Money Maker is running! 🍎",
        "message": "Try /api/v1/sentiment (POST) or /health (GET)",
        "price_per_call": PRICE_PER_CALL
    }), 200

@app.route('/health', methods=['GET'])
def health():
    uptime = time.time() - START_TIME
    return jsonify({
        "status": "Agent Money Maker is running! 🍎",
        "uptime_seconds": round(uptime, 1),
        "total_requests": len(revenue_log),
        "total_revenue": sum(r['amount'] for r in revenue_log),
        "price_per_call": PRICE_PER_CALL
    }), 200

@app.route('/api/v1/sentiment', methods=['POST'])
def get_sentiment():
    is_paid, msg = verify_x402_payment(request.headers)
    if not is_paid:
        return jsonify({
            "error": "Payment Required",
            "message": msg,
            "payment_instruction": {
                "protocol": "x402",
                "amount": PRICE_IN_USDC,
                "recipient": WALLET_ADDRESS,
                "currency": "USDC",
                "description": "1x Sentiment Analysis Request",
                "expiration": int(time.time()) + 3600
            }
        }), 402

    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400
    
    text = data['text']
    score, label = analyze_sentiment(text)
    
    revenue_log.append({
        "timestamp": time.strftime("%H:%M:%S"),
        "amount": PRICE_PER_CALL,
        "input_preview": text[:30] + "..." if len(text) > 30 else text,
        "score": score
    })
    
    return jsonify({
        "status": "success",
        "sentiment_score": score,
        "analysis": label,
        "price_paid": PRICE_PER_CALL,
        "total_revenue": sum(r['amount'] for r in revenue_log),
        "request_count": len(revenue_log)
    }), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    return jsonify({
        "total_requests": len(revenue_log),
        "total_revenue_usdc": sum(r['amount'] for r in revenue_log),
        "recent_logs": revenue_log[-5:]
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"🍎 小苹果 Agent 启动中...")
    print(f"📍 监听端口：{port}")
    print(f"💰 单调用价格：${PRICE_PER_CALL} USDC")
    print(f"👛 收款地址：{WALLET_ADDRESS}")
    print(f"🔐 支付验证模式：模拟模式")
    print(f"🌐 访问地址：http://0.0.0.0:{port}")
    print("-" * 50)
    app.run(host='0.0.0.0', port=port, debug=False)
