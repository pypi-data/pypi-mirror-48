﻿# ibm-apidocs-cli
![Status](https://img.shields.io/badge/status-beta-yellow.svg)
[![Latest Stable Version](https://img.shields.io/pypi/v/ibm-apidocs-cli.svg)](https://pypi.python.org/pypi/ibm-apidocs-cli)

This tool allows users to generate the api documentation.

## Installation

- To install the CLI, use `pip` or `easy_install`:

    ```bash
    pip install -U ibm-apidocs-cli
    ```

    or

    ```bash
    easy_install -U ibm-apidocs-cli
    ```

- Clone the [frontmatter generator](https://github.ibm.com/cloud-doc-build/frontmatter-generator) to a local directory.

- Install the [SDK generator](https://github.ibm.com/CloudEngineering/openapi-sdkgen/releases) to a local directory.

    You do not need to clone or download the full repository or build the project. Instead, use the [installer](https://github.ibm.com/CloudEngineering/openapi-sdkgen/releases). For more information, see [the generator README](https://github.ibm.com/CloudEngineering/openapi-sdkgen#using-a-pre-built-installer).

    **Note:** The SDK generator .jar file must be named `openapi-sdkgen.jar`. If you have downloaded or built a version of the file with a different name (e.g. `openapi-sdkgen-<version>.jar`), you must rename it.

- Clone a [cloud-api-docs](https://github.ibm.com/cloud-api-docs) repo to a local directory. Make sure the repo contains the required `apiref-index.json` file and the front-matter configuration file (typically `<openapi>-config.json`).

## Usage

```
ibm-apidocs-cli --help
```

```
usage: ibm-apidocs-cli [-h] -i <openapi_file> -c <config_file>
                       -f <frontmatter_path> -s <sdk_generator_path>
                       [--apidocs <apidocs_path>]
                       [--templates <templates_path>]
                       [--output_folder <output_path>]
                       [--keep_sdk] [--verbose] [--version]
```

Required arguments:

- `-i <openapi_file>`: The path to the input OpenAPI definition file (e.g. `assistant-v1.json`).
- `-c <config_file>`: The front matter config file (e.g. `assistant-v1-config.json`). You can optionally specify the full path to the config file; if you do not include the path, the file is assumed to be in the `apidocs` directory.
- `-f <frontmatter_path>`: Path to the directory containing the front-matter generator `app.js` file.
- `-s <sdk_generator_path>`: Path to the directory containing the SDK generator `openapi-sdkgen.jar` file.

Optional arguments:

- `--apidocs <apidocs_path>`: The path to the `cloud-api-docs` repository or other directory containing `apiref-index.json` and front matter config file. If you do not specify this argument, the current directory is used.
- `--templates <templates_path>`: Path to a directory containing custom front-matter templates.
- `--output_folder <output_folder>`: The target directory for generated files. If you do not specify this argument, output files are written to the current directory.
- `--keep_sdk`: Preserve the `_sdktemp` directory containing generated SDK artifacts. Useful for debugging purposes.
- `--no_update`: Use front-matter config file as-is without updating SDK versions. If you do not specify this argument, the config file is updated with the latest GitHub release for each supported SDK language.
- `-h`, `--help`: Show usage information and exit.
- `--verbose`: Verbose flag.
- `--version`: Show program's version number and exit.

### Example commands

This example assumes that the command is being run from the `apidocs` repo directory containing the
API Reference files. All output files are written to the current directory:

```bash
ibm-apidocs-cli -i assistant-v1.json -c assistant-v1-config.json\
                -f '/Users/my_user/GitHub/frontmatter-generator' \
                -s '/Users/my_user/openapi-sdkgen/lib'
```

This example uses different locations for the input and output files:

```
ibm-apidocs-cli --openapi '/Users/my_user/Documents/GitHub/api-apidocs-cli/test/resources/config/assistant-openapi3-v1.json' \
                --config '/Users/my_user/Documents/GitHub/api-apidocs-cli/test/resources/config/test-input-config.yaml' \
                --output_folder '/Users/my_user/Documents/GitHub/api-apidocs-cli/test/target' \
                --frontmatter '/Users/my_user/Documents/GitHub/frontmatter-generator' \
                --sdk_generator '/Users/my_user/Documents/Release/openapi-sdkgen/lib'
```

## Python version

✅ Tested on Python 2.7, 3.4, 3.5, and 3.6.

## Contributing

See [CONTRIBUTING.md][CONTRIBUTING].

## License

MIT

[ibm_cloud]: https://cloud.ibm.com
[responses]: https://github.com/getsentry/responses
[requests]: http://docs.python-requests.org/en/latest/
[CONTRIBUTING]: ./CONTRIBUTING.md
