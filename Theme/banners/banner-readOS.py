# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


logo = """\x1b[0;31m


                     :.                   i
                    LBRBB.             :BBBR.
                  .QQBBBBQBQi       7BQBQBQBBQ
                   BBBBQBBBBQQRi:BQBQBBBBBBQBi
                  .  QQBQBQRBBQQBBBQBQBQBBBB :.
                 7BQB BRBRBBQBRBQQBQBQBBBQ  BBB
                 vBBBQBQBBBBBQRQRBBBBBBQBBQBBBR.
                  QBBBBBBRBBBQBBQBBQBRQQBQBQQQQ
                  BQR  iBQBBBQQBBBBBBQQBB. QRBB
                rBQBBQ   RBBBBBBBQBBBBQi  lBBQQ.
                 BBQQQi  \x1b[00m\x1b[0;33m #\x1b[00m\x1b[0;31mBBBQQBBBQBQ\x1b[00m\x1b[0;33m#\x1b[00m   \x1b[0;31mBBQBRr
                   BBQBBQ.   QBBBBQB   .QBBBB.
               vB    BBQBQRBQBQBBRBBQBRBBBBB    Br
            .QBQQQBB. :QBBBQBQBB RBQBQBQBR  BBBBBBQB
           QQQBBB.QBQ.  BQBQ:BB  .BBQBBBi  BBBBQBQBQBv
          QQBQQBQBB BB   :B  QB   BB .Q   .QB.BRBBBRQBv
          iBBBQBQBBBBQi     QB  B rB:     7BBQBBBBBBQB.
           LB:QBBQBQB        QBBBQQr        QRBBBQBBB:
            :BiBRBR.           BQi           iBBBBB7. 
               . :                             i.\x1b[00m


\x1b[00m"""

def show():
	os.system('clear')
	slowprint(logo)

show()

