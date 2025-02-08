---
layout: post
title: 【翻译】MSH3 Homology and Potential Recombination Link to SARS-CoV-2 Furin Cleavage Site
subtitle: MSH3 同源物可能与 SARS-CoV-2 弗林蛋白酶切割位点链重组
author: Direct-A
toc: true
top: false
cover: false
mathjax: true
categories:
  - blog
tags:
  - sars-cov-2
date: 2022-03-25 09:45:22
description:
password:
summary:
---

SARS-CoV-2 和蝙蝠 RaTG13 冠状病毒的多个点突变中，仅有 12 个核苷酸长度的[弗林蛋白酶](https://zh.wikipedia.org/zh-cn/%E5%BC%97%E6%9E%97%E8%9B%8B%E7%99%BD%E9%85%B6)裂解位点（FCS）有超过三个核苷酸的差异。**通过 BLAST 检索发现 SARS.Cov2 基因组中包含标记裂解位点的 19 个核苷酸部分与密码子优化专有序列（人类 [MSH3](https://zh.wikipedia.org/zh-cn/DNA%E9%94%99%E9%85%8D%E4%BF%AE%E5%A4%8D) 的补充序列） 100% 互补**。SARS-Cov-2 中出现的反向互补序列可能是随机出现的但也有必要考虑其他可能。中间宿主内发生重组不像可能的解释。SARS-Cov-2 这类单链 RNA 病毒利用感染细胞的 RNA 负链作为模板，这有可能导致 SARS-CoV-2 反义链 RNA 与细胞内 MSH3 负链（包含 FCS）发生复制选择重组入病毒基因组。无论如何，这段包含 FCS 19 个核苷酸，且与 MSH3 mRNA 100% 反向互补的 RNA 序列的出现都是高度反常的并需要进一步研究。

关键词：SARS-CoV-2 刺突蛋白，弗林酶裂解位点，MSH3 基因，序列同源物，重组
<!-- more -->


## 前言

基于近期发表的一篇描述SARS-CoV-2插入变异的文章，我们带来了我们近期在 SARS-CoV-2 刺突（S）蛋白中弗林酶裂解位点 （FCS）序列的研究。SARS-CoV-2 造成了 COVID-19 流感，与蝙蝠冠状病毒 SL-CoVZC45 存在 82.3% 的核苷酸相似，与 SARS-CoV 有 77.2% 的核苷酸相似，**同时与蝙蝠冠状病毒 RaTG13 基因组序列相似性达 96.2%** 。在  SARS-CoV-2 和 RaTG13 的多个点突变中，仅有一个插入和三个核苷酸的插入： 12 个核苷酸，其编码 SARS-CoV-2 S 蛋白中发现的 4 个氨基酸（aa 681-684, PRRA）。这种多元 FCS 将 SARS-CoV-2 与其他 b 系 β 冠状病毒或任何其他沙贝病毒区分开来。FCS 的插入增强了  SARS-CoV-2 在 2019 年的感染能力。而 FCS  缺失使SARS-CoV-2 减毒变体其可用于动物疫苗接种，这与人类感染相关。FCS 在人和雪豹间传播至关重要，其将病毒传播至人类细胞，并造成两种  SARS-CoV-2 动物模型的严重疾病。

{% asset_img 20220325123356.png 图1 %}

图1：SARS-CoV-2 中弗林蛋白酶的原始序列。比对 SARS-CoV，RaTG13 和 SARS-CoV-2 在 S1/S2 连接处的蛋白序列，表明弗林蛋白酶裂解位点（FCS）PRRA 仅在 SARS-CoV-2 中出现。基于 BLAST 检索结果这段编码 FCS PRRA 的 12 核苷酸片段与专利（US 9587003）中 19 核苷酸长的特异序列（Seq ID11652）完全一致。Seq ID11652 转录为 MSH3 mRNA 似乎针对人类密码子进行了优化。这 19 核苷酸的序列包含了人类 MSH3 基因中 12 个编码 FCS PRRA 的核苷酸，可能通过在感染 SARS-CoV-2 人类细胞中复制选择重组机制介导入 SARS-CoV-2 基因中，并过表达 MSH3 基因，如上图所示。

##  SARS-CoV-2 刺突蛋白和 MSH3

这段序列中两个连续的 CGG 密码子的一个奇怪特性是编码 SARS-CoV-2 S 蛋白 PRRA 的弗林蛋白酶裂解位点。该精氨酸密码子在冠状病毒中很罕见：CGG在穿山甲 CoV 中的同义密码子相对使用度（RSCU）为 0，蝙蝠中为 0.08，SARA-CoV 为 0.19，MERS-CoV 中为 0.25，SARS-CoV-2 中为 0.299。

我们的 BLAST 检索结果发现，插入的这 12 个核苷酸与特异序列（Seq ID11652） 100% 反向互补配对，该序列在 2016 年 2 月 4 日的美国专利 9587003 中。Seq ID11652 检测结果显示 12 个核苷酸的匹配扩展插入到 19 个核苷酸序列：5′-CTACGTGCCCGCCGAGGAG-3′ （SEQ ID11652 的 2733-2751 个核苷酸），进而合成的 mRNA 将包含 3′- GAUGCACGGGCGGCUCCUC-5′ ，即 5′- CU **CCU CGG CGG GCA** CGU AG-3′ （SARS-CoV-2 基因组中 23547-23565 的核苷酸，其中四个加测的密码子产生 PRRA，刺突蛋白中 681–684 的氨基酸）。以上结果在 NCBI BLAST 数据库中非常罕见。

SARS-CoV-2 中这以序列和反向互补的特异性 mRNA 序列来源未知。传统的生物统计学分析表明，该序列随机出现在3万个核苷酸病毒基因组中的概率为 $3.21 \times 10^{-11}$ 。

{% asset_img 20220325130802.png 图2 %}

图2：研究中 19 核苷酸序列自然出现的可能性计算。SARS-CoV-2 基因组大约 30000 核苷酸长（P1）。专利序列约 3300 核苷酸长（P2）。专利的序列库包含 24712 个不同长度的序列，中位长度在 3300 左右。经典可能性计算给出人类基因组中的 19 核苷酸序列（也是专利序列库中序列之一）的自然出现概率。

特异序列 Seq ID11652 自上游开始读取，将编码与人类为 mutS 同源物 3（MSH3） 100% 匹配的氨基酸。MSH3 是 DNA 错配修复蛋白（MutS β 复合体的一部分）。Seq ID11652 转录为 MSH3 mRNA 似乎针对人类密码子进行了优化。除了 SARS-CoV-2，我们在任何的真核细胞或病毒基因组和 BLAST 数据库中均为发现这一 100% 重叠的 19 核苷酸序列。

## 讨论

使用密码子优化的 mRNA 序列替换 MSH3 在人体中表达，已在有错配修复失调的癌症中应用。但是在 SARS-CoV-2 中出现一片段完全反向互补的序列可能是随机的，同时其他可能也值得考虑。

已知过表达 MSH3 干扰错配修复（MSH2 从包含 MSH2 和 MSH6 的 MutS α 复合体中分离，导致 MSH6 降解和 MutS α 耗尽），这一功能具有病毒学意义。介导 DNA 错配修复将带来人呼吸道细胞甲型流感病毒易感性及致病性的增加。错配修复失调还会为 SARS-CoV-2 增加保护性。

CTCCTCGGCGGGCACGTA 在任何真核细胞或 BLAST 数据库的病毒基因组中都不存在，用来解释中间宿主重组，并不是其在 SARS-CoV-2 中出现的合理解释。在本病毒研究中，这一人类密码子优化的 mRNA 所编码人类 MSH3 的 100% 同源物无意中或故意诱导人类细胞系中的不匹配修复缺陷，并增加对 SARS 样病毒的易感性。使用 SARS 样病毒感染 SEQ ID11652-MSH3 转染的人类细胞将引发复制选择重组。SARA-CoV-2 和其他含正义链的单链 RNA 病毒通过在感染细胞胞质内启动q负链合成完成复制。负链 RNA 作为合成的正链RNA的模板，同时用于合成翻译非结构蛋白（复制和转录复合体），或新的病毒性衣壳。冠状病毒在感染早期同构基因组复制和 mRNA 翻译生成双连 RNA。

通过带反义链的 SARS-CoV-2 RNA 中间宿主中发生复制选择重组，将模板从一链转入另一链，可以利用过表达 MSH3 mRNA 正义链获取 FCS 的反向互补序列。SARS-CoV-2 和其他已知的冠状病毒之间的同源性是不连续的，同时大部分 SARS-CoV-2 序列是源 RaTG13 相对近的祖先。此外，相似性图（SimPlots）在两者序列之间发现的突变，是潜在重组事件的信号，这就可以解释 SARS-CoV-2 能通过 RBD 与 ACE2 结合，而 RaTG13 不能。

本假设的一个不足在于比对所用的序列在 Seq ID11652 另一链上开放阅读框内。但是使用 MSH3 转染细胞将诱导错配修复失调，导致双连 cDNA 编码 Seq ID11652。这种细胞与表达 RdRp 的 SARSS 样病毒共转染后，可以连接到这个 19 核苷酸序列，并允许从负f链中的一个片段（包括 FCS）整合到病毒基因组中，尽管其位于开放阅读框的另一链上。错配修复机制使得在实验模型中从反义链整合小片段成为可能。微同源性可以指导中 MSH3 和 SARS 样病毒之间的重组，就如发生在 19 个核苷酸序列上的一样。

这个出现在 SARS-CoV-2 中的 19 核苷酸 RNA 序列很不寻常，其能够编码位于刺突蛋白 681 处氨基酸的 FCS，且与特异 MSH3 mRNA 序列 100% 反向互补配对。它最可能的解释应当进一步调查。

## 补充材料

SEQ ID11652：
[FASTA](https://www.ncbi.nlm.nih.gov/nuccore/KH664781.1?report=fasta) [Graphics](https://www.ncbi.nlm.nih.gov/nuccore/KH664781.1?report=graph)

```palntext
# Sequence 11652 from patent US 9587003

GenBank: KH664781.1

LOCUS       KH664781                3387 bp    DNA     linear   PAT 14-OCT-2017
DEFINITION  Sequence 11652 from patent US 9587003.
ACCESSION   KH664781
VERSION     KH664781.1
KEYWORDS    .
SOURCE      Unknown.
  ORGANISM  Unknown.
            Unclassified.
REFERENCE   1  (bases 1 to 3387)
  AUTHORS   Bancel,S., Chakraborty,T., de Fougerolles,A., Elbashir,S.M.,
            John,M., Roy,A., Whoriskey,S., Wood,K.M., Hatala,P., Schrum,J.P.,
            Ejebe,K., Ellsworth,J.L. and Guild,J.
  TITLE     Modified polynucleotides for the production of oncology-related
            proteins and peptides
  JOURNAL   Patent: US [9587003](https://patft.uspto.gov/netacgi/nph-Parser?patentnumber=9587003)-B2 11652 07-MAR-2017;
            ModernaTX, Inc.; Cambridge, MA
  REMARK    CAMBIA Patent Lens: US [9587003](https://www.lens.org/lens/search/patent/list?q=US%209587003)
FEATURES             Location/Qualifiers
 source          1..3387
                     /organism="unknown"
                     /mol_type="genomic DNA" ORIGIN      
        1 atgagcagaa gaaagcccgc cagcggcggc ctggccgcca gcagcagcgc ccccgccaga
       61 caggccgtgc tgagcagatt cttccagagc accggcagcc tgaagagcac cagcagcagc
      121 accggcgccg ccgaccaggt ggaccccggc gccgccgccg ccgccgcccc ccccgccccc
      181 gccttccccc cccagctgcc cccccacatc gccaccgaga tcgacagaag aaagaagaga
      241 cccctggaga acgacggccc cgtgaagaag aaggtgaaga aggtgcagca gaaggagggc
      301 ggcagcgacc tgggcatgag cggcaacagc gagcccaaga agtgcctgag aaccagaaac
      361 gtgagcaaga gcctggagaa gctgaaggag ttctgctgcg acagcgccct gccccagagc
      421 agagtgcaga ccgagagcct gcaggagaga ttcgccgtgc tgcccaagtg caccgacttc
      481 gacgacatca gcctgctgca cgccaagaac gccgtgagca gcgaggacag caagagacag
      541 atcaaccaga aggacaccac cctgttcgac ctgagccagt tcggcagcag caacaccagc
      601 cacgagaacc tgcagaagac cgccagcaag agcgccaaca agagaagcaa gagcatctac
      661 acccccctgg agctgcagta catcgagatg aagcagcagc acaaggacgc cgtgctgtgc
      721 gtggagtgcg gctacaagta cagattcttc ggcgaggacg ccgagatcgc cgccagagag
      781 ctgaacatct actgccacct ggaccacaac ttcatgaccg ccagcatccc cacccacaga
      841 ctgttcgtgc acgtgagaag actggtggcc aagggctaca aggtgggcgt ggtgaagcag
      901 accgagaccg ccgccctgaa ggccatcggc gacaacagaa gcagcctgtt cagcagaaag
      961 ctgaccgccc tgtacaccaa gagcaccctg atcggcgagg acgtgaaccc cctgatcaag
     1021 ctggacgacg ccgtgaacgt ggacgagatc atgaccgaca ccagcaccag ctacctgctg
     1081 tgcatcagcg agaacaagga gaacgtgaga gacaagaaga agggcaacat cttcatcggc
     1141 atcgtgggcg tgcagcccgc caccggcgag gtggtgttcg acagcttcca ggacagcgcc
     1201 agcagaagcg agctggagac cagaatgagc agcctgcagc ccgtggagct gctgctgccc
     1261 agcgccctga gcgagcagac cgaggccctg atccacagag ccaccagcgt gagcgtgcag
     1321 gacgacagaa tcagagtgga gagaatggac aacatctact tcgagtacag ccacgccttc
     1381 caggccgtga ccgagttcta cgccaaggac accgtggaca tcaagggcag ccagatcatc
     1441 agcggcatcg tgaacctgga gaagcccgtg atctgcagcc tggccgccat catcaagtac
     1501 ctgaaggagt tcaacctgga gaagatgctg agcaagcccg agaacttcaa gcagctgagc
     1561 agcaagatgg agttcatgac catcaacggc accaccctga gaaacctgga gatcctgcag
     1621 aaccagaccg acatgaagac caagggcagc ctgctgtggg tgctggacca caccaagacc
     1681 agcttcggca gaagaaagct gaagaagtgg gtgacccagc ccctgctgaa gctgagagag
     1741 atcaacgcca gactggacgc cgtgagcgag gtgctgcaca gcgagagcag cgtgttcggc
     1801 cagatcgaga accacctgag aaagctgccc gacatcgaga gaggcctgtg cagcatctac
     1861 cacaagaagt gcagcaccca ggagttcttc ctgatcgtga agaccctgta ccacctgaag
     1921 agcgagttcc aggccatcat ccccgccgtg aacagccaca tccagagcga cctgctgaga
     1981 accgtgatcc tggagatccc cgagctgctg agccccgtgg agcactacct gaagatcctg
     2041 aacgagcagg ccgccaaggt gggcgacaag accgagctgt tcaaggacct gagcgacttc
     2101 cccctgatca agaagagaaa ggacgagatc cagggcgtga tcgacgagat cagaatgcac
     2161 ctgcaggaga tcagaaagat cctgaagaac cccagcgccc agtacgtgac cgtgagcggc
     2221 caggagttca tgatcgagat caagaacagc gccgtgagct gcatccccac cgactgggtg
     2281 aaggtgggca gcaccaaggc cgtgagcaga ttccacagcc ccttcatcgt ggagaactac
     2341 agacacctga accagctgag agagcagctg gtgctggact gcagcgccga gtggctggac
     2401 ttcctggaga agttcagcga gcactaccac agcctgtgca aggccgtgca ccacctggcc
     2461 accgtggact gcatcttcag cctggccaag gtggccaagc agggcgacta ctgcagaccc
     2521 accgtgcagg aggagagaaa gatcgtgatc aagaacggca gacaccccgt gatcgacgtg
     2581 ctgctgggcg agcaggacca gtacgtgccc aacaacaccg acctgagcga ggacagcgag
     2641 agagtgatga tcatcaccgg ccccaacatg ggcggcaaga gcagctacat caagcaggtg
     2701 gccctgatca ccatcatggc ccagatcggc agctacgtgc ccgccgagga ggccaccatc
     2761 ggcatcgtgg acggcatctt caccagaatg ggcgccgccg acaacatcta caagggccag
     2821 agcaccttca tggaggagct gaccgacacc gccgagatca tcagaaaggc caccagccag
     2881 agcctggtga tcctggacga gctgggcaga ggcaccagca cccacgacgg catcgccatc
     2941 gcctacgcca ccctggagta cttcatcaga gacgtgaaga gcctgaccct gttcgtgacc
     3001 cactaccccc ccgtgtgcga gctggagaag aactacagcc accaggtggg caactaccac
     3061 atgggcttcc tggtgagcga ggacgagagc aagctggacc ccggcgccgc cgagcaggtg
     3121 cccgacttcg tgaccttcct gtaccagatc accagaggca tcgccgccag aagctacggc
     3181 ctgaacgtgg ccaagctggc cgacgtgccc ggcgagatcc tgaagaaggc cgcccacaag
     3241 agcaaggagc tggagggcct gatcaacacc aagagaaaga gactgaagta cttcgccaag
     3301 ctgtggacca tgcacaacgc ccaggacctg cagaagtgga ccgaggagtt caacatggag
     3361 gagacccaga ccagcctgct gcactag
//
```

{% lg /images/xlsx.png %}
table1 | https://www.frontiersin.org/articles/file/downloadfile/834808_supplementary-materials_tables_1_xlsx/octet-stream/Table%201.XLSX/1/834808 | table1.xlsx
table2 | https://www.frontiersin.org/articles/file/downloadfile/834808_supplementary-materials_tables_2_xlsx/octet-stream/Table%202.XLSX/1/834808 | table1.xlsx
table3 | https://www.frontiersin.org/articles/file/downloadfile/834808_supplementary-materials_tables_3_xlsx/octet-stream/Table%203.XLSX/1/834808 | table1.xlsx
{% endlg %}

## 原文

{% pdf /2022/Potential-Recombination-Link-to-SARS-CoV-2/fviro-02-834808.pdf 600px %}

网页版链接
[Frontiers | MSH3 Homology and Potential Recombination Link to SARS-CoV-2 Furin Cleavage Site | Virology](https://www.frontiersin.org/articles/10.3389/fviro.2022.834808/full)
