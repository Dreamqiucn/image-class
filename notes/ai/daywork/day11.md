# Day 11：raise 与 try/except——明确报告并处理错误

日期：2026-10-14。任务量约 60 分钟，不限制实际耗时。沿用现有扫描器，重点学习异常如何中断和传递。

## 今天的目标

扫描前检查输入路径，用 raise 主动报告无效目录；在主程序用 try/except 处理预期错误。有效空目录仍正常返回 {}。

修改文件：C:/Users/24718/Desktop/image-class/scripts/file_scanner.py。
沿用实际类名 Folderscanner、Imagesacnner，以及 p、excluded、included 三参数初始化。

## 1. 理解异常控制流程（约 15 分钟）

```python
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

try:
    result = divide(10, 0)
    print("结果：", result)
except ValueError as error:
    print("计算失败：", error)

print("程序继续执行")
```

预期输出：

```text
计算失败： 除数不能为 0
程序继续执行
```

- ValueError 是内置异常类；ValueError("说明") 创建一个异常对象。
- raise 触发异常，中断当前正常执行；本例不会执行 return a / b，也不会执行 try 中后面的结果打印。
- 异常向调用方传递，直到遇到匹配的 except；若没有处理器，会显示 traceback 并终止当前执行。
- try 包住需要处理错误的代码；没有异常时 except 不执行。
- except ValueError as error 接收对应异常对象；error 是变量名，可以换。
- 处理完成后，从整个 try/except 后面的语句继续，不会自动回到出错那一行重试。
- print 只是显示信息；return 正常返回值；raise 报告错误并改变正常执行流程。

参考：https://docs.python.org/zh-cn/3.12/tutorial/errors.html 。

## 2. 在父类扫描前检查目录（约 20 分钟）

当前代码实测：不存在目录会得到 {}，难以和合法空目录区分。

在 Folderscanner.collect_suffixes() 的遍历之前，自行补两种检查：
1. self.p.exists() 为 False：raise ValueError，消息说明路径不存在。
2. 路径存在但 self.p.is_dir() 为 False：raise ValueError，消息说明需要目录。

第一种写法示例：

```python
if not self.p.exists():
    raise ValueError(f"路径不存在：{self.p}")
```

另一种检查由用户补齐。原来的正常收集与计数逻辑继续使用。

放在父类的理由：普通对象调用它，图片子类的 super().collect_suffixes() 也调用它，一处检查服务两种扫描器。

## 3. 主程序处理预期异常（约 15 分钟）

将实际需要运行的创建扫描器、调用统计和输出放入 try，分别处理预期类型：

```python
try:
    # 使用自己的 p、excluded、included 创建扫描器
    # 调用 count 并打印结果
    ...
except ValueError as error:
    print(f"输入错误：{error}")
except OSError as error:
    print(f"文件操作失败：{error}")
```

ValueError 用于本次主动报告的路径值不合要求；OSError 用于文件操作中实际传播出来的系统错误。捕获明确的预期类型，保留编程错误用于排查，例如把 lower 拼成 low 的 AttributeError 应修正代码。

不需要为了完成本日增加新的交互重试机制。先理解并实现异常报告、传播和处理。

## 4. 简短功能验收与理解（约 10 分钟）

用自己方便的目录检查这些有意义的情况：
- 有效目录：原统计功能正常。
- 空目录：得到 {}，不是输入错误。
- 不存在的目录：显示清楚提示，停止这次统计，不输出成功统计。
- 一个文件的路径：提示需要目录。

两种扫描器应共享路径检查，不要求分别机械重做全部案例。没有真实触发 OSError 时，不声称系统错误处理已实测通过。

理解三个关键点：
1. raise ValueError(...) 与 print(...) 对执行流程有什么区别？
2. 父类方法抛出的异常，主程序的 try/except 为什么能接到？
3. 捕获异常后，会不会自动重新执行出错的那一行？

完成标准：有效目录和空目录结果保持正确，无效输入得到明确提示；能解释异常中断、向外传播、按类型处理及处理后的执行位置。以实际功能和关键理解验收，不机械要求照模板重复动作。

每日任务在开始时保存。Day 11 学习过程、问答与实际验收等任务结束后统一写入 records/day11-record.md，再同步总进度。核心代码由用户完成，不自动提交或推送 Git。

