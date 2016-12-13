#!/usr/bin
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import tree
import sklearn.ensemble as ske
import VerificationCodeGenerator as generator
import VerificationCodeSpliter as spilter
import os
import shutil
#保存结果
def saveResult(result,filename):
    """
    保存预测结果
    第一行为: ImageId,Label
    后面为: {id},{predictValue}
    :param result: 预测结果集
    :param filename: 存储文件名
    """
    file_handler = open(filename, 'w')
    file_handler.write("ImageId,Label\n")
    index = 0
    for value in result.flat:
        index += 1
        file_handler.write("%d,%d\n" % (index, value))
    file_handler.flush()
    file_handler.close()


def predict(x_train, y_train, test_df, model):
    """
    使用model来训练和预测
    :param x_train: 训练集合特征
    :param y_train: 训练集合输出
    :param test_df: 测试集合
    :param model: 预测模型
    :return: 预测值集合
    """
    model.fit(X_train, Y_train)
    predictResult = model.predict(test_df)
    return predictResult



#main

if(os.path.isdir("image")):
    shutil.rmtree("image")
if(os.path.isdir("image2")):
    shutil.rmtree("image2")
if(os.path.isdir("matrix")):
    shutil.rmtree("matrix")
os.mkdir("image")
os.mkdir("image2")
os.mkdir("matrix")

# 生成训练样例图片
generator.gene_easyVerificationCode(100, "/home/zhongjianlv/ML/VerificationCodeRecognition/image/",
                                    "/usr/share/fonts/truetype/ubuntu-font-family/")

#生成测试样例图片
generator.gene_easyVerificationCode(10, "/home/zhongjianlv/ML/VerificationCodeRecognition/image2/",
                          "/usr/share/fonts/truetype/ubuntu-font-family/")

basepath = "/home/zhongjianlv/ML/VerificationCodeRecognition/"

#训练图片转csv
spilter.split(basepath+"image/", basepath + "matrix/train.csv")

#测试图片转csv
spilter.split(basepath + "image2/", basepath + "matrix/test.csv")

#读取训练数据和测试数据
train_df = pd.read_csv('matrix/train.csv')
# test_df = pd.read_csv('test.csv')
X_train = train_df.drop('label', axis=1).values
Y_train = train_df['label'].values

#决策树
decisionTree_clf = tree.DecisionTreeClassifier()
# predictResult = predict(X_train, Y_train, test_df, decisionTree_clf)
#输出
# saveResult(predictResult, 'decisionTree_submission.csv')

#随机森林
randomForest_clf = ske.RandomForestClassifier()
# predictResult = predict(X_train, Y_train, test_df, randomForest_clf)
#输出
# saveResult(predictResult, 'randomForest_submission.csv')

test_df = pd.read_csv("matrix/test.csv")
X_test = test_df.drop('label', axis=1).values
Y_test = test_df['label'].values
print Y_test
randomForest_clf.fit(X_train, Y_train)
predictResult = randomForest_clf.predict(X_test)
print predictResult

# 5 [253, 255, 255, 236, 253, 231, 125, 137, 99, 0, 11, 10, 3, 2, 1, 1, 1, 1, 1, 1, 0, 4, 5, 113, 132, 135, 131, 243, 251, 158, 148, 23, 32, 26, 0, 0, 0, 5, 3, 5, 3, 2, 1, 1, 1, 1, 1, 1, 0, 7, 2, 0, 0, 0, 0, 30, 248, 0, 0, 0, 0, 0, 6, 8, 15, 5, 6, 8, 6, 4, 4, 4, 4, 4, 4, 4, 4, 8, 7, 9, 14, 10, 9, 0, 248, 5, 5, 1, 2, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 248, 0, 1, 0, 1, 3, 2, 15, 85, 174, 170, 177, 176, 178, 177, 177, 177, 177, 177, 177, 178, 174, 178, 63, 44, 41, 45, 0, 248, 0, 1, 0, 0, 4, 1, 75, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 161, 248, 0, 1, 0, 0, 3, 0, 46, 254, 238, 245, 247, 246, 248, 248, 250, 247, 247, 250, 247, 250, 251, 252, 254, 253, 255, 253, 255, 248, 0, 1, 0, 2, 2, 22, 154, 251, 244, 247, 250, 240, 251, 251, 249, 253, 251, 250, 255, 255, 255, 255, 255, 255, 255, 255, 251, 248, 0, 1, 0, 3, 0, 60, 255, 244, 255, 255, 255, 255, 255, 247, 252, 244, 248, 252, 248, 253, 255, 255, 255, 255, 255, 255, 255, 248, 0, 1, 0, 2, 0, 53, 255, 232, 174, 170, 173, 171, 216, 255, 255, 255, 255, 255, 255, 253, 252, 253, 255, 255, 255, 255, 255, 245, 0, 4, 2, 1, 1, 17, 61, 40, 0, 0, 0, 0, 23, 59, 63, 60, 145, 199, 189, 252, 255, 255, 247, 248, 254, 253, 255, 248, 0, 2, 16, 0, 5, 9, 0, 2, 6, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 59, 176, 211, 255, 242, 252, 248, 245, 244, 5, 10, 0, 11, 0, 0, 0, 7, 22, 0, 0, 0, 0, 8, 11, 8, 9, 9, 5, 0, 0, 0, 190, 255, 255, 245, 251, 242, 0, 0, 31, 16, 40, 138, 133, 180, 223, 134, 146, 80, 15, 2, 0, 8, 6, 4, 5, 5, 7, 7, 2, 103, 232, 255, 248, 249, 118, 129, 247, 239, 245, 255, 255, 255, 255, 255, 255, 255, 238, 175, 54, 0, 0, 8, 1, 1, 0, 9, 2, 0, 15, 126, 251, 255, 255, 255, 255, 255, 255, 250, 251, 252, 253, 251, 251, 255, 253, 255, 242, 149, 27, 3, 8, 4, 2, 1, 5, 11, 0, 0, 247, 255, 250, 250, 254, 254, 254, 255, 255, 255, 255, 255, 255, 250, 250, 248, 243, 255, 149, 23, 7, 6, 6, 2, 1, 3, 2, 15, 47, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 251, 252, 255, 241, 255, 86, 0, 9, 4, 4, 3, 3, 8, 3, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 253, 252, 253, 251, 245, 252, 78, 0, 8, 1, 1, 3, 1, 2, 0, 5, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 254, 252, 252, 253, 245, 255, 80, 0, 6, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 253, 250, 252, 250, 243, 247, 76, 0, 6, 0, 0, 0, 0, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 250, 248, 246, 249, 255, 101, 5, 10, 3, 0, 0, 0, 0, 0, 0, 3, 254, 252, 255, 252, 252, 253, 252, 253, 253, 252, 253, 252, 255, 255, 255, 200, 79, 10, 8, 5, 1, 0, 0, 0, 0, 3, 3, 0, 245, 255, 242, 255, 255, 255, 255, 255, 255, 255, 255, 255, 227, 176, 114, 13, 0, 0, 0, 2, 4, 2, 6, 2, 9, 0, 0, 73, 255, 201, 255, 194, 189, 193, 194, 195, 156, 61, 65, 59, 31, 0, 0, 4, 14, 6, 9, 7, 14, 0, 0, 0, 0, 53, 190, 255, 74, 0, 79, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 14, 11, 0, 0, 0, 0, 0, 0, 30, 46, 45, 158, 255, 255, 246, 0, 2, 0, 8, 4, 5, 11, 3, 1, 0, 0, 0, 0, 0, 0, 12, 33, 34, 27, 124, 159, 232, 255, 253, 255, 250, 251, 247, 9, 1, 6, 3, 6, 1, 2, 1, 40, 132, 128, 132, 132, 136, 133, 197, 252, 252, 247, 255, 255, 255, 253, 252, 253, 252, 253, 254]
# 8 [255, 255, 255, 255, 255, 255, 255, 254, 255, 253, 252, 255, 255, 255, 255, 237, 159, 103, 7, 1, 4, 3, 3, 82, 133, 248, 255, 251, 255, 255, 255, 251, 255, 249, 251, 248, 252, 255, 255, 236, 238, 151, 101, 21, 0, 0, 9, 2, 3, 2, 6, 0, 0, 55, 192, 250, 255, 255, 255, 252, 253, 253, 244, 251, 245, 240, 125, 13, 21, 0, 0, 0, 0, 0, 0, 2, 5, 3, 5, 9, 9, 0, 0, 199, 255, 255, 255, 249, 253, 245, 255, 243, 140, 13, 0, 4, 4, 0, 0, 17, 94, 58, 91, 0, 2, 6, 5, 3, 8, 7, 0, 197, 255, 255, 255, 252, 249, 255, 153, 23, 6, 0, 5, 0, 2, 108, 150, 238, 255, 249, 255, 178, 27, 8, 1, 2, 4, 9, 11, 203, 255, 255, 255, 248, 251, 175, 12, 0, 5, 0, 27, 128, 185, 255, 255, 255, 252, 251, 245, 255, 58, 0, 5, 6, 12, 0, 128, 253, 255, 255, 251, 255, 166, 0, 8, 5, 9, 9, 217, 255, 255, 248, 244, 250, 252, 248, 245, 241, 49, 2, 7, 11, 0, 24, 198, 252, 255, 254, 255, 129, 8, 2, 5, 8, 0, 163, 255, 240, 246, 250, 247, 254, 254, 244, 255, 131, 3, 13, 9, 0, 24, 174, 255, 245, 254, 254, 246, 15, 0, 4, 3, 10, 0, 191, 255, 240, 249, 253, 252, 249, 243, 252, 204, 56, 3, 5, 0, 3, 217, 255, 246, 251, 247, 255, 89, 5, 4, 0, 1, 2, 1, 81, 232, 255, 255, 252, 255, 255, 255, 221, 3, 0, 0, 0, 58, 201, 251, 250, 250, 252, 247, 255, 85, 1, 4, 0, 0, 0, 1, 0, 26, 128, 190, 239, 231, 239, 164, 24, 10, 9, 28, 81, 255, 255, 252, 248, 249, 250, 244, 255, 69, 0, 5, 0, 0, 0, 0, 5, 2, 0, 4, 17, 20, 18, 0, 0, 10, 5, 89, 119, 126, 202, 244, 255, 253, 249, 251, 254, 166, 24, 0, 1, 5, 1, 0, 0, 7, 12, 3, 0, 0, 0, 4, 10, 0, 6, 0, 0, 0, 11, 27, 165, 239, 248, 255, 254, 255, 216, 14, 4, 0, 0, 5, 5, 6, 5, 9, 11, 4, 6, 9, 1, 4, 6, 4, 8, 10, 8, 0, 0, 14, 189, 255, 255, 252, 249, 238, 176, 140, 36, 6, 8, 7, 0, 0, 0, 0, 0, 4, 6, 4, 8, 2, 5, 3, 2, 5, 2, 0, 19, 255, 255, 255, 247, 249, 255, 179, 90, 4, 11, 0, 63, 70, 80, 61, 87, 15, 0, 9, 0, 7, 1, 3, 5, 1, 6, 5, 4, 254, 255, 255, 255, 245, 174, 6, 0, 8, 0, 122, 255, 251, 252, 251, 255, 234, 159, 202, 128, 16, 1, 3, 1, 1, 5, 2, 6, 250, 253, 245, 241, 168, 0, 9, 12, 0, 77, 255, 252, 255, 243, 253, 250, 255, 255, 255, 255, 148, 8, 5, 2, 1, 4, 3, 5, 249, 248, 255, 47, 8, 13, 11, 6, 56, 228, 247, 252, 248, 252, 253, 251, 253, 244, 248, 249, 255, 12, 2, 5, 10, 2, 6, 6, 254, 255, 164, 13, 1, 6, 14, 2, 132, 255, 245, 250, 252, 251, 253, 255, 254, 250, 247, 254, 233, 10, 2, 4, 7, 9, 0, 10, 224, 79, 0, 2, 1, 5, 0, 50, 244, 246, 250, 253, 250, 252, 254, 251, 255, 251, 247, 250, 63, 1, 2, 1, 11, 0, 65, 217, 209, 0, 9, 3, 3, 6, 0, 60, 255, 244, 250, 253, 250, 250, 246, 252, 245, 254, 255, 118, 0, 7, 4, 10, 0, 51, 210, 255, 99, 4, 3, 6, 5, 7, 1, 51, 255, 255, 253, 248, 246, 247, 243, 255, 255, 233, 90, 4, 6, 4, 0, 0, 118, 254, 255, 246, 0, 3, 1, 3, 4, 5, 5, 6, 65, 205, 243, 255, 255, 255, 255, 240, 170, 22, 0, 8, 1, 0, 61, 127, 254, 253, 247, 247, 14, 6, 4, 1, 0, 2, 5, 1, 0, 5, 39, 126, 198, 160, 101, 16, 0, 3, 0, 1, 20, 147, 254, 255, 246, 247, 254, 252, 7, 0, 5, 2, 3, 4, 5, 4, 9, 4, 0, 0, 6, 0, 0, 0, 0, 0, 49, 191, 239, 255, 255, 250, 253, 255, 255, 255, 220, 67, 0, 7, 7, 5, 3, 10, 3, 4, 5, 8, 6, 0, 4, 18, 94, 141, 246, 255, 250, 249, 255, 255, 255, 255, 255, 255, 255, 211, 36, 10, 4, 4, 1, 3, 8, 1, 7, 3, 4, 90, 149, 241, 255, 255, 254, 245, 251, 250, 255, 255, 255, 255, 255, 255]
# 3 [239, 98, 1, 85, 62, 0, 12, 111, 9, 50, 128, 118, 214, 243, 245, 255, 255, 255, 241, 251, 252, 255, 255, 255, 255, 255, 255, 255, 220, 0, 2, 0, 0, 0, 3, 0, 5, 0, 0, 0, 21, 21, 34, 145, 134, 198, 255, 255, 253, 251, 253, 255, 255, 255, 255, 255, 222, 0, 14, 11, 9, 8, 8, 14, 9, 1, 0, 0, 0, 0, 0, 0, 0, 65, 140, 219, 246, 255, 250, 248, 252, 255, 250, 254, 229, 132, 226, 226, 233, 227, 225, 225, 228, 188, 108, 117, 31, 4, 0, 9, 17, 2, 0, 14, 28, 152, 255, 255, 246, 251, 251, 253, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 237, 226, 99, 0, 0, 12, 10, 1, 0, 0, 52, 199, 255, 243, 253, 248, 253, 247, 250, 249, 245, 248, 250, 249, 248, 250, 245, 248, 255, 255, 255, 194, 58, 0, 8, 5, 2, 12, 0, 44, 206, 248, 252, 250, 255, 254, 253, 255, 255, 255, 254, 255, 255, 254, 255, 255, 254, 253, 248, 255, 211, 48, 5, 5, 4, 3, 6, 4, 6, 175, 253, 248, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 253, 241, 255, 137, 0, 8, 3, 7, 6, 7, 8, 21, 207, 255, 255, 255, 255, 255, 253, 251, 251, 255, 255, 255, 255, 255, 255, 255, 253, 242, 255, 134, 0, 8, 1, 4, 3, 3, 3, 0, 35, 224, 255, 255, 255, 255, 255, 255, 255, 254, 253, 253, 253, 254, 252, 253, 250, 251, 236, 87, 3, 5, 5, 2, 5, 2, 5, 4, 0, 219, 251, 253, 250, 254, 203, 176, 180, 255, 255, 255, 255, 255, 255, 255, 255, 245, 106, 0, 7, 5, 8, 4, 2, 4, 7, 10, 0, 222, 250, 252, 246, 255, 84, 0, 0, 54, 55, 113, 135, 48, 162, 75, 51, 39, 0, 7, 3, 4, 4, 8, 2, 7, 5, 9, 57, 233, 252, 254, 248, 255, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 5, 6, 4, 5, 0, 4, 0, 0, 0, 208, 255, 250, 252, 246, 255, 130, 64, 67, 0, 0, 0, 0, 0, 5, 14, 13, 6, 0, 3, 3, 0, 0, 47, 11, 65, 132, 192, 233, 249, 253, 255, 255, 255, 255, 255, 255, 189, 188, 144, 61, 64, 9, 0, 0, 5, 11, 13, 0, 159, 211, 255, 204, 255, 255, 255, 253, 255, 255, 255, 255, 255, 253, 252, 252, 255, 255, 255, 255, 255, 106, 55, 55, 0, 2, 11, 2, 65, 83, 90, 255, 255, 241, 247, 249, 251, 255, 255, 255, 255, 255, 255, 254, 246, 251, 246, 249, 246, 255, 255, 238, 52, 33, 0, 5, 0, 0, 0, 71, 142, 255, 249, 247, 250, 255, 255, 255, 255, 255, 255, 255, 253, 249, 246, 241, 252, 247, 250, 249, 255, 236, 78, 0, 13, 6, 6, 0, 19, 136, 241, 247, 248, 250, 252, 250, 253, 250, 254, 254, 254, 250, 255, 250, 251, 255, 253, 251, 248, 251, 225, 50, 0, 5, 3, 9, 2, 0, 134, 255, 246, 255, 248, 247, 245, 251, 250, 252, 255, 255, 255, 255, 255, 255, 255, 250, 249, 244, 255, 208, 39, 1, 5, 4, 4, 13, 0, 65, 252, 219, 255, 255, 255, 243, 244, 248, 255, 255, 255, 255, 255, 255, 255, 250, 253, 249, 245, 255, 63, 0, 13, 2, 5, 2, 6, 0, 82, 11, 99, 95, 181, 255, 255, 255, 251, 250, 252, 254, 254, 255, 255, 252, 251, 251, 244, 255, 59, 0, 9, 4, 5, 4, 6, 7, 0, 0, 0, 0, 48, 105, 97, 106, 255, 255, 255, 255, 255, 249, 250, 255, 249, 255, 255, 243, 51, 2, 3, 0, 1, 1, 2, 1, 2, 27, 0, 0, 0, 0, 0, 0, 108, 108, 148, 228, 221, 255, 255, 234, 255, 226, 171, 37, 7, 3, 0, 0, 0, 0, 0, 0, 0, 240, 137, 149, 64, 0, 0, 0, 0, 0, 0, 10, 5, 88, 111, 26, 90, 9, 1, 0, 11, 3, 0, 0, 0, 0, 0, 1, 1, 255, 255, 255, 199, 136, 143, 136, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 9, 3, 7, 0, 0, 0, 0, 0, 0, 0, 252, 252, 249, 255, 255, 255, 255, 136, 138, 97, 22, 24, 0, 0, 0, 8, 5, 6, 2, 5, 1, 0, 2, 1, 3, 0, 15, 20, 255, 255, 255, 253, 250, 250, 251, 255, 255, 255, 235, 245, 150, 124, 113, 1, 0, 7, 6, 2, 5, 9, 5, 3, 9, 0, 189, 244]
