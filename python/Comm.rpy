init python:

    comm_names = ["设定委托", "同人清水委托", "甜文委托", "感伤委托", "色文委托", "设定背景委托", "人物背景故事委托", "外包游戏剧情文案", "网络游戏游戏世界观背景"]
    comm_informal_names = ["阳台", "窗户", "风", "都市", "眼皮", "愤怒", "入迷", "气泡，旋涡",
                        "放浪", "征服者", "我", "被害者", "假意", "研究", "撤离", "品味",
                        "恐惧", "余烬", "败者", "诋毁与拯救", "嘈杂", "吊兰调研笔记",
                        "外星生命调研笔记", "被捕食者调研笔记", "触摸", "与触手", "共浴",
                        "逝者", "水妖", "服务", "待命", "他和为他工作之人", "深入", "极寒",
                        "刻印", "鱼水", "报酬", "远行", "洗濯", "擢升", "奖励", "讨伐",
                        "晋升胸针", "断骨", "讴歌终焉之诗", "阿斯卡隆漫游指南", "活着", "未知之物"]


    class Comm:
        def __init__(self, player):
            def wri(p):
                return r2(ra(p, 75, 105) * 0.01 * player.wri())

            def genePrice():
                if WriterProof.hasByType(player):
                    pr = 0.9
                    pr += (player.wri() - 1) / 3
                    f = ((player.wri() - 1) / 3.5) + 1
                    while rra(player, 60):
                        pr += ra(player, 15 * f, 40 * f) * 0.01
                else:
                    pr = 0.75
                    pr += (player.wri() - 1) / 4
                    f = ((player.wri() - 1) / 4) + 1
                    r = 0
                    while rra(player, 60):
                        pr += ra(player, 5 * f, 25 * f) * 0.01
                return r2(pr)

            self.name = rca(player, comm_names)
            self.require = wri(player)
            self.priceFluctuation = genePrice()
            self.needWord = -1
            self.needInspiration = -1
            self.du = -1
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needWord = int(wri(player) ** 2 * 1000 * f())
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.needInspiration = ra(player, 20, 35)
            if rra(player, 40) or self.priceFluctuation > 1.5:
                self.du = ra(player, 14, 28)
            self.writeCounts = 0
            self.content = []
            self.info = ""
            self.inputs = None
            self.remarks = []
            self.broken = False

        def __eq__(self, other):
            if type(other) == type(
                    self) and other.du == self.du and other.require == self.require and other.content == self.content:
                return True
            else:
                return False

        def show(self):
            print('委托名:%s, 写作技巧需求:%s\n价格修正:%s倍' % (self.name, self.require, self.priceFluctuation))
            if self.needWord != -1:
                print('字数需求:%s ' % self.needWord, end='')
            else:
                print('无字数需求 ', end='')
            if self.needInspiration != -1:
                print('灵感需求:%s ' % self.needInspiration, end='')
            else:
                print('无灵感需求 ', end='')
            if self.du != -1:
                print('委托到期时间:%s' % self.du)
            else:
                print('无时间要求')

        def commInfo(self):
            info1 = '{size=+2}委托内容：' + self.name + '{/size}\n写作技巧需求：' + str(self.require) + '\n价格修正：' + str(
                int(self.priceFluctuation * 100)) + '%'
            if self.needWord != -1:
                info2 = '\n字数需求：' + str(self.needWord)
            else:
                info2 = '\n无字数需求 '
            if self.needInspiration != -1:
                info2 += '\n灵感需求：' + str(self.needInspiration)
            else:
                info2 += '\n无灵感需求 '
                
            if self.broken == True:
                info2 += '\n委托已超时'
            elif self.du != -1:
                info2 += '\n委托到期时间：' + str(self.du)
            else:
                info2 += '\n无时间要求'

            return info1 + info2

        def contentInfo(self):
            word = 0
            rewara = 0
            ins = 0
            for i in self.content:
                word += i[0]
                rewara += i[1]
                ins += i[2]
            return [int(word), r2(rewara), ins]

        def write(self, player):
            if player.retval1 is not None:
                self.inputs = player.retval1
                player.retval1 = None

            price = -0.052 * player.wri() ** 2 + 0.746 * player.wri() - 0.12 if player.wri() < 8 else 2.5
            price *= 180
            word = int(player.wri() ** 2 * 1000 * f())

            ins = 1
            if Inspiration.has(player):
                ins += Inspiration.get(player).stacks
                Inspiration.get(player).clear(player)
            if FixedInspiration.has(player):
                ins += FixedInspiration.get(player).stacks
                FixedInspiration.get(player).clear(player)

            value = ins * 0.1 * price * self.priceFluctuation * player.writeValuable

            if self.needInspiration != -1:
                value *= 1.1

            if self.du != -1:
                value *= 1.05

            if self.needWord != -1:
                value *= 1.05
                if word > self.needWord:
                    reward = value * self.needWord
                else:
                    reward = value * word
            else:
                reward = value * word

            reward /= player.sev()
            reward *= 0.001

            MentRezA.add(player, int(ins * 0.15))

            Notify.add('已进行一次写作，字数%s，价值%s元，消耗灵感%s层。' % (int(word), r2(reward), ins))

            g = int(ins / 15 + player.writingGain)

            if g >= 1:
                player.writing += g * 0.01
                Notify.add('额外获得%s点写作技巧。' % g)

            self.content.append([int(word), r2(reward), ins])
            self.writeCounts += 1

            word = 0
            rewara = 0
            ins = 0
            for i in self.content:
                word += i[0]
                rewara += i[1]
                ins += i[2]

            finished = 0

            if self.needWord != -1:
                if word >= self.needWord:
                    finished += 1
            else:
                if word > 0:
                    finished += 1

            if self.needInspiration != -1:
                if ins >= self.needInspiration:
                    finished += 1
            else:
                finished += 1


            if finished == 2:
                CommissionReward.add(player)
                cms = FinishedCommission(player)
                cms.comm = self
                return cms

            cms = UnfinishedCommission(player)
            cms.comm = self
            return cms

            # self.inputs.append(inputs)

        def checkWritable(self, player):
            if self.broken == True:
                return '委托已经超出期限！'
            if player.wri() < self.require:
                return '写作技巧未达要求！'
            if self.needInspiration != -1:
                ins = 0
                if Inspiration.has(player):
                    ins += Inspiration.get(player).stacks
                if FixedInspiration.has(player):
                    ins += FixedInspiration.get(player).stacks
                if ins < self.needInspiration - self.contentInfo()[-1]:
                    return '灵感层数未达要求！'
            return True

        def timeUpdate(self, player):
            if self.du > 0:
                self.du -= 1
                if self.du == 0:
                    self.broken = True
