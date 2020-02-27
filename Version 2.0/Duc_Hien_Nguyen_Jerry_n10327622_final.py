#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct". 
#
#    Student no: n10327622
#    Student name: Duc Hien Nguyen - Jerry
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [81022PT]
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import *

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
from tkinter.ttk import *

# import ctypes for keyboard and foreground event
from ctypes import *

# import message box
from tkinter import messagebox

# import os and webbrowser for openning invoice
import webbrowser, os

# imoprt ssl for disabling ssl certificate verification
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import *

# Functions for pausing execution (in order to read messages)
# (see sleep function in PythonDocs)
from time import *
#

# YOU ARE NOT PERMITTED TO IMPORT ANY FURTHER MODULES

#--------------------------------------------------------------------#

#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the invoice file. To simplify marking, your program should
# produce its results using this file name.
invoice_file = 'invoice.html'

### download the archive html file (washing mmachine)
##archive_site = 'https://www.betta.com.au/laundry/washing-machines'
##archive_page = urlopen(archive_site)
##archive_bytes = archive_page.read()
##archive_contents = archive_bytes.decode('UTF-8')
##
### write contents to a local text file using unicode
##washing_machine_html = open('archive\washing_machine.html', 'w', encoding = 'UTF-8')
##washing_machine_html.write(archive_contents)
##washing_machine_html.close()

# Archived data
# washing machine
# open the archived html file
washing_machine_html = open('archive\washing_machine.html', 'U').read()

# find product's name
washing_machine_name = findall('<img class="first_image" src=".*?" alt="(.*?)">', washing_machine_html)

# find product's price
washing_machine_price = findall('<h2 class="product-name"><a href=".*?".*?data-price="(.*?)000"',
                            washing_machine_html)
# change currency format to 2 decimal places
for index in range(len(washing_machine_price)):
    washing_machine_price[index] = '%.2f' % float(washing_machine_price[index])

# find product's image
washing_machine_image = findall('<img class="first_image" src="(.*?)" alt=".*?">',
                                washing_machine_html)

# create tuples for product's data:
washing_machine_value = []
for index in range(len(washing_machine_image)):
    washing_machine_value += [(index + 1, washing_machine_name[index].replace("&amp;amp;", "&"),
                           washing_machine_price[index],
                           washing_machine_image[index])]
    
#--------------------------------------------------------------------#

# GPU
# download gpu contents from url
gpu_contents = download('https://www.umart.com.au/Graphics-Cards---GPU_610C.html','GPU')

# find product's name
gpu_name = findall('alt="(.*?)"', gpu_contents)

# find product's price
gpu_price = findall('itemprop="price" content="(.*?)"', gpu_contents)

# change currency format to 2 decimal places
for index in range(len(gpu_price)):
    gpu_price[index] = '%.2f' % float(gpu_price[index].replace(',', '')) 

# find product's image with provided temp name        
gpu_image = findall('title=".*?" ><img src="(.*?)" alt', gpu_contents)
    
# create tuples for adding values into table    
gpu_value = []
for index in range(len(gpu_name)):
    gpu_value += [(index + 1, gpu_name[index], gpu_price[index], gpu_image[index])]
    
#--------------------------------------------------------------------#
    
# Phone
# download phone contents from url
phone_contents = download('https://www.kogan.com/au/shop/phones/','phones')

# find product's name
phone_name = findall(r'title="(.*?)">\1', phone_contents)

# find product's price
phone_price = findall('itemProp="price" content="(.*?)"',
                            phone_contents)
# change format of currency to 2 decimal places
for index in range(len(phone_price)):
        phone_price[index] = '%.2f' % float(phone_price[index])

# find product's image

# create temporary name replace "(" with "\(", ")" with "\)" and "|" with "\|"
# and "+" with "\+" for regex to understand
temp_name = []
for index in range(len(phone_name)):
    temp_name += [sub('\(','\(', phone_name[index])]
    temp_name[index] = sub('\)','\)', temp_name[index])
    temp_name[index] = sub('\|','\|', temp_name[index])
    temp_name[index] = sub('\+','\+', temp_name[index])
    
phone_image = []
for name in temp_name:
    phone_image += findall('title="' + name + '".*?<img src="(.*?) alt="' + name,phone_contents)

# create tuples for product's data:
phone_value = []
for index in range(len(phone_name)):
    phone_value += [(index + 1, phone_name[index].replace("&amp;", "&"),
                           phone_price[index],
                           phone_image[index])]
    
#--------------------------------------------------------------------#
    
# functions for main window, categories and data for product table

# Steal focus function which virtuallize the state of input a key from
# keyboard to that window, and make that window on top of others
set_foreground = windll.user32.SetForegroundWindow
keyboard_event = windll.user32.keybd_event

ctr_key = 0x11 # choose random key, for example ctrl key
extended_key = 0x0001 # extend key which is from the numpad
key_up = 0x0002 # is used to release the button

def take_focus():
    window.attributes("-topmost", True) # make window top of another applications
    keyboard_event(ctr_key, 0, extended_key | 0, 0) # press the ctr key
    # make window a foreground thread in which is given keyboard input to
    set_foreground(window.winfo_id())
    keyboard_event(ctr_key, 0, extended_key | key_up, 0)# release button
    addtocart.focus_set() # set focus to a random place in window
    window.attributes("-topmost", False) # stop forcing window to be on top
    
# insert value function for inserting each shop's products into table
def insert_value():
    
    # change value of the table according to radiobutton being chosen
    if category.get() == 1:
        table_data = washing_machine_value
        source['text'] = 'https://www.betta.com.au/laundry/washing-machines'
    elif category.get() == 2:
        table_data = phone_value
        source['text'] = 'https://www.kogan.com/au/shop/phones/'
    else:
        table_data = gpu_value
        source['text'] = 'https://www.umart.com.au/Graphics-Cards---GPU_610C.html'

    # disable spinbox and addtocart button when product is not selected    
    addtocart['state'] = DISABLED
    quantity['state'] = DISABLED

    # delete all elements in table for importing new data
    table.delete(*table.get_children())

    # insert data into table
    index = iid = 0    
    for row in table_data:
        table.insert("", index, iid, values = row)
        index = iid = index + 1
        
#--------------------------------------------------------------------#

# Create the GUI
# main window
window = Tk()

# make window on top of other as well as focus on that window
window.after(200, lambda: take_focus())

# title
window.title('Online shopping app')

# variable for categories
category = IntVar()

# opening shopping image:
shopping_img = PhotoImage(file = 'shopping.gif')

# label
label = Label(window, text = 'Welcome to JerrITech online shop!',
              font = ('Times', '24', 'bold'), image = shopping_img,
              compound = BOTTOM)
label.grid(row = 1, column = 1, columnspan = 3)

# archive frame
archive_frame = LabelFrame(window, text = 'Archive Sales')
archive_frame.grid(row = 4, column = 1, pady = 5)

# washing machine radio button
washing_machine = Radiobutton(archive_frame, text = 'Washing machines',
                  variable = category, value = 1,
                  command = insert_value)
washing_machine.pack()
       
# online frame
online_frame = LabelFrame(window, text = 'Online Sales')
online_frame.grid(row = 4, column = 3, pady = 5)

# phone radio button
phone = Radiobutton(online_frame, text = 'Phones and accessories',
                  variable = category, value = 2,
                  command = insert_value)
phone.grid(row = 1, column =  1, sticky = 'w')

# GPU radio button
gpu = Radiobutton(online_frame, text = 'Graphics cards',
                          variable = category, value = 3,
                  command = insert_value)
gpu.grid(row = 2, column =  1, sticky = 'w')


# source label
source = Label(window, text = 'Waiting for shop selection...')
source.grid(row = 3, column = 1, columnspan = 3, pady = 5)

#--------------------------------------------------------------------#

# function for taking value out of current selected product in table
# dict using to store data of current selected product
cur_value = {}
def product_select_item(a):
    global cur_value
        
    # reset the quantity spinbox each time choosing new item
    quantity.delete(0, END)
    quantity.insert(0, '1')

    # take the data of current selected product
    curitem = table.focus()
    cur_value = table.item(curitem)
    
    # enable spinbox and addtocart button when product is selected
    # and disable if nothing is selected or the product has already
    # been in the shopping cart list
    if cur_value['values'] != '': # if the values is not empty
        # product has already been in the cart
        if set([cur_value['values'][1]]).issubset(product_cart_list):
            addtocart['state'] = DISABLED
            quantity['state'] = DISABLED
        else:
            addtocart['state'] = NORMAL
            quantity['state'] = NORMAL
        
# create a table containing list of products
table = Treeview(window, selectmode='browse')
table.grid(column = 1,row = 2, columnspan = 3, pady = 5)

# create columns
table['columns'] = ['No', 'Product Name', 'Price (AUD)']
table['show'] = 'headings'
table.heading('No', text = 'No', anchor = 'w')
table.column('No', minwidth = 0, width = 25)
table.heading('Product Name', text = 'Product Name', anchor = 'w')
table.column('Product Name', minwidth = 0, width = 530)
table.heading('Price (AUD)', text = 'Price (AUD)', anchor = 'e')
table.column('Price (AUD)', minwidth = 0, width = 70, anchor = 'e')
table.bind('<ButtonRelease-1>', product_select_item) # bind left mouse release
table.bind('<KeyRelease-Up>', product_select_item) # bind up arrow release
table.bind('<KeyRelease-Down>', product_select_item) # bind down arrow release
table.focus_set()


#--------------------------------------------------------------------#

# create spinbox for the quantity chosen for each product
# and add to cart button

# create frame for spinbox and add-to-cart button
shopping_frame = LabelFrame(window, text = 'Select quantity for this product',
                            labelanchor = 'nw')
shopping_frame.grid(row = 5, column = 2)

# create spinbox for quantity select
quantity = Spinbox(shopping_frame, from_ = 1, to = 99,
                   wrap = True, state =  DISABLED)
quantity.grid(column = 1, row = 1)

#--------------------------------------------------------------------#

# functions for interacting with shopping cart window and it's widgets

# close shopping cart function
# and reset databases
def close_shopping_cart():
    global product_cart_list, cart_detail, cart_iid
    cart_list.destroy()
    product_cart_list = [] # reset chosen products' name
    cart_detail  = [] # reset chosen products' detail
    cart_iid = []  # reset cart iid list

    # enable spinbox and addtocart button if currently disabled
    addtocart['state'] = NORMAL
    quantity['state'] = NORMAL

# close window function    
def close_window():
    # Thank you before closing
    if not messagebox.askyesno("JerrITech Shopping App", "Do you want to continue shopping?"):
        if messagebox.showinfo("Goodbye!!!", "Thank you for shopping at JerrITech"):
            window.destroy()
        
# take value of selected item in shopping cart for deleting:
selected_item = {}
def cart_select_item(b):
    global selected_item, pos_in_cart
    selected_item = cart_table.item(cart_table.focus())

    # enable delete button when product is selected
    # if and only if the current value is not empty
    if selected_item['values'] != '':
        delete['state'] = NORMAL
        # position of possible deleted item (to be used in delete function)
        pos_in_cart = cart_iid.index(selected_item['values'][5])
        
# delete function
def delete_fn():
    iid_pos = selected_item['values'][5] # delete position in cart table
    cart_table.delete(iid_pos) # delete from table
    position = product_cart_list.index(selected_item['values'][2]) # position in databases
    del product_cart_list[position] #  delete from list of products' name
    del cart_detail[position] # delete from list of products' detail
    del cart_iid[position] # delete from list of chosen products' iid list

    # reset the order after deleting
    for order in range(len(product_cart_list)):
        cart_table.set(cart_iid[order], column = 'No', value = order + 1)

    # enable add to cart button and quantity spinbox
    # if current selected item in product list
    # is the item that has just been deleted out of the cart list
    if selected_item['values'][2] == cur_value['values'][1]:
        addtocart['state'] = NORMAL
        quantity['state'] = NORMAL

    # disable invoice and delete button if there is nothing in cart
    if cart_iid == []:
        invoice['state'] = DISABLED
        delete['state'] = DISABLED
    # if the deleted item was in the last place then move the focus
    # and seletion to the upper one so that we can delete continously
    elif pos_in_cart == len(cart_iid):
        cart_table.selection_set(cart_iid[pos_in_cart - 1])
        cart_table.focus([cart_iid[pos_in_cart - 1]])
        cart_select_item(None)
    # else if the deleted item wasn't in the last place then move the focus
    # and seletion to the lower one
    else:
        cart_table.selection_set(cart_iid[pos_in_cart])
        cart_table.focus([cart_iid[pos_in_cart]])
        cart_select_item(None)
        
# printing invoice function:
def print_invoice():
    # create invoice file
    invoice_html = open(invoice_file, 'w', encoding = 'UTF-8')

    # update progress
    progress['value'] = 25
    status['text'] = 'Generating your invoice...'
    cart_list.update_idletasks()
    
    # write header, style, body opening:
    invoice_html.write\
(
'''
<!DOCTYPE html>
<html>
<head>
<!-- add a favicon to the tab -->
<link rel="icon" 
      type="image/jpg" 
      href="https://yt3.ggpht.com/--0pKjYfcdfw/AAAAAAAAAAI/AAAAAAAAAAA/Rck6FqtsuPY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg">
<!-- formatting style for div box, class for center image and table format -->
<style>
div {
	max-width: 1000px;
	padding: 30px;
    margin: auto;
	border: 1px solid rgb(238,238,238);
	box-shadow: 0 0 10px rgba(0, 0, 0, .15);
    padding: 30px;
    margin: auto;
}

body {background-color: white;}
h1   {color: black;}
p    {color: black;}
.center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
}

table {
    width: 100%;
}

th {
    height: 50px;
	text-align: center;
}
td{
	text-align: center;
}
</style>
</head>
<!-- title -->
<title>JerrITech Shopping Inoice</title>
<body>
	<!-- heading -->
	<h1 align="left"><i>JerrITech Online Shopper Co. Invoice</i></h1>
	<!-- company logo -->
	<img class="right" src="https://yt3.ggpht.com/--0pKjYfcdfw/AAAAAAAAAAI/AAAAAAAAAAA/Rck6FqtsuPY/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg" style="max-width:100px;">
'''
)

    # update progress
    sleep(1)
    progress['value'] = 50
    status['text'] = 'Listing your purchases...'
    cart_list.update_idletasks()
    
    # write each product detail:
    price_list = []
    for each_product in cart_detail:
        product_quantity =  each_product[0]
        product_name = each_product[1]
        product_price = each_product[2]
        price_list.append(float(product_price))
        product_image = each_product[3]
        invoice_html.write\
(
'''
	<div>
		<!-- Product Name -->
		<h3 align="center">{}</h3>
		<!-- Product image -->
		<img class="center" src="{}">
		<!-- Table for Product's detail -->
		<table>
			<tr>
				<th>Amount</th>
				<th>Price/Product</th>
				<th>Total Price</th>
			</tr>
			<tr>
				<!-- Quantity -->
				<td>{}</td>
				<!-- Price/Product -->
				<td>${}AUD</td>
				<!-- Total Price -->
				<td>${}AUD</td>
			</tr>
		</table>
	</div>
'''.format(product_name, product_image, product_quantity,
           '%.2f' % (float(product_price) / product_quantity), product_price)
)
    # update progress
    sleep(1)
    progress['value'] = 75
    status['text'] = 'Caculating total price...'
    cart_list.update_idletasks()
    
    invoice_html.write\
(
'''
	<div>
		<h2 align="center">Total of the above purchases</h2>
		<h2 align="center">${}AUD</h2>
		<h4>Archive Store's</h4>
		<ul>
			<li>
				<a href="https://www.umart.com.au/Graphics-Cards---GPU_610C.html">
				https://www.umart.com.au/Graphics-Cards---GPU_610C.html
				</a>
			</li>
		</ul>
		<h4>Online Store's</h4>
		<ul>
			<li>
				<a href="https://www.kogan.com/au/shop/phones/">
				https://www.kogan.com/au/shop/phones/
				</a>
			</li>
			<li>
				<a href="https://www.betta.com.au/laundry/washing-machines">
				https://www.betta.com.au/laundry/washing-machines
				</a>
			</li>		
		</ul> 
</body>
</html>
'''.format('%.2f' % sum(price_list))
)
    # update progress
    sleep(1)
    progress['value']= 100
    status['text'] = 'Done!...'

    # close html file
    invoice_html.close()
    
    # close shopping cart
    window.after(500, lambda: close_shopping_cart())

    # open invoice after closing shopping cart
    window.after(700, lambda: webbrowser.open('file://' + os.path.realpath(invoice_file)))
    
#--------------------------------------------------------------------#
    
# add to cart function for adding current select item into cart
index = iid = 1 # set index equal to iid in cart table
product_cart_list = [] # store chosen product's name
cart_detail  = [] # store detail for printing invoice
cart_iid = [] # store iid position of chosen items
def add_to_cart():
    global index, iid, cart_list, cart_table, product_cart_list, invoice,\
           delete, cart_detail, cart_iid, progress, status
    
    # defining values for products chosen
    try: # raise exception in case user type wrong value
        number = int(quantity.get()) # quantity
        if number < 1: # quantity should always be positive
            raise Exception
        product_name = cur_value['values'][1] # name
        price = '%.2f' % (eval(cur_value['values'][2]) * number) # take the price and make it two decimal places
        image = cur_value['values'][3] # image
        product_cart_list.append(product_name) # storing products' names
        cart_detail.append([number, product_name, price, image]) # storing detail for invoice
        order = len(product_cart_list) # order in table
        cur_pro_data = (order, number, product_name, price, image, iid) # data to be add into cart table
        cart_iid.append(iid) # append iid into the iid list

        # create cart table
        
        # if it's the first time or cart table was closed
        # create it again
        if index == 1 or not cart_list.winfo_exists():
            # create new window for tracing customer's cart list
            cart_list = Toplevel()
                    
            # title
            cart_list.title('Shopping cart list')

            # create table for tracing for chosen product:
            cart_table = Treeview(cart_list, selectmode='browse')
            cart_table.grid(column = 1,row = 1, columnspan = 2, pady = 5)

            # create columns
            cart_table['columns'] = ['No','Quantity', 'Product Name', 'Price (AUD)']
            cart_table['show'] = 'headings'
            cart_table.heading('No', text = 'No', anchor = 'w')
            cart_table.column('No', minwidth = 0, width = 50)
            cart_table.heading('Quantity', text = 'Quantity', anchor = 'w')
            cart_table.column('Quantity', minwidth = 0, width = 60)
            cart_table.heading('Product Name', text = 'Product Name', anchor = 'w')
            cart_table.column('Product Name', minwidth = 0, width = 600)
            cart_table.heading('Price (AUD)', text = 'Price (AUD)', anchor = 'e')
            cart_table.column('Price (AUD)', minwidth = 0, width = 70, anchor = 'e')
            cart_table.bind('<ButtonRelease-1>', cart_select_item) # bind left mouse release
            cart_table.bind('<KeyRelease-Up>', cart_select_item) # bind up arrow release
            cart_table.bind('<KeyRelease-Down>', cart_select_item) # bind down arrow release 
            cart_table.focus_set()
            
            # insert current selected product
            cart_table.insert("", index, iid, values = cur_pro_data)

            # create delete button
            delete = Button(cart_list, text = 'Delete', command = delete_fn,
                            state = DISABLED)
            delete.grid(column = 1, row = 2, pady = 5)
            
            # create invoce button
            invoice = Button(cart_list, text = 'Print Invoice',
                             command = print_invoice)
            invoice.grid(column = 2, row = 2, pady = 5)

            # create a frame for updating progress
            status = LabelFrame(cart_list, labelanchor = 'n',
                                text = 'Waiting for selection...')
            status.grid(column = 1, row = 3, columnspan = 2, pady = 5)
            
            # create a progressbar
            progress = Progressbar(status, orient = HORIZONTAL,
                                   length = 700, mode = 'determinate')
            progress.grid(column = 1, row = 1, columnspan = 2)
            
        # if cart table has already been opened
        else:
            # insert data into cart table
            cart_table.insert("", index, iid, values = cur_pro_data)

        # reset quantity spinbox  to 1 after adding product
        quantity.delete(0, END)
        quantity.insert(0, '1')
        
        # enable invoice button, make addtocart button, quantity spinbox
        # disabled after adding product, until that product is deleted
        # from cart table the button will be active
        invoice['state'] = NORMAL
        addtocart['state'] = DISABLED
        quantity['state'] = DISABLED

        # move the focus, selection and scroll to the newly added item
        # so that users can keep track of them and delete them if they want
        cart_table.selection_set(iid)
        cart_table.focus(iid)
        
        # take value of selected item
        cart_select_item(None)
        
        # autoscroll to last item in cart list(have to delay some time for
        # the yview to be updated)
        cart_list.after(100, lambda: cart_table.yview_moveto(1)) 
    
        # position in cart table
        index = iid = index + 1
        
        # change geometry relative to main window
        x = window.winfo_x()
        y = window.winfo_y()
        cart_list.geometry("+%d+%d" % (x + 650, y + 150))
        
        # focus
        cart_list.focus()
        
        # on close event
        cart_list.protocol("WM_DELETE_WINDOW", close_shopping_cart)
     
        # start window's event loop
        cart_list.mainloop()

    except: # print error if user enters inapproriate value
        print('Invalid value entered')
        # reset quantity spinbox when wrong value entered
        quantity.delete(0, END)
        quantity.insert(0, '1')
    
# create add-to-cart button
addtocart = Button(shopping_frame, text = 'Add to cart',
                   state = DISABLED, command = add_to_cart)
addtocart.grid(column = 2, row = 1, pady = 5)

#--------------------------------------------------------------------#

# start window's event loop
window.protocol("WM_DELETE_WINDOW", close_window)
window.mainloop()
