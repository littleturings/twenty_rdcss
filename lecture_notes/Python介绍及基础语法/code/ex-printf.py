#打印字符串
print("My name is %s" %("Orash-Shi"))
#打印整数
print("I am %d years old." %(25))
#打印浮点数
print ("His height is %f m"%(1.70))
#打印浮点数（指定保留两位小数）
print ("His height is %.2f m"%(1.70))
#指定占位符宽度
print ("Name:%10s Age:%8d Height:%8.2f"%("Orash",16,1.83))
#指定占位符宽度（左对齐）
print ("Name:%-10s Age:%-8d Height:%-8.2f"%("Orash",16,1.83))
#指定占位符（只能用0档占位符？）
print ("Name:%-10s Age:%08d Height:%08.2f"%("Orash",16,1.83))
#科学计数法
format(0.0026,".2e")
