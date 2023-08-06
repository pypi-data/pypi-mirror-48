# -*- coding: utf-8 -*-
"""
faereld.graphs.box_plot
-----------
"""

from datetime import timedelta

from faereld import utils
from numpy import percentile


class BoxPlot(object):
    left_whisker = "┣"
    right_whisker = "┫"
    whisker = "━"
    box_body = "█"
    median = "\033[91m█\033[0m"

    def __init__(self, values_map):
        self.values_map = values_map
        self.max_width = utils.terminal_width()
        self.exclude_list = []

    def set_max_width(self, max_width):
        self.max_width = max_width
        return self

    def set_exclude_list(self, exclude_list):
        self.exclude_list = exclude_list
        return self

    def generate(self):
        # First, filter out any areas that have no values.
        values = dict(filter(lambda x: len(x[1]) > 0, self.values_map.items()))
        # Filter out areas that are invalid for this analysis
        values = dict(filter(lambda x: x[0] not in self.exclude_list, values.items()))
        # Convert the timedeltas into ints
        for key, value in values.items():
            values[key] = list(map(lambda x: x.seconds, value))
        # Used to determine where to place things
        overall_min = None
        overall_max = None
        # Should be of the form key: (max, min, 1st quart, 2nd quart, 3rd quart)
        box_plot_tuples = {}
        for key, area_value in values.items():
            min_val = min(area_value)
            max_val = max(area_value)
            first = percentile(area_value, 25)
            second = percentile(area_value, 50)
            third = percentile(area_value, 75)
            box_plot_tuples[key] = (min_val, max_val, first, second, third)
            if overall_max is None or overall_min is None:
                overall_min = min_val
                overall_max = max_val
            if min_val < overall_min:
                overall_min = min_val
            if max_val > overall_max:
                overall_max = max_val
        # Transform the values to character positions from the minimum
        # Max width is reduced by 7 for 'KEY :: '
        max_width_bar = self.max_width - len("KEY :: ")
        for key, values in box_plot_tuples.items():
            if overall_min == overall_max:
                box_plot_tuples[key] = self._create_box_plot(0, 0, 0, 0, 0)
            else:
                positions = list(
                    map(
                        lambda x: int(
                            round(
                                max_width_bar
                                * ((x - overall_min) / (overall_max - overall_min))
                            )
                        ),
                        values,
                    )
                )
                box_plot_tuples[key] = self._create_box_plot(*positions)
        # Merge the labels and the box plots into a single string
        returnable_list = list(
            map(lambda x: "{0} :: {1}\n".format(x[0], x[1]), box_plot_tuples.items())
        )
        # Add the min/max labels
        min_formatted = utils.format_time_delta(timedelta(0, overall_min))
        max_formatted = utils.format_time_delta(timedelta(0, overall_max))
        returnable_list.append(
            "MIN :: {0} // MAX :: {1}".format(min_formatted, max_formatted)
        )
        return returnable_list

    def _create_box_plot(self, min_pos, max_pos, first_pos, second_pos, third_pos):
        # First, pad out the string with spaces until the min
        box_string = " " * (min_pos - 1)
        # Add the whisker
        box_string += self.left_whisker
        # Pad until the first quartile
        box_string += self.whisker * ((first_pos - 1) - len(box_string))
        # Pad until the second quartile
        box_string += self.box_body * ((second_pos - 1) - len(box_string))
        # Add the second quartile
        box_string += self.median
        # Pad until the third quartile
        box_string += self.box_body * (
            third_pos - len(utils.strip_colour_codes(box_string))
        )
        # Pad until the max
        box_string += self.whisker * (
            (max_pos - 1) - len(utils.strip_colour_codes(box_string))
        )
        # Add the whisker
        box_string += self.right_whisker
        return box_string
