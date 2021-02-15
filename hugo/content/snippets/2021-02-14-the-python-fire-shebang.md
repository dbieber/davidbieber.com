+++
title = "The Python Fire shebang"
date = 2021-02-14T00:00:00
uid = "O_izatGFP"

+++

Happy valentine's day! Today's snippet is about a feature of Python Fire, new in v0.4.0, and how you can use it to create Python Fire executables just by adding a shebang to an existing Python file. This idea is courtesy of [c6401](https://github.com/c6401) in GitHub issue [#319](https://github.com/google/python-fire/issues/319). The shebang line is `#!/usr/bin/env -S python3 -m fire`.

The feature introduced in fire v0.4.0 is that `python -m fire` now accepts filepaths.

Suppose you have a Python file at `path/to/module.py`. Previously, you could invoke module.py as a Fire CLI with the command `python -m fire path.to.module`. That still works, but now you can also use the command `python -m fire path/to/module.py`. This is roughly equivalent to running module.py and then calling `fire.Fire()` as the final line of the module.

A consequence of this new feature is that the shebang `#!/usr/bin/env -S python3 -m fire` allows you to create executable CLIs out of Python files. `/usr/bin/env -S` is explained [here](https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html). To create a Python Fire executable, simply add the shebang line as the first line of the file, and then use `chmod +x` to mark the file as executable.

Here's a quick example:

<script src="https://gist.github.com/dbieber/ab8ed63ebbd7afad3c1f19c70028ae31.js"></script>

Save it as e.g. `shebang.py`, run `chmod +x shebang.py` to make it executable, and run it with `./shebang.py hello --name=David`
