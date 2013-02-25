from Tkinter import *
import sys
import os
import array
import time

class Finestra(Tk):
            def __init__(self):
                    """Costruttore della classe Finestra
                  """
                    iargv = 1
                    Tk.__init__(self)
                    self.title(sys.argv[iargv])
                    self.geometry("%dx%d" % (220, 150))
                    i = 1
                    iv = 1
                    stext = 0
                    itb = 0
                    Etb = []
                    while sys.argv[iargv] != "end":
                        iargv = iargv + 1
                        if sys.argv[iargv] == "button":
                                # creo il bottone
                                iargv = iargv + 1
                                buttontext = sys.argv[iargv]
                                iargv = iargv + 1
                                sym = sys.argv[iargv]
                                if sym == "%":
                                    iargv = iargv + 1
                                    comm = sys.argv[iargv]
                                    b = Button(self, text=buttontext, command=lambda: self.action(sym,comm,iargv))
                                    iargv = iargv + 1
                                    locx = int(sys.argv[iargv])
                                    iargv = iargv + 1
                                    locy = int(sys.argv[iargv])
                                    b.place(x=locx, y=locy)
                                    i = i + 1
                                if sym == "&":
                                    iargv = iargv + 1
                                    comm = sys.argv[iargv]
                                    b = Button(self, text=buttontext, command=lambda: self.action(sym,comm,iargv))
                                    b.pack()
                                    i = i + 1
                        if sys.argv[iargv] == "label":
                                iargv = iargv + 1
                                ltext = sys.argv[iargv]
                                iargv = iargv + 1
                                sym = sys.argv[iargv]
                                if sym == "%":
                                    iargv = iargv + 1
                                    llocx = int(sys.argv[iargv])
                                    iargv = iargv + 1
                                    llocy = int(sys.argv[iargv])
                                    w = Label(self, text=ltext)
                                    w.place(x=llocx , y=llocy)
                                if sym == "&":
                                    w = Label(self, text=ltext)
                                    w.pack()
                        if sys.argv[iargv] == "textbox":
                                iargv = iargv + 1
                                size = int(sys.argv[iargv])
                                E1 = Entry(self, bd =size)
                                E1.pack()
                                iargv = iargv + 1
                                buttontext = sys.argv[iargv]
                                iargv = iargv + 1
                                ff = sys.argv[iargv]
                                bb = Button(self, text=buttontext, command=lambda: self.actionc(E1,ff))
                                bb.pack()
                                
                    # registro l'evento di chiusura della finestra        
                    self.protocol('WM_DELETE_WINDOW', self.__chiudi)
                   
            def mostra(self):
                    """Visualizza la finestra
                  """
                    # mando in loop l'applicazione
                    self.mainloop()
            def actionc(self,E1,ff):

                s = E1.get()
                miofile = open(ff,'a')
                miofile.write(s)
                miofile.close()
            def action(self,sym,comm,iargv):
                    """Stampa sullo standard output la stringa 'Hello world !
                  """
                    os.system(comm)
            def __chiudi(self):
                    """Chiude l'applicazione alla chiusura della finestra
                  """
                    self.destroy()
                   
                   
if __name__ == '__main__':
            f = Finestra()
            f.mostra()
