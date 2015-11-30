# -*- coding: utf-8 -*-
import MySQLdb as mdb
class Query:
    def __init__(self):
        try:
            self.con = mdb.connect('localhost', 'cpd', '12341234', 'busstation');
            self.cur = self.con.cursor()
            self.cur.execute("SET NAMES utf8")
            self.cur.execute("SELECT VERSION()")
            ver = self.cur.fetchone()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def quering_add(self,sql):
        try:
            self.cur.execute(sql)
            self.cur.fetchone()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def quering_select(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)

    def end(self):
        self.con.commit()
        self.con.close()
