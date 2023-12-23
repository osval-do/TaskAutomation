# TaskAutomation

An extendable python based multiplatform program for execution of high level tasks. This program uses simple YAML instructions like this:

```yml
program:
  tasks:
    - class: set_context_vars
      vars:
        base_url: http://somesite.com/api/
        user: my_user
        pass: asdf4567
    - class: login
      url: ${base_url}token-auth/
      user: ${user}
      pass: ${pass}
      token_prop: access
    - class: http
      name: rest_api_call
      action: post
      url: http://mysyte.com/api/command/
      fields:
        value1: True
        value2: test-rest
```

This program only contains the barebones and is indented to be extended to fulfill your needs.

## Execution of task files

Once compiled, a file can be executed with the following command:

```bat
taskAutomation.exe my_prog1.yml
```

Is also possible to mix multiple task files:

```bat
taskAutomation.exe my_prog1.yml some-path/my_prog2.yml
```

## Adding custom tasks

New custom tasks can be added in the main.py file, just register them in the get_tasks function.

## Compiling

This project uses by default the PyInstaller to generate binaries for Windows, Linux or Mac. 
Follow the instructions in (here)[https://pypi.org/project/pyinstaller/] to compile to your system.

As an example, this commands will generate compile for Windows:

```bat
rmdir /s /q build
rmdir /s /q dist
pyinstaller main.py --noconfirm --onefile
cd dist
rename main.exe TaskAutomation.exe
```