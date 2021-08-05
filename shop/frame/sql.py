class Sql:
    userlist = "SELECT * FROM usertb";
    userlistone = "SELECT * FROM usertb WHERE id= '%s' ";
    userinsert = "INSERT INTO usertb VALUES ('%s','%s','%s')";
    userdelete = "DELETE FROM usertb WHERE id= '%s' ";
    userupdate = "UPDATE usertb SET pwd='%s',name='%s' WHERE id= '%s' ";

    itemlist = "SELECT * FROM itemtb";
    itemlistone = "SELECT * FROM itemtb WHERE id= %d ";
    iteminsert = "INSERT INTO itemtb VALUES (null,'%s',%d,CURRENT_DATE(), '%s')";
    itemdelete = "DELETE FROM itemtb WHERE id= %d ";
    itemupdate = "UPDATE itemtb SET name='%s',price=%d, imgname='%s' WHERE id= %d ";