_base_ = './pointrend_r50_512x1024_80k_lars.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
