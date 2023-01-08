# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tms"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS package_366( PackageId varchar(50) NOT NULL,PackageName varchar(200) NOT NULL,PackageType varchar(150) DEFAULT NULL, PackageLocation varchar(100) DEFAULT NULL,PackagePrice int(11) NOT NULL,PackageFeatures varchar(255) DEFAULT NULL,PackageDetails mediumtext NOT NULL,PackageImage varchar(100) DEFAULT NULL,NumberOfDays int(100) DEFAULT NULL,Creationdate timestamp NULL DEFAULT current_timestamp())')


def add_data(PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate):
    c.execute('INSERT INTO package_366(PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM package_366')
    data = c.fetchall()
    return data


def view_only_package_names():
    c.execute('SELECT PackageName FROM package_366')
    data = c.fetchall()
    return data


def get_package(PackageName):
    c.execute('SELECT * FROM package_366 WHERE PackageName="{}"'.format(PackageName))
    data = c.fetchall()
    return data


def edit_package_data(new_PackageId, new_PackageName, new_PackageType, new_PackageLocation, new_PackagePrice,new_PackageFeatures,new_PackageDetails,new_PackageImage,new_NumberOfDays,new_Creationdate,PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate):
    c.execute("UPDATE Package_366 SET PackageId=%s,PackageName=%s,PackageType=%s,PackageLocation=%s,PackagePrice=%s,PackageFeatures=%s,PackageDetails=%s,PackageImage=%s,NumberOfDays=%s,Creationdate=%s WHERE PackageId=%s and PackageName=%s and PackageType=%s and PackageLocation=%s and PackagePrice=%s and PackageFeatures=%s and PackageDetails=%s and PackageImage=%s and NumberOfDays=%s and Creationdate=%s ",( new_PackageId, new_PackageName, new_PackageType, new_PackageLocation, new_PackagePrice,new_PackageFeatures,new_PackageDetails,new_PackageImage,new_NumberOfDays,new_Creationdate,PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate))
    mydb.commit()
    
   
def view_all_bookings():
    c.execute('SELECT * FROM booking_366')
    data=c.fetchall()
    return data

def delete_data(PackageName):
    c.execute('DELETE FROM package_366 WHERE PackageName="{}"'.format(PackageName))
    mydb.commit()

def view_all(query):
    c.execute(query)
    num_fields=len(c.description)
    field_names=[i[0] for i in c.description]
    print(num_fields,field_names)
    data=c.fetchall()
    return [num_fields,field_names,data]