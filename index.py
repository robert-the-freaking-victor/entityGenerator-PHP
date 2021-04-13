import os
import sys

# sys.argv order: entityName, outputPath

def main():
  config = get_config()
  print("[INFO] Creating the file configuration")
  create_new_files(config["entity_name"], config["output_path"], "./configs", ".xml", ".xml")
  create_new_files(config["entity_name"], config["output_path"], "./models", ".txt", ".php")

def create_new_files(entity_name, output_path, model_path, ext_model, ext_new_file):
  filenames = ["Controller", "Factory", "Service"]
  for file in filenames:
    full_filename = file + ext_model
    full_path = os.path.join(model_path, full_filename)
    new_filename = entity_name + file + ext_new_file
    full_output_path = os.path.join(output_path, new_filename)
    with open(full_path, "r") as file_stream:
      text = file_stream.readlines()
      formated_text = []
      for line in text:
        new_line = fill_line(line, entity_name)
        formated_text.append(new_line)
      with open(full_output_path, "w") as file2_stream:
        file2_stream.writelines(formated_text)

def fill_line(line, value):
  line = line.replace("{}", value)
  return line

def get_config():
  config = {
    "entity_name": sys.argv[1],
    "output_path": sys.argv[2]
  }
  print(config)
  return config

if __name__ == "__main__":
  main()
