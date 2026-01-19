import io
from matplotlib import pyplot
from matplotlib.figure import Figure
import numpy

class Extra_plotter:
    def __init__(self):
        pass

    def category_expense_png(self, expense_list: list, year:str) -> bytes:
        print('category_expense_png')
        category_list = []
        amount_list = []
        
        # For displaying purposes we short all category names to max 8 chars
        for expense in expense_list:
            amount_list.append(round(expense[0], 2))
            if len(expense[1]) > 8:
                short_name = expense[1][:8]
                category_list.append(short_name)
            else:
                category_list.append(expense[1])

        print(len(amount_list))
        if not len(amount_list):
            return False

        labels = category_list
        values = numpy.array(amount_list)
        fig, ax = pyplot.subplots(figsize=(7,5))
        bars = ax.bar(labels, values)

        ax.set_title(f'Ausgaben pro Kategorie im Jahr {year}')
        ax.set_ylabel("Ausgaben in €")

        ax.set_ylim(0, self.calc_ylim_max(values.max()))

        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9,
                rotation=90
            )
        pyplot.xticks(rotation=90)
        pyplot.tight_layout()

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
        pyplot.close(fig)
        buf.seek(0)
        return buf.getvalue()

    def monthly_expense_png(self, expense_list: list, year:str) -> bytes:

        # return false if there are no expense in the year
        if not len(expense_list):
            return False

        amount_list = []
        month_list = []

        # We want every month in the year displayed, even if 
        # no expenses are tracked (yet).
        for i in range(1, 13):
            istring = str(i)
            if len(istring) == 1:
                istring = '0' + istring
            month_list.append(istring)

        counter = 0
        for month in month_list:
            if counter < len(expense_list) and month == expense_list[counter][1]:
                amount_list.append(expense_list[counter][0])
                counter += 1
                continue
            amount_list.append(0)

        for expense in expense_list:
            amount_list.append(expense[0])
            month_list.append(expense[1])

       # print(len(amount_list))
        print(amount_list)
        if not len(amount_list):
            return False

        labels = month_list
        values = numpy.array(amount_list)

        fig, ax = pyplot.subplots(figsize=(7,5))
        #bars = ax.bar(labels, values, color="red", edgecolor="black")
        bars = ax.bar(labels, values)

        ax.set_title(f'Ausgaben pro Monat im Jahr {year}')
        ax.set_ylabel("Ausgaben in €")
        ax.set_ylim(0, self.calc_ylim_max(values.max()))

        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=7
            )

        pyplot.tight_layout()

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
        pyplot.close(fig)
        buf.seek(0)
        return buf.getvalue()

    def calc_ylim_max(self, maxval):
        if maxval == 0:
            return 1000
        return maxval * 1.15
    '''
    def monthly_expense(self, expense_list: list, year:str) -> None:
        month_list = []
        amount_list = []

        for expense in expense_list:
            amount_list.append(expense[0])
            month_list.append(expense[1])

        labels = month_list
        values = numpy.array(amount_list)

        fig, ax = pyplot.subplots(figsize=(8,6))
        bars = ax.bar(labels, values, color="red", edgecolor="black")

        ax.set_title(f'Ausgaben pro Monat im Jahr {year}')
        ax.set_ylabel("Ausgaben in €")
        ax.set_ylim(0, values.max() * 1.15)

        for bar in bars:
            height = bar.get_height()
            ax.annotate(
                f"{height}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9
            )

        pyplot.tight_layout()
        pyplot.show()
    '''


