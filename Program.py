import sys, tkinter, tkinter.filedialog, tkinter.messagebox, pyperclip

root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.mcfunction")]
file = tkinter.filedialog.askopenfilename(filetypes = fTyp)
try:
    f = open(file, 'r')
except FileNotFoundError as e:
    sys.exit()
    
text='player.onChat("run", function () {'
for data in f:
    text=text+'\nplayer.execute("'+data.replace('\n','')+'")'
text=text+"\n})"
tkinter.messagebox.showinfo("Mcfunction2MakeCode","変換完了\nクリップボードにコピーしました")
pyperclip.copy(text)
