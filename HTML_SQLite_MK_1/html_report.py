import report
from dominate import document
from dominate.tags import *
import logging


class HtmlReport(report.Report):

    def __init__(self, list_with_records, file_path, searched_phrase, log_level = logging.DEBUG):
        super(HtmlReport, self).__init__(list_with_records, file_path)
        self.searched_phrase = searched_phrase
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(log_level)

    def generate_report(self):
        """
        Creating file with html report with using dominate module
        :param list_with_records:
        :param file_path:
        :param searched_phrase:
        :return: result in boolean
        """
        result = True
        value_key = self.searched_phrase[:-2]
        #building html string and save it as doc
        self.logger.debug("Html Report is generated")

        with document(title='Records') as doc:
            h1('Records')
            try:
                for dict in self.list_with_records:
                    #Everything will be in this indentation has place in <div:
                    with div():
                        record = self.searched_phrase + dict[value_key] + " Date : " + dict["date"] + " Time : " + dict["time"]
                        p(record)
            except (KeyError) as e:
                self.logger.error("Check given keys, used for generating html report, please")
                result =  False
        # saving doc string to file with given path
        try:
            with open(self.file_path, 'w') as f:
                f.write(doc.render())
        except IOError as e:
            self.logger.error("Unfortunately given path to html log is not available")
            result =  False

        return result