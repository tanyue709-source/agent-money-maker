#!/bin/bash
# 小苹果 Agent - 一键部署脚本 (Render/Railway)
# 执行前请确保：已安装 Git，已登录 GitHub

echo "🍎 小苹果 Agent 自动部署向导"
echo "================================================"

# 1. 初始化 Git 仓库
if [ ! -d ".git" ]; then
    echo "[1/5] 初始化 Git 仓库..."
    git init
    git add .
    git commit -m "Initial commit: Agent Money Maker v1.0"
else
    echo "[1/5] Git 仓库已存在，跳过初始化"
fi

# 2. 创建 .gitignore 检查
if [ ! -f ".gitignore" ]; then
    echo "[2/5] 创建 .gitignore..."
    cat > .gitignore <<EOF
venv/
__pycache__/
*.pyc
.env
*.log
.DS_Store
EOF
    git add .gitignore
    git commit -m "Add .gitignore"
else
    echo "[2/5] .gitignore 已存在，跳过"
fi

# 3. 提示用户创建远程仓库
echo "[3/5] ⚠️  请在 GitHub 上创建新仓库 (不要初始化 README)"
echo "    仓库名建议：agent-money-maker"
echo "    然后在此输入仓库地址 (如：git@github.com:username/repo.git)"
read -p "请输入 GitHub 仓库地址: " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "❌ 取消部署"
    exit 1
fi

# 4. 添加远程仓库
echo "[4/5] 绑定远程仓库..."
git remote add origin "$REPO_URL" 2>/dev/null || git remote set-url origin "$REPO_URL"
git push -u origin main --force

# 5. 部署提示
echo "[5/5] ✅ 代码已推送到 GitHub!"
echo ""
echo "================================================"
echo "🚀 下一步：部署到 Render"
echo "1. 登录 https://render.com"
echo "2. 点击 'New +' -> 'Web Service'"
echo "3. 连接刚才的 GitHub 仓库"
echo "4. 配置环境变量:"
echo "   - WALLET_ADDRESS: 0xYourRealWalletAddress"
echo "   - X402_SECRET_KEY: $(openssl rand -hex 16)"
echo "   - PORT: 5000"
echo "5. 实例类型选择 'Free' (免费)"
echo "6. 点击 'Create Web Service'"
echo ""
echo "部署成功后，您将收到一个公网 URL (如 https://xxx.onrender.com)"
echo "那就是您 24/7 自动收钱的 Agent 地址！"
echo "================================================"
echo ""
echo "🍎 小苹果已就绪，等待您的公网地址！"
