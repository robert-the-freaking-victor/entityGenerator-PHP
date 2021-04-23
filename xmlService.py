import os
from service import Service

class XMLService(Service):

  def append_xml(self, service_path, entity_name, path_template):
    formated_text = []
    service_text = []
    with open(path_template, "r") as file_stream:
      text = file_stream.readlines()
      for line in text:
        new_line = self._fill_line(line, entity_name)
        service_text.append("\t\t{}".format(new_line))
    full_text = None
    with open(service_path, "r") as file_stream:
      full_text = file_stream.readlines()
    for line in full_text:
      if line.strip() == "</services>":
        formated_text += service_text
        formated_text+= "\n\n\t</services>\n</container>"
        break
      else:
        formated_text.append(line)
    with open(service_path, "w") as file_stream:
      file_stream.writelines(formated_text)