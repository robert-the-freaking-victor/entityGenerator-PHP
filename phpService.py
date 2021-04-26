import os
from service import Service

class PHPService(Service):

  def create_php(self, output_path, entity_name, path_template, type_service):
    """[summary]

    Args:
        output_path (string): path where the entity will be saved
        entity_name (string): name of the entity that will be created
        path_template (string): full path of the example file that will be used as template to the new file
    """
    output_name = "{}{}.php".format(entity_name, type_service)
    full_output_path = os.path.join(output_path, output_name)
    formated_text = []
    with open(path_template, "r") as file_stream:
      text = file_stream.readlines()
      for line in text:
        new_line = self._fill_line(line, entity_name)
        formated_text.append(new_line)
    with open(full_output_path, "w") as file2_stream:
      file2_stream.writelines(formated_text)
