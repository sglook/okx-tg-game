# okx-tg-game

this is a script about okx game in telegram 欧易在tg里积分赛车空投小游戏脚本

**本代码用于欧易在telegram小程序点击获得积分空投奖励**

打开小程序利用<a href = "https://github.com/zhuolhc/okx-tg-game/blob/main/coordinate.py">coordinate.py</a> 获取上涨和下跌坐标位置

然后将输出的坐标填写在<a href = "https://github.com/zhuolhc/okx-tg-game/blob/main/script.py">script.py</a>相应位置中

由于本游戏机制是在连续点击情况下获胜获得更多奖励于是策略为一次性点击完后休息至结束

实测连续点击赛车奔跑+结算时间 = 8.5s 恢复时间为1箱油 = 90s

本脚本方案为初始计划10油箱，等待时间10 ✖️ 90 - 10 ✖️ 8.5 = 815s

本策略为交替点击，可自行更改（实测上涨概率更大些）
