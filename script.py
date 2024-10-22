import os
from datetime import date

def get_data(prompt:str, default:str) -> str :
    ret = str(input(prompt))
    if ret == "" :
        ret = default
        print(f"set by default to {default}")
    return ret
def create_directory(directoryName:str):
    try:
        os.mkdir(directoryName)
        print(f"Directory '{directoryName}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directoryName}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directoryName}'.")
    except Exception as error:
        print(f"An error occurred: {error}")
def create_file(fileName:str, content:str = "") :
    f = open(fileName, "w")
    f.write(content)

projectName = get_data("The name of your project : ", "blank project")
author = get_data("Your username : ", "blank user")
description = get_data("The description of your project : ", "blank description")
gitLink = get_data("The link to your git repository : ", "https://github.com")

create_directory("docs")
create_directory("sample")
create_directory("tests")

create_file("setup.py", '# -*- coding: utf-8 -*-\n\nfrom setuptools import setup, find_packages\n\nwith open("README.md") as f:\n    readme = f.read()\n\nwith open("LICENSE") as f:\n    license = f.read()\n\n\nsetup (\n    name = "'+projectName+'",\n    version = "1.0.0",\n    description = "'+description+'",\n    long_description = readme,\n    author = "'+author+'",\n    url = "'+gitLink+'",\n    license = license,\n    packages=find_packages(exclude=("tests", "docs"))\n)')
create_file("LICENSE", 'Copyright (c) '+str(date.today().year)+', '+author+'\n\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:\n\nRedistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.\nRedistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.')
create_file("README.md")
create_file("requirements.txt")

create_file("docs/conf.py")

create_file("sample/core.py")
create_file("sample/__init__.py", "import .core")

create_file("tests/__init__.py")
create_file("tests/context.py", "# -*- coding: utf-8 -*-\n\nimport sys\nimport os\nsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))\n\nimport sample")
create_file("tests/test_advanced.py", '# -*- coding: utf-8 -*-\nfrom .context import sample\n\nimport unittest\n\n\nclass AdvancedTestSuite(unittest.TestCase):\n    """Advanced test cases."""\n\n    def test_blank_func(self):\n        self.assertIsNone(sample.blank_func())\n\n\nif __name__ == "__main__":\n    unittest.main()")\n')
create_file("tests/test_basic.py", '# -*- coding: utf-8 -*-\n\nfrom .context import sample\n\nimport unittest\n\n\nclass BasicTestSuite(unittest.TestCase):\n    """Basic test cases."""\n\n    def blank_test(self):\n        assert True\n\n\nif __name__ == "__main__":\n    unittest.main()")')

os.remove("script.py")