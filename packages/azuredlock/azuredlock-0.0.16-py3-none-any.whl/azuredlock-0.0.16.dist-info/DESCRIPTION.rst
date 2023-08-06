# azuredlock

azure + redlock onboarding script.

This is mainly just a wrapper around the `az cli` which is a dependency.

The quickest path is to do a `pip install azuredlock` and then
run `azuredlock onboard` from the Azure Cloud Shell which is in the 
Azure Portal since it already has the cli and uses a form of 
Managed Identities so you don't even have to login for it to work.

## Install in Azure Cloud Shell

1.  Use the `bash` shell
2.  Run `pip install --user azuredlock`
3.  Put the newly installed command in your path: `export PATH=$PATH:~/.local/bin`
4.  Run `azuredlock` to see help commands or `azuredlock onboard --help`


