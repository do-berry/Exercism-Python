def slices(series, length):
    if len(series) < length or length <= 0:
        raise ValueError("The length argument doesn't fit the series.")
    return [series[i : i+length] for i in range(len(series) - length + 1)]
