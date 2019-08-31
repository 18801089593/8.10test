import xlrd


class readExcel():

    read_book = xlrd.open_workbook(r'D:\学习文件\8.10test\testdata\data.xls')
    urlSheet = read_book.sheet_by_name('urlSheet')
    rownum = urlSheet.nrows


    def readbook(self):

        urllist = []
        for i in range(1,self.rownum):
            rowvalue = self.urlSheet.row_values(i)
            urllist.append(rowvalue)
        list = []
        for i in urllist:
            list.append(i[0])
        print(list)
        return list



#readExcel()


























readExcel().readbook()




