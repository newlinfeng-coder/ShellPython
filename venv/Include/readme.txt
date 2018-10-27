#配置第一个网口，局域网
vi /etc/sysconfig/network-scripts/ifcfg-em1

#进入编辑，按A进入编辑，下面会显示一个INSERT
88888888888888888888888888
DEVICE=em1
TYPE=Ethernet
HWADDR=xx:xx:xx:xx:xx:xx
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=none
IPADDR=172.168.0.7
NETMASK=255.255.0.0
IPV4_FAILURE_FATAL=yes
IPV6INIT=no
NAME="System em1"
99999999999999999999999999999999
#先按ESC
#:wq 回车保存

#配置第二个网口，可以上网，后面要下载安装网络补丁
vi /etc/sysconfig/network-scripts/ifcfg-em2

#进入编辑，按A进入编辑，下面会显示一个INSERT
888888888888888888888888888888888
DEVICE=em2
TYPE=Ethernet
HWADDR=xx:xx:xx:xx:xx:xx
ONBOOT=yes
NM_CONTROLLED=yes
BOOTPROTO=none
IPADDR=222.61.19.71
NETMASK=255.255.255.240
GATEWAY=222.61.19.65
DNS1=222.61.0.98
DNS2=222.61.0.98
PEERDNS=yes
DEFROUTE=yes
IPV4_FAILURE_FATAL=yes
IPV6INIT=no
NAME="System em2"
9999999999999999999999999999999999
#先按ESC
#:wq #回车保存



#向防火墙添加端口
/sbin/iptables -I INPUT -p tcp --dport 7998 -j ACCEPT
/sbin/iptables -I INPUT -p udp --dport 5000:9998 -j ACCEPT
/etc/rc.d/init.d/iptables save


#系统安装包
yum -y install sqlite sqlite-devel wget vconfig tcpdump unzip dmidecode


#开机自启动监听程序, 组播路由, 也可能是 eth0
echo 'cd /home' >> /etc/profile
echo 'route add -net 224.0.0.0 netmask 240.0.0.0 dev em1' >> /etc/rc.local
echo '/home/listen > /dev/null 2>&1 &' >> /etc/rc.local


#编辑服务器支持 编码，单播，回看
vi /home/iptv.conf
8888888888888888888888
HWADDR=eth0
INPUT=eth0
OUTPUT=eth1
ENCODER=no
M3U8=yes
DOWNLOAD=no
DXLT=no
SERVER=172.16.0.2
999999999999999999999999999
#先按ESC
#:wq #回车保存

#重新启动网络配置，需要等待一会
service network restart

#解压包
cd /home
tar -jxvf tomcat.tar.bz2
cd /home
tar -jxvf ffmpeg.tar.bz2


#安装动态库
cd /home/ffmpeg; ./install


# 安装JDK (只有是单播，或者回看，则安装此程序)
cd /home
rpm -ivh jdk-8u45-linux-x64.rpm


#安装 tomcat (只有是单播，或者回看，才安装此程序)
mv /home/tomcatd /etc/init.d/tomcatd 
chkconfig --add tomcatd 
chkconfig tomcatd on 
service tomcatd start 
