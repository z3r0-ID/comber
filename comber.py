try:
  import base64
  import marshal
  import os, sys
  import click
  import uncompyle6
  from uncompyle6 import main
  from time import sleep
except ImportError:
  os.system('pip install click')
  os.system('pip install uncompyle6')

class Com:
  def __init__(self,fil,jum):
    self.file=fil
    self.cout=0
    self.jml=jum
    self.mars(open(fil,'r').read())

  def mars(self,strg):
    x=compile(strg,'<script>','exec')
    xx=marshal.dumps(x)
    xxx=f"#Compile Berlapis\n#By z3r0_ID\n\nimport marshal\nexec(marshal.loads({xx}))"
    if self.cout == self.jml:
      with open(self.file.replace('.py','_comber.py'),'w') as com:
        com.write(xxx)
        print(f"[#] File tersimpan: {self.file.replace('.py','_comber.py')}")
        return True
    self.bes(xxx)

  def bes(self,strg):
    en=base64.b64encode(bytes(strg,'utf-8'))
    de=f"#Dah lah\n\nimport base64\nexec(base64.b64decode({en}).decode('utf-8','ignore'))"
    self.cout+=1
    self.mars(de)

os.system('clear')
banner = """

\033[1;30m                  /)-._             
\033[1;30m                 Y. \033[1;31m' \033[1;30m_]           \033[1;33m[\033[0;35m#\033[1;33m] \033[1;36mCompiler Marshal Berlapis \033[1;33m[\033[0;35m#\033[1;33m]
\033[1;30m          ,.._   |`--"=             
\033[1;30m         /    "-/   \                       \033[1;32mAuthor \033[1;37m: \033[1;31mz3r0_ID
\033[1;30m/) \033[0;35m0.1  \033[1;30m|   |_     `\|___           
\033[1;30m\:::::::\___/_\__\_______\          

"""

print(banner)
try:
  ofile=input("\033[1;33m[\033[1;37m?\033[1;33m] \033[0;35mFile Ori \033[1;37m: \033[1;32m")
  juml=int(input("\033[1;33m[\033[1;37m?\033[1;33m] \033[0;35mMasukan Jumlah Compile \033[1;37m: \033[1;32m"))
  for i in "-\|/-\|-":
    print('\rProcess ['+i+'] ',end="",flush=True)
    sleep(0.3)
  os.system('clear')
  print(banner)
  if juml > 10:
    click.pause("\033[1;31m[WARNING] anda memasukan lebih dari 10 file ini bisa membuat ukuran file membengkak [ENTER]")
  Com(ofile,juml)
  pil=input("\033[1;33m[\033[0;35m?\033[1;33m] \033[1;36mCompile ke bytes code \033[1;32m(y/n) \033[1;30m")
  if pil.lower() == 'y':
    main.compile_file(ofile.replace('.py','_comber.py'))
    print("\033[1;32m[#] Done [#]")
  else:
    print("\033[1;32m[#] Done [#]")
except KeyboardInterrupt:
  print("\033[1;31m[ Key Interrupt ]")
except Exception as F:
  print(f"\033[1;31m[Err] {str(F)}")
