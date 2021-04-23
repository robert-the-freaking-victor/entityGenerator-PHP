class Service:

  def _fill_line(self, line, value):
    line = line.replace("{}", value)
    return line