#电脑上的Python为3.5，安装在Windows上，虽然安装过程中选择了pip，但是在命令行输入pip后仍然不能成功，尝试一下方法，终于解决问题
#win10  CMD  命令提示符下使用
//1、使用下面的语句确保没有报错了
python -m ensurepip
//2、使用pip -V命令查看，依然提示没有，继续输入如下命令测试是否可用
python -m pip install readline 
//3.怀疑可能是环境没配置好，所以更新一下pip试试
python -m pip install --upgrade pip
//再输入pip，就正常了
