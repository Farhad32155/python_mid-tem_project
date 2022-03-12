from msilib import add_data
from tkinter import*
from turtle import width
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        # --------variables-------
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # -------Title---------
        lbl_title = Label(self.root, text='ADD CUSTOMER DETAILS', font=(
            'times new roman', 18, 'bold'), bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # -----------logo image----------
        img2 = Image.open(r'D:\hotel_management_system\images\hotel2.jpg')
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=5, width=100, height=40)

        # ---------label-frame-----
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='Customer Details', font=(
            'times new roman', 12, 'bold'), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # -------labels and entries-----

        # custRef
        lbl_cust_ref = Label(labelframeleft, text='Customer Ref', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, width=29, textvariable=self.var_ref,
                              font=('arial', 13, 'bold'), state='readonly')
        entry_ref.grid(row=0, column=1)

        # cust Name
        cname = Label(labelframeleft, text='Customer Name:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29, textvariable=self.var_cust_name,
                             font=('arial', 13, 'bold'))
        txtcname.grid(row=1, column=1)

        # Mother name
        lblmname = Label(labelframeleft, text='Mother Name:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mother,
                             font=('arial', 13, 'bold'))
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, text='Gender:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(
            labelframeleft, textvariable=self.var_gender, font=('arial', 12, 'bold'), width=27, state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # post code
        lblPostCode = Label(labelframeleft, text='PostCode:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, width=29, textvariable=self.var_post,
                                font=('arial', 13, 'bold'))
        txtPostCode.grid(row=4, column=1)

        # mobile Number
        lblMobile = Label(labelframeleft, text='Mobile:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mobile,
                              font=('arial', 13, 'bold'))
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, text='Email:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29,
                             font=('arial', 13, 'bold'))
        txtEmail.grid(row=6, column=1)

        # nationality-combobox
        lblNationality = Label(labelframeleft, text='Nationality:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(
            labelframeleft, textvariable=self.var_nationality, font=('arial', 12, 'bold'), width=27, state='readonly')
        combo_Nationality['values'] = ('Bangladeshi', 'Pakistani', 'Indian')
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # id proof type combobox
        lblIdProof = Label(labelframeleft, text='Id Proof Type:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(
            labelframeleft, textvariable=self.var_id_proof, font=('arial', 12, 'bold'), width=27, state='readonly')
        combo_id['values'] = ('NID', 'DrivingLicense', 'Passport')
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        # Id number
        lblIdNumber = Label(labelframeleft, text='Id Number:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, width=29, textvariable=self.var_id_number,
                                font=('arial', 13, 'bold'))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text='Address:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft, width=29, textvariable=self.var_address,
                               font=('arial', 13, 'bold'))
        txtAddress.grid(row=10, column=1)

        # -----buttons-------
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text='ADD', command=self.add_data, font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text='UPDATE', font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text='DELETE', font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnDelete.grid(row=0, column=3, padx=1)

        btnReset = Button(btn_frame, text='RESET', font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnReset.grid(row=0, column=4, padx=1)

        # -----table frame----
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='VIEW DETAILS AND SEARCH SYSTEM', font=(
            'times new roman', 12, 'bold'), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text='Search By:', font=(
            'arial', 12, 'bold'), bg='red', fg='white')
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        combo_Search = ttk.Combobox(
            Table_Frame, font=('arial', 12, 'bold'), width=24, state='readonly')
        combo_Search['values'] = ('Mobile', 'Ref')
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        txtSearch = ttk.Entry(Table_Frame, width=24,
                              font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text='Search', font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text='Show All', font=(
            'arial', 12, 'bold'), bg='black', fg='gold', width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # -------Show data table-----
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(
            details_table, columns=('ref', 'name', 'mother', 'gender', 'post', 'mobile', 'email', 'nationality', 'idproof', 'idnumber', 'address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading('ref', text='Refer No')
        self.Cust_Details_Table.heading('name', text='Name')
        self.Cust_Details_Table.heading('mother', text='Mother Name')
        self.Cust_Details_Table.heading('gender', text='Gender')
        self.Cust_Details_Table.heading('post', text='PostCode')
        self.Cust_Details_Table.heading('mobile', text='Mobile')
        self.Cust_Details_Table.heading('email', text='Email')
        self.Cust_Details_Table.heading('nationality', text='Nationality')
        self.Cust_Details_Table.heading('idproof', text='Id Proof')
        self.Cust_Details_Table.heading('idnumber', text='Id Number')
        self.Cust_Details_Table.heading('address', text='Address')

        self.Cust_Details_Table['show'] = 'headings'

        self.Cust_Details_Table.column('ref', width=100)
        self.Cust_Details_Table.column('name', width=100)
        self.Cust_Details_Table.column('mother', width=100)
        self.Cust_Details_Table.column('gender', width=100)
        self.Cust_Details_Table.column('post', width=100)
        self.Cust_Details_Table.column('mobile', width=100)
        self.Cust_Details_Table.column('email', width=100)
        self.Cust_Details_Table.column('nationality', width=100)
        self.Cust_Details_Table.column('idproof', width=100)
        self.Cust_Details_Table.column('idnumber', width=100)
        self.Cust_Details_Table.column('address', width=100)
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind('<ButtonRelease-1>', self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == '' or self.var_mother.get() == '':
            messagebox.showerror(
                'Error', 'All fields are required to fill', parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(
                    host='localhost', username='root', password='', database='management')
                my_cursor = conn.cursor()
                my_cursor.execute(
                    'insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (

                        self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get()

                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Customer has been added', parent=self.root)

            except Exception as es:
                messagebox.showwarning(
                    'Warning', f'Something went wrong:{str(es)}', parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', username='root', password='', database='management')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from customer')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=''):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content['values']

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])


if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
