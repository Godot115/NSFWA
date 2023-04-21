# -*- coding: utf-8 -*-
# @Time    : 10/29/22 00:03
# @Author  : godot
# @FileName: main.py
# @Project : pyOED
# @Software: PyCharm
import time

import numpy as np

from algorithms.algorithm_util import AlgorithmUtil
from models.custom_model import CustomModel
from models.model5 import Model5
from models.model_util import ModelUtil

if __name__ == '__main__':
    # model = CustomModel("t_1*x_1 + t_2 * x_2 + t_3 * x_1 * x_2",
    #                     ["x_1", "x_2"],
    #                     ["t_1", "t_2", "t_3"],
    #                     [1, 1, 1])
    # lb = [0.01, 0.01]
    # ub = [10, 10]
    # grid_size = 11
    # model_util = ModelUtil(model, "D-optimal", lb, ub, grid_size)

    # model = CustomModel("(t_1*x_1*x_1 + t_2*x_2*x_2 + t_3*x_1*x_2 + t_4*x_1*x_2*e**x_3)/(t_5**x_4)",
    #                     ["x_1", "x_2", "x_3", "x_4"],
    #                     ["t_1", "t_2", "t_3", "t_4", "t_5"],
    #                     [1, 1, 1, 1, 1])
    # lb = [0.01, 0.01, 0.01, 0.01]
    # hb = [10, 10, 10, 10]
    # grid_size = 11
    # model_util = ModelUtil(model, "D-optimal", lb, hb, grid_size)

    # case 2:
    # model = Model5([349.0268, 1067.0434, 0.7633, 2.6055])
    # model_util = ModelUtil(model, "D-optimal", [[1, 2500]], 10000)

    # case 3:

    # model = CustomModel(
    #     "beta_0 + beta_1 * x_1 + beta_2 * x_2 +beta_3 * x_3 + beta_4 * x_4 + beta_5 * x_1*x_2 + beta_6 * x_1*x_3 + beta_7 * x_1*x_4 + beta_8 * x_1*x_2*x_3",
    #     ["x_1", "x_2", "x_3", "x_4"],
    #     ["beta_0", "beta_1", "beta_2", "beta_3", "beta_4", "beta_5", "beta_6", "beta_7", "beta_8"],
    #     [-20.8709, 8.2127, -0.9426, -2.0756, 31.2762, 0.6642, 0.7178, -11.1521, -0.0969])
    # restrictions = [[1950, 2450], [1, 3.5], [0.5, 3.5], [8300, 9000]]
    # lb = [1950, 1, 0.5, 8300]
    # hb = [2450, 3.5, 3.5, 9000]
    # grid_size = 10
    # model_util = ModelUtil(model, "D-optimal", lb, hb, grid_size)

    # case 4: 枯草杆菌Bacillus与培养基环境试验
    # x_1 Methanol (ml)
    # x_2 Ethanol (ml)
    # x_3 Propanol (ml)
    # x_4 Butanol (ml)
    # x_5 pH
    # x_6 Time (h)
    # y_1 Growth (mg)
    # model = CustomModel(
    #     "beta_0+ beta_1*x_1 + beta_2 * x_2 + beta_3 * x_3 + beta_4* x_4 + beta_5 * x_5 + beta_6 * x_6 + beta_7*x_2 *x_3",
    #     ["x_1", "x_2", "x_3", "x_4", "x_5", "x_6"],
    #     ["beta_0", "beta_1", "beta_2", "beta_3", "beta_4", "beta_5", "beta_6", "beta_7"],
    #     [27.79, 9.0, 4.27, 1.0, 1.8, -3.07, 4.63, -1.77])
    # lb = [0, 0, 0, 0, 6, 1]
    # hb = [10, 10, 10, 10, 9, 2]
    # grid_size = 10
    # model_util = ModelUtil(model, "D-optimal", lb, hb, grid_size)

    # case
    # model = CustomModel(
    #     "beta_0+ beta_1*x_1 + beta_2 * x_2 + beta_3* x_3 + beta_4 * x_4 + beta_5 * x_5",
    #     ["x_1", "x_2", "x_3", "x_4", "x_5"],
    #     ["beta_0", "beta_1", "beta_2", "beta_3", "beta_4", "beta_5"],
    #     [27.79, 9.0, 1.0, 1.8, -3.07, 4.63])
    # restrictions = [[0, 10], [0, 10], [0, 10], [6, 9], [1, 2]]
    # grid_size = 10
    # model_util = ModelUtil(model, "D-optimal", restrictions, grid_size)

    # MM
    # model = CustomModel("t_1 *x/(x+t_2)",
    #                     ["x"],
    #                     ["t_1", "t_2"],
    #                     [1, 1])
    # model_util = ModelUtil(model, "D-optimal", lb=[0.01], hb=[2000], grid_size=1001)

    # Exponential
    model = CustomModel("t_0+t_1 * e**(x_1+x_2+x_3/t_2)",
                        ["x_1", "x_2", "x_3"],
                        ["t_0", "t_1", "t_2"],
                        [1, 1, 200])
    model_util = ModelUtil(model, "D-optimal", lob=[0] * 3, hib=[10] * 3, grid_size=11)
    star = model_util.generate_star_set((5, 5, 5))
    point_len = len(list(star)[0])
    star = [int(s) for i in star for s in i]
    star_res = []
    for i in range(0, len(star), point_len):
        star_res.append(tuple(star[i:i + point_len]))

    print(sorted(star_res))
    threshole = 1e-6

    au = AlgorithmUtil(model_util, "rex", threshole)
    start = time.time()
    au.start()
    # print(len(au.generate_star_set((0.01, 0.01))))
    print(au.algorithm, time.time() - start)
    print("c_val: ", au.criterion_val)
    print("eff: ", au.eff)
    print("det", au.model_util.get_det_fim())
    # print(au.design_points)
    # au.plot_eq()
    #######################################

    # au = AlgorithmUtil(model_util, "rex", threshole)
    #
    # start = time.time()
    # au.start()
    # # print(len(au.generate_star_set((0.01, 0.01))))
    # print(au.algorithm, time.time() - start)
    # print("c_val: ", au.criterion_val)
    # print("eff: ", au.eff)
    #
    # au = AlgorithmUtil(model_util, "fwa", threshole)
    #
    # start = time.time()
    # au.start()
    # # print(len(au.generate_star_set((0.01, 0.01))))
    # print(au.algorithm, time.time() - start)
    # print("c_val: ", au.criterion_val)
    # print("eff: ", au.eff)
    #
    # au = AlgorithmUtil(model_util, "mul", threshole)
    #
    # start = time.time()
    # au.start()
    # # print(len(au.generate_star_set((0.01, 0.01))))
    # print(au.algorithm, time.time() - start)
    # print("c_val: ", au.criterion_val)
    # print("eff: ", au.eff)
