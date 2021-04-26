import os
import sys
import json
from phpService import PHPService
from xmlService import XMLService

def main():
  config = None
  with open("./config.json") as file_stream:
    config = json.load(file_stream)
  entity_name = sys.argv[1]
  print("[INFO] Creating the file configuration...")
  xml = XMLService()
  php = PHPService()
  xml.append_xml(config["xmlControllerReal"], entity_name, config["xmlControllerTemplate"])
  xml.append_xml(config["xmlFactoryReal"], entity_name, config["xmlFactoryTemplate"])
  xml.append_xml(config["xmlServiceReal"], entity_name, config["xmlServiceTemplate"])
  print("[INFO] Creating the php files...")
  php.create_php(config["phpControllerOutput"], entity_name, config["phpControllerTemplate"], "Controller")
  php.create_php(config["phpFactoryOutput"], entity_name, config["phpFactoryTemplate"], "Factory")
  php.create_php(config["phpServiceOutput"], entity_name, config["phpServiceTemplate"], "Service")
  print("[INFO] Entity was created without errors.")

if __name__ == "__main__":
  main()
