"""
 * Project name(项目名称)：Python_open函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 21:27
 * Version(版本): 1.0
 * Description(描述)： 
 """
import os

if __name__ == '__main__':
    print(os.getcwd())
    print(os.path.abspath("./.idea"))
    print(os.path.isabs("."))
    print(os.path.isabs(os.getcwd()))
    print(os.path.dirname("H:\\程序\\大三下期\\Python_open函数\\.idea"))
