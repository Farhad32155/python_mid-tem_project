from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

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

        entry_ref = ttk.Entry(labelframeleft, width=29,
                              font=('arial', 13, 'bold'))
        entry_ref.grid(row=0, column=1)

        # cust Name
        cname = Label(labelframeleft, text='Customer Name:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'))
        txtcname.grid(row=1, column=1)

        # Mother name
        lblmname = Label(labelframeleft, text='Mother Name:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'))
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, text='Gender:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(
            labelframeleft, font=('arial', 12, 'bold'), width=27, state='readonly')
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # post code
        lblPostCode = Label(labelframeleft, text='PostCode:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'))
        txtPostCode.grid(row=4, column=1)

        # mobile Number
        lblMobile = Label(labelframeleft, text='Mobile:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, width=29,
                              font=('arial', 13, 'bold'))
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, text='PostCode:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, width=29,
                             font=('arial', 13, 'bold'))
        txtEmail.grid(row=6, column=1)

        # nationality-combobox
        lblNationality = Label(labelframeleft, text='Nationality:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        # id proof type combobox
        lblIdProof = Label(labelframeleft, text='Id Proof Type:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        # Id number
        lblIdNumber = Label(labelframeleft, text='Id Number:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, width=29,
                                font=('arial', 13, 'bold'))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text='Address:', font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft, width=29,
                               font=('arial', 13, 'bold'))
        txtAddress.grid(row=10, column=1)


if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
