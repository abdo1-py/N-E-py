import mysql.connector





def dbautonum(table,column):
    
    try:
        
        
        
        
        con= mysql.connector.connect(
                host =  " localhost ",
                user ='TestDB',
                
                passwd ='123456',
                database= 'mybdpy'
                
                )

            

        cur=con.cursor()
            
        cur.execute(""" SELECT MAX(%s)+1 FROM %s """ % (table,column ) )
        row = cur.fetchone()
        if row[0]==None :
            return '1'
        
        else:
            return""
        
    except mysql.connector.Error as kk:
        print(kk)
        
       




