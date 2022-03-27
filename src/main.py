#!/usr/bin/env python3

import os
import shutil
import yaml


def main():
    try:
        signature_content = yaml_content = None

        with open("config.yaml", "r") as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)

        os.makedirs("../output", exist_ok=True)

        with open("template.html", "r") as template_file:
            signature_content = template_file.read()

        with open("../output/signature.html", "w") as signature_file:
            for key, value in yaml_content.items():
                signature_content = signature_content.replace(f'${key}', value)

            signature_file.write(signature_content)

    except IOError as err:
        print("IOError:", err)


main()
