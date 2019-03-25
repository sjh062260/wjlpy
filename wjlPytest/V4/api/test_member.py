#! /usr/bin/env python
# _*_ coding: UTF-8 _*_

"""
@author:sjh
@time:2018/5/24 19:19
"""

class TestCouponBase:

    testData = {
        "host":"http://192.168.122.116:8602/crm/MemberGradeClient/",
        "groupId":"1200",
        "tenantId":"4021",
        "regionId":"120001"
    }

    def test_change_mobile(self):
        # 修改手机号

    def test_change_password(self):
        # 修改密码

    def test_del_member(self):
        #删除会员

    def test_freeze_member(self):
        #冻结会员

    def test_unfreeze_member(self):
        #解冻会员

    def test_get_member_all_info(self):
        #获取会员所有信息

    def test_get_member_by_member_id(self):
        #通过ID获取会员信息

    def test_get_member_by_mobile(self):
        #通过手机号获取会员信息

    def test_get_member_detail_info(self):
        #获取会员详细信息

    def test_get_member_detail_info_by_openId(self):
        #通过openId 获取会员详细信息

    def test_modify_member(self):
        # 修改会员资料

    def test_register(self):
        # 会员注册