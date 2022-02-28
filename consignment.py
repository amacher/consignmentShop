from cProfile import label
from cgitb import text
from ctypes import alignment
from multiprocessing import Value
from re import search
from tkinter import *
from turtle import left
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk
import os

#put all GUI in this file, funtions in other files
root = Tk()

root.title('Consignment Shop')
root.iconbitmap('favicon.ico')
root.geometry("700x700")


mydb = mysql.connector.connect(
    host = "localhost",
    port = 2828, 
    user = "user",
    password = "password",
    database = "consignment",
)
print(mydb)

#create a cursor
my_cursor = mydb.cursor()

#################  Clear fields
def clear_fields(type):
    if type == seller:
        sellerID_box.delete(0, END)
        first_name_box.delete(0, END)
        last_name_box.delete(0, END)
        address1_box.delete(0, END)
        address2_box.delete(0, END)
        city_box.delete(0, END)
        state_box.delete(0, END)
        zipcode_box.delete(0, END)
        country_box.delete(0, END)
        phone_box.delete(0, END)
        email_box.delete(0, END)
    elif type == addInv:
        invID_box.delete(0, END)
        title_name_box.delete(0, END)
        inv_amt_box.delete(0, END)
        desc_name_box.delete(0, END)
        price_box.delete(0, END)
        seller_box.delete(0, END)
    elif type == purchase:
        item_box.delete(0, END)
        salesBox.grid_remove()
        
        
        

#################  LOOK UP SELLER
def look_seller():
    #when sellerId put in and checked pulls it in and runs SQL
    sellID = sellerID_box.get()
    ### If want to look up with phone or email
    # phNum = phone_box.get()
    # emailAdd = email_box.get()
    sql_command = "SELECT * FROM seller WHERE sellerId = " + sellID + ";"
    my_cursor = mydb.cursor()
    my_cursor.execute(sql_command)
    records = my_cursor.fetchone()

    #Inserts the data from DB to populate the fields.
    first_name_box.insert (0, records[1])
    last_name_box.insert (0, records[2])
    address1_box.insert (0, records[3])
    address2_box.insert (0, records[4])
    city_box.insert (0, records[5])
    state_box.insert (0, records[6])
    zipcode_box.insert (0, records[7])
    country_box.insert (0, records[8])
    phone_box.insert (0, records[9])
    email_box.insert (0, records[10])



#################  ADD A SELLER
def add_seller():
    #create a cursor
    my_cursor = mydb.cursor()
    # conditional if ID entered, run update
    if sellerID_box.get() != "":
        sql_command = """UPDATE seller SET firstName = %s, lastName = %s, address1 = %s, address2 = %s, city = %s, state = %s, zipcode = %s, country = %s, phone = %s, email = %s WHERE sellerId = %s"""
        firstname = first_name_box.get()
        lastname = last_name_box.get()
        address1 = address1_box.get()
        address2 = address2_box.get()
        city = city_box.get()
        state = state_box.get()
        zipcode = zipcode_box.get()
        country = country_box.get()
        phone = phone_box.get()
        email = email_box.get()
        id_value = sellerID_box.get()
        inputs = (firstname, lastname, address1, address2, city, state, zipcode, country, phone, email, id_value)
        my_cursor.execute(sql_command, inputs)
        mydb.commit()
    else:
    #else add the seller
        sql_command = "INSERT INTO seller (firstName, lastName, address1, address2, city, state, zipcode, country, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name_box.get(), last_name_box.get(), address1_box.get(), address2_box.get(), city_box.get(), state_box.get(), zipcode_box.get(), country_box.get(), phone_box.get(), email_box.get())
        my_cursor.execute(sql_command, values)
    #commit the changes to db
    mydb.commit()
    clear_fields(seller)

    
####################   SELLER
def seller():
    seller = Tk()
    seller.title("Sellers list")
    seller.iconbitmap('favicon.ico')
    seller.geometry("400x600")

    sellerID_label = Label(seller, text="Seller ID*: ").grid(row=2, column=0, sticky=W, padx=10)
    first_name_label = Label(seller, text="First Name: ").grid(row=3, column=0, sticky=W, padx=10)
    last_name_label = Label(seller, text="Last Name: ").grid(row=4, column=0, sticky=W, padx=10)
    address1_label = Label(seller, text="Address 1: ").grid(row=5, column=0, sticky=W, padx=10)
    address2_label = Label(seller, text="Address 2: ").grid(row=6, column=0, sticky=W, padx=10)
    city_label = Label(seller, text="City: ").grid(row=7, column=0, sticky=W, padx=10)
    state_label = Label(seller, text="State: ").grid(row=8, column=0, sticky=W, padx=10)
    zipcode_label = Label(seller, text="Zipcode: ").grid(row=9, column=0, sticky=W, padx=10)
    country_label = Label(seller, text="Country: ").grid(row=10, column=0, sticky=W, padx=10)
    phone_label = Label(seller, text="Phone: ").grid(row=11, column=0, sticky=W, padx=10)
    email_label = Label(seller, text="Email: ").grid(row=12, column=0, sticky=W, padx=10)
    #Create Entry Boxes
    global sellerID_box
    sellerID_box = Entry(seller)
    sellerID_box.grid(row=2, column=1, pady=5)
    global first_name_box
    first_name_box = Entry(seller)
    first_name_box.grid(row=3, column=1, pady=5)
    global last_name_box
    last_name_box = Entry(seller)
    last_name_box.grid(row=4, column=1, pady=5)
    global address1_box
    address1_box = Entry(seller)
    address1_box.grid(row=5, column=1, pady=5)
    global address2_box
    address2_box = Entry(seller)
    address2_box.grid(row=6, column=1, pady=5)
    global city_box
    city_box = Entry(seller)
    city_box.grid(row=7, column=1, pady=5)
    global state_box
    state_box = Entry(seller)
    state_box.grid(row=8, column=1, pady=5)
    global zipcode_box
    zipcode_box = Entry(seller)
    zipcode_box.grid(row=9, column=1, pady=5)
    global country_box
    country_box = Entry(seller)
    country_box.grid(row=10, column=1, pady=5)
    global phone_box
    phone_box = Entry(seller)
    phone_box.grid(row=11, column=1, pady=5)
    global email_box
    email_box = Entry(seller)
    email_box.grid(row=12, column=1, pady=5)

    ####Try getting them then passing them?
    firstName = first_name_box.get()
    lastName = last_name_box.get()
    address1 = address1_box.get()
    address2 = address2_box.get()
    city = city_box.get()
    state = state_box.get()
    zipcode = zipcode_box.get()
    country = country_box.get()
    phone = phone_box.get()
    email = email_box.get()
    add_seller_button = Button(seller, text="Add/Update Seller", command=add_seller)
    add_seller_button.grid(row=16, column=1, padx=10, pady=10)
    lookup_button = Button(seller, text="Lookup Seller*", command=look_seller)
    lookup_button.grid(row=17, column=1, padx=10, pady=10)
    lookup_info = Label(seller, text="Search with the * items.").grid(row=18, column=1, padx=10, pady=10)

####################   LOOKUP INVENTORY
def look_inv():
    #when sellerId put in and checked pulls it in and runs SQL
    invID = invID_box.get()
    ### If want to look up with phone or email
    # phNum = phone_box.get()
    # emailAdd = email_box.get()
    sql_command = "SELECT * FROM inventory WHERE itemNum = " + invID + ";"
    my_cursor = mydb.cursor()
    my_cursor.execute(sql_command)
    records = my_cursor.fetchone()

    #Inserts the data from DB to populate the fields.
    title_name_box.insert (0, records[1])
    inv_amt_box.insert (0, records[2])
    desc_name_box.insert (0, records[3])
    price_box.insert (0, records[4])
    seller_box.insert (0, records[6])


####################   ADD INVENTORY
def addInv():
    #create a cursor
    my_cursor = mydb.cursor()
    if invID_box.get() != "":
        sql_command = """UPDATE inventory SET itemName = %s, inventory = %s, description = %s, price = %s, seller = %s WHERE itemNum = %s"""
        itemName = title_name_box.get()
        inventory = inv_amt_box.get()
        description = desc_name_box.get()
        price = price_box.get()
        seller = seller_box.get()
        id_value = invID_box.get()
        inputs = (itemName, inventory, description, price, seller, id_value)
        my_cursor.execute(sql_command, inputs)
        mydb.commit()
    else:
    #else add the inv
        sql_command = "INSERT INTO inventory (itemName, inventory, description, price, seller) VALUES (%s, %s, %s, %s, %s)"
        values = (title_name_box.get(), inv_amt_box.get(), desc_name_box.get(), price_box.get(), seller_box.get())
        my_cursor.execute(sql_command, values)
    #commit the changes to db
    mydb.commit()
    clear_fields(addInv)


####################   INVENTORY
def inventory():
    inventory = Tk()
    inventory.title("Inventory")
    inventory.iconbitmap('favicon.ico')
    inventory.geometry("400x300")
    invID_label = Label(inventory, text="Item ID*: ").grid(row=2, column=0, sticky=W, padx=10)
    title_name_label = Label(inventory, text="Title: ").grid(row=3, column=0, sticky=W, padx=10)
    title_name_label = Label(inventory, text="Inventory: ").grid(row=4, column=0, sticky=W, padx=10)
    desc_name_label = Label(inventory, text="Description: ").grid(row=5, column=0, sticky=W, padx=10)
    price_label = Label(inventory, text="Price: $").grid(row=6, column=0, sticky=W, padx=10)
    seller_label = Label(inventory, text="Seller ID: ").grid(row=7, column=0, sticky=W, padx=10)
    #Create Entry Boxes
    global invID_box
    invID_box = Entry(inventory)
    invID_box.grid(row=2, column=1)
    global title_name_box
    title_name_box = Entry(inventory)
    title_name_box.grid(row=3, column=1)
    global inv_amt_box
    inv_amt_box = Entry(inventory)
    inv_amt_box.grid(row=4, column=1)
    global desc_name_box
    desc_name_box = Entry(inventory)
    desc_name_box.grid(row=5, column=1, pady=5)
    global price_box
    price_box = Entry(inventory)
    price_box.grid(row=6, column=1, pady=5)
    global seller_box
    seller_box = Entry(inventory)
    seller_box.grid(row=7, column=1, pady=5)
    addInv_button = Button(inventory, text='Add/Update Inventory', command=addInv)
    addInv_button.grid(row=10, column=1, sticky=W, padx=10)
    lookup_button = Button(inventory, text="Lookup Inventory*", command=look_inv)
    lookup_button.grid(row=17, column=1, padx=10, sticky=W, pady=10)
    lookup_info = Label(inventory, text="Search with the * items.").grid(row=18, column=1, padx=10, pady=10)

#save to CSV
def write_to_csv(result):
    with open("customers.csv", 'a') as f:
        w = csv.writer(f, dialect='excel')
        w.writerows(result)


####################   REPORTS
def report():
    #   RUN REPORTS
    def runReport():
        ivd_label = Label(report, text="Ivd. #", font=('Arial', 13, 'bold')).grid(row=7, column=0, padx=10)
        price_label = Label(report, text="Price", font=('Arial', 13, 'bold')).grid(row=7, column=1, padx=10)
        commission_label = Label(report, text="Commission\n20%", font=('Arial', 13, 'bold')).grid(row=7, column=2, padx=10)
        price_label = Label(report, text="Pay\nSeller", font=('Arial', 13, 'bold')).grid(row=7, column=3, padx=10)
        seller_label = Label(report, text="Seller #", font=('Arial', 13, 'bold')).grid(row=7, column=4, padx=10)

        #Creates CSV file and writes the first name elements
        # my_cursor.execute("SELECT * FROM sells")
        date_from = str(from_box.get())
        date_to = str(to_box.get())
        sql_command = "SELECT * FROM sells WHERE date BETWEEN '" + date_to + "-" + date_from + "-01' AND '" + date_to + "-" + date_from + "-31';"
        my_cursor.execute(sql_command)
        results = my_cursor.fetchall()
        transaction = str(results[0][1]).split(";")
        
        REPORT_TOTAL = 0.00
        COMMISSION_TOTAL = 0.00
        PAID_OUT_TOTAL = 0.00
        reportRow = 15
        csvFile=date_from + date_to + '.csv'
        # with open(csvFile, 'w') as consignmentReport:
        #     firstLine = ('Inventory Number', 'Price', '20% Commission', 'Pay Seller', 'Seller ID')
        #     writer = csv.writer( consignmentReport )
        #     writer.writerow( firstLine )
        for x in results:
            # print("x=", x[1])
            transaction = str(x[1]).split(";")
            # print("rowItem in loop= ", transaction)
            # with open(csvFile, 'a') as consignmentReport:
            #     writer = csv.writer( consignmentReport )
            for y in transaction:
                num=0
                thing = y.split(",")
                # print("thing=", thing)
                # print("Price=", thing[2], "Seller ID: ", thing[1])
                for z in thing:
                    # print("price=", z[1])
                    item = z.split(",")
                    # print("item= ", item)
                    
                    for a in item:
                        if "." in a:
                            price = float(a)
                            REPORT_TOTAL += price
                            price_format = "${:,.2f}".format(price)
                            # writer.writerow( [price_format] )
                            lookup_label = Label(report, text=price_format)
                            lookup_label.grid(row=reportRow, column=num, sticky=E, padx=10)
                            num += 1
                            amount = float(a) * 0.20
                            COMMISSION_TOTAL += amount
                            amount_format = "${:,.2f}".format(amount)
                            # writer.writerow( [amount_format] )
                            comm_label = Label(report, text = amount_format)
                            comm_label.grid(row=reportRow, column=num, sticky=E, padx=10)
                            num += 1
                            total_amount = float(a) * 0.80
                            PAID_OUT_TOTAL += total_amount
                            total_format = "${:,.2f}".format(total_amount)
                            # writer.writerow( [total_format] )
                            comm_label = Label(report, text = total_format)
                            comm_label.grid(row=reportRow, column=num, sticky=E, padx=10)
                        elif a == '':
                            break
                        else:
                            lookup_label = Label(report, text=a) 
                            strlookup = str(lookup_label) 
                            lookup_label.grid(row=reportRow, column=num, sticky=E, padx=10)
                        num +=1
                
                # writer.writerow( theLine )
                    # with open(csvFile, 'a') as consignmentReport:
                    #     stringLookUp = str(lookup_label)
                    #     writer = csv.writer( consignmentReport )
                    #     theLine = (total_format, price_format, amount_format, strlookup, stringLookUp)
                    #     writer.writerow( theLine )
                        
                reportRow += 1
                
        REPORT_TOTAL = "${:,.2f}".format(REPORT_TOTAL)
        COMMISSION_TOTAL = "${:,.2f}".format(COMMISSION_TOTAL)
        PAID_OUT_TOTAL = "${:,.2f}".format(PAID_OUT_TOTAL)
        ReportTotal = Label(report, text="Totals:", font=('Arial', 13, 'bold')).grid(row=700, column=0, padx=10)
        ReportTotalPrice = Label(report, text=REPORT_TOTAL, font=('Arial', 13, 'bold')).grid(row=700, sticky=E, column=1, padx=10)
        COMMISSTotalPrice = Label(report, text=COMMISSION_TOTAL, font=('Arial', 13, 'bold')).grid(row=700, sticky=E, column=2, padx=10)
        PAIDOUTTotalPrice = Label(report, text=PAID_OUT_TOTAL, font=('Arial', 13, 'bold')).grid(row=700, sticky=E, column=3, padx=10)
        with open(csvFile, 'a') as consignmentReport:
            # stringLookUp = str(lookup_label)
            finalLine = ('TOTAL:', REPORT_TOTAL, COMMISSION_TOTAL, PAID_OUT_TOTAL)
            writer = csv.writer( consignmentReport)
            writer.writerow( finalLine )
        # csv_button = Button(report, text="Save to CSV", command=lambda: write_to_csv(results))
        # csv_button.grid(row=reportRow+1, column=0)


    report = Tk()
    report.title("Reports")
    report.iconbitmap('favicon.ico')
    report.geometry("750x900")
    reportFromlabel = Label(report, text="Sales Month (##): ").grid(row=2, column=0, sticky=W, padx=10)
    reportTolabel = Label(report, text="Year (####): ").grid(row=2, column=3, sticky=W, padx=10)
    # total_label = Label(report, text="Total: ").grid(row=5, column=0, sticky=W, padx=10)
    #Create Entry Boxes
    from_box = Entry(report)
    from_box.grid(row=2, column=1)
    to_box = Entry(report)
    to_box.grid(row=2, column=4, columnspan=2)
    # total_box = Entry(report)
    # total_box.grid(row=5, column=1)
    runReport_button = Button(report, text='Run Report', command=runReport)
    runReport_button.grid(row=6, column=1, sticky=W, padx=10)

####################   PURCHASE
def purchase():
    selection = r.get()
    ERROR_label = Label(root, text="", font=('Arial', 18, 'bold')).grid(row=415, column=0, sticky=E, padx=10, columnspan=5)
    
    print("selection: ", selection)
    if selection == 0:
        ERROR_label = Label(root, text="ADD PAYMENT METHOD", font=('Arial', 18, 'bold')).grid(row=415, column=0, sticky=E, padx=10, columnspan=5)
    # print(FINALPURCHASE, selection)
    else:
        #create a cursor
        my_cursor = mydb.cursor()
        
        #add the sells
        sql_command = "INSERT INTO sells (purchased, paidBy) VALUES (%s, %s)"
        values = (FINALPURCHASE, selection)
        my_cursor.execute(sql_command, values)
        
        #commit the changes to db
        mydb.commit()
        clear_fields(purchase)

####################   ITEM SOLD
def itemSold(self):
    global salesBox
    salesBox = ttk.LabelFrame(root)

    salesBox.grid(column=0, row=5, padx=20, pady=20, columnspan=5)
    thisItem_label = Label(salesBox, text="Item Desc.:", font=('Arial', 13, 'bold')).grid(row=4, column=0, sticky=W, padx=10)
    total_label = Label(salesBox, text="Price:", font=('Arial', 13, 'bold')).grid(row=4, column=1, sticky=E, padx=10)
    seller_label = Label(salesBox, text="Seller:", font=('Arial', 13, 'bold')).grid(row=4, column=2, sticky=E, padx=10)

    #get items price from DB
    #create a cursor
    my_cursor = mydb.cursor()
    #split incoming
    global itemNums
    itemNums = item_box.get()
    itemNums = itemNums.split(' ')
    global salesItems
    salesItems = []
    global GRANDTOTAL
    GRANDTOTAL = 0.00
    global FINALPURCHASE
    FINALPURCHASE = ""
    #loop through itemNums to get prices for each
    for item in itemNums:
        sql_command = "SELECT * FROM inventory where itemNum = " + item + ";"
        my_cursor.execute(sql_command)
        itemPrice = my_cursor.fetchone()
        FINALPURCHASE += str(itemPrice[0]) + "," + str(itemPrice[4]) + "," + str(itemPrice[6]) + ";"
        thisItem = [itemPrice[1], itemPrice[4], itemPrice[6]]
        #pulling price from original call
        GRANDTOTAL += float(itemPrice[4])
        salesItems.append(thisItem)
    
    global lookup_label
    displayRow = 6
    #display the purchases:
    for x in salesItems:
        num=0
        for y in x:
            if type(y) == float:
                price = float(y)
                price_format = "${:,.2f}".format(price)
                lookup_label = Label(salesBox, text=price_format)
                lookup_label.grid(row=displayRow, column=num, sticky=E, padx=10)
            else:
                lookup_label = Label(salesBox, text=y) #[0] + ' ' +x[1] + ' ' + x[2]
                lookup_label.grid(row=displayRow, column=num, sticky=W, padx=10)
            num +=1
        displayRow += 1
    # GRANDTOTAL = float(GRANDTOTAL) + itemPrice[0]
    # grandTotal_box.delete(0, 'end')
    displayGRANDTOTAL = "${:,.2f}".format(GRANDTOTAL)
    grandTotal_label = Label(salesBox, text="Grand Total: ", font=('Arial', 16, 'bold')).grid(row=400, column=0, sticky=W, padx=10)
    GRANDTOTAL_label = Label(salesBox, text=displayGRANDTOTAL, font=('Arial', 16, 'bold'))
    GRANDTOTAL_label.grid(row=400, column=1, sticky=E, padx=10)
    # grandTotal_box.insert (0, displayGRANDTOTAL)
    #Add new line to enter


####################   MAIN/SALES
###Top row column for buttons for: Add Inventory, Sellers Accounts, Reports
###Sales will be the main screen the others will open in new window
lf = ttk.LabelFrame(root, text='Other forms')
lf.grid(column=0, row=0, padx=20, pady=20, columnspan=3)
global GRANDTOTAL
GRANDTOTAL = 0.00

# sellers_button.pack(side=TOP)
sellers_button = Button(lf, text='Sellers', command=seller)
sellers_button.grid(row=0, column=1, sticky=W, padx=10)

# inventory_button.grid(side=TOP)
inventory_button = Button(lf, text='Inventory', command=inventory)
inventory_button.grid(row=0, column=2, sticky=W, padx=10)

# report_button.grid(side=TOP)
report_button = Button(lf, text='Reports', command=report)
report_button.grid(row=0, column=3, sticky=W, padx=10)

#Title for column heads: Enter Item #, amount
item_label = Label(root, text="Enter Item #(s) for sale then hit Return").grid(row=2, column=0, sticky=W, padx=10, columnspan=4)


#Create Entry Boxes
#Box to have Item number entered:
global item_box
item_box = Entry(root)
item_box.grid(row=3, column=0, sticky=W, padx=10, columnspan=4)
item_box.bind('<Return>', itemSold)

# global total_box
# total_box = Entry(root)
# total_box.grid(row=3, column=1)

####GRAND TOTAL BOX
# global grandTotal_box
# grandTotal_box = Entry(root)
# grandTotal_box.grid(row=400, column=1)


###Radio Buttons
payButton = ttk.LabelFrame(root, text='Payment Method')
payButton.grid(column=0, row=402, padx=20, pady=20, columnspan=2)
global r
r = IntVar()

Radiobutton(payButton, text="Cash", variable=r, value=1).pack(side=LEFT)
Radiobutton(payButton, text="Check", variable=r, value=2).pack(side=LEFT)
Radiobutton(payButton, text="Credit Card", variable=r, value=3).pack(side=LEFT)
Radiobutton(payButton, text="PayPal", variable=r, value=4).pack(side=LEFT)


###Purchase buttons
purchase_button = Button(root, text='Complete Purchase', command=purchase)
purchase_button.grid(row=405, column=1, sticky=W, padx=10)



root.mainloop()