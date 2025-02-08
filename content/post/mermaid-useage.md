---
layout: post
title: 你来描述，让程序自动绘制流程图——mermaid
subtitle: mermaid 快速上手
author: Direct-A
date: 2021-12-04
toc: true
top: false
cover: false
mathjax: true
categories:
  - programming
tags:
  - mermaid
  - 流程图
  - markdown
  - programming
summary:
password:
description: mermaid 快速上手
---

最开始做流程图都是在 draw.io 里，拖拖拉拉，牵线搭桥，最后导出，然后由需要修改了就回到源文件重新改导出，源文件丢了就得自己重新描，虽然现成模块也挺快的，但是拖拖拽拽，一会儿就把之前脑内构思好的点子给忘了，简直恼人。

最近写 markdown 看有人可以直接在里面生成流程图，可给我高兴坏了，赶紧搜了一下，是 **mermaid** ，真有可以实现的方法，而且 obsidian typora 都兼容，不错！很棒！

<!-- more -->

## 基本语法

- 在代码块内第一行需要声明图片类型

- 之后的绘图内容可缩进输入

- 可以使用注释 `%%` 开头即可

- 字符使用 `“”` 进行包裹

- `#quot` `#9829` 转义字符

- 使用 `style` 可以对节点样式进行定义

  ```javascript
  style id2 fill:#ccf,stroke:#f66,stroke-width:2px,stroke-dasharray: 5, 5;
  ```

- 使用 `click` 可以为节点添加点击行为

  ```javascript
  click nodeId callback
  ```

- 使用 `classDef` 可以定义一个回调函数

  ```javascript
  classDef default fill:#f9f,stroke:#333,stroke-width:4px;
  ```

- 使用 `class` 可以定义节点样式

  ```javascript
  class sq,e green
  ```

mermaid 实现绘图需要指定绘制的图片类型：

{% mermaid graph %}
  %% 我是注释
  A["A double quote:#quot;"] -->B["A dec char:#9829;"]
  C --"(^v^)"--> D
{% endmermaid %}

1. `pie` 饼状图

   - `title` 图片标题，可选
   - `“ ”:` 分类名称，分隔符，后接数字，支持小数，占比会自动计算

2. `graph` **流程图**

   1. `TB/BT/LR/RL` 图片方向 top bottom left right

   2. 元素形状

      {% mermaid graph LR %}
      矩形 -->
      id1[正方形] -->
      id2(圆角矩形) -->
      id3([体育场]) -->
      id4[[子程序]] -->
      id5[(圆柱)] -->
      id6((圆))

      id7{菱形} -->
      id8{{六角形}} -->
      id9[/平行四边形/] -->
      id10[\反向平行四边形\] -->
      id11[/梯形\] -->
      id12[\反向梯形/]

      id13>标签形]
      {% endmermaid %}

   3. 连线样式

      {% mermaid graph LR %}
      a-->b
      c--文本-->d-->|文本|e
      f==>g
      h==文本==>i
      j-.->k
      l-.文本.->m
      {% endmermaid %}

      连线时使用的间隔符号可以 $\ge$ 2个

      图片关键字换成 `flowchart` 对 graph 的连线形式也是兼容的，同时会存在更多种连线类型

      {% mermaid flowchart LR %}
      a o--o b
      c <--> d
      e x--x f
      g --文本--> h
      {% endmermaid %}

      使用 `&` 可以进行多重连接

      `subgraph` 可以指定子图

      `end` 结尾

      {% mermaid flowchart LR %}
      subgraph 多重连接
      A & B --> C & D
      end
      subgraph 子图
      E --> F
      end
      F --> A & B
      {% endmermaid %}

      {% mermaid graph LR %}
      emperor((朱八八))-.子.->朱五四-.子.->朱四九-.子.->朱百六

      朱雄英--长子-->朱标--长子-->emperor
      emperor2((朱允炆))--次子-->朱标
      朱樉--次子-->emperor
      朱棡--三子-->emperor
      emperor3((朱棣))--四子-->emperor
      emperor4((朱高炽))--长子-->emperor3
      {% endmermaid %}

3. `sequenceDiagram` 序列图，时序图

   {% mermaid sequenceDiagram %}
      %% 自动编号
      autonumber
      %% 定义参与者并取别名，aliases：别名
           participant A as Aly
           participant B as Bob
           participant C as CofCai
           %% 便签说明
           Note left of A: 只复习了一部分
           Note right of B: 没复习
           Note over A,B: are contacting
           
           A->>B: 明天是要考试吗？
           B-->>A: 好像是的！
           
           %% 显示并行发生的动作，parallel：平行
           %% par [action1]
           rect rgb(0, 255, 255)
               par askA
                   C -->> A:你复习好了吗？
               and askB
                   C -->> B:你复习好了吗？
               and self
                   C ->>C:我还没准备复习......
               end
           end
           
           %% 背景高亮，提供一个有颜色的背景矩形
           rect rgb(255, 255, 0)
               loop 自问/Every min
               %% <br/>可以换行
               C ->> C:我什么时候<br/>开始复习呢？
               end
           end
           
           %% 可选择路径
           rect rgb(200, 100, 100)
               alt is good
                   A ->> C:复习了一点
               else is common
                   B ->> C:我也是
               end
               %% 没有else时可以提供默认的opt
               opt Extra response
                   C ->> C:你们怎么不回答我
               end
           end
   {% endmermaid %}

4. `gantt` 甘特图

   {% mermaid gantt %}
   title A Gantt Diagram
   dateFormat  YYYY-MM-DD
   section Section
   A task           :a1, 2014-01-01, 30d
   Another task     :after a1  , 20d
   section Another
   Task in sec      :2014-01-12  , 12d
   another task      : 24d
   {% endmermaid %}

5. `classDiagram` 类图

   {% mermaid classDiagram %}
   %% Duck继承自Animal
        Animal <|-- Duck
        Animal <|-- Fish
        Animal <|-- Zebra
        %% +即public；-即private；#即protected；~即Package/Internal
        Animal : +int age
        Animal : +String gender
        %% 返回值类型，在括号后面加，记得要有一个空格
        Animal: +isMammal() bool
        Animal: +mate()
        %% Duck有Animal的属性和方法
        class Duck{
            +String beakColor
            +swim()
            +quack()
        }
        class Fish{
            -int sizeInFeet
            -canEat()
        }
        class Zebra{
            +bool is_wild
            +run(speed)
        }
        Duck <|-- yellowDuck
        class yellowDuck{
          -string color
          -int size
        }
   {% endmermaid %}

   {% mermaid classDiagram %}
   %% [classA][Arrow][ClassB]:LabelText
        classA --|> classB : Inheritance
        classC --* classD : Composition
        classE --o classF : Aggregation
        classG --> classH : Association
        classI -- classJ : Link(Solid)
        classK ..> classL : Dependency
        classM ..|> classN : Realization
        classO .. classP : Link(Dashed)
   {% endmermaid %}

   {% mermaid classDiagram  %}
    class Shape {
        <<interface>>
        noOfVertices
        -len
        -high
        drawPoint()
        drawLine()
        drawRctangle()
    }
    class Color {
        <<enumeration>>
        RED
        BLUE
        GREEN
        WHITE
        BLACK
    }
    class type {
      <<abstract>>
      Animal
    }
   {% endmermaid %}

6. `stateDiagram` 状态图

   {% mermaid stateDiagram-v2 %}
   State1: The state with a note
   note right of State1
     Important information! You can write
     notes.
   end note
   State1 --> State2
   note left of State2 : This is the note to the left.
   {% endmermaid %}

7. `journey` 用户旅程图



太多了，有些也不太常用，不想学了，等用的时候再更新吧。
