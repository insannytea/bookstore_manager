#===IMPORT SECTION===
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class BookstoreManagerApp(tk.Tk):
    # initialise app
    def __init__(self):
        super().__init__()

        #===Connect database to python===
        self.data_base = "book_database"
        self.db = sqlite3.connect(f'data/{self.data_base}')
        self.cursor = self.db.cursor()

        #-Main Window Settings-
        self.title('Bookstore Manager')
        self.geometry('1200x500')

        #-Header-
        self.header_label = ttk.Label(self, text='Bookstore Manager App')
        self.header_label.grid(row=0, column=0, columnspan=3)

        #-Table select drop down menu-
        self.options = self.query_table_names()
        self.variable = tk.StringVar()
        self.select_table_dd = ttk.Combobox(self, textvariable=self.variable)

        self.select_table_dd['values'] = self.options
        self.select_table_dd['state'] = 'readonly'
        self.select_table_dd.grid(row=1, column=0, sticky='e')
        # self.select_table_dd.bind("<<ComboboxSelected>>", self.get_selection)


        #-Submit table choice button-
        self.submit_table_choice_btn = ttk.Button(self, text="Submit", command=self.display_table)
        self.submit_table_choice_btn.grid(row=1, column=1, sticky='w')

        # self.data_table = self.display_table()

        #-Add data button-
        self.add_data_btn = ttk.Button(self, text="Add Data")
        self.add_data_btn.grid(row=3, column=0)

        #-Edit data button-
        self.edit_data_btn = ttk.Button(self, text="Update Data")
        self.edit_data_btn.grid(row=3, column=1)

        #-Delete data button-
        self.delete_data_btn = ttk.Button(self, text="Delete Entry")
        self.delete_data_btn.grid(row=3, column=2)
        


        #-Close database and cursor-
        # self.cursor.close()
        # self.db.close()

    #===GUI FUNCTIONS===
    
    #-Get table selection-
    def get_selection(self):
            dd_selection = self.variable.get()
            return dd_selection




    #-Display table function-
    def display_table(self):
        
        columns = self.query_column_names()
        data_display = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        for item in columns:
            data_display.heading(item, text=item)

        data_display.bind('<<TreeviewSelect>>', self.item_selected)
        data_display.grid(row=2, column=0, columnspan=3, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=data_display.yview)
        data_display.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=4, sticky='nws')


        # add data to the treeview
        table_contents = self.query_table_contents()
        for table_row in table_contents:
            data_display.insert('', tk.END, values=table_row)

        return data_display

    def item_selected(self, event):
        for selected_item in self.data_display.selection():
            item = self.data_display.item(selected_item)
            record = item['values']
            # show a message
            messagebox.showinfo(title='Information', message=','.join(record))
    



    #===QUERY FUNCTIONS===
    #-Get table names from database-
    def query_table_names(self):
        table_query = self.cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        table_names = self.cursor.fetchall()
        table_names_list = []
        for item in table_names:
            table_names_list.append(item[0])
        return table_names_list
    
    #-Column names query of a particular table-
    def query_column_names(self):
        print(self.variable.get())
        table_pragma_query = self.cursor.execute(f"PRAGMA table_info({self.get_selection()});")
        table_pragma = self.cursor.fetchall()
        
        column_names = []
        for parameter in table_pragma:
            column_names.append(parameter[1])
        
        print(column_names)
        return column_names

    #-Table content query-
    def query_table_contents(self):
        table_contents_query = self.cursor.execute(f"SELECT * FROM {self.variable.get()};")
        table_contents = self.cursor.fetchall()
        return table_contents
    
    #-Update data query-
    def query_update_data(self, ):
        pass

        
    
    def produce_table(self):
        
         pass
    






if __name__ == "__main__":
    app = BookstoreManagerApp()
    app.mainloop()