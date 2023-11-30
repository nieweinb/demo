import uiautomator2 as u2
d = u2.connect_usb('133562ad')  #连接手机设备ID
d.app_start('com.ss.android.lark')  #打开飞书应用
d(resourceId="com.ss.android.lark:id/left_icon").click() #关闭手机号码一键登录界面
d(resourceId="com.ss.android.lark:id/phone_number_edit").click()  #点击手机输入框
d.send_keys('13617051315')  #输入账号
d(resourceId="com.ss.android.lark:id/checkBoxPolicy").click()  #勾选同意隐私协议
d(text="下一步").click()  #下一步
d.send_keys('nw123456')   #输入密码
d(text="下一步").click()    #登录成功进入飞书主界面
d(resourceId="com.ss.android.lark:id/textItem", text="通讯录").click()   #从主界面中找到菜单栏->"通讯录"页面
d(resourceId="com.ss.android.lark:id/tv_item", text="外部联系人").click()  #测试账号在外部联系人
#d(resourceId="com.ss.android.lark:id/layout_user_info").click() #选中测试账号联系人
d(text="tester2").click()
d(text="消息").click()   #点击消息进入对话框
d(resourceId="com.ss.android.lark:id/normal_message_et_layout").click()  #点击文本框
d.send_keys('这是一个测试消息')  #输入文本消息
d(resourceId="com.ss.android.lark:id/right_insets").click()  #点击发送