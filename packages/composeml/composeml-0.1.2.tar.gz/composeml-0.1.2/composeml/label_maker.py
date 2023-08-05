import pandas as pd
from tqdm import tqdm

from composeml.label_times import LabelTimes


def on_slice(make_label, window, min_data, gap, n_examples):
    """
    Returns a function that transforms a data frame to labels.

    Args:
        make_label (function) : Function that transforms a data slice to a label.
        window (str or int) : Duration of each data slice.
        min_data (str or int) : Minimum data before starting search.
        n_examples (int) : Number of labels to make.
        gap (str or int) : Time between examples.

    Returns:
        df_to_labels (function) : Function that transforms a data frame to labels.
    """

    def offset_time(index, value):
        if isinstance(value, int):
            value += 1
            value = index[:value][-1]
            return value

        if isinstance(value, str):
            value = pd.Timedelta(value)
            value = index[0] + value
            return value

    def df_to_labels(df, *args, **kwargs):
        labels = pd.Series(name=make_label.__name__)

        df = df.loc[df.index.notnull()]
        df.sort_index(inplace=True)

        if df.empty:
            return labels.to_frame()

        cutoff_time = offset_time(df.index, min_data)

        for example in range(n_examples):
            df = df[cutoff_time:]

            if df.empty:
                break

            time = offset_time(df.index, window)
            label = make_label(df[:time], *args, **kwargs)

            not_none = label is not None
            not_nan = label is not pd.np.nan
            if not_none and not_nan:
                labels[cutoff_time] = label

            cutoff_time = offset_time(df.index, gap)

        labels.index = labels.index.rename('time')
        labels.index = labels.index.astype('datetime64[ns]')
        return labels.to_frame()

    return df_to_labels


def assert_valid_offset(value):
    if isinstance(value, int):
        assert value >= 0, 'negative offset'

    elif isinstance(value, str):
        offset = pd.Timedelta(value)
        assert offset is not pd.NaT, 'invalid offset'
        assert offset.total_seconds() >= 0, 'negative offset'

    else:
        raise TypeError('invalid offset type')


class LabelMaker:
    """Automatically makes labels for prediction problems."""

    def __init__(self, target_entity, time_index, labeling_function, window_size):
        """
        Creates an instance of label maker.

        Args:
            target_entity (str) : Entity on which to make labels.
            time_index (str): Name of time column in the data frame.
            labeling_function (function) : Function that transforms a data slice to a label.
            window_size (str or int) : Duration of each data slice.
        """
        self.target_entity = target_entity
        self.time_index = time_index
        self.labeling_function = labeling_function
        self.window_size = window_size

    def _preprocess(self, df):
        if df.index.name != self.time_index:
            df = df.set_index(self.time_index)

        if 'time' not in str(df.index.dtype):
            df.index = df.index.astype('datetime64[ns]')

        return df

    def search(self, df, minimum_data, num_examples_per_instance, gap, verbose=True, *args, **kwargs):
        """
        Searches and extracts labels from a data frame.

        Args:
            df (DataFrame) : Data frame to search and extract labels.
            minimum_data (str) : Minimum data before starting search.
            num_examples_per_instance (int) : Number of examples per unique instance of target entity.
            gap (str) : Time between examples.
            args : Positional arguments for labeling function.
            kwargs : Keyword arguments for labeling function.

        Returns:
            labels (LabelTimes) : A data frame of the extracted labels.
        """
        df = self._preprocess(df)

        assert_valid_offset(minimum_data)
        assert_valid_offset(self.window_size)
        assert_valid_offset(gap)

        df_to_labels = on_slice(
            self.labeling_function,
            min_data=minimum_data,
            window=self.window_size,
            n_examples=num_examples_per_instance,
            gap=gap,
        )

        if verbose:
            bar_format = "Elapsed: {elapsed} | Remaining: {remaining} | "
            bar_format += "Progress: {l_bar}{bar}| "
            bar_format += self.target_entity + ": {n}/{total} "
            tqdm.pandas(bar_format=bar_format, ncols=90)

        labels = df.groupby(self.target_entity)

        apply = labels.progress_apply if verbose else labels.apply
        labels = apply(df_to_labels, *args, **kwargs)

        if labels.empty:
            return LabelTimes()

        labels = labels.reset_index().rename_axis('label_id')
        labels = LabelTimes(labels)._with_plots()

        labels.settings = {
            'name': self.labeling_function.__name__,
            'target_entity': self.target_entity,
            'num_examples_per_instance': num_examples_per_instance,
            'minimum_data': minimum_data,
            'window_size': self.window_size,
            'gap': gap,
        }

        return labels
