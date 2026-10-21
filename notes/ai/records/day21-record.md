# Day 21 每日记录

日期：2026-10-21。性质：休息或轻量复盘。用户选择在聊天内口头问答，随后明确“day21到此为止吧”，本日结束。没有新增功能、安装依赖、修复 Day 20 遗留或运行代码验收；不将本次口头复盘记为整套项目通过。

## 复盘方式

用户要求只在聊天框里提问，不需要每天逐项提问。因此挑选重点，一次一题；没有生成额外的知识点总览或试卷。结束后按既定规则统一保存本记录，具体问答不放入总进度。

## 问题、回答与解释

### 1. 字典计数与 get 默认值

题目为 counts={}、label='cat'、counts[label]=counts.get(label,0)+1。用户回答 counts 是字典、默认值是 0，判断正确；助手补充执行后的完整结果是 {'cat':1}。get 在键不存在时提供默认值，赋值才写入计数。用户未独立给出完整最终字典，不扩大考核结论。

### 2. 局部赋值与未接收的返回值

模块 number=10，change 函数内部 number=20 并 return number，直接 change() 后 print(number)。用户正确回答输出 10，原因是函数修改局部变量，没有修改外部变量。助手补充返回的 20 没有被调用处接住。

### 3. 继承、重写与 self 方法查找

A.collect 返回两项，A.count 使用 len(self.collect())；B 继承 A 并重写 collect 只返回一项，询问 B().count()。用户正确预测 1。助手解释 count 虽来自 A，但 self 是 B 对象，因此使用 B.collect。用户未单独解释方法查找过程，不记为已经独立论证。

### 4. JSON 与集合

字典 summary 的 included 值写成 {'.jpg','.png'}，询问是否可直接 json.dump。用户提出把 included 的花括号改为方括号，改法正确；最初把不能保存的类型说成字典，随后明确纠正“写错了，是集合不是字典”。记录最终判断正确，不能把口误当成未理解。字典可保存为 JSON 对象，列表可保存为数组，set 默认不支持。

### 5. Path.parent、name、stem 与属性

给定 Path('images/cat/a.jpg')，用户回答 parent 为 cat、name 为 a.jpg、stem 为 a，且不用括号。name/stem 与属性不调用的判断正确。助手纠正 parent 是完整父路径 images/cat，p.parent.name 才是 cat。纠正后没有独立复答，不记为已完全掌握 parent。

### 6. 列表中嵌套字典

rows=[{'path':'cat/a.jpg','label':'cat'},{'path':'dog/b.jpg','label':'dog'}]。用户正确回答 rows[1]['label'] 为 dog，rows 是列表，rows[1] 是字典。

### 7. try/except 在循环内外与 continue

题目为 try 在 for 外包住整轮读图，第二张抛 OSError。用户正确回答第三张不会继续，应该把 try/except 放进 for；进一步提问放入循环后是否仍必须 continue。

助手说明：不一定。异常处理结束且循环体没有后续语句时，for 自然进入下一轮；continue 的作用是立即跳过本轮剩余语句。如果 except 之后还有 valid_paths.append(path)，失败分支可使用 continue 避免坏图被追加。没有将“必须 continue 循环才继续”记成正确规则。用户没有在解释后独立复述，不声称该细节已经重新考核通过。

### 8. __name__ 与直接运行保护

demo.py 在模块顶层 print('A')，在 if __name__=='__main__' 内 print('B')。用户正确回答导入时输出 A，直接运行时输出 A 和 B，并理解保护块只在直接运行当前文件时执行。助手精确说明模块被导入时保护块不执行。

### 9. 不同文件的模块全局作用域

helper.py 定义 show(): print(number)，main.py 导入 show 后定义 number=10 并调用。用户先认为可以输出 10，表示不清楚原因。助手解释会报 NameError：show 中未限定的 number 按函数定义所在模块查找，调用方 main 的模块变量不会自动传入 helper。给出 show(number) 参数传递的示例。

这一点属于本日仍需逐渐巩固的知识，不记为用户独立回答正确。即使使用 global，指向的也是函数所属模块的全局作用域，不是任意调用者的模块。

## 结束与接续

用户明确结束本日后停止提问，不追加测试或修复。Day 18 保持跳过；Day 20 是部分实现后用户结束，不自动要求回头修复。

下一学习日 Day 22 开始 NumPy。需要开始时再核对环境、安装状态并布置数组、形状和基础运算；本日没有预先安装 NumPy、生成 Day 22 任务或替写核心代码，没有 Git 暂存、提交、推送。
