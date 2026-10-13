# ResumeBuilder · 简历生成器

纯前端、零后端的本地简历生成器，支持浅色 / 深色主题，所有数据保存在浏览器 `localStorage`，完全离线可用。

## 功能特性

- **八步内容编辑**：基本信息、教育经历、实习经历、项目经历、实践经历、技能、爱好、自定义栏目，边写边预览。
- **本地自动保存**：编辑内容自动存入浏览器，刷新不丢失；支持导入 / 导出 JSON 备份与迁移。
- **主题与壁纸**：浅色 / 深色双主题；壁纸支持内置极光动画、内置渐变或自定义图片，均离线可用。
- **单文件运行**：打包为无控制台 EXE，启动后常驻系统托盘，右键可「打开 / 退出」，不弹黑框。
- **一键安装**：提供 Inno Setup 安装包，自动创建桌面与开始菜单快捷方式，含卸载程序。

## 获取与安装

到 [Releases](../../releases) 下载 **ResumeBuilder_Setup.exe** 安装（自动创建桌面 + 开始菜单快捷方式），
或直接取独立版 `ResumeBuilder.exe` 双击运行。未签名程序首次运行可能被 SmartScreen / 杀软提示，点「仍要运行」即可。

## 关于

- 交大邮箱：mali040929@sjtu.edu.cn
- 个人邮箱：mali040929@gmail.com

## 自行重新打包

```bash
pip install pyinstaller pystray pillow
python gen_assets.py
pyinstaller --onefile --windowed --name ResumeBuilder --icon logo.ico \
  --hidden-import pystray --hidden-import PIL --collect-all pystray launcher.py
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" ResumeBuilder.iss
```

## 版本

当前版本 **v1.0.0**，更新记录见 [CHANGELOG.md](CHANGELOG.md)。
