def saddle_points(matrix):
    result = []

    for i, i_value in enumerate(matrix):
      if len(i_value) != len(matrix[0]):
        raise ValueError('matrix does not have correct format')

      for j, j_value in enumerate(i_value):
        if j_value == max(i_value) and min(list(map(lambda value: value[j], matrix))) == j_value:
          result.append({ "row": i + 1, "column": j + 1 })

    return result if result else [{}]
