from os import path

from .Error import ErrorUtils

from ..state.State import State

import csv


class DataUtils:

    def create_dataset(dataset_name_list):
        file_path_dict = State.get('file_path_dict')
        for dataset_name in dataset_name_list:
            if (file_path_dict.get(dataset_name) == None):
                # invalid dataset name
                return ErrorUtils('INVALID_DATASET_NAME', 'Invalid dataset name: {}'.format(dataset_name))
            else:
                # valid dataset name, proceed with the file operations
                fpd_entry = file_path_dict.get(dataset_name)
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
