
label Sleep_beginning:
    scene bedroom with fade
    "是的，休息。"
    "我会听你的命令。"
    call Task_processing from _call_Task_processing_6
    $p.times+=1
    $Sleep.executeTask(p)

label Sleep_result_exce:
    scene bedroom with fade
    $Notify.show()
    "睡了一个好觉，做了一个好梦。"
    $p.times+=1
    jump TaskExecuting

label Sleep_result_good:
    scene bedroom with fade
    $Notify.show()
    "无梦，就像右键床铺直接跳到下一回合一样舒畅。"
    $p.times+=1
    jump TaskExecuting

label Sleep_result_norm:
    scene bedroom with fade
    $Notify.show()
    "至少病痛没有在梦里伴随着我。"
    $p.times+=1
    jump TaskExecuting

label Sleep_result_bad:
    scene bedroom with fade
    $Notify.show()
    "做了一个噩梦……但是至少算是休息。"
    $p.times+=1
    jump TaskExecuting


label ComputerGaming_beginning:
    scene workarea with fade
    "也许应该把时间放在其他地方，但游戏放在库里不玩都要臭了。"
    "我按下家里台式的开机键。"
    "就这样消磨多余的时间精力也好……"
    call Task_processing from _call_Task_processing_7
    $p.times+=1
    $ComputerGaming.executeTask(p)

label ComputerGaming_result_exce:
    scene workarea with fade
    $Notify.show()
    "嗨！我直接进行一个横冲直撞！"
    "至少游戏里的我天下无敌，至少游戏里的我就算死了也能重新复活……"
    $p.times+=1
    jump TaskExecuting

label ComputerGaming_result_good:
    scene workarea with fade
    $Notify.show()
    "哦！在我的努力奋斗下，至少我们把这该死的火狼杀掉了。"
    "要是我的脑袋不痛的话这波该是绝杀。"
    $p.times+=1
    jump TaskExecuting

label ComputerGaming_result_norm:
    scene workarea with fade
    $Notify.show()
    "一局普通的游戏罢了。"
    "既不刺激，也不无聊。"
    "也许应该把时间放在其他地方。"
    $p.times+=1
    jump TaskExecuting

label ComputerGaming_result_bad:
    scene workarea with fade
    $Notify.show()
    "该死……这群人都是什么废物。"
    "头疼……这游戏真是一秒都不想玩了。"
    $p.times+=1
    jump TaskExecuting


label CleanRoom_beginning:
    scene workarea with fade
    "啊……垃圾桶里的那个，是不是上周吃剩的外卖盒子啊……"
    "看来真得打扫卫生……"
    call Task_processing from _call_Task_processing_8
    $p.times+=1
    $CleanRoom.executeTask(p)

label CleanRoom_result:
    scene workarea with fade
    $Notify.show()
    "房间干净了很多诶，这样就算是在家里赶工也能不会感觉很烦躁吧……"
    $p.times+=1
    jump TaskExecuting



label DoNothing_beginning:
    scene workarea with fade
    "这样么……我明白了。"
    call Task_processing from _call_Task_processing_9
    $p.times+=1
    $DoNothing.executeTask(p)

label DoNothing_result:
    scene workarea with fade
    $Notify.show()
    "谢谢你，我终于能有机会花时间做我自己真正想做的事。"
    $p.times+=1
    jump TaskExecuting


#0.4尚未开放
label SocialMedia_beginning:
    scene agonal with fade
    "当前日程尚未完成文案。"
    call Task_processing from _call_Task_processing_10
    $p.times+=1
    $SocialMedia.executeTask(p)

label SocialMedia_result_exce:
    scene agonal with fade
    $Notify.show()
    "当前日程尚未完成文案。"
    $p.times+=1
    jump TaskExecuting

label SocialMedia_result_good:
    scene agonal with fade
    $Notify.show()
    "当前日程尚未完成文案。"
    $p.times+=1
    jump TaskExecuting

label SocialMedia_result_norm:
    scene agonal with fade
    $Notify.show()
    "当前日程尚未完成文案。"
    $p.times+=1
    jump TaskExecuting

label SocialMedia_result_bad:
    scene agonal with fade
    $Notify.show()
    "当前日程尚未完成文案。"
    $p.times+=1
    jump TaskExecuting