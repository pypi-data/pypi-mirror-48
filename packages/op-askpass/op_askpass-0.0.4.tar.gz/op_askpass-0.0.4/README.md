# op_askpass

Load password-protected ssh keys to your agent without prompts using 1Password.

Currently tested on Ubuntu only.

## Getting started

```bash
$ pip install op_askpass
# This installs 1Password cli locally.
$ op-askpass setup-op-client my.1password.com my_username@gmail.com
$ op-askpass add-key ~/.ssh/id_rsa "my 1Password item name"
# This fetches the password from 1Password and calls ssh-add.
$ op-askpass login my
```

## Details

`op-askpass` stores a small configuration file and 1Password cli called `op`
in your `$HOME/.op-askpass` directory.

The configuration file contains a mapping from ssh key fingerprint to key path
and 1Password item name. The key path is needed for loading the key when
calling `op-askpass login`. The item name is looked up for password and
provided instead of prompt.

Underneath, `op-askpass` uses `SSH_ASKPASS` command to override prompt and
instead provide the password from 1Password. The only prompt is during `op-askpass login`
to 1Password to retrieve a 30-minutes long session key.

You can list keys added to `op-askpass` using `list-keys` command, and delete not needed
ones with `op-askpass delete-key <path_to_key>`.


### 1Password domain name

For regular, non-company users the 1Password domain is `my.1password.com`. For
company users it is usually `company.1password.com`.
