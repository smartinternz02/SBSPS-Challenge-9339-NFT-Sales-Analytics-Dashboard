from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class nft_analytics:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1500x790+0+0")
                self.root.title("NFT SALES ANALYTICS DASHBOARD")
                
                # first image

                img = Image.open(r"C:\Users\snehal\Desktop\python project\img\ap.jpg")
                img = img.resize((500,130),Image.ANTIALIAS)
                self.photoimg = ImageTk.PhotoImage(img)

                f_lbl = Label(self.root,image=self.photoimg)
                f_lbl.place(x=0,y=0,width=500,height=130)

                # second image

                img1 = Image.open(r"C:\Users\snehal\Desktop\python project\img\apsit.jpg")
                img1 = img1.resize((500,130),Image.ANTIALIAS)
                self.photoimg1 = ImageTk.PhotoImage(img1)

                f_lbl = Label(self.root,image=self.photoimg1)
                f_lbl.place(x=500,y=0,width=500,height=130)

                

                # third image

                img2 = Image.open(r"C:\Users\snehal\Desktop\python project\img\itsa.jpg")
                img2 = img2.resize((500,130),Image.ANTIALIAS)
                self.photoimg2 = ImageTk.PhotoImage(img2)

                f_lbl = Label(self.root,image=self.photoimg2)
                f_lbl.place(x=1000,y=0,width=500,height=130)

                title_lbl = Label(self.root, text ="NFT SALES ANALYTICS DASHBOARD" , font =("times new roman",35,"bold"),fg="black")
                title_lbl.place(x=0,y=130,width=1530,height =45)
                nft_frame=LabelFrame(self.root ,bd =2 , relief = RIDGE , text = "NFT sales visualization" , font=("times new roman",12,"bold"))
                nft_frame.place(x=5,y=200,width=1485,height=300)

                btn_frame=Frame(nft_frame , bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=200,width=1300,height=135)
                no_of_sales_btn=Button(btn_frame , text="NUMBER OF SALES" ,command=self.nft  ,width=25 ,font =("times new roman",13,"bold"),bg ="white")
                no_of_sales_btn.grid(row=0,column=0, padx=25)
                average_btn=Button(btn_frame,text="AVERAGE SALE PRICE" ,command=self.nft_2,width =25,font=("times new roman",13,"bold"),bg ="white")
                average_btn.grid(row=0,column=1,padx=25)
                market_btn=Button(btn_frame,text="ACTIVE MARKET WALLETS",command=self.nft_3,width =25,font=("times new roman",13,"bold"),bg ="white")
                market_btn.grid(row=0,column=2,padx=25)
                sale_btn=Button(btn_frame,text="ACTIVE SALES" , command=self.nft_4,width =25,font=("times new roman",13,"bold"),bg ="white")
                sale_btn.grid(row=0,column=3,padx=25)
        def nft(self):
                
                df=pd.read_csv("C:/Users/snehal/Desktop/NFT-Sales-Analytics/NFT_Sales.csv")
                def plot_df(df, x, y, title="", xlabel='Date', ylabel='NFT', dpi=100):
                        figure=plt.figure(figsize=(16,8), dpi=dpi)
                        plt.plot(x, y, color='tab:red')
                        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
                        line2 = FigureCanvasTkAgg(figure, root)
                        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,)
                plot_df(df, x=df.index, y=df.Number_of_Sales, title='Daily NFT Sales.')
        def nft_2(self):
                df=pd.read_csv("C:/Users/snehal/Desktop/NFT-Sales-Analytics/NFT_Sales.csv")
                def plot_df2(df, x, y, title="", xlabel='Date', ylabel='NFT', dpi=100):
                        figure=plt.figure(figsize=(16,8), dpi=dpi)
                        plt.plot(x, y, color='tab:red')
                        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
                        line2 = FigureCanvasTkAgg(figure, root)
                        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,)
                plot_df2(df, x=df.index, y=df.AverageUSD_cum, title='Average Sale Price.')
        def nft_3(self):
                
                df=pd.read_csv("C:/Users/snehal/Desktop/NFT-Sales-Analytics/NFT_Sales.csv")
                def plot_df3(df, x, y, title="", xlabel='Date', ylabel='NFT', dpi=100):
                        figure=plt.figure(figsize=(16,8), dpi=dpi)
                        plt.plot(x, y, color='tab:red')
                        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
                        line2 = FigureCanvasTkAgg(figure, root)
                        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,)
                plot_df3(df, x=df.index, y=df.Active_Market_Wallets_cumsum, title='Active Market Wallets')
        def nft_4(self):
                
                df=pd.read_csv("C:/Users/snehal/Desktop/NFT-Sales-Analytics/NFT_Sales.csv")
                def plot_df4(df, x, y, title="", xlabel='Date', ylabel='NFT', dpi=100):
                        figure=plt.figure(figsize=(16,8), dpi=dpi)
                        plt.plot(x, y, color='tab:red')
                        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
                        line2 = FigureCanvasTkAgg(figure, root)
                        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,)
                plot_df4(df, x=df.index, y=df.Sales_USD_cumsum, title='Active Sales')
                
                
           

      

if __name__ == "__main__":
        root = tk.Tk()
        obj = nft_analytics(root)
        root.mainloop()
