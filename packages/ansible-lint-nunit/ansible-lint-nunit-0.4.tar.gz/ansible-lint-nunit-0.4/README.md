[ansible-lint](https://github.com/willthames/ansible-lint) to NUnit converter
---

### Installation
via pip;
```shell
pip install ansible-lint-nunit
```
### Updating
via pip;
```shell
pip install ansible-lint-nunit --upgrade
```

### Usage:
1. run `ansible-lint` on your playbook(s) with parameter `-p` (it is required) and redirect output to file
  ```shell
  ansible-lint -p your_fancy_playbook.yml > ansible-lint.txt
  ```
2. run `ansible-lint-nunit` and pass generated file to it
  ```shell
  ansible-lint-nunit ansible-lint.txt -o ansible-lint.xml
  ```

### Output
* if there are any lint errors, full NUnit XML will be created
* Compatible with Azure DevOps NUnit parser
