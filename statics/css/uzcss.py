f = open('popup.css')
f1 = open('popup1.css',"w+")
buf = f.read()
bufnew = buf.replace("}","}\n")
bufnew = bufnew.replace(";",";\n")
f1.write(bufnew)
f.close()
f1.close()
