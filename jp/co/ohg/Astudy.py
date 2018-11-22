
import fibo
import os


#要写入一个文件，你必须在打开文件时设置第二个参数来为 'w' 模式：


print(os.getcwd())
print(os.path.abspath('Sapmle.txt'))
fout = open('Sapmle.txt', 'w')

#如果该文件已经存在，那么用写入模式打开它将会清空原来的数据并从新开始，所以要小心！ 如果文件不存在，那么将创建一个新的文件。

#open会返回一个文件对象，该对象提供了操作文件的方法。write 方法将数据写入文件。

line1 = "This here's the wattle,\n"
lines = fout.write(line1)
print(lines)


#返回值是被写入字符的个数。文件对象将跟踪自身的位置，所以下次你调用 write 的时候，它会在文件末尾添加新的数据。

line2 = "the emblem of our land."
lines = fout.write(line2)
print(lines)


#完成文件写入后，你应该关闭文件。

fout.close()


try:
    fin = open('bad_file')
except:
    print('Something went wrong.')

cmd = 'dir C:\\Users\\b1659'
fp = os.popen(cmd)

res = fp.read()
res = fp.read()
res = fp.read()
res = fp.read()
res = fp.read()
stat = fp.close()
print(stat)

#定義
class aPoint:
    print("I'm a class.")

    def aDef(self):
        print("I'm aDef.")


#実例化
aPointD = aPoint()
aPointD.x=123

print(aPointD.x)

aPointD.aDef();

