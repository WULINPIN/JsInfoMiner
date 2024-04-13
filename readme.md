# JsInfoMiner

![logo](https://github.com/WULINPIN/JsInfoMiner/assets/30523752/9ab5f9a3-0037-4d5e-afc7-d12c3aece8b4)

此工具的主要目的是通过脚本配合类似HAE的burpsuite插件提取本地js文件中的敏感信息。
想必大家都知道，HAE或者其他的同类工具只能对通过burpsuite的流量中的敏感信息提取；那么如果在小程序的测试中，解包后想提取源码js文件中的敏感信息基本上都是手动查看；还有包括app解包后的js文件、js.map还原后的源码文件等等；即便写了加载HAE规则的脚本，也没法做到点击就能查看源文件以及查看js文件的上下文，而这个工具的出现恰好解决了这个痛点问题。

## 安装

```
pip install -r requirement.txt
```

## 使用

第一步：
需要打开burpsuite（监听在8080端口），并且成功加载HAE插件

第二步：
此处只需要传入js文件所在的根目录即可，工具会进行递归遍历，不错过任何一个js文件

```
python JsInfoExtract.py "js文件根目录"
```

第三步：
在HAE的数据表盘中查看提取到的敏感信息

![1](https://github.com/WULINPIN/JsInfoMiner/assets/30523752/98c18e50-03fd-414b-8e06-7cda46881c9c)

## 案例

案例一：
用户名密码泄露

![2](https://github.com/WULINPIN/JsInfoMiner/assets/30523752/38a7a3e0-a224-4fc4-9e11-0124f765ea13)


还有许多其他案例，就不一一列举出来了
