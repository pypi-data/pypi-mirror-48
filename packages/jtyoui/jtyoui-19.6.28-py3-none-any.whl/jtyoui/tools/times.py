#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2019/4/24 17:29
# @Author: Jtyoui@qq.com
from jtyoui.data import chinese_mon_number, add_time
import re
import datetime
import time
import itertools
import copy


class StringTime:
    def __init__(self, sentence, date_str=None, date_format='%Y-%m-%d %H:%M:%S'):
        """传入一个字符串时间和现在时间。
        >>> st = StringTime('二零零七年十月三十一号下午2点半')
        >>> print(st.find_times())
        :param sentence: 字符串时间
        :param date_str: 你认为的现在时间，不传默认是当前时间
        :param date_format:时间格式
        """
        self._sentence = sentence
        self._localtime = date_str if date_str else time.strftime(date_format)
        self.format = date_format
        # 自定义
        self.local = time.strptime(self._localtime, self.format)
        self.re_year = r'(今年)|(明年)|(后年)|(昨年)|(前年)|(去年)|(\d*年)'
        self.re_mon = r'(上个月)|(这个月)|(下个月)|(上月)|(这月)|(下月)|(\d*月)'
        self.re_day = r'(今天)|(明天)|(后天)|(昨天)|(前天)|(\d*日)|(\d*号)'
        self.re_week = r'(上周)|(下周)|(上个周)|(下个周)|(星期日)|(星期天)|(星期\d*)'
        self.re_hour = r'(早上)|(下午)|(\d*点)'
        self.re_min = r'(\d*分)|(\d*点半)'
        self.re_sec = r'(\d*秒)'
        self.now_year = self.local.tm_year
        self.now_mon = self.local.tm_mon
        self.now_day = self.local.tm_mday
        self.now_week = self.local.tm_wday + 1
        self.chinese_numerals = copy.deepcopy(chinese_mon_number)
        self.chinese_numerals.pop('十')
        self.add_time = add_time

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, sentence):
        self._sentence = sentence

    def adds(self, x, fmt):
        add = datetime.datetime.strptime(self._localtime, self.format) + datetime.timedelta(days=x)
        return add.strftime(fmt)

    def find(self, name):
        """根据名字来查找年月日号
        ：:param name:填写：年、月、日、号、来找对应的日期
        """
        if name == '年':
            flag = '%Y'
            re_ = self.re_year
        elif name == '月':
            flag = '%M'
            re_ = self.re_mon
        elif name == '日' or name == '号':
            flag = '%d'
            re_ = self.re_day
        elif name == '周':
            flag = '%d'
            re_ = self.re_week
        else:
            flag = None
            re_ = ''
        date_time, day, add = [], 0, 0
        for d in re.findall(re_, self.sentence):
            for i in d:
                if i:
                    if i in ['星期日', '星期天']:
                        day = 7 - self.now_week
                    elif '星期' in i and i[-1].isdigit():
                        week = int(i[-1])
                        day = week - self.now_week
                    elif '周' in i:
                        add = self.add_time[i]
                    else:
                        if i in self.add_time:
                            date_time.append(self.adds(self.add_time[i], flag))
                        elif name in i:
                            if i[:-1].isdigit():
                                date_time.append(i[:-1])
        if day != 0 or add != 0:
            days = self.adds(day + add, flag)
            if int(days) >= self.now_day:
                date_time.append(days)
            else:
                date_time.append(days)
                return date_time, 1
        return date_time if date_time else []

    def find_hour(self):
        """找对应的小时"""
        hours = []
        flag = 0
        for d in re.findall(self.re_hour, self.sentence):
            for i in d:
                if i:
                    if i == '早上':
                        flag = 0
                    elif i == '下午':
                        flag = 12
                    else:
                        if i[:-1].isdigit():
                            hours.append(int(i[:-1]) + flag)
                        else:
                            hours.append(0)
        return hours if hours else []

    def find_min(self):
        """找对应的分钟"""
        minute = []
        for d in re.findall(self.re_min, self.sentence):
            for i in d:
                if i:
                    if i[:-1].isdigit():
                        minute.append(int(i[:-1]))
                    elif '半' in i:
                        minute.append(30)
        return minute if minute else []

    def find_sec(self):
        """找对应的秒钟"""
        second = []
        for d in re.findall(self.re_sec, self.sentence):
            if d:
                if d[:-1].isdigit():
                    second.append(d[:-1])
        return second if second else []

    def find_times(self):
        """ 根据一句话来找对应的时间"""
        str_ = [self.chinese_numerals.get(s, s) for s in self.sentence] + [' ']  # 加[' ']的原因保证index+1不会出现list索引溢出
        string = ''
        for index, c in enumerate(str_):  # 判断十在每个位置上的不同意义
            if c == '十':
                if str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：二十一实际上十可以取空，变成21
                    c = ''
                elif str_[index - 1].isdigit() and (not str_[index + 1].isdigit()):  # 比如：二十实际上十变成0，变成20
                    c = '0'
                elif not str_[index - 1].isdigit() and str_[index + 1].isdigit():  # 比如：十三实际上十变成1，变成13
                    c = '1'
                else:
                    c = '10'  # 其余情况十就变成10
            string += c
        self._sentence = string
        y = self.find('年')  # 找到一句话中的年份
        m = self.find('月')  # 找到一句话中的月份
        d = self.find('号')  # 找到一句话中的天数
        d = d + self.find('日')  # 找到一句话中的天数
        w = self.find('周')  # 找到一句话中的天数
        if isinstance(w, tuple):
            if m:
                m[0] = int(m[0]) + w[1]
            else:
                m = [self.now_mon + w[1]]
            d += d + w[0]
        else:
            d += d + w
        h = self.find_hour()  # 找到一句话中的小时
        mi = self.find_min()  # 找到一句话中的分钟
        sec = self.find_sec()  # 找到一句话中的秒钟
        for y_, m_, d_, h_, mi_, sec_ in itertools.zip_longest(y, m, d, h, mi, sec):
            if not y_ and not m_ and not d_:
                return '未找到时间年月日'
            if not y_ and m_:
                y_ = self.now_year
            if not m_ and d_:
                if not y_:
                    y_ = self.now_year
                m_ = self.now_mon
            if not mi_:
                mi_ = '00'
            if not sec_:
                sec_ = '00'
            if not m_:
                return f'{y_}'
            elif not d_:
                return f'{y_}-{m_:0>2}'
            elif not h_:
                return f'{y_}-{m_:0>2}-{d_:0>2}'
            else:
                return f'{y_}-{m_:0>2}-{d_:0>2} {h_:0>2}:{mi_:0>2}:{sec_:0>2}'
        else:
            return '未找到时间'


if __name__ == '__main__':
    # 默认是当日期
    st = StringTime('二零零七年十月三十一号下午2点半')
    print(st.find_times())
    st.sentence = '下周星期一下午2点半开会'
    print(st.find_times())
    print('-----------------------------------')
    # 切换日期
    st = StringTime('下周星期一下午2点半开会', '2019-4-17 00:00:00')
    print(st.find_times())
