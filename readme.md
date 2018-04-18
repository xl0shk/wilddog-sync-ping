## wilddog-sync-ping ##

wilddog-sync-ping项目实现全国节点网络时延的实时监测和数据展示。  
基于野狗Sync实时引擎实现（野狗Sync实时引擎类似于国外的Firebase产品），非常推荐。    

wilddog-sync-ping由两个子项目组成，分别是wd-sync-ping-server和wd-sync-ping-web；  



## 运行方式 ##

server --(rest api)--> wilddog sync <------> js sdk  

wd-sync-ping-server是服务端程序，用于网络检测数据的产生，并通过rest api写入数据到wilddog sync；  
wd-sync-ping-web则通过js sdk对wilddog sync的数据进行实时监听，当监听到有数据变化时，页面对应区域会有颜色变化，并进行数据变更。    


## 演示Demo ## 
[http://wd-sync-ping.xl0shk.com/](http://wd-sync-ping.xl0shk.com/)

## 截图 ##
当监听到有数据变化时，页面对应区域会有颜色变化，并进行数据变更。
![展示页面](images/1.png)


## wd-sync-ping-server ##
##### 开发环境 #####
Python3.6  

##### 依赖模块 #####
```
pip3 install requests
pip3 install apscheduler
```

#### 运行方法 #####
进入Python3虚拟环境中，运行app.py

## wd-sync-ping-web ##
wd-sync-ping-web是静态页面，直接调用wilddog sync js sdk
