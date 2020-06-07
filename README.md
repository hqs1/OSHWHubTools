# OSHWHub自动签到助手
## 简介
这是一个简易的OSHWHub自动签到工具

支持自动保存cookies,无需频繁输入cookies
## 如何使用

### 安装依赖
`pip install requests`

### 首次运行
1. 打开 `https://oshwhub.com/sign_in`
2. 登陆你的账号
3. 按下`F12`,然后刷新页面,找到`sign_in`的`get`请求
4. 在`Request Headers`里找到`cookie`字段,将其复制出来
5. 运行`main.py`输入你复制的`cookie`,即可自动签到

### 使用
直接运行`main.py`即可,程序会自动加载之前保存的cookies

## TODO
- [x] 自动签到
- [ ] 自动获取签到奖励
- [ ] 获取签到天数

