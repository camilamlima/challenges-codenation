import re
import numpy as np
from datetime import datetime, timedelta


class ManagerDates:
    def date_is_valid(self, date):
        try:
            day, month, year = date.split("/")
            datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False

    def date_weekday(self, date):
       return date.strftime("%A")

    def convert_string_to_date(self, date_str):
        
        formats = ["%d/%m/%Y","%d-%m-%Y","%d%m%Y"]
        obj_date = False
        
        for format in formats:
            try:
                obj_date = datetime.strptime(date_str, format)
                break
            except ValueError:
                continue

        return obj_date

    def get_all_dates(self, month, year):
        n_array = np.arange(
            start=datetime(int(year), int(month), 1),
            stop=datetime(int(year), int(month)+1, 1),
            step=timedelta(days=1),
            dtype=datetime,
        )
        return n_array

    def count_days_mounth(self, month, year):
        days_of_month = self.get_all_dates(month, year)
        workdays = np.is_busday(np.array(days_of_month).astype("datetime64[D]"))
        return np.count_nonzero(workdays)

    def get_first_monday(self, year):
        date = np.busday_offset("%s-05" % year, 0, roll="forward",
                                holidays=["%s-05-01" % year], weekmask="Mon")
        return date.tolist().strftime("%d/%m/%Y")