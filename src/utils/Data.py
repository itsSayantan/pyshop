from os import path
from .Error import ErrorUtils
import csv


class DataUtils:
    file_path_dict = {
        'users': {
            'file_path': './data/users.csv',
            'template_file_path': './data/users.template.csv'
        }
    }

    @classmethod
    def create_dataset(cls, dataset_name_list):
        for dataset_name in dataset_name_list:
            if (cls.file_path_dict.get(dataset_name) == None):
                # invalid dataset name
                return ErrorUtils('INVALID_DATASET_NAME', 'Invalid dataset name: {}'.format(dataset_name))
            else:
                # valid dataset name, proceed with the file operations
                fpd_entry = cls.file_path_dict.get(dataset_name)
                with open(fpd_entry.get('template_file_path'), newline='') as csvfile:
                    reader = csv.reader(
                        csvfile, delimiter='|')
                    """
                        We are only interested with the first line of this file.
                        Hence, we are using the counter approach.
                    """
                    count = 0
                    for row in reader:
                        if count != 0:
                            break
                        else:
                            """
                                Create the [dataset_name].csv file if it does not exist with the columns same as 'row'.
                            """
                            if path.exists(fpd_entry.get('file_path')) == True:
                                # do not create a new file
                                continue
                            else:
                                # create a new file
                                with open(fpd_entry.get('file_path'), 'w', newline='') as csvfileforwriting:
                                    csvwriter = csv.writer(
                                        csvfileforwriting, delimiter='|', quotechar='|')
                                    firstrow = [row]
                                    csvwriter.writerows(firstrow)
