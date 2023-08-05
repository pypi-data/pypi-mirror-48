"""This file implements the markdown table generate from a csv file"""

import csv

__version__ = "0.1"


def handle_aligns(aligns):
    """Converts comma delimited string of alignments to tuple

    Arguments:
        aligns: comma delimited string of 'l', 'r', 'c' or empty string
    Returns:
        aligns_tuple: tuple of alignments or None
    """
    if not aligns:
        aligns_tuple = None
    else:
        aligns_tuple = tuple(aligns.lower().replace(" ", "").split(","))
    return aligns_tuple


class MDTable:
    """MDTable

        Arguments:
            filepath: string pointing to input csv file
            aligns: tuple of alignments, must have same number as number of columns
            delimiter: delimiter character in csv
            quotechar: quote character in csv
            escapechar: escape character in csv
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        filepath: str,
        aligns: tuple = None,
        delimiter: str = ",",
        quotechar: str = '"',
        escapechar: str = "",
        padding: int = "1",
    ):
        """MDTable

        Arguments:
            filepath: string pointing to input csv file
            aligns: tuple of alignments, must have same number as number of columns
            delimiter: delimiter character in csv
            quotechar: quote character in csv
            escapechar: escape character in csv
            padding: padding for table border
        """
        self.filepath = filepath
        self.aligns = aligns
        self.padding = padding
        self._csv_dict = read_csv(
            filepath, delimiter=delimiter, quotechar=quotechar, escapechar=escapechar
        )
        self._num_cols = len(self._csv_dict.keys())
        if aligns:
            self._validate_aligns(self.aligns)

    def get_table(self) -> str:
        """Method to return markdown formatted table as string
        """
        header, dashes = self._prep_header()
        table = header + dashes
        for row in self._prep_body():
            table += row
        return table

    def save_table(self, filepath: str, mode: str = "w"):
        """Saves the output to a specified file

        Arguments:
            filepath: string representing filepath to save file
            mode: mode to open file (w, w+, a, a+)
        """
        table = self.get_table()
        with open(filepath, mode=mode) as save_file:
            save_file.write(table)

    def _validate_aligns(self, aligns):
        for align in aligns:
            if not align in ("l", "r", "c"):
                raise ValueError(
                    "Aligns must be a tuple of 'l', 'r' and 'c' for left, right and centre. Found {} instead".format(
                        align
                    )
                )
        if not len(aligns) == self._num_cols:
            raise ValueError(
                "You need to specify the alignment for all columns. There are {} columns, but you provided {} alignments".format(
                    self._num_cols, len(aligns)
                )
            )

    def _prep_header(self) -> str:
        """Returns the header of the file in markdown given a list of column names
        Returns:
            header: a string of markdown formatted header
            dashes: a string of markdown formatted dashes
        """
        word_length_dict = self._get_max_word_per_col()
        header = "|"
        dashes = "|"
        for col in range(self._num_cols):
            col_title = self._csv_dict[col][0]
            num_spaces = word_length_dict[col] - len(col_title)
            num_dashes = word_length_dict[col]
            header += " " + col_title + " " * num_spaces + " |"

            if not self.aligns or self.aligns[col] == "l":
                dashes += " " + "-" * num_dashes + " |"
            elif self.aligns[col] == "r":
                dashes += " " + "-" * num_dashes + ":|"
            elif self.aligns[col] == "c":
                dashes += ":-" + "-" * (num_dashes - 1) + ":|"

        return header + "\n", dashes + "\n"

    def _prep_body(self) -> str:
        self._prep_header()
        num_rows = len(self._csv_dict[0])
        word_length_dict = self._get_max_word_per_col()
        for row_num in range(1, num_rows):
            row = "|"

            for col in range(self._num_cols):
                word = self._csv_dict[col][row_num]
                num_spaces = word_length_dict[col] - len(word)
                row += " " + word + " " * num_spaces + " |"
            yield row + "\n"

    def _get_max_word_per_col(self) -> dict:
        """Computes the maximum word lengthin for each column

        Returns:
            word_length_dict: a dictionary whose keys are column numbers and whose values are the maximum word length for that column
        """
        word_length_dict = {}
        for key in self._csv_dict:
            max_word_length = 0
            for val in self._csv_dict[key]:
                if len(val) > max_word_length:
                    max_word_length = len(val)
            word_length_dict[key] = max_word_length
        return word_length_dict


def read_csv(
    filepath: str, delimiter: str = ",", quotechar: str = '"', escapechar: str = ""
) -> dict:
    """Process a given csv into a python dictionary

    Arguments:
        filepath: string pointing to csv file
        delimiter: string that denotes what char seperates values in csv, default is ','
        quotechar: string that denotes what char surrounds fields containing delimeter char, default is '"'
        escapechar: string that denotes what char escaptes the delimeter char, default is no escape char.
    Returns:
        csv_dict: dictionary whose keys are column numbers and values are column lists
    """
    csv_dict = {}
    with open(filepath, "r") as csv_file:
        csv_reader = csv.reader(
            csv_file, delimiter=delimiter, quotechar=quotechar, escapechar=escapechar
        )
        header = next(csv_reader)
        num_cols = len(header)
        for num in range(num_cols):
            csv_dict[num] = [header[num]]
        for row in csv_reader:
            for num in range(num_cols):
                csv_dict[num].append(row[num])
    return csv_dict
