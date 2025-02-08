---
layout:          post
title:           【翻译】甲基化特异性PCR：引物设计的四步"
subtitle:        MSP Primer Design
header-img:      img/post-bg-pcr.jpg
header-mask:     0.5
catalog:         true
author:          Direct-A
date:            2019-08-18
categories:
  - lab
tags:
  - msp
  - pcr
  - Primer
  - 引物设计
  - 文献翻译
  - 翻译
---

# 概述

甲基化特异性PCR方法仍是单一基因甲基化研究的选择之一。恰当的引物设计是获得可靠的PCR结果的先决条件。虽然有众多的文章阐述MSP引物设计的规则，但没有一个提供全面的解答。本文的目的在于阐述一个简洁明了，易于操作的引物设计流程。为了达到这一目标，我会提供丰富的启动序列检索工具、MSP引物设计软件，以及后续的计算机分析也会进行解析和呈现。一些优劣引物对比的例子也会展示出来作为指导。最后要说的是，本文引物设计是根据建议的流程来展现的。本文旨在为对单基因甲基化研究感兴趣的研究者在成功设计引物上给出建议。

**关键词**：甲基化特异性PCR、引物设计、数据库、MSP引物设计软件、转录起始位点

<!-- more -->

# 简介

基因表达的后天调控对于一个器官的发生发展有重要影响作用，调控可以在不同水平呈现[1,2]，关于这一现象，CpG二磷酸核苷是研究最多的一部分。预估在人类基因组内大约有20%的CpG位于一个称作CpG岛的区域内[3]。CpG岛是有着丰富CpG的一串DNA[4,5]，跨度超过200bp，至少有50%的G+C，并且检测到的CpG至少占统计预期CpG的60%[6]。大约60%的人类基因启动子包含CpG岛[5]，但在大多数组织中CpG岛是未甲基化的。这两个因素影响着CpG岛的调控功能。在CpG岛内甲基化的胞嘧啶对转录起到抑制效应[4,5,7]，就是说DNA甲基化的调控对器官内分泌有重要的意义。不出意外的话，通过更多的研究可以明确DNA甲基化模式的结构以及在病理和生理状态下的改变过程。
异常甲基化造成了像癌症和遗传疾病的众多疾病和病理过程的发生发展[8]。例如：抑癌基因启动子的过甲基化就是癌症的早期特征事件[9,10]；但是印记的缺失--在父母等位基因的一方甲基化的缺失，是某些综合症的病因[8]。前面这两个例子足以证明DNA甲基化研究的重要性。为了评估基因甲基化状态，有许多可行的方法。这些方法都依赖以下两个策略：

  1. 用甲基化特异性酶裂解DNA
  2. 利用亚硫酸化修饰基因组DNA[11,12]

我们的关注后者。

甲基化特异性PCR是研究特定基因甲基化状态最方便的方法[13]。虽然有些学者考虑弃用它，但是它高效，敏感性高并且使用频繁，让它成为单基因甲基化研究的最佳方法。MSP基于预先亚硫酸盐处理的DNA样本。在处理后未甲基化的胞嘧啶转化为尿嘧啶而5'mC未转化；因而最后DNA序列不再互补（图1）。之后亚硫酸盐修饰的DNA通过PCR利用两对引物进行扩增，其中一对引物识别甲基化DNA，另外一对识别未甲基化的DNA。最终通过最合适的PCR反应在数千条未甲基化的DNA中给出检测到的甲基化DNA。MSP为基础的方法具有的高灵敏度，在检验上有潜在应用[14,15]。但是，最适的MSP反应也是有挑战性的，因为引物设计可是绝对的关键步骤，并且在这一过程中需要考虑众多限制因素。本文的目的在于描述一个简洁明了，易于操作的引物设计流程。

{% asset_img MSP_1.jpg "图1" %}

**图1**  MSP是基于原始DNA亚硫酸盐修饰的。首先经过亚硫酸盐处理，DNA变性。变性之后，单链DNA进入修饰过程。未甲基化胞嘧啶转化为尿嘧啶，甲基化胞嘧啶不转化。经过PCR尿嘧啶被胸腺嘧啶取代。亚硫酸处理的结果就是DNA双链不再互补。CpG位点以粗体显示。

# 工作流程和数据库

MSP引物设计的整个过程可以分为四个步骤：

1. 启动子检索
2. 识别引物应当处在启动子的部位
3. 选择恰当的软件设计引物
4. 通过电脑分析选择分数最合适的一对引物（图2）

{% asset_img MSP_2.jpg "图2" %}

**图2：**引物设计的四步通过流程图展示。启动子检索在整个过程中是关键步骤。确定TSS所在位置后，就该选取引物所在的启动子区域。通过恰当的软件辅助，以所想的序列作为模板进行引物设计。最后，得到一些可供选择的引物对。通过电脑分析的辅助选择最好的一对。但是最好的引物在试管里并不一定表现的很好。如果出现这种情况，就该设计新的引物了。

有相当数量的网络资源和出版物在描述MSP引物设计上的大致规则和使用软件。但很少注意到第一步**检索启动子**。虽然像 [ENSEMBL](http://www.ensembl.org/index.html) 和 [NCBI](http://www.ncbi.nlm.nih.gov/) 的数据库包含基因和mRNA序列，但检索启动子仍然不是一件简单或容易的事。另一方面，并不推荐用启动子预测软件，因为知道真正启动子的位置很有必要。幸运的是，众多科技在过去十年的发展提升了启动子在基因水平的辨识。因而覆盖广泛且包含启动子的可靠数据库已经可用。这里，我们会探讨两个数据库：

  1. DBTSS(Database of Transcriptional Start Sites)
  2. EPD(Eukaryotic Promoter Database)

我们之所以讨论这俩特定的数据库，是我认为他俩用户友好且覆盖面广。值得注意的是DBTSS和EPD的初衷并不是提供给研究者启动子，而是促进相关的功能研究。

DBTSS的转录启动序列的数据，包含包含28种人的组织或细胞以及4种老鼠的组织或细胞[16]。另外，相同转录起始位点 不同状态的信息也有提供（如有氧/缺氧）。明显搭建者的目的是创建一个提供转录调控 动态总览的数据库。为建立这样的数据库，创建者用了一种叫做TSS-seq的技术[17]。该技术是依托于illumina众多平行序列的oligo-capping方案[18]。

检索TSS的定位很简单明了。在选择物种之后，选择目的基因。Entrez和Ensemble数据库中准确的染色体位置和退火温度以及对相关CpG岛位置的图片介绍和SNPs、TSS的定位也会呈现出来。你可以选择检索FASTA格式的启动子序列以及高亮的TSS定位。基于TSS的上下游可以自行选择。数据库可以通过 [链接](http://dbtss.hgc.jp/) 来访问。

EPD是建立超过25年的数据库[19]。在漫长的历史中，数据库发生可许多重大变化。但最重要的就是加入了启动子信息。分子生物学方法的发展对EPD产生了极大的影响。在基因组水平识别TSS序列的方法取代了从相应出版物获取启动子，这一漫长费时又枯燥过程。直到笔者当前的时间，该数据库已经包含25988个人类启动子，9773个小鼠启动子，11389个黑腹果蝇的启动子以及11719个斑马鱼启动子。为了获取TSS相关信息，你需要选择基因所对应物种的数据库。你还可以从引用内容的细节了解关于数据库的结构和机构，以及查看使用者手册和链接到其他数据库。需要强调的一点是**EPD只考虑DNA聚合酶Ⅱ的结合位点**。还有**创建者把启动子定义为TSS**。以此为基础，启动子被分成了三类：

  1. 单TSS位点
  2. 多TSS位点
  3. 启动区

数据库可以通过 [链接](http://epd.vital-it.ch/) 访问。

关于展示出的数据库还有两点需要强调：

  1. 对数据库潜力和性能的详细分析超出了本文的范围
  2. 同一基因的TSS位置在不同数据库可能相差甚远。但是差异并不显著，不影响后续步骤中的过程。

## 引物该呆在哪

在检索到启动子后，逻辑上下一步就是确定引物在启动子的位置。虽然，这一步看起来微不足道，但会影响到实验的结局。习惯上，引物应该在TSS的附近。这背后的道理是在TSS附近的甲基化在基因转录有着深远影响。这种方法也常在实验室中使用。然而，启动子转录激活的必要区域可能离TSS区域很远。因此，为了找到具有生物学意义的甲基化序列，比较可取的是搜索有关启动子功能研究的文献数据。总的来说，了解CpG岛内是否有序列和转录因子相结合还是有用的。在CpG岛内甲基化的C可以防止转录因子与目的基因启动子结合，从而导致表达降低[20]。在这方面，Zhu 等人发表了一些有趣的结论[21]。这些作者在ERβ基因启动子ON中定义了三个称作甲基化“热点”的部位。“热点”在共同序列包含的转录因子结合位点上。这些发现[23]被Bozovic 等人[22]使用并成功为ERβ设计甲基化研究引物（图3A）。

在引物设计的过程中，研究者有时会忽视基因所在序列的上下文，这会导致对启动子甲基化状态相关信息的误读。图4所描述的例子就展现出PTEN基因启动子和PTENP1假基因之间的高度的序列同一性。Zysman和Bapat[23]证明先前发表的关于多种癌症PTEN基因甲基化状态是假阳性的结果。事实上，这些研究所使用的引物都位于和PTEN假基因(PTENP1)有很高同源性的区域。Hesson和coworkers[24]也证实了他俩的结论。他们还指出由于PTEN的CpG岛和KLLN基因 共享，评估PTEN的甲基化远要复杂的多。这两篇文献的结果就告诉我们谨慎的选择引物序列对甲基化研究的成功是必要的。此外，这个例子也表明，由于启动子结构组织和基因组本身的限制，一些基因甲基化分析用的引物 设计要求 非常苛刻。

基于先前的讨论，可以在引物设计之前得出一个结论--我们得知道一些关键点。TSS就是显著影响引物位点的关键点。如先前所说，DBTSS和EPD能提供TSS相关的信息。因此，非常建议在TSS位点附近寻找引物。自TSS上游1000bp到下游500bp就是很好的起点。但是，CpG岛的搜索可能包含在一个相当宽的范围 (自 -5 kb 至 +5 kb) [25]。有趣的是，某些情况下，远端启动子的甲基化，而没有核心启动子的甲基化，可能在目的基因表达上扮演着很重要的角色[26-28]。转录因子结合位点也可以是进一步确定引物设置区域的关键点。例如，四个Sp1转录结合位点处在靠近PADI2基因TSS区域[29]，因此引物应当尽可能靠近这一区域（图3B）。

{% asset_img MSP_3.jpg "图3" %}

**图3**  A. ERβ基因启动子序列的574 bp (-222 / +352)片段。甲基化的“核心”部位用灰色高亮。为MSP设计的引物通过下划线标明。可以发现它位于第二和第三甲基化区域。B. PADI2基因的启动子序列。Sp1结合区域通过灰色高亮。假设引物对的设计使得正向引物跨越两个Sp1结合位点; 转录起始位点被指定为+1; 起始密码子用斜体表示; CpG网站是粗体。图中展示的序列是没有经亚硫酸盐修饰的。

关键点很重要，他们指明引物应当处在哪里，在最终决定之前还因当给予考虑其他的因素。这些因素决定了“限制位点”，即引物不应该位于的序列。例如，建议避开包含常见的SNPs[30]。和其他基因具有高度同一性的区段也应当避免。

{% asset_img MSP_4.jpg "图4" %}

**图4**  使用 [BLAST](http://blast.ncbi.nlm.nih.gov/) 工具对PTEN和PTENP1假基因进行校对。上方的是PTEN基因，下方是伪基因PTENP1。PTEN的转录起始位点通过虚线框出来。转录起始位点位于起始密码子上游1034个碱基处，这里没有显示出来。序列有90%的相似性。

## 引物设计的规则和软件使用

在网上MSP引物设计有很多可用的免费软件（表1）。

**表1：**MSP引物设计工具以及他们的功能。

| Tool            |                                                                                                                           Description                                                                                                                           | Link                                                                                                 |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------- |
| MSPprimer       | 基于Web的MSP工具，嵌套MSP和BSP入门设计。 包含SDSS（特异性决定子序列）算法，该算法负责更高的引物特异性[50]。 该程序需要天然DNA序列作为输入。 用户可以调整CpGs数量，Tm值，引物和产品长度。 还可以选择在输入序列中设置TSS的位置。 该程序可以自由使用，但需要注册。 | [http://www.mspprimer.org/cgi-bin/design.cgi](http://www.mspprimer.org/cgi-bin/design.cgi)           |
| MethMarker      |                     Methmarker是甲基化研究设计的全方位计划。 它支持以下方法的引物设计：COBRA，双硫酸盐SnuPE，MSP，MethyLight，亚硫酸氢盐焦磷酸测序，MeDIP qPCR。 该工具的另一个目的是支持表观遗传标记优化。 MethMarker可以免费下载和使用。                      | [http://methmarker.mpi-inf.mpg.de/](http://methmarker.mpi-inf.mpg.de/)                               |
| Beacon designer |    可用于设计定量MSP（MethyLight）研究的引物和探针的软件解决方案。 提供有关引物设计和引物特性分析的大量选项。 可以选择哪个链（正义/反义）作为模板。 此外，还可以选择设定引物的热力学性质。 主要缺点是该软件是共享软件。 免费试用期到期后，只能运行演示模式。    | [http://www.premierbiosoft.com/molecular_beacons/](http://www.premierbiosoft.com/molecular_beacons/) |
| Primo MSP       |                                               基于Web的MSP和BSP引物设计工具。 不包含一些重要功能，例如可调数量的非CpG C和CpG岛检索。 似乎应用程序没有足够的优化。 一些结果没有意义（例如，获得的产品长度为1bp）。                                               | [http://www.changbioscience.com/primo/primom.html](http://www.changbioscience.com/primo/primom.html) |

在介绍MSP引物设计软件之前，我会先列出和解释 MSP引物的设计规则。PCR引物设计的一般规则[31,32]在这也是适用的，但因为亚硫酸盐处理，也增加了额外的规则。一开始，考虑到为亚硫酸盐修饰的DNA设计引物，就需要记住以下的条件：

  1. 引物必须区分开亚硫酸盐修饰的DNA链和未修饰的链
  2. 引物必须区分开甲基化和未甲基化的双链

为了达到这些要求引物必须包括：

  1. 在引物靠近3'端至少包含一个CpG，以区分甲基化和未甲基化序列
  2. 为了利于亚硫酸盐修饰的序列扩增必须有足够多的非CpG的C，越多越好

为了评估基因甲基化状态，甲基化和未甲基化序列的引物包含相同的CpG也同等重要。但这并不意味着引物需要覆盖同一DNA片段。相反，推荐未甲基化引物比相应的甲基化引物长。亚硫酸盐修饰的DNA包含一长串“T”。因此，未甲基化引物是富有AT且低Tm值。可以通过长序列来弥补。原则上，由于胞嘧啶转化，MSP需要比一般PCR更长的引物。合适MSP的引物在20bp到30bp范围内。亚硫酸盐处理的另一个结果就是支离破碎DNA样本。所以，PCR产物不因当超过300bp[33]。

推荐设计的引物对Tm值差异不超过5℃，因为不这样的话反应效率会下降。需要着重提醒一下，同一引物对的Tm估计值在不同的软件大相近庭（表2）。

**表2：**通过三种不同的免费可在线访问的工具计算两种MSP引物[22]的Tm值：Oligoanalyzer，Perlprimer和BiSearch。 引物的Tm计算参数如下：一价阳离子（Na<sup>+</sup>），Mg<sup>2+</sup>和引物的浓度分别为50mM，1.5mM和200nM。

| 软件              | Olygoanalyzer | Perlprimer | BiSearch |
| ----------------- | ------------- | ---------- | -------- |
| Forward_primer_Tm | 60.1ºC        | 59.3ºC     | 61.7ºC   |
| Reverse_primer_Tm | 55.7ºC        | 54.4ºC     | 60.4ºC   |

Tm值计算主要基于邻近法（NN），这不仅考虑胞嘧啶和鸟嘌呤的相对含量还要考虑引物序列[34,35]。通过邻近法来计算的Tm值需要输入数个热力学界限。在计算Tm值时产生的差异主要是由于使用不同的热力学表格造成[36]。目前，对于使用哪个热力学表格计算Tm值最准确，没有一个定论。其他计算Tm值得方法的叙述可以看[37,38]。

在我看来，只了解规则而不提供充足例子是不够的。 Brandes和coworkers [39]表示，可能高估了ATM甲基化的角色在乳房和NSCLC样本中的作用。他们发现之前的文献是基于缺乏特异性的引物。事实上，因为缺乏非CpG的胞嘧啶，原始DNA和亚硫酸盐处理后的引物没有区别。

在这个情况下，我们不讨论这些软件的数学背景或通过数据做出特别合适软件的定论。我们提出的要求并不复杂，但也同样成功且合理。他们都是科学出版物中频繁出现，界面简洁，并且免费访问的。根据这些标准，我们将评价三个软件：Methprimer, Methylprimer express和 BiSearch。

[Methprimer](http://www.urogene.org/cgi-bin/methprimer/methprimer.cgi) 是一款免费访问的网页端软件。处理MSP还可以为亚硫酸盐序列PCR（BSP）进行引物设计。特别的好处就是，它可以输入任何格式的序列。用户需要提供gDNA序列，因为软件通过把序列转换为亚硫酸盐修饰再来运行。软件提供许多选项，都是关于引物功能以及在输入基因内所处的位置（表3）。

**表3：**Methprimer，BiSearch和Methylprimer express的可修改选项列表。给的值是默认值。

| 参数                     | Methprimer | BiSearch  | Methylprimer express |
| ------------------------ | ---------- | --------- | -------------------- |
| 产物长度 (bp)            | 100-300    | Up to 400 | 100-175              |
| 引物 Tm (°C)             | 50-60      | 45-70     | 56-64                |
| 引物 size (bp)           | 20-30      | 20-35     | 18-22                |
| 引物对间Tm值差异 (°C)    | ≤5         | N/A       | N/A                  |
| 正向和反向引物间Tm值差异 | N/A        | <8        | <8                   |
| 每引物最小CpG值          | 1          | 1         | 2                    |
| 每引物最小非CpG胞嘧啶值  | 4          | N/A       | 2                    |
| 3’ CpG 限制              | yes        | yes       | yes                  |
| 可调CpG 岛检索           | yes        | N/A       | yes                  |
| 引物打分                 | N/A        | yes       | N/A                  |

设计结果以图表介绍和序列对比的形式给出。但Methprimer并不是没有缺点。比如，高估Tm以及引物报告富含AT[39]。还有一个反对意见就是，Methprimer背后的算法仅仅是Primer3软件的修改[40]。这个软件更多的相关信息在[33]。

**Methylprimer express**是Applied Biosystems开发的MSP引物设计软件解决方案。软件已经可以通过向当地的Applied Biosystems官方申请获取。Methylprimer express可以用于MSP、BSP的引物寻找中。在输入序列中定义TSS基和转录起点是逻辑选项。如果用户愿意使用这些选项，引物会尽可能的定位于标记的位置。用户还可以调整引物特征，比如搜索CpG岛。结果输出是图像形式和基础序列。在引物序列的Tm值结果下面是CpG的数量和非CpG的胞嘧啶数量。另外，还指出了引物可能修饰的地方。但需要指出仍有不足：高估Tm值，有时未甲基化序列过短Tm值太低。

**BiSearch**是一款网页端软件，通过 [链接](http://bisearch.enzim.hu/) 访问。和前两个软件不同的是，BiSearch能够在选定的天然或亚硫酸氢盐修饰的基因组上 用设计的引物进行 相似性搜索[40]。**这个选项用于检测引物特异性。**BiSearch的另一个优势就是服务器速度快[41]。软件只提供有显著差异的引物对，这能为相同的样品建立备选PCR程序[40]。另外一个有趣的选项是选择哪条链--正向或反向，作为MSP引物设计的模版。用户需要提供全文本形式的原始DNA（并非亚硫酸盐修饰的）序列。

实际中要考虑的是怎样设置界定范围才能获得可信赖的甲基化研究引物。**恰当的选择和消除方法中主要的缺陷**：得到假阳性的结果[30]。假阳性结果可能是甲基化不完全，或者甲基化引物区分甲基化或未甲基化双链的能力低。为了防止扩增未转化DNA，**至少有一条引物在靠近3'端应当包含数个非CpG的胞嘧啶**[42]。5'端不匹配并不能满足引物特异性。另外，退火温度低 也可以在30个PCR反应中 稳定结合 不匹配的引物[43]。为了研究清楚，我们通过电脑测试展现。通过DBTSS获取五个启动子序列（下列基因TSS的上游序列1000bp和下游序列200bp区域间：p14, p16, DAPK, MGMT, RASSF1A），用作引物设计的模版。开始我们使用之前所说的软件的默认值。结果显示：

   1. Methprimer设计的一些引物区分甲基化和未甲基化引物的能力低（图5A）行内显示的是Brandes 等人[39]完成的研究
   2. BiSearch设计的引物只能在p14和MGMT中使用
   3. Methylprimer express提供的引物太短（18-22nt），这也难怪未甲基化的引物Tm值低。就比如说，MGMT的未甲基化正向序列预测Tm值才49.89℃（数据未展示）。

基于之前的讨论，使用默认值（表3）并不是设计引物最好的选择，无论软件。

但是，Methprimer和Methylprimer express (图5B) 在适当定制后生成引物，还是给出了满意的答案。事实证明，BiSearch在某些情况下难以设计特定的引物（图5C）。而且BiSearch很有意思，它并没有给选择非CpG胞嘧啶数量的选项。此外还没有给关于检索CpG岛的选项。

设计特异性引物，建议遵循的以下原则。每个引物设置2-4个CpG，并且引物在靠近3'端CpG使用的越多越好。还有非CpG的胞嘧啶应当设置4个或更多，但是这些胞嘧啶最好尽可能位于引物3'端。Tm值应当设置在60℃和70℃之间，但这也不是严格标准。根据我们实验室的结果，使用产物<150 bp的引物对可以获得最佳结果。这可能是因为我们研究中使用福尔马林固定石蜡包埋的样本。但是，设计产物不大于150bp的引物对可能有潜在的优势。如果设计合适的探针，这种引物可以用于甲基化状态的定量评估。研究者可以试着组合多种限制条件，以及根据上述标准对比引物。

{% asset_img MSP_5.jpg "图5" %}

**图5：**A. 为使用Methprimer默认值，设计评估DAPK启动子甲基化状态的MSP引物对。正向引物含有单个CpG和四个非CpG的胞嘧啶。甚至在很靠近3'末端的单个胞嘧啶也不能保证引物特异性，即正向引物具有低的区分甲基化和未甲基化等位基因的能力。四个非CpG在序列中定位不佳。它们都没有位于3'端。反向引物具有两个CpG，非CpG胞嘧啶定位很好。然而，3个CpG（正向+反向）不足以可靠地评估启动子甲基化状态。B. 利用Methylprimer express使用自定义设置设计的MSP引物对。RASSF1A基因的启动子序列作为引物设计的模板。C. 由BiSearch使用p16启动子序列作为模板设计的甲基化引物对。反向引物不含任何非CpG胞嘧啶，而正向引物仅含有两个。该引物对易于产生假阳性结果。 在引物序列中用小写字母表示的胸腺嘧啶表示原始DNA中非CpG胞嘧啶的位置。

## 电脑分析引物的适用性

多数情况下，设计引物的软件并不提供关于引物的发卡结构、引物二聚体和3'端稳定性的信息。但这些限制条件又显著影响PCR的效率和收获[31,44]。引物二极体和发卡结构并不显著影响引物浓度，但是减低扩增效率。换句话说，引物3'端稳定性影响他的引物特异性。**稳定的3'端引发在一定程度上是可取的；过度稳定的3'端导致非特异性扩增**。

发卡结构由于引物自身互补而形成。原则上来说，3'端的发卡结构在PCR扩增上有更加实质的影响[45]。Taq酶可以利用5'端作为模板扩增3'端。结果就是，有利于生成结构稳定，非特异性的产物。在研究发夹结构对PCR影响的研究中，根据Singh等人的报导，长度大于4个核苷酸的以上发卡结构显著影响扩增效率[44]。

引物二聚体是由于两个相同的引物分子间的反应（自身二聚体），或者正义链和反义链之间有互补序列（交插二聚体）。由于3'末端互补形成的引物二具体相较于引物内的二聚体有更大的影响。在PCR过程中，Taq酶执行互补序列3'末端的扩增，进而形成引物二聚体。因此，在引物二聚体和模板之间就构成了竞争。最终扩增匮乏。

为了减少引物二级结构的形成，下面几条应当避免：引物之间相似序列，回问序列，以及3'末端3个及以上的重复C或G[46]。

结构的稳定程度通过dG来描述。dG代表吉布斯自由能，通过在恒定压力下操作过程中，生成功的量来定义。简单讲，就是自发反应的度量单位。如果dG<0，利于反应发生，反之亦然。关于发卡结构，引物二聚体和3'末端稳定性可以接受的dG值的信息可以在 [链接](http://www.premierbiosoft.com/tech_notes/) 查找。需要提醒的是软件计算的dG默认是在25℃到37℃之间的。在这些温度下，他算出来PCR中产生的二级结构稳定性信不过。因此推荐输入退火温度。

电脑分析引物稳定性，需要利用适当的软件来预测引物在试管中的行为。通过这种方法，更有可能根据存在特异性不够或者稳定的发卡结构 识别和抛弃引物对。过程可以分为两步：

  1. 通过计算和预测引物的热力学特征
  2. 通过利用适当的基因组运行同一性检测，检查引物的的特异性。

适合用来引物分析的有很多网页端工具。一些软件和程序可以帮助估计潜在结构、发卡结构稳定性和引物二聚体，他们在表4中呈现。

**表4：**可用于检查引物热力学性质的软件和Web应用程序列表。

| Tools          | Description                                                                                                                                                                                                         | Reference                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primerlist     | Java应用程序; 界面简洁; 计算Tm，Ta和潜在的引物二级结构。                                                                                                                                                            | [http://primerdigital.com/tools/](http://primerdigital.com/tools/)                                                                                                   |
| PerlPrimer     | 用Perl编写的程序。 可以免费下载和使用。 实现标准PCR，qPCR，BSP和测序的引物设计。 为用户提供有关设计引物（Tm，二级结构）的相关信息。 可以分析预先设计的引物。 该软件计算引物二聚体和发夹结构的引物Tm，GC含量和dG值。 | [http://perlprimer.sourceforge.net/](http://perlprimer.sourceforge.net/)                                                                                             |
| Primer Premier | 有一个下载和安装的过程。 Primer premier是一款商业软件。 演示版免费使用，可进行预先设计的引物分析。 该软件为用户提供有关引物功能的详细信息。 用户可以更改用于计算Tm和dG的参数。                                      | [http://www.premierbiosoft.com/primerdesign/index.html](http://www.premierbiosoft.com/primerdesign/index.html)                                                       |
| Autodimer      | 设计用于快速筛选预选的PCR引物对，用于分析潜在的交叉反应。用于检查设计用于多重PCR的引物对的便利工具。 用户可以调整温度以进行dG计算，总链浓度和最低分数要求。 用户应提供FASTA格式的引物序列。                         | [http://www.cstl.nist.gov/strbase/AutoDimerHomepage/AutoDimerProgramHomepage.html](http://www.cstl.nist.gov/strbase/AutoDimerHomepage/AutoDimerProgramHomepage.html) |
| Oligoanalyzer  | 基于网络的工具，用于预先选择的引物检查。 提供有关Tm，引物二聚体和发夹的信息。 用户可以调整引物，dNTPs，Na<sup>+</sup> 和Mg<sup>2+</sup> 的浓度。                                                                    | [http://eu.idtdna.com/analyzer/applications/oligoanalyzer/](http://eu.idtdna.com/analyzer/applications/oligoanalyzer/)                                               |

利用工具进行电脑分析引物适宜程度的一般功能，我会通过使用 [Netprimer](http://www.premierbiosoft.com/) 为例进行叙述。他是一个网页端应用，在我们的实验室日常用来检查引物。程序让用户设定核酸浓度值，离子浓度(Na<sup>+</sup>, Mg<sup>2+</sup>)和温度用以计算。Netprimer显示以下信息：二级结构稳定性，Tm值，5'和3'端稳定性，以及引物分子重量等等。为估计引物效率，Netprimer计算分值。这个分值根据二聚体和发卡结构稳定性以下面的方式计算：

>分值=100+(dG(二聚体)*0.8+dG(发卡结构)*1.4)

因此，如果dG(二聚体)=dG(发卡结构)=0，引物评分100分。通过分值计算软件得出最稳定的结构。

比较好的做法是“校准”NetPrimer和其他类似的应用程序。换句话说，就是建议研究者知道软件会为二级结构和3'末端稳定性提供正确的结果（经过实验验证）。软件并不总提供所有影响PCR结果的变量，这就是这么做背后的原因。例如，没有一个选项可以设定用在PCR Mix中其他试剂的浓度。另外，还有各种不同的与软件选项预测二级结构形成相关。由Netprimer计算出来的dG值可能比建议的大，但是这并不意味着检验过的引物对会在试管内表现差。

Netprimer一类的工具并不提供任何关于引物特异性的信息。为了检验引物是否只和感兴趣的序列区段结合，建议使用BiSearch做个亚硫酸盐修饰基因组同一性检索（图6）。

{% asset_img MSP_6.jpg "图6" %}

**图6：**在亚硫酸氢盐处理的甲基化基因组上对选自[23]的引物对进行相似性搜索。结果显示引物对与靶序列（染色体10）结合，而且也与染色体9上的序列结合。

这里给出三个建议：

   1. 用原始基因进行同一性检验
   2. 在未甲基化的亚硫酸盐修饰基因组上进行同一性检验
   3. 在甲基化的亚硫酸盐修饰基因组上进行同一性检验

用户可以选择以下基因组：人类，小家鼠，挪威大鼠和黑猩猩。应注意，默认设置仅在不匹配位于5'末端时才显示非特异性引物结合。考虑到3'末端对于引物PCR特异性的重要性，这还是有道理的。但还是建议调整软件，在3'端出现错配时把序列认定为“相似”。即便在非常临近3'端的位置出现单个错配也不能满足反应的特异性[47-49]。

引物设计的整过过程通过图7的例子进行总结和展示。

{% asset_img MSP_7.jpg 图7 %}

**图7：**设计用于人RASSF1A基因的甲基化猜想的研究的引物。首先，RefSeq ID（NM_007182）是从[NCBI](http://www.ncbi.nlm.nih.gov/nuccore/NM_007182.4)检索的。为了检索RASSF1A启动子序列，而使用DBTSS。在适当的字段中输入RASSF1A ID，进一步访问有关RASSF1A启动子的信息（参见正文）。使用默认设置，DBTSS显示TSS上游1000bp和下游200bp的启动子序列。选中此选项。将获得的序列复制并粘贴在Methprimer的相应区域中。Methprimer选项配置为程序屏幕截图所示。通过NetPrimer分析所得的引物对。甲基化等位基因特异的最佳引物对就显示在图中。

# 总结

理论上说，PCR已经足够灵敏以在试管中扩增单个分子，也足够稳固来为下游分析生产质量足够满意的原料。为了接近这一理论反应，正确的设计引物是关键步骤。草草的引物设计会造成对各种病理状况下甲基化状态的误解。考虑到MSP的诊断应用，假阳性结果不是选项之一。本文的目的在于阐述一个简单的MSP引物设计流程。之外是为了指出关键步骤和过程中可能的错误。

# 致谢

本工作受自塞尔维亚共和国，教育部，科学与技术发展的173049授权的支持。

# 参考文献

[1] Kiefer J. C., Epigenetics in development, Dev Dyn, 2007, 236, 1144-1156
[2] Delcuve G. P., Rastegar M., Davie J. R., Epigenetic control, J Cell Physiol, 2009, 219, 243-250
[3] Wan J., Oliver V. F., Zhu H., Zack D. J., Qian J., Merbs S. L., Integrative analysis of tissue-specific methylation and alternative splicing identifies conserved transcription factor binding motifs, Nucleic acids research, 2013,10.1093/nar/gkt652,
[4] Deaton A. M., Bird A., CpG islands and the regulation of transcription, Genes Dev, 2011, 25, 1010-1022
[5] Santos K. F., Mazzola, T. F., Carvalho, H. F., The prima donna of epigenetics: the regulation of gene expression by DNA methylation, Brazilian Journal of Medical and Biological Research, 2005, 38, 1531-1541
[6] Portela A., Esteller M., Epigenetic modifications and human disease, Nature biotechnology, 2010, 28, 1057-1068
[7] Esteller M., CpG island hypermethylation and tumor suppressor genes: a booming present, a brighter future, Oncogene, 2002, 21, 5427-5440
[8] Egger G. L., G.; Aparicio, A.; Jones, P.A., Epigenetics in human disease and prospects for epigenetic therapy, Nature, 2004, 429, 457-463
[9] Das P. M., Singal R., DNA methylation and cancer, Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 2004, 22, 4632-4642
[10] Kanai Y., Hirohashi S., Alterations of DNA methylation associated with abnormalities of DNA methyltransferases in human cancers during transition from a precancerous to a malignant state, Carcinogenesis, 2007, 28, 2434-2442
[11] Kondo Y., Issa J. P., DNA methylation profiling in cancer, Expert Rev Mol Med, 2010, 12, 23
[12] Mansego M. L., Milagro F. I., Campion J., Martinez J. A., Techniques of DNA methylation analysis with nutritional applications, Journal of nutrigenetics and nutrigenomics, 2013, 6, 83-96
[13] Herman J. G., Graff J. R., Myohanen S., Nelkin B. D., Baylin S. B., Methylation-specific PCR: a novel PCR assay for methylation status of CpG islands, Proceedings of the National Academy of Sciences of the United States of America, 1996, 93, 9821-9826
[14] Zhang Z., Sun D., Hutajulu S. H., Nawaz I., Nguyen Van D., Huang G., et al., Development of a non-invasive method, multiplex methylation specific PCR (MMSP), for early diagnosis of nasopharyngeal carcinoma, PloS one, 2012, 7, 45908
[15] Delpu Y., Cordelier P., Cho W. C., Torrisani J., DNA methylation and cancer diagnosis, Int J Mol Sci, 2013, 14, 15029-15058
[16] Yamashita R., Sugano S., Suzuki Y., Nakai K., DBTSS: DataBase of Transcriptional Start Sites progress report in 2012, Nucleic acids research, 2012, 40, 150-154
[17] Tsuchihara K., Suzuki Y., Wakaguri H., Irie T., Tanimoto K., Hashimoto S., et al., Massive transcriptional start site analysis of human genes in hypoxia cells, Nucleic acids research, 2009, 37, 2249-2263
[18] Maruyama K., Sugano S., Oligo-capping: a simple method to replace the cap structure of eukaryotic mRNAs with oligoribonucleotides, Gene, 1994, 138, 171-174
[19] Dreos R., Ambrosini G., Cavin Perier R., Bucher P., EPD and EPDnew, high-quality promoter resources in the next-generation sequencing era, Nucleic acids research, 2012, 41, 157-164
[20] Brait M., Sidransky D., Cancer epigenetics: above and beyond, Toxicology mechanisms and methods, 2011, 21, 275-288
[21] Zhu X., Leav I., Leung Y. K., Wu M., Liu Q., Gao Y., et al., Dynamic regulation of estrogen receptor- beta expression by DNA methylation during prostate cancer development and metastasis, The American journal of pathology, 2004, 164, 2003-2012
[22] Bozovic A., Markicevic M., Dimitrijevic B., Jovanovic Cupic S., Krajnovic M., Lukic S., et al., Potential clinical significance of ERbeta ON promoter methylation in sporadic breast cancer, Med Oncol, 2013, 30, 642
[23] Zysman M. C., WB. , Bapat B., Considerations When Analyzing the Methylation Status of PTEN Tumor Suppressor Gene, American Journal of Pathology, 2002, 60, 795-800
[24] Hesson L. B., Packham D., Pontzer E., Funchain P., Eng C., Ward R. L., A reinvestigation of somatic hypermethylation at the PTEN CpG island in cancer cell lines, Biol Proced Online, 2012, 14, 5
[25] Cho Y. G., Chang X., Park I. S., Yamashita K., Shao C., Ha P. K., et al., Promoter methylation of leukemia inhibitory factor receptor gene in colorectal carcinoma, International journal of oncology, 2011, 39, 337-344
[26] Fasan A., Alpermann T., Haferlach C., Grossmann V., Roller A., Kohlmann A., et al., Frequency and prognostic impact of CEBPA proximal, distal and core promoter methylation in normal karyotype AML: a study on 623 cases, PloS one, 2013, 8, e54365
[27] Tada Y., Brena R. M., Hackanson B., Morrison C., Otterson G. A., Plass C., Epigenetic modulation of tumor suppressor CCAAT/enhancer binding protein alpha activity in lung cancer, Journal of the National Cancer Institute, 2006, 98, 396-406
[28] Lin T. C., Hou H. A., Chou W. C., Ou D. L., Yu S. L., Tien H. F., et al., CEBPA methylation as a prognostic biomarker in patients with de novo acute myeloid leukemia, Leukemia, 2011, 25, 32-40
[29] Dong S., Kojima T., Shiraiwa M., Mechin M. C., Chavanas S., Serre G., et al., Regulation of the expression of peptidylarginine deiminase type II gene (PADI2) in human keratinocytes involves Sp1 and Sp3 transcription factors, The Journal of investigative dermatology, 2005, 124, 1026-1033
[30] Hernandez H. G., Tse M. Y., Pang S. C., Arboleda H., Forero D. A., Optimizing methodologies for PCR-based DNA methylation analysis, Biotechniques, 2013, 55, 181-197
[31] Dieffenbach C. W., Lowe T. M., Dveksler G. S., General concepts for PCR primer design, PCR Methods Appl, 1993, 3, 30-37
[32] Chuang L. Y., Cheng Y. H., Yang C. H., Specific primer design for the polymerase chain reaction, Biotechnol Lett, 2013,10.1007/ s10529-013-1249-8
[33] Li L. C., Dahiya, R. , MethPrimer designing primers for methylation PCRs, Bioinformatics, 2002, 18, 1427-1431
[34] Borer P. N., Dengler B., Tinoco I., Jr., Uhlenbeck O. C., Stability of ribonucleic acid double-stranded helices, J Mol Biol, 1974, 86, 843-853
[35] SantaLucia J., Jr., A unified view of polymer, dumbbell, and oligonucleotide DNA nearestneighbor thermodynamics, Proc Natl Acad Sci U S A, 1998, 95, 1460-1465
[36] Panjkovich A., Melo F., Comparison of different melting temperature calculation methods for short DNA sequences, Bioinformatics, 2005, 21, 711-722
[37] Marmur J., Doty P., Determination of the base composition of deoxyribonucleic acid from its thermal denaturation temperature, J Mol Biol, 1962, 5, 109-118
[38] Wallace R. B., Shaffer J., Murphy R. F., Bonner J., Hirose T., Itakura K., Hybridization of synthetic oligodeoxyribonucleotides to phi chi 174 DNA: the effect of single base pair mismatch, Nucleic acids research, 1979, 6, 3543-3557
[39] Brandes J. C., Carraway H., Herman J. G., Optimal primer design using the novel primer design program: MSPprimer provides accurate methylation analysis of the ATM promoter, Oncogene, 2007, 26, 6229-6237
[40] Tusnady G. E., Simon I., Varadi A., Aranyi T., BiSearch: primer-design and search tool for PCR on bisulfite-treated genomes, Nucleic acids research, 2005, 33, 9
[41] Aranyi T., Varadi A., Simon I., Tusnady G. E., The BiSearch web server, BMC Bioinformatics, 2006, 7, 431
[42] Kristensen L. S., Raynor M. P., Candiloro I., Dobrovic A., Methylation profiling of normal individuals reveals mosaic promoter methylation of cancer-associated genes, Oncotarget, 2012, 3, 450-461
[43] Rand K., Qu W., Ho T., Clark S. J., Molloy P., Conversion-specific detection of DNA methylation using real-time polymerase chain reaction (ConLight-MSP) to avoid false positives, Methods, 2002, 27, 114-120
[44] Singh V. K., Govindarajan, R., Naik, S., Kumar, A., The Effect of Hairpin Structure on PCR Amplification Efficiency, Molecular Biology Today, 2000, 1, 67-69
[45] Rychlik W., Selection of primers for polymerase chain reaction, Mol Biotechnol, 1995, 3, 129-134
[46] Innis M. A., Gelfand, D. H., Optimization of PCRs, in PCR Protocols (Innis, M A, Gelfand, D H, Sninsky, J J, and White, T J, eds), Academic, New York, 3-12, 1990,
[47] Simsek M., Adnan H., Effect of single mismatches at 3’-end of primers on polymerase chain reaction, Journal for scientific research Medical sciences / Sultan Qaboos University, 2000, 2, 11-14
[48] Kwok S., Kellogg D. E., McKinney N., Spasic D., Goda L., Levenson C., et al., Effects of primertemplate mismatches on the polymerase chain reaction: human immunodeficiency virus type 1 model studies, Nucleic acids research, 1990, 18, 999-1005
[49] Huang M. M., Arnheim N., Goodman M. F., Extension of base mispairs by Taq DNA polymerase: implications for single nucleotide discrimination in PCR, Nucleic acids research, 1992, 20, 4567-4573
[50] Miura F., Uematsu C., Sakaki Y., Ito T., A novel strategy to design highly specific PCR primers based on the stability and uniqueness of 3’-end subsequences,

{% asset_link MSP_primer_design_four_steps.pdf "原文下载" %}
