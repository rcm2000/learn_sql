from frame.db import Db
from frame.sql import Sql
from frame.value import Cust


class CustDB(Db):
    def update(self, id, pwd, name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custupdate % (pwd, name, id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
            print(ErrorCode.e0002)
        finally:
            super().close(conn, cursor);
    def delete(self,id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custdelete % id);
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
            print(ErrorCode.e0002)
        finally:
            super().close(cursor, conn)
    def insert(self,id,pwd,name):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.custinsert % (id,pwd,name));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor, conn)
    def selectone(self,id):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.custlistone % id);
        c = cursor.fetchone()
        cust = Cust(c[0],c[1],c[2])
        super().close(cursor, conn)
        return cust;


    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.custlist);
        result = cursor.fetchall();
        for c in result:
            cust = Cust(c[0],c[1],c[2])
            all.append(cust)

        super().close(cursor,conn);
        return all;

# userlist Test Function ................
def userlist_test():
    users = CustDB().select();
    for u in users:
        print(u);

def userlistone_test():
    users = CustDB().selectone('id01');
    print(users);
def userinsert_test():
    CustDB().insert('id04','pwd04','jeams');

def userupdate_test():
    CustDB().update('id03','pwd9111','홍말숙');


if __name__ == '__main__':
    userupdate_test()
