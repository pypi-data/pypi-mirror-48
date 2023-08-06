# -*- coding: utf-8 -*-
import numpy as np
import geatpy as ea

class CON(ea.Problem): # 继承Problem父类
    def __init__(self, M = 2):
        self.name = 'CON' # 初始化name（函数名称，可以随意设置）
        self.M = M # 初始化M（目标维数）
        self.maxormins = [1] * self.M # 初始化maxormins（目标最小最大化标记列表）
        self.Dim = 2 # 初始化Dim（决策变量维数）
        self.varTypes = np.array([0] * self.Dim) # 初始化varTypes（决策变量的类型）
        lb = [0.1, 0] # 决策变量下界
        ub = [1, 5] # 决策变量上界
        self.ranges = np.array([lb, ub]) # 初始化ranges（决策变量范围矩阵）
        lbin = [1] * self.Dim
        ubin = [1] * self.Dim
        self.borders = np.array([lbin, ubin]) # 初始化borders（决策变量范围边界矩阵）
    
    def aimFuc(self, Vars, CV):
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        f1 = x1
        f2 = (1 + x2) / x1
#        # 采用罚函数法处理约束
#        exIdx1 = np.where(x2 + 9*x1 < 6)[0]
#        exIdx2 = np.where(-x2 + 9 * x1 < 1)[0]
#        exIdx = np.unique(np.hstack([exIdx1, exIdx2]))
#        f1[exIdx] = f1[exIdx] + np.max(f1) - np.min(f1)
#        f2[exIdx] = f2[exIdx] + np.max(f2) - np.min(f2)
        # 采用可行性法则处理约束
        CV = np.hstack([6 - x2 - 9*x1,
                       1 + x2 - 9 * x1])
        
        return np.hstack([f1, f2]), CV
    
    