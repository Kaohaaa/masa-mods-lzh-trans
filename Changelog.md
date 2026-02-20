# Changelog
这里是更新日志。

## R1.1
- 更新了一些翻译。

## B1.1.202602190303
- 更新了一些翻译。
- <details>
   <summary>新的版本命名规则确立</summary>

  1. 资源包分为`Release` `Alpha` `Beta` 三类。分别对应正式版、测试版、早期测试版。R1.0之前的版本都是Alpha版本，R1.0之后的所有测试版都是Beta版本。

  2. 正式版命名规则如下
  
     `摩挲改囊文言全譯 R{version}.zip`
     
     例如：摩挲改囊文言全譯 R1.0.zip

     其中`version`由两位有效数字组成。第一位为大版本号，第二位为大版本号的修订号。大版本号分配计划如下表所示：

     |序号|达成标志|大版本号|情况|
     |---|---|---|---|
     |1|资源包被Sakura合并|1.0|√已达成|
     |2|完成Litematica翻译|2.0|×未达成|
     |3|完成MaLiLib翻译|3.0|×未达成|
     |4|完成Tweakeroo翻译|4.0|×未达成|
     |5|完成MiniHUD翻译|5.0|×未达成|
     |6|完成Servux翻译|6.0|×未达成|
     |敬请期待|……|……|……|

   3. 测试版命名规则如下
   
      `摩挲改囊文言全譯 B{version}.{timestamp}.zip`

      例如：摩挲改囊文言全譯 B1.1.260219.zip

      其中`version`为对应预发布的正式版本号。`timestamp`为构建时间。

      > 注意，早期Alpha测试版以`摩挲改囊文言全譯_A{version}.zip`命名。因为之后不再会有Alpha版本（只有Beta版本），所以这种方式将不再使用。
    
      希望这能帮助你更好理解并下载本翻译包。
      </details>



## B1.1.0
- 更新了一些翻译
- 更新了 `pack.mcmeta`

## R1.0
- 这是本翻译包**第一个正式版**。
- 修改了``pack.png``和``pack.mcmeta``。
- Litematica翻译进度已达80%。
- Tweakeroo和MaLiLib翻译也有所推进。

## A0.7
- _重要变动：经由空岛明日川提出，"**Masa**"一词的文言译名由“**摩薩**”改为“**摩挲**”。（这是古汉语音译，与“摩挲”的现代意无关）_
- **Litematica**翻译进度已到达**67%**。
- 资源包适配版本增加至**1.21.10**。

## A0.6
1. 修改了```pack.mcmeta```中的文本
2. **Litematica**模组翻译进度已过**50%**。总进度已至**22%**。
3. 修复了一些翻译问题：
     
     ```litematica.config.hotkeys.name.executeOperation```-```施作```→```施行```
   
     ```litematica.config.hotkeys.name.cloneSelection```-```複製擇匡```→```複製選區```
   
     ```litematica.config.generic.name.pasteNbtRestoreBehavior```-```謄NBT之法```→```謄復NBT之法```
   
     ```litematica.config.generic.name.renderThreadNoTimeout```-```除繪失期```→```繪緒無期限```

     ```litematica.config.generic.name.entityDataSyncCacheTimeout```-```同調實體錄快取失期```→```同調實體錄快取期約```


## A0.5.1
添加新了的```pack.png```

## A0.5
新加入模组Servux的翻译支持。

## A0.4
1. 更改了**项目icon**。
2. 照常推动翻译进度。
3. 以后项目翻译进度不再写于Changelog，而是更新项目Description中的几个**Crowdin挂件**以展示进度。

## A0.3
1. 检查并解决了许多翻译错误。
2. 照常推进翻译进度，_现在**投影模组**所有的功能名称都确定了_ 剩余一些功能介绍未翻译。
    ### 当前翻译进度
    - litematica 34%
    - malilib 6%
    - minihud 2%
    - tweakeroo 2%
    - 总进度 14%

## A0.2.1
1. **修复了一些 Alpha 0.2版本 的翻译问题。**
2. 更改资源包名称为「摩薩改囊文言全譯」。
3. 略微推进翻译进度
    ### 当前翻译进度
    - litematica 29%
    - malilib 5%
    - minihud 2%
    - tweakeroo 2%

## A0.2
1. **更改了游戏版本**。

    ### 当前翻译进度
    - litematica 28%
    - malilib 4%
    - minihud 2%
    - tweakeroo 2%

## A0.1
Alpha测试第一个版本，相当原始，进度超级低。