
# Import standard modules 
################################################################################
import sys, os, datetime, math, time, signal
import psycopg2
import psycopg2.extras

################################################################################
# 
################################################################################
class Db(object):
    ''' Provides database utility functions
        The default database name is considered as commondb, it can be changed 
        while initializing or also passed when executing any query.
        The script is also enhanced to use ODBC connection to execute query. 
    '''

    ############################################################################
    #
    ############################################################################    
    def __init__(self, host = "127.0.0.1", port = "5432", user_name = "postgres", db_name = "postgres"):
    
        self.__host = host
        self.__port = port
        self.__user_name = user_name
        self.__db_name = db_name
    # End function
    
    ############################################################################
    #
    ############################################################################    
    def set_host(self, host):
    
        self.__host = host
    
    # End function

    ############################################################################
    #
    ############################################################################

    def exec_select_stmt_odbc(self, sql_select_stmt, db_name = None, host = None):
        '''
            Execute SQL select statement using psycopg2 and return status and output
            USAGE :  rows = ipcs_db.exec_select_stmt_odbc("select * from <table_name>");
                     for row in rows :
                     print "  ",row[column_no] | print "  ",row[column_name] | print "  ",row
        '''

        if db_name == None :
            db_name = self.__db_name
        
        if host == None :
            host = self.__host  

        print("[exec_select_stmt_odbc]: db_name: %s host: %s sql_select_stmt: %s " %(db_name,host,sql_select_stmt))

        dbconn = None
        try:
            try:
                dbconn = psycopg2.connect(database = db_name, user = self.__user_name, host = host) 
            except TypeError as e:
                print("[exec_select_stmt_odbc]: Error: %s" % e)
                dbconn = psycopg2.connect(database = db_name, user = self.__user_name, host = host) 
            cur = dbconn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            cur.execute(sql_select_stmt)
        
            print("[exec_select_stmt_odbc]: status message %s" %cur.statusmessage)
            rows = cur.fetchall()
            return rows 
        except psycopg2.Error as e:
            print("[exec_select_stmt_odbc]: error: %s (pgerror: %s)" % (e, e.pgerror))
            raise e
        finally:
            if dbconn:
                 dbconn.close()
    # End function
    
if __name__ == '__main__':
    db = Db()
    rows = db.exec_select_stmt_odbc("select * from information_schema.domains")
    print(rows)


