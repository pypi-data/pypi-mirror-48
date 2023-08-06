# Local Judge


## What's this?

Local Judge 类似于 Online Judge，但因其运行在本地，故命名为 **Local** Judge。

它可以让你在练习算法题目时，自动将文件的测试用例输入stdin，而不需要使用`freopen`等方法。(因为 freopen 每次提交OJ时必须注释代码)。

当然，控制台管道重定向也可以实现此功能，但是输入命令比较繁琐。

另一优势在于可以存储、管理多份测试用例，方便复习查阅。


## 快速入门

目录结构如下：

```
.
├── poj-1000 题目文件夹，需要和源码文件名前缀相同
│   ├── 1.in 输入，必须为*.in
│   ├── 1.out 预期输出，必须为*.out
│   ├── 2.in
│   ├── 2.out
│   ├── 3.in
│   ├── 3.out
│   ├── README.md 问题描述文件
└── poj-1000.c 代码


```

### 运行实例

```
➜ lj poj-1000.c
judging
case count: 4
-> case [1] <- accepted
   in 5 ms
-> case [2] <- accepted
   in 6 ms
-> case [3] <- accepted
   in 7 ms
-> case [test-error] <- wrong answer
   stdin:
   1 2
   stdout:
   3
   expected:
   5
   in 5 ms
=====summary=====
Wrong Answer: 1 Time Limit Exceeded : 0 Memory Limit Exceeded : 0
All: 4 Accepted: 3 (75.000000 %)

```



## 安装

```bash
pip install https://github.com/NoCLin/LocalJudge/archive/master.zip
```


termtosvg

## 编译器配置

建议将编译器所在目录加入环境变量 `path`。

修改文件 `~/.localjudge.json` 以自定义编译器及参数，内容如下：

```
➜  cat ~/.localjudge.json
{
  "c": "gcc ${src} -o ${temp_exe}",
  "c++": "g++ ${src} -o ${temp_exe}"
}
```

> ${src} 为源文件路径，${temp_exe}为生成的二进制文件路径，程序会将这些值自动替换


## 工具

```

➜  lj -h
usage: lj [-h] [-c CASE] [-t TIMELIMIT] [-d] [-s] [--clean] [--json] src

Local Judge

positional arguments:
  src                   source file

optional arguments:
  -h, --help            show this help message and exit
  -c CASE, --case CASE  index of test case
  -t TIMELIMIT, --timelimit TIMELIMIT
                        time limit (ms)
  -d, --debug           debug mode
  -s, --show            show cases
  --clean               clean temp directory
  --json                output as json


# ljc 自动生成工程文件
➜  ljc poj-1001.c
➜  ls poj-1001*
poj-1001.c

poj-1001:
1.in      1.out     2.in      2.out     README.md




```

## TODO

- [ ] pypi
- [ ] 内存限制 (使用沙盒？)
- [ ] 支持更多的语言
- [ ] VSCode 插件
