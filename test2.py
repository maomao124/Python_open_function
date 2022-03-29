"""
 * Project name(项目名称)：Python_open函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 21:32
 * Version(版本): 1.0
 * Description(描述)：
 open() 函数用于创建或打开指定文件，该函数的常用语法格式如下：
file = open(file_name [, mode='r' [ , buffering=-1 [ , encoding = None ]]])
file：表示要创建的文件对象。
file_name：要创建或打开文件的文件名称，该名称要用引号（单引号或双引号都可以）括起来。需要注意的是，
            如果要打开的文件和当前执行的代码文件位于同一目录，则直接写文件名即可；否则，此参数需要指定打开文件所在的完整路径。
mode：可选参数，用于指定文件的打开模式。可选的打开模式如表 1 所示。如果不写，则默认以只读（r）模式打开文件。
buffering：可选参数，用于指定对文件做读写操作时，是否使用缓冲区
encoding：手动设定打开文件时所使用的编码格式，不同平台的 ecoding 参数值也不同，以 Windows 为例，其默认为 cp936（实际上就是 GBK 编码）。


模式	意义	注意事项
r	只读模式打开文件，读文件内容的指针会放在文件的开头。	操作的文件必须存在。
rb	以二进制格式、采用只读模式打开文件，读文件内容的指针位于文件的开头，一般用于非文本文件，如图片文件、音频文件等。
r+	打开文件后，既可以从头读取文件内容，也可以从开头向文件中写入新的内容，写入的新内容会覆盖文件中等长度的原有内容。
rb+	以二进制格式、采用读写模式打开文件，读写文件的指针会放在文件的开头，通常针对非文本文件（如音频文件）。
w	以只写模式打开文件，若该文件存在，打开时会清空文件中原有的内容。	若文件存在，会清空其原有内容（覆盖文件）；反之，则创建新文件。
wb	以二进制格式、只写模式打开文件，一般用于非文本文件（如音频文件）
w+	打开文件后，会对原有内容进行清空，并对该文件有读写权限。
wb+	以二进制格式、读写模式打开文件，一般用于非文本文件
a	以追加模式打开一个文件，对文件只有写入权限，如果文件已经存在，文件指针将放在文件的末尾（即新写入内容会位于已有内容之后）；反之，则会创建新文件。
ab	以二进制格式打开文件，并采用追加模式，对文件只有写权限。如果该文件已存在，文件指针位于文件末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。
a+	以读写模式打开文件；如果文件存在，文件指针放在文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。
ab+	以二进制模式打开文件，并采用追加模式，对文件具有读写权限，如果文件存在，则文件指针位于文件的末尾（新写入文件会位于已有内容之后）；反之，则创建新文件。

file.name：返回文件的名称；
file.mode：返回打开文件时，采用的文件打开模式；
file.encoding：返回打开文件时使用的编码格式；
file.closed：判断文件是否己经关闭。

 """

if __name__ == '__main__':
    file1 = open("info.txt", "a", encoding="UTF-8")
    print(file1.name)
    print(file1.mode)
    print(file1.encoding)
    print(file1.closed)
    print("文件输出", file=file1)
    file1.close()
    print(file1.closed)
    file2 = open("info1.txt", "w", encoding="UTF-8")
    print("文件输出", file=file2)
    file2.close()
    file3 = open("info2.txt", "wb")
    file3.close()
