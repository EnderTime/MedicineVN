label end_call:
    if p.times == 11:
        $p.times = 10
    call screen screen_index(p)
    hide screen info
    hide screen info2
    hide screen info3
    $p.times+=1
    jump TaskExecuting


label call_parents:
    if p.hadAskedForMoney:
        "算了……"
        "我已经管他们要过钱了。"
    elif p.meds()*p.price+p.money>500:
        "没什么必要还是不要给他们打电话了……"
    else:
        stop music fadeout 5
        "拨通了电话……"
        "……"
        mom"“[p.name]！好久没听到你声音啦！”"
        dad"“你在大城市找了份好工作啊，不愧是我的好儿子。”"
        dad"“爸爸妈妈在家里过的很好，开了一家超市，平时卖一些烟酒零食，也能养活得起自己，不用担心我们啦！”"
        mom"“是啊，我和你爸现在的日子过得很好，你只需要在那边好好上班，养活好自己就行啦！”"
        mom"“过年还回来不？啥时候找个女朋友啊？”"
        dad"“哎呀，你少说几句吧，不然他又不乐意了。”"
        mom"“宝贝打电话给爸妈有什么事呀？心情不好也可以来和妈聊聊，你都挺长时间没和我们说点啥了！”"
        menu:
            "要钱":
                mom"“啊……是这个事啊。”"
                mom"“你在那边工作困难的话，尽管和我们要钱就是，要是丢了工作或者受了欺负，就回家里就行。”"
                mom"“钱打过去了，爸妈不在你身边，你已经是个大人了，在那边照顾好自己啊。”"
                s"“嗯，没什么事我就挂了。”"
                mom"“妈啥也不懂，也就不多问了，怕你被我们问得烦。”"
                mom"“有啥事下次再打电话给我们啊。”"
                s"“嗯。”"
                play sound audio.interruption
                "……挂断了电话。"
                $p.hadAskedForMoney = True
                $p.money += 2000.0
                $showNotify(['X付宝到账：2000元！'])
    jump end_call

label call_Arnel:
    if p.times != 2:
        "这个时间给他打电话干什么……要请假还是早上请假好了……"
        jump end_call
    "给Arnel打电话。"
    "……"
    ar"“干嘛？又想请假？”"
    jump arnel_q


label arnel_q:
    menu:
        ar"“干嘛？又想请假？”{fast}"
        "请假":
            if p.hadAskedForLeave:
                ar"“你这周不是请过假了吗？”"
                ar"“我看你的工作也没完成多少啊，这么喜欢在家呆着那就去人事处办一下辞职手续吧？”"
                s"“……不……不用了……”"
                ar"“有话快说，我还忙着呢。”"
                jump arnel_q
            s"“是。”"
            ar"“请假回家睡觉？这样你就不会把口水流到桌子上了，噗哈哈哈。”"
            ar"“请呗？都可以请。”"
            ar"“不过公司不养闲人，也不养在工位上睡觉的人，你要干什么随你便，但是得在周五之前把该干的都给我干完了。”"
            ar"“公司不缺新员工，完不成工作就给我卷铺盖走人。”"
            s"“好。”"
            ar"“你这周的工资我已经给你扣了，建议你回去之后有时间把留给你们小组的那几个客户需求都写得明明白白的，好自为之吧。”"
            s"“嗯。”"
            "挂断了电话。"
            "呼，可以回家歇一会了。"
            "……"
            play music rareleisure
            $beforemusic=renpy.music.get_playing()
            scene workarea with fade  
            $p.wages = r2(p.wages * 0.9)
            $p.onVacation = True
            $p.stime(55)
            $p.checkTask()
            $p.hadAskedForLeave = True
            "光速打车回家了……"
            jump end_call
        "闲聊":
            s"“那个……最近我……在工位上睡觉的事……”"
            ar"“你给我打电话就因为这个？”"
            ar"“说些有用的吧。”"
            jump arnel_q
        "薪资问题":
            ar"“突然问我这个，是想好好工作了吗？”"
            ar"“虽然也指望不上你能超额帮组内分担任务，但是你能问我这个还是让我比较开心。”"
            ar"“那就来谈谈我们的完成度和薪资关系吧？”"
            ar"“超额完成任务时（>=120\%），必定获得成就感，具体薪水为当前面板薪水*完成度*1.1，并额外获得50~200块奖金，下周工资为2000*1.05^周数。”"
            ar"“正常完成任务时（>=100\%），75\%获得成就感，具体薪水为当前面板薪水*完成度，并额外获得0~50块奖金，下周工资为2000*1.03^周数。”"
            ar"“勉强算完成任务时（>=80\%），具体薪水为当前面板薪水*完成度*0.8，下周工资为1900*1.01^周数。”"
            ar"“完成半数任务时（>=50\%），具体薪水为当前面板薪水*完成度*0.6，下周工资为1900*1.00^周数。”"
            ar"“没有完成任务时（<50\%），具体薪水为当前面板薪水*完成度*0.55，下周工资为1900*1.00^周数。”"
            ar"“总结一下就是，尽量完成的越多越好，虽然这句话和废话一样就是了，但完成度超过120\%就可以稍微放松下，毕竟不能把你累死了。”"
            ar"“另外就是，下一周的工资和本周工资关系并不是太大，如果上周工资很少，只要这周努力点，很快就能恢复正常水平。”"
            ar"“就是这样。”"
            ar"“还有什么想问的吗？”"
            jump arnel_q
        "调情":
            s"“……”"
            s"“……那个。”"
            s"“今天有时间和我出来吃个晚饭吗？”"
            $temp=rd(0,13)
            if temp==0:
                ar"“你把你的活都干完了再约我出门吧。”"
            if temp==1:
                ar"“哟，你不是应该很讨厌我吗？”"
                ar"“想不到你也会对我感兴趣啊啊哈哈哈……”"
                ar"“等你长大一点再来约我吃饭吧？”"
            if temp==2:
                ar"“想透我？”"
            if temp==3:
                ar"“有时候看到你请假直接跑去医院，是不是就是着急治脑子啊？”"
            if temp==4:
                ar"“好了，再说就烦了。”"
            if temp==5:
                ar"“说点有用的行吗？”"
            if temp==6:
                ar"“你觉得现在是聊这个的时候吗？”"
            if temp==7:
                ar"“你认真的？”"
                ar"“带我吃楼下的麻辣烫还是扬州炒面啊？”"
            if temp==8:
                ar"“……别吧？”"
            if temp==9:
                ar"“无语，我是不是该联系一下人事部的人了。”"
            if temp==10:
                ar"“你给我打电话不会就因为这个吧？”"
            if temp==11:
                ar"“我还不如从咱们的楼层直接跳下去。”"
            if temp==12:
                ar"“呃，你是不是有病啊？”"
            if temp==13:
                ar"“公司帮你缴的电话费不是为了让你打电话和我开玩笑的。”"
            s"“呃……”"
            "我为什么要和这家伙聊这么久……"
            jump arnel_q
        "结束通话":
            s"“那个，也没什么事……”"
            ar"“下次想清楚了自己想说什么再打。”"
            s"“抱歉……”"
            play sound audio.interruption
            "电话中响起嘟嘟声。"
            jump end_call

label call_Pathos:
    "给Pathos打电话。"
    "……"
    pathos"“是我，有什么想问的就说吧，我赶时间。”"
    jump pathos_q


label pathos_q:
    menu:
        pathos"“是我，有什么想问的就说吧，我赶时间。”{fast}"
        "关于药物使用的疑问":
            pathos"“我就知道你没听我说话，算了，谁让我是你的专属医生呢？”"
            pathos"“使用一次药物后，再次使用相同的药物会降低恢复效率到33\%，使用其他的药物会降低恢复效率到50\%。”"
            pathos"“而隔一段时间后（再一次看到菜单界面），再次使用相同的药物会降低恢复效率到66\%，其他种类的药物的使用效率就不会被降低了。”"
            pathos"“再过一段时间，你就可以使用之前的药物了。”"
            pathos"“举个例子，早上吃，下午可以再吃；上午吃，睡前可以再吃；如果下午吃了，晚上就只能吃其他种类的药了。”"
            pathos"“不过例外的是，如果你晚上吃药，第二天早上不会受影响。”"
            pathos"“总之自己探索吧，有很多信息可以自己查看，不懂就问问别人？”"
            pathos"“哦，我差点忘了，似乎全球只有你有这种病。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "生病相关的疑问":
            pathos"“你是刚出生的孩子吗？这都不懂？”"
            pathos"“算了，可能吃那种药把你脑子都吃坏了。”"
            pathos"“首先生病的来源有两个，一个是平时工作太多，过劳的层数过多，也就是4层及以上，在第二天就会转化成生病。”"
            pathos"“另一个是阴冷天气，如果身体平时不多运动，很容易着凉感冒。”"
            pathos"“生病会降低基础属性，也会影响精神状态的消耗恢复和专注度等，尽量避免自己不要生病。”"
            pathos"“生病了的话，可以自己选择治愈的方式。”"
            pathos"“去医院治疗的话需要花一笔钱，越早越好；另一种方式是靠休息来恢复，以这种方法恢复会获得基础属性，而且不用花钱，缺点是需要消耗状态。”"
            pathos"“消耗良好的运动和良好的睡眠来提高恢复率，阴天也能让恢复率提升。”"
            pathos"“吃感冒药可以延长生病的时间来减缓病情，每天一片，能够按层数来增加休息治疗的概率。”"
            pathos"“受伤也能根据这个方法来恢复，但是偏执不能靠休息恢复。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "伤痕相关的疑问":
            pathos"“如果不去管生病的话，病情会恶化直到自愈，但是会给身体留下不可逆的损伤。”"
            pathos"“体弱会百分比降低属性，尽量不要获得。”"
            pathos"“另外有时候会莫名其妙多出来伤痕，可能是因为灵感过剩和酸痛堆积导致的，要经常关注一下自己的身体状况哦。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "实验药物保质期相关的疑问":
            pathos"“为什么保质期只有一周？”"
            pathos"“……这个，以后会告诉你的。”"
            pathos"“现在你还不需要知道。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "普通药物相关的疑问":
            pathos"“普通药物啊……就是普通人也会吃的那些药咯。”"
            pathos"“你所服用的实验药物都是快速见效的那种，正常人吃的药对你来说不仅恢复力弱，见效也慢。”"
            pathos"“反正具体效果自己看说明书吧，要遵循用法用量，一次性吃太多小心第二天下不来床哦。”"
            pathos"“如果你喜欢就去药房买点，我已经和下面的人说过了，你买什么处方药都不需要医嘱，只是不要买太多就行。”"
            pathos"“还有什么想问的吗？”"
            jump pathos_q
        "调情":
            s"“……”"
            s"“……那个。”"
            s"“今天有时间和我出来吃个晚饭吗？”"
            $temp=rd(0,13)
            if temp==0:
                pathos"“没时间。”"
            if temp==1:
                pathos"“下次。”"
                pathos"“最近很忙。”"
            if temp==2:
                pathos"“我今晚有约了。”"
            if temp==3:
                pathos"“如果你的精神状态还算良好，就不要对你的主治医师发情了。”"
            if temp==4:
                pathos"“其实我有男朋友的。”"
                pathos"“他今晚好不容易有时间陪我。”"
            if temp==5:
                pathos"“我拒绝。”"
            if temp==6:
                pathos"“没兴趣。”"
            if temp==7:
                pathos"“今天不行。”"
            if temp==8:
                pathos"“……”"
            if temp==9:
                pathos"“你没有其他的事可以做了吗？”"
            if temp==10:
                pathos"“别开玩笑，严肃点。”"
            if temp==11:
                pathos"“下次下次。”"
            if temp==12:
                pathos"“唉，我现在可是在上班时间诶，能不能说点正经的？”"
            if temp==13:
                pathos"“下次你这样我就要收费了。”"
            s"“好吧。”"
            jump pathos_q
        "结束通话":
            s"“没什么想问的了。”"
            pathos"“耽误我这么久连句谢谢都没有？”"
            s"“你真无聊……”"
            pathos"“呵呵。”"
            play sound audio.interruption
            "我挂断了电话。"
            jump end_call
