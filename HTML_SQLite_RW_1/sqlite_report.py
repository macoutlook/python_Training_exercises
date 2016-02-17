import report
import sqlite3
import logging


class SqlLiteReport(report.Report):

    def __init__(self, list_with_records, file_path, log_level = logging.DEBUG):
        super(SqlLiteReport, self).__init__(list_with_records, file_path)

    def generate_report(self):
        """
        This method creates records in databases. It uses sqlite3, result is saved in file
        :param list_with_records:
        :param file_path: path where file with database will be saved
        :return:
        """
        result = True
        #getting connection with database
        conn = sqlite3.connect(self.file_path)
        #getting cursor
        c = conn.cursor()
        #in try catch block we create table, if this table exists it only pass
        self.logger.debug("Sqlite Report is generated")

        try:
            c.execute('''CREATE TABLE records
                 (value text, date text, time text)''')
        except sqlite3.OperationalError as e:
            self.logger.debug("Report exists. This time report is only updated")

        try:
            for list in self.list_with_records:
                binded_list = SqlLiteReport.turn_dict_into_list(list)
                #nice way to bind query with list with tuples
                # ? tell that here should be added value from var binded_list
                c.executemany("INSERT INTO records VALUES (?, ?, ?)", binded_list)
                conn.commit()

            c.execute("SELECT * FROM records")
            print c.fetchall()
            conn.close()
        except:
            result = False

        return result

    @staticmethod
    def turn_dict_into_list(dict_with_rec):
        """
        Turning dict into list with tuple for binding in INSERT
        :param dict_with_rec:
        :return:
        """
        list_with_dict_values = []
        tup = tuple()
        keys_list = dict_with_rec
        for key in keys_list:
            if key == "time":
                list_with_dict_values.insert(2, dict_with_rec[key] )
            elif key == "date":
                list_with_dict_values.insert(1, dict_with_rec[key] )
            else:
                list_with_dict_values.insert(0, dict_with_rec[key] )
        tup = tuple(list_with_dict_values)
        returned_list = []
        returned_list.append(tup)

        return returned_list