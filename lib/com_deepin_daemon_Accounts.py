#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusAccounts:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Accounts"
        self.obj_path  = "/com/deepin/daemon/Accounts"
        self.interface = "com.deepin.daemon.Accounts"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

    def FindUserById(self, user_id):
        return self.ifc_methods.FindUserById(user_id)

    def FindUserByName(self, user_name):
        """
        获取到输入账户的dbus Object path
        """
        return self.ifc_methods.FindUserByName(user_name)

    def RandUserIcon(self):
        return self.ifc_methods.RandUserIcon()


class DbusUser:
    def __init__(self, UserObjPath):
        self.dbus_name = "com.deepin.daemon.Accounts"
        self.obj_path  = UserObjPath
        self.interface = "com.deepin.daemon.Accounts.User"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

        self.dbus_properties_DesktopBackgrounds = "DesktopBackgrounds"
        self.dbus_properties_IconFile = "IconFile"
        self.dbus_properties_Uid = "Uid"
        self.dbus_properties_UserName = "UserName"

    def getDesktopBackgrounds(self):
        """
        获取四个工作区的壁纸
        """
        return self.ifc_properties.Get(self.interface,
                                       self.dbus_properties_DesktopBackgrounds)

    def getIconFile(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_IconFile)

    def getUid(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_Uid)

    def getUserName(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_UserName)

    def SetDesktopBackgrounds(self, list_desktop_file):
        """
        设置桌面背景，四个工作区
        """
        self.ifc_methods.SetDesktopBackgrounds(list_desktop_file)

    def SetPassword(self, pw):
        pid = os.fork()

        if 0 == pid:
            self.ifc_methods.SetPassword(pw)

class DbusImageBlur:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Accounts"
        self.obj_path  = "/com/deepin/daemon/ImageBlur"
        self.interface = "com.deepin.daemon.ImageBlur"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

    def Get(self, imagePath):
        """
        获取模糊图片路径
        入参：
            imagePath: 需要模糊图片的绝对路径

        返回值：
            模糊图片的绝对路径
        """
        return self.ifc_methods.Get(imagePath)
